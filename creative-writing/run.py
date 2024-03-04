import os
import json
import itertools
import argparse
import numpy as np
from functools import partial
from models import gpt, gpt_usage
from tasks import get_task
from copy import deepcopy

import re

def get_value(task, x, y, n_evaluate_sample, cache_value=True):
    value_prompt = task.value_prompt_wrap(x, y)
    if cache_value and value_prompt in task.value_cache:
        return task.value_cache[value_prompt]
    value_outputs = gpt(value_prompt, n=n_evaluate_sample, stop=None)
    value = task.value_outputs_unwrap(x, y, value_outputs)
    if cache_value:
        task.value_cache[value_prompt] = value
    return value

def get_values(task, x, ys, n_evaluate_sample, cache_value=True):
    values = []
    local_value_cache = {}
    for y in ys:  # each partial output
        if y in local_value_cache:  # avoid duplicate candidates
            value = 0
        else:    
            value = get_value(task, x, y, n_evaluate_sample, cache_value=cache_value)
            local_value_cache[y] = value
        values.append(value)
    return values

def get_votes(task, x, ys, n_evaluate_sample):
    vote_prompt = task.vote_prompt_wrap(x, ys)
    vote_outputs = gpt(vote_prompt, n=n_evaluate_sample, stop=None)
    values = task.vote_outputs_unwrap(vote_outputs, len(ys))
    return values

def get_proposals(task, x, y): 
    propose_prompt = task.propose_prompt_wrap(x, y)
    proposals = gpt(propose_prompt, n=1, stop=None)[0].split('\n')
    return [y + _ + '\n' for _ in proposals]


def get_text_plan_samples(task, x, y, n_generate_sample, stop): # text_plan generation only generate tex plans and do not generate passages.

    prompt = task.node_plan_prompt_warp(x, y)

    samples = gpt(prompt, n=n_generate_sample, stop=stop)
    return [y + _ for _ in samples]

def get_text_passage_samples(task, x, warp_init_solution, n_generate_sample, stop):
    prompt = task.node_passage_prompt_warp(x, warp_init_solution)

    samples = gpt(prompt, n=n_generate_sample, stop=stop)

    return [_ for _ in samples]

def get_samples(task, x, y, n_generate_sample, prompt_sample, stop):
    if prompt_sample == 'standard':
        prompt = task.standard_prompt_wrap(x, y)
    elif prompt_sample == 'cot':
        prompt = task.cot_prompt_wrap(x, y)
    else:
        raise ValueError(f'prompt_sample {prompt_sample} not recognized')
    samples = gpt(prompt, n=n_generate_sample, stop=stop)
    return [y + _ for _ in samples]

def get_neighborhood_problem(task, x, central_node, n_generate_sample): # return neighborhood problem related to original problem

    neighborhood_prompt = task.neigborhood_propose_prompt_wrap(x)
    neighborhood = gpt(neighborhood_prompt, n=n_generate_sample, stop=None)
    return [i.strip('Output:\n').replace('\n', ' ') for i in neighborhood]


def get_node_solution(task, x, y, n_generate_sample, prompt_sample, stop):

    node_solution = get_text_plan_samples(task, x, y, n_generate_sample, stop)
    return node_solution

def get_neighborhood_aggregation(task, x, neighborhood_solution_list, source_node, target_node): # i is the problem index
    aggregated_input = task.neighborhood_aggregation_prompt_warp(neighborhood_solution_list, x, source_node, target_node)
    aggregated_result = gpt(aggregated_input, n=1, stop=None)[0].split('\n')[-1]

    return aggregated_result

def get_readout(task, x, key, target_node, original_solution, aggregated_solution):
    readout_input = task.readout_prompt_warp(x, key, target_node, original_solution, aggregated_solution)
    readout_result = gpt(readout_input, n=1, stop=None)[0].split('\n')[-1]

    return readout_result

def tot_solve(args, task, idx, to_print=True):
    global gpt
    gpt = partial(gpt, model=args.backend, temperature=args.temperature)
    print(gpt)
    x = task.get_input(idx)  # input
    ys = ['']  # current output candidates
    infos = []
    for step in range(task.steps):
        # generation
        if args.method_generate == 'sample':
            new_ys = [get_samples(task, x, y, args.n_generate_sample, prompt_sample=args.prompt_sample, stop=task.stops[step]) for y in ys]
        elif args.method_generate == 'propose':
            new_ys = [get_proposals(task, x, y) for y in ys]
        new_ys = list(itertools.chain(*new_ys))
        ids = list(range(len(new_ys)))
        # evaluation
        if args.method_evaluate == 'vote':
            values = get_votes(task, x, new_ys, args.n_evaluate_sample)
        elif args.method_evaluate == 'value':
            values = get_values(task, x, new_ys, args.n_evaluate_sample)

        # selection
        if args.method_select == 'sample':
            ps = np.array(values) / sum(values)
            select_ids = np.random.choice(ids, size=args.n_select_sample, p=ps).tolist()
        elif args.method_select == 'greedy':
            select_ids = sorted(ids, key=lambda x: values[x], reverse=True)[:args.n_select_sample]
        select_new_ys = [new_ys[select_id] for select_id in select_ids]
        # log
        if to_print: 
            sorted_new_ys, sorted_values = zip(*sorted(zip(new_ys, values), key=lambda x: x[1], reverse=True))
            print(f'-- new_ys --: {sorted_new_ys}\n-- sol values --: {sorted_values}\n-- choices --: {select_new_ys}\n')
        
        infos.append({'step': step, 'x': x, 'ys': ys, 'new_ys': new_ys, 'values': values, 'select_new_ys': select_new_ys})
        ys = select_new_ys
    
    if to_print: 
        print(ys)
    return ys, {'steps': infos}

def got_solve_text(args, task, idx, to_print=True):

    x = task.get_input(idx)
    init_solution = get_node_solution(task, x, '', 1, args.prompt_sample, stop=None)[0]
    warp_init_solution = task.plan_output_warp(init_solution)

    thought_map = {1:{'plan': warp_init_solution, 'sentence': x, 'neighborhood': None}}
    thought_map_iter = {} 
    write_passage = get_text_passage_samples(task, x, warp_init_solution, args.n_generate_sample, stop=None)
    infos = [task.test_output(idx, y) for y in write_passage]
    print(infos)
    thought_map_iter[0] = {'graph': deepcopy(thought_map), 'test_output': write_passage, 'infos':infos}
    thought_count = 2

    for step in range(task.steps-1):
        for key, value in thought_map.copy().items():
            if value['neighborhood'] == None:
                neighborhood_problems = get_neighborhood_problem(task, x, '', args.n_neighborhood_sample)
                num_neigborhood = len(neighborhood_problems)
                value['neighborhood'] = [id for id in range(thought_count, thought_count + num_neigborhood)]

                for nei_id in range(thought_count, thought_count + num_neigborhood):
                    rephrase_x = neighborhood_problems[nei_id-thought_count]
                    node_solution = get_node_solution(task, rephrase_x, '', 1, args.prompt_sample, stop=None)[0]#.strip('Plan:\n')
                    warp_node_solution = task.plan_output_warp(node_solution)
                    thought_map[nei_id] = {'plan':warp_node_solution, 'sentence':rephrase_x, 'neighborhood': None}
                thought_count += num_neigborhood
    
        key_list = list(thought_map.copy().keys())
        key_list.reverse()

        for key in key_list:
            if thought_map[key]['neighborhood'] != None:
                # aggregation
                neighborhood_idx_list = thought_map[key]['neighborhood']
                # get aggregated plan for comparison
                plans_list = []
                plans_list.append(thought_map[1]['plan'])
                for neighborhood_id in neighborhood_idx_list:
                    plans_list.append(thought_map[neighborhood_id]['plan'])
                aggregated_prompt = task.neighborhood_aggregation_prompt_warp(plans_list)

                '''
                there is a technical concern that:
                results = gpt(aggregated_prompt, n=args.n_evaluate_sample, stop=None) where n_evaluate_sample = 5
                works fine with gpt-3.5-turbo. But for gpt-4, it seems that setting n = 5 blocks the results for coming out.
                Maybe it reach the Token per minite (TPM) for sth. To make it work smoothly, I set n = 1 and eval 5 times
                '''

                # results = gpt(aggregated_prompt, n=args.n_evaluate_sample, stop=None) # n_evaluate_sample
                # out = task.vote_outputs_unwrap(results, len(plans_list))

                select_out = [0, 0, 0, 0, 0, 0]
                for _ in range(args.n_evaluate_sample):
                    results = gpt(aggregated_prompt, n=1, stop=None)
                    one_out = task.vote_outputs_unwrap(results, len(plans_list))
                    temp_out = []
                    for result_idx in range(0, len(one_out)):
                        temp_val = select_out[result_idx] + one_out[result_idx]
                        temp_out.append(temp_val)
                    select_out = temp_out
                
                out= select_out
                aggregated_plan_votes = max(out)
                aggregated_plan_index = out.index(aggregated_plan_votes)
                aggregated_plan = plans_list[aggregated_plan_index]
                # check if it is really a valid one
                if '1.' in aggregated_plan and '2.' in aggregated_plan and '3.' in aggregated_plan and '4.' in aggregated_plan:
                    thought_map[key]['plan'] = aggregated_plan
        
        write_passage = get_text_passage_samples(task, x, thought_map[1]['plan'], args.n_generate_sample, stop=None)#args.n_generate_sample
        concate_message = []
        for message in write_passage:
            concate_message.append(thought_map[1]['plan'] + message)

        concate_message_prompt = task.vote_prompt_wrap('', concate_message)

        '''
        there is a technical concern that:
        results = gpt(aggregated_prompt, n=args.n_evaluate_sample, stop=None) where n_evaluate_sample = 5
        works fine with gpt-3.5-turbo. But for gpt-4, it seems that setting n = 5 blocks the results for coming out.
        To make it work smoothly, I set n = 1 and eval 5 times
        '''
        select_out = [0, 0, 0, 0, 0]
        for _ in range(args.n_evaluate_sample):
            one_results = gpt(concate_message_prompt, n=1, stop=None)
            one_out = task.vote_outputs_unwrap(one_results, len(concate_message))
            temp_list = []
            for result_idx in range(0, len(one_out)):
                temp_val = select_out[result_idx] + one_out[result_idx]
                temp_list.append(temp_val)
            select_out = temp_list

        out = select_out
        aggregated_plan_votes = max(out)
        aggregated_plan_index = out.index(aggregated_plan_votes)
        final_message = concate_message[aggregated_plan_index]
        infos = task.test_output(idx, final_message)

        thought_map_iter[step+1] = {'graph': deepcopy(thought_map), 'test_output': final_message, 'infos':infos}


    return infos, thought_map_iter


def naive_solve(args, task, idx, to_print=True):
    x = task.get_input(idx)  # input
    ys = get_samples(task, x, '', args.n_generate_sample, args.prompt_sample, stop=None)
    return ys, {}

def run(args):

    for run_iter in range(0, args.num_rum):
        task = get_task(args.task, args.task_file_path, args.difficulty, args.prompt_difficulty, args.shot, args.thought_steps)
        logs, cnt_avg, cnt_any = [], 0, 0
        global gpt
        gpt = partial(gpt, model=args.backend, temperature=args.temperature)
        if args.naive_run:
            file = f'logs/{args.task}/{args.prompt_sample}/{args.shot}/{args.difficulty}/promptlevel_{args.prompt_difficulty}/{run_iter}_{args.backend}_{args.temperature}_naive_sample_{args.n_generate_sample}_start{args.task_start_index}_end{args.task_end_index}.json'
        elif args.tot:
            file = f'logs/{args.task}/ToT/{args.prompt_sample}/{args.shot}/{args.difficulty}/promptlevel_{args.prompt_difficulty}/{run_iter}_{args.backend}_{args.temperature}_naive_sample_{args.n_generate_sample}_start{args.task_start_index}_end{args.task_end_index}.json'
        else:
            file = f'logs/{args.task}/TP/{args.prompt_sample}/{args.shot}/{args.difficulty}/promptlevel_{args.prompt_difficulty}/{run_iter}_{args.backend}_{args.temperature}_naive_sample_{args.n_generate_sample}_start{args.task_start_index}_end{args.task_end_index}.json'
            #f'logs/{args.task}/{args.backend}_{args.temperature}_{args.method_generate}{args.n_generate_sample}_{args.method_evaluate}{args.n_evaluate_sample}_{args.method_select}{args.n_select_sample}_start{args.task_start_index}_end{args.task_end_index}.json'
        os.makedirs(os.path.dirname(file), exist_ok=True)

        for i in range(args.task_start_index, args.task_end_index): # args.task_end_index
            # solve
            if args.naive_run:
                ys, info = naive_solve(args, task, i) 
                infos = [task.test_output(i, y) for y in ys]
                print(infos)
                info.update({'idx': i, 'ys': ys, 'infos': infos, 'usage_so_far': gpt_usage(args.backend)})
            elif args.tot:
                ys, info = tot_solve(args, task, i)
                infos = [task.test_output(i, y) for y in ys]
                print(infos)
                info.update({'idx': i, 'ys': ys, 'infos': infos, 'usage_so_far': gpt_usage(args.backend)})
            
            else:
                ys, info = got_solve_text(args, task, i)
                info.update({'idx': i, 'ys': ys, 'usage_so_far': gpt_usage(args.backend)})

            logs.append(info)
            with open(file, 'w') as f:
                json.dump(logs, f, indent=4)
            
            print('run', run_iter, i, 'cnt_avg', cnt_avg, 'cnt_any', cnt_any, '\n')
        
        n = args.task_end_index - args.task_start_index
        print(cnt_avg / n, cnt_any / n)
        print('usage_so_far', gpt_usage(args.backend))


def parse_args():
    args = argparse.ArgumentParser()
    args.add_argument('--backend', type=str, choices=['gpt-4', 'gpt-3.5-turbo', 'gpt-3.5-turbo-16k'], default='gpt-4')
    args.add_argument('--temperature', type=float, default=0.7)
    args.add_argument('--num_rum', type=int, default=1)

    args.add_argument('--task', type=str, required=True, choices=['text'])
    args.add_argument('--task_file_path', type=str, required=True)
    args.add_argument('--task_start_index', type=int, default=900)
    args.add_argument('--task_end_index', type=int, default=1000)
    args.add_argument('--difficulty', type=str, default='easy')
    args.add_argument('--thought_steps', type=int, default=2)

    args.add_argument('--naive_run', action='store_true')
    args.add_argument('--tot', action='store_true')
    args.add_argument('--shot', type=str, choices=['5-shot', '1-shot', '0-shot'])
    args.add_argument('--prompt_sample', type=str, choices=['standard', 'cot', 'bog'])  
    args.add_argument('--prompt_difficulty', type=str, default='easy') 

    args.add_argument('--method_generate', type=str, choices=['sample', 'propose'])
    args.add_argument('--method_evaluate', type=str, choices=['value', 'vote'])
    args.add_argument('--method_select', type=str, choices=['sample', 'greedy'])
    args.add_argument('--n_generate_sample', type=int, default=1)  # only thing needed if naive_run
    args.add_argument('--n_evaluate_sample', type=int, default=1)
    args.add_argument('--n_neighborhood_sample', type=int, default=5)
    args.add_argument('--n_select_sample', type=int, default=1)

    args = args.parse_args()
    return args



if __name__ == '__main__':
    args = parse_args()
    print(args)
    run(args)