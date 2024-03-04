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

# this function is to generate the next_node_candidate for tree of thought.
def get_proposals(task, x, y): 
    propose_prompt = task.propose_prompt_wrap(x, y)
    proposals = gpt(propose_prompt, n=1, stop=None)[0].split('\n')
    return [y + _ + '\n' for _ in proposals]


def get_neighborhood_evaluate(task, x, n_generate_sample, prompt_difficulty='easy', shot='0-shot'): # return neighborhood problem related to original problem
    if task.name == 'shortest_path':
        neighborhood_prompt = task.neigborhood_evaluate_prompt_wrap(x,prompt_difficulty=prompt_difficulty, shot=shot)
        neighborhood = gpt(neighborhood_prompt, n=n_generate_sample, stop=None)[0].split('\n')[-1]
        try:
            if 'already' in neighborhood:
                return -1
            #best_neighbor =  re.findall(r"Answer:\n(.*)", neighborhood)
            best_neighbor = re.findall(r"is (.*).", neighborhood)[0].split('.')[0]
            if 'node' in best_neighbor or 'Node' in best_neighbor:
                best_neighbor = best_neighbor.split(' ')[-1]
            if best_neighbor[-1] < '0' or best_neighbor[-1] > '9':
                best_neighbor = best_neighbor[1:-1]
            best_neighbor = int(best_neighbor)
            return best_neighbor
        except:
            return neighborhood
    else:
        raise ValueError('text')

# tree-of-thought goes here
def tot_solve(args, task, idx, to_print=True):
    x = task.get_input(idx)  # input
    # use re to parse source node and target node

    source_node = re.findall(r"Source Node:(.+?) Target Node:", x)
    if source_node != []:
        source_node = source_node[0]
    else:
        source_node = re.findall(r"Source Node:(.+?)\nTarget Node:", x)[0]
    # print(re.findall(r"Target Node:(.+)", x), re.findall(r"Target Node:(.+)", x)[0])
    target_node = re.findall(r"Target Node:(.+)", x)[0]
    source_node = source_node.replace(' ','')
    source_node = source_node.replace('\n','')
    target_node = target_node.replace(' ','')
    target_node = target_node.replace('\n','')
    print(source_node, target_node)

    if args.graph_encoding == 'vallina':
        node_and_edge_desc = re.findall(r"(.+?)Edge distance", x)[0]
        node_and_edge_and_dist_desc = re.findall(r"(.+?)Source Node", x)[0]
    elif args.graph_encoding == 'edge_description':
        cutoff_index = x.find('Source Node')
        node_and_edge_and_dist_desc = x[:cutoff_index-2]
        #print('original_node_and_edge_and_dist_desc', node_and_edge_and_dist_desc)
        node_and_edge_desc = node_and_edge_and_dist_desc
        # delete the distance information to construct node_and_edge_desc
        delete_handel = re.findall(r' with distance.*?\d', node_and_edge_desc)
        for handel in delete_handel:
            if handel in node_and_edge_desc:
                node_and_edge_desc = node_and_edge_desc.replace(handel, '')
    elif args.graph_encoding == 'graph_modeling_language':
        cutoff_index = x.find('Source Node')
        node_and_edge_and_dist_desc = x[:cutoff_index-2]

        # similar to what we do in edge_description to obtain node_and_edge_desc
        node_and_edge_desc = node_and_edge_and_dist_desc
        delete_handel = re.findall(r' with distance.*?\d', node_and_edge_desc)
        for handel in delete_handel:
            if handel in node_and_edge_desc:
                node_and_edge_desc = node_and_edge_desc.replace(handel, '')


    init_solution = get_node_solution(task, x, '', args.n_generate_sample, args.prompt_sample, stop=None)#naive_solve(args, task, idx) # get_node_silution
    init_solution = task.node_solution_prompt_warp(init_solution, source_node, target_node, args.prompt_sample)
    #print(x)
    #print(init_ys)
    print(init_solution, source_node, target_node)
    warpped_init_solution_for_test = task.warp_got_output(init_solution, source_node, target_node)
    test_result = task.test_output(idx, warpped_init_solution_for_test)#args.prompt_sample
    
    path = [int(source_node)]
    count = 0
    node_set = task.get_node_set(idx)

    record_nei = {}
    
    while(path[-1] != int(target_node) and count <= len(node_set)):
        nei_node_problem = get_neighborhood_problem(task, node_and_edge_desc, str(path[-1]), n_generate_sample=1)
        try:
            nei_node_problem = re.findall(r"is (.*).",nei_node_problem)[0]
            nei_node_problem = nei_node_problem.replace('[', '')
            nei_node_problem = nei_node_problem.replace(']', '')
            nei_node_problem = nei_node_problem.replace(' ', '')
            nei_node_list = nei_node_problem.split(',')
            nei_node_list = [int(j) for j in nei_node_list]
        except:
            record_nei[str(count)] = nei_node_problem
            return [init_solution, record_nei, path]
        
        if int(source_node) in nei_node_list:
            nei_node_list.remove(int(source_node))
        record_nei[str(count)] = nei_node_list
        
        if args.nei_tar:
            if int(target_node) in nei_node_list:
                path.append(int(target_node))
                return [init_solution, record_nei, path]
            
        if 'Source Node:' + source_node in x:
            x_with_alter_input = x.replace('Source Node:' + source_node, 'Input Nodes: ' + str(nei_node_list))
        elif 'Target Node: ' + target_node in x:
            x_with_alter_input = x.replace('Source Node: ' + source_node, 'Input Nodes: ' + str(nei_node_list))
        else:
            print('Unrecognized neighborhood handle. Pass to next round')
            continue

        best_neighbor = get_neighborhood_evaluate(task, x_with_alter_input, n_generate_sample=1, prompt_difficulty = args.prompt_difficulty, shot = args.shot)
        
        if type(best_neighbor) is not int:
            path.append(best_neighbor)
            return [init_solution, record_nei, path]
        elif best_neighbor == -1:
            path.append(int(target_node))
        else:
            path.append(best_neighbor)
        count += 1
    
    return [init_solution, record_nei, path]

# get shortest path results using base reasoning methods
def get_shortest_path_samples(task, x, y, n_generate_sample, prompt_sample, stop):
    if prompt_sample == 'standard':
        prompt = task.standard_prompt_wrap(x, y, task.prompt_difficulty, task.shot)
    elif prompt_sample == 'cot':
        prompt = task.cot_prompt_wrap(x, y, task.prompt_difficulty, task.shot)
    elif prompt_sample == 'bog':
        prompt = task.bog_prompt_wrap(x, y, task.prompt_difficulty, task.shot)
    else:
        raise ValueError(f'prompt_sample {prompt_sample} not recognized')
    samples = gpt(prompt, n=n_generate_sample, stop=stop)
    return [y + _ for _ in samples]

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
    if task.name == 'shortest_path':
        neighborhood_prompt = task.neigborhood_propose_prompt_wrap(x, central_node)
        neighborhood = gpt(neighborhood_prompt, n=n_generate_sample, stop=None)[0].split('\n')[-1]
    return neighborhood


def get_node_solution(task, x, y, n_generate_sample, prompt_sample, stop):
    if task.name == 'shortest_path':
        node_solution = get_shortest_path_samples(task, x, y, n_generate_sample, prompt_sample, stop)[0].split('\n')[-1]
    return node_solution

def get_neighborhood_aggregation(task, x, node_and_edge_and_dist_desc, neighborhood_solution_list, source_node, target_node, eval_one_by_one): 
    if not eval_one_by_one:
        aggregated_input = task.neighborhood_aggregation_prompt_warp(neighborhood_solution_list, x, node_and_edge_and_dist_desc, source_node, target_node)
        aggregated_result = gpt(aggregated_input, n=1, stop=None)[0].split('\n')[-1]
    else:
        neighborhood_input_list = task.one_by_one_neighborhood_aggregation_input_warp(neighborhood_solution_list, x, node_and_edge_and_dist_desc, source_node, target_node)
        neighborhood_output_prompt_list = []
        for neighborhood_input in neighborhood_input_list:
            neighborhood_output = gpt(neighborhood_input, n=1, stop=None)[0].split('\n')[-1]
            neighborhood_output_prompt_list.append(neighborhood_output)
        
        neighborhood_output_prompt_list = [i.strip('Using the above hints,') for i in neighborhood_output_prompt_list]
        neighborhood_output_prompt_list = [i.strip('using the above hints,') for i in neighborhood_output_prompt_list]

        num_neighborhood_count = len(neighborhood_output_prompt_list)
        neighborhood_output_prompt_warp = task.one_by_one_neighborhood_aggregation_eval_warp(neighborhood_output_prompt_list, x, node_and_edge_and_dist_desc, source_node, target_node)
        neighborhood_output_index_pred = gpt(neighborhood_output_prompt_warp, n=5, stop=None)

        output_index = task.vote_outputs_unwrap(neighborhood_output_index_pred, num_neighborhood_count)

        if output_index == []:
            max_vote_result = 'No result.'
        else:
            max_vote_value = max(output_index)
            max_vote_index = output_index.index(max_vote_value)
            max_vote_result = neighborhood_output_prompt_list[max_vote_index]
        aggregated_result = max_vote_result

    return aggregated_result

def get_readout(task, x, node_and_edge_and_dist_desc, key, target_node, original_solution, aggregated_solution):
    readout_input = task.readout_prompt_warp(x, node_and_edge_and_dist_desc, key, target_node, original_solution, aggregated_solution)
    readout_result = gpt(readout_input, n=1, stop=None)[0].split('\n')[-1]

    return readout_result

# thought propagation goes here, we initially named tp as got.
def got_solve_shortestpath(args, task, idx, to_print=True):

    x = task.get_input(idx)  # input
    source_node = re.findall(r"Source Node:(.+?) Target Node:", x)
    if source_node != []:
        source_node = source_node[0]
    else:
        source_node = re.findall(r"Source Node:(.+?)\nTarget Node:", x)[0]
    # print(re.findall(r"Target Node:(.+)", x), re.findall(r"Target Node:(.+)", x)[0])
    target_node = re.findall(r"Target Node:(.+)", x)[0]
    source_node = source_node.replace(' ','')
    source_node = source_node.replace('\n','')
    target_node = target_node.replace(' ','')
    target_node = target_node.replace('\n','')
    
    if args.graph_encoding == 'vallina':
        node_and_edge_desc = re.findall(r"(.+?)Edge distance", x)[0]
        node_and_edge_and_dist_desc = re.findall(r"(.+?)Source Node", x)[0]
    elif args.graph_encoding == 'edge_description':
        cutoff_index = x.find('Source Node')
        node_and_edge_and_dist_desc = x[:cutoff_index-2]
        #print('original_node_and_edge_and_dist_desc', node_and_edge_and_dist_desc)
        node_and_edge_desc = node_and_edge_and_dist_desc
        # delete the distance information to construct node_and_edge_desc
        delete_handel = re.findall(r' with distance.*?\d', node_and_edge_desc)
        for handel in delete_handel:
            if handel in node_and_edge_desc:
                node_and_edge_desc = node_and_edge_desc.replace(handel, '')
    elif args.graph_encoding == 'graph_modeling_language':
        cutoff_index = x.find('Source Node')
        node_and_edge_and_dist_desc = x[:cutoff_index-2]

        # similar to what we do in edge_description to obtain node_and_edge_desc
        node_and_edge_desc = node_and_edge_and_dist_desc
        delete_handel = re.findall(r' with distance.*?\d', node_and_edge_desc)
        for handel in delete_handel:
            if handel in node_and_edge_desc:
                node_and_edge_desc = node_and_edge_desc.replace(handel, '')
           
    feasible_node = [str(i) for i in range(int(target_node))]

    init_solution = get_node_solution(task, x, '', args.n_generate_sample, args.prompt_sample, stop=None)
    init_solution = task.node_solution_prompt_warp(init_solution, source_node, target_node, args.prompt_sample)
    warpped_init_solution_for_test = task.warp_got_output(init_solution, source_node, target_node)
    test_result = task.test_output(idx, warpped_init_solution_for_test)#args.prompt_sample
    thought_map = {target_node:{'solution': init_solution, 'neighborhood': None}} # node:{'solution': solution, 'neigborhood':[]}

    thought_map_iter = {} # {key=iteration, val = thought_map}
    thought_map_iter[0] = {'graph': deepcopy(thought_map), 'test_output': test_result}

    print(thought_map_iter)
    path_validity_handle = 'The shortest path from the source node to the target node is'
    length_validity_handle = 'The shortest distance is'
    
    for step in range(task.steps):
        # neighborhood generation and neighborhood solution
        for key, value in thought_map.copy().items():
            #print(key, value)
            if value['neighborhood'] == None:
                nei_node_problem = get_neighborhood_problem(task, node_and_edge_desc, key, n_generate_sample=1)
                nei_node_problem = re.findall('\[.+?\]',nei_node_problem)
                if nei_node_problem == []:
                    print('NO Neighborhood Node Found!')
                    continue
                else:
                    nei_node_problem = nei_node_problem[0]
                    nei_node_problem = nei_node_problem.replace('[', '')
                    nei_node_problem = nei_node_problem.replace(']', '')
                    nei_node_problem = nei_node_problem.replace(' ', '')
                    nei_node_problem = nei_node_problem.split(',')
                    # drop the source node in the thought graph
                    if source_node in nei_node_problem:
                        nei_node_problem.remove(source_node)

                    if len(nei_node_problem) >= 1:
                        value['neighborhood'] = nei_node_problem
                        for nei_node in nei_node_problem:
                            if nei_node not in thought_map and nei_node != source_node:
                                # print(x)
                                if 'Target Node:'+target_node in x:
                                    x_with_alter_target = x.replace('Target Node:'+target_node, 'Target Node:'+nei_node)
                                elif 'Target Node: '+target_node in x:
                                    x_with_alter_target = x.replace('Target Node: '+target_node, 'Target Node: '+nei_node)
                                else:
                                    print('Unrecognized neighborhood handle. Pass to next round')
                                    continue

                                neighborhood_solution = get_node_solution(task, x_with_alter_target, '', args.n_generate_sample, args.prompt_sample, stop=None)
                                #print(neighborhood_solution)
                                # when test with cot method, we find the parsed results start with 'The', thus, we change into .lower() when doing experiemnts for rebuttal
                                neighborhood_solution = neighborhood_solution.lower()
                                path_validity_handle = path_validity_handle.lower()
                                length_validity_handle = length_validity_handle.lower()
                                
                                # drop the undesired format of neighborhood solutions for valid prompt method
                                if neighborhood_solution.find(path_validity_handle) != -1 and neighborhood_solution.find(length_validity_handle) != -1:
                                    neighborhood_solution = task.node_solution_prompt_warp(neighborhood_solution, source_node, nei_node, args.prompt_sample)
                                    #print(neighborhood_solution)
                                    thought_map[nei_node] = {'solution':neighborhood_solution, 'neighborhood': None}
        
        # neighborhood aggregation and readout
        key_list = list(thought_map.copy().keys())
        key_list.reverse()
        #reversed_thought_map = dict(reversed(list(thought_map.copy().items())))
        for key in key_list:
            if thought_map[key]['neighborhood'] != None:
                #print(thought_map)
                # aggregation
                neighborhood_idx_list = thought_map[key]['neighborhood']
                neighborhood_solution_list = [thought_map[i]['solution'] for i in neighborhood_idx_list if i in thought_map] # .copy()
                neighborhood_agg_solution = get_neighborhood_aggregation(task, x, node_and_edge_and_dist_desc, neighborhood_solution_list, source_node, key, eval_one_by_one = args.eval_one_by_one)
                print('neighborhood_agg:', neighborhood_agg_solution)
                # readout
                original_solution = thought_map[key]['solution']
                readout_solution = get_readout(task, x, node_and_edge_and_dist_desc, key, target_node, original_solution, neighborhood_agg_solution) # key is the target node and source node is 0
                print('readout_func:', readout_solution)
                warpped_readout_solution = task.warp_readout_output(readout_solution)
                #print(warpped_readout_solution)
                if warpped_readout_solution != None:
                    thought_map[key]['solution'] = warpped_readout_solution

        warpped_readout_solution_for_test = task.warp_got_output(thought_map[target_node]['solution'], source_node, target_node)
        test_result = task.test_output(idx, warpped_readout_solution_for_test)#, args.prompt_sample
        
        thought_map_iter[step+1] = {'graph': deepcopy(thought_map), 'test_output': test_result}
        print(thought_map_iter)

    warpped_final_solution_for_test = task.warp_got_output(thought_map[target_node]['solution'], source_node, target_node)
    return [warpped_final_solution_for_test], thought_map_iter  # ys is the results of last iter

def naive_solve(args, task, idx, to_print=True):
    x = task.get_input(idx)  # input
    print(x)
    ys = get_shortest_path_samples(task, x, '', args.n_generate_sample, args.prompt_sample, stop=None)
    return ys, {}

def run(args):

    for run_iter in range(0, args.num_rum):
        task = get_task(args.task, args.task_file_path, args.difficulty, args.prompt_difficulty, args.shot, args.thought_steps)
        logs, cnt_avg, cnt_any = [], 0, 0
        global gpt
        gpt = partial(gpt, model=args.backend, temperature=args.temperature)
        if args.naive_run:
            file = f'logs/{args.task}/{args.prompt_sample}/{args.graph_encoding}/{args.shot}/{args.difficulty}/promptlevel_{args.prompt_difficulty}/{run_iter}_{args.backend}_{args.temperature}_naive_sample_{args.n_generate_sample}_start{args.task_start_index}_end{args.task_end_index}.json'
        elif args.tot:
            file = f'logs/{args.task}/ToT/{args.prompt_sample}/{args.graph_encoding}/{args.shot}/{args.difficulty}/promptlevel_{args.prompt_difficulty}/{run_iter}_{args.backend}_{args.temperature}_naive_sample_{args.n_generate_sample}_start{args.task_start_index}_end{args.task_end_index}.json'
        else:
            # tp-settings: eval the neighborhood one by one/ eval them altogether; use IO / CoT as the base reasoner.
            if args.eval_one_by_one:
                file = f'logs/{args.task}/TP/{args.prompt_sample}/{args.graph_encoding}/{args.shot}/{run_iter}_{args.backend}_{args.temperature}_eval_one_by_one_{args.n_generate_sample}_start{args.task_start_index}_end{args.task_end_index}.json'
            else:
                file = f'logs/{args.task}/TP/{args.prompt_sample}/{args.graph_encoding}/{args.shot}/{run_iter}_{args.backend}_{args.temperature}_eval_together_{args.n_generate_sample}_start{args.task_start_index}_end{args.task_end_index}.json'
        
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

            else: # instantiate Thought Propagation
                ys, info = got_solve_shortestpath(args, task, i)
                infos = [task.test_output(i, y) for y in ys]
                print(infos)
                info.update({'idx': i, 'ys': ys, 'infos': infos, 'usage_so_far': gpt_usage(args.backend)})

            logs.append(info)
            with open(file, 'w') as f:
                json.dump(logs, f, indent=4)
            
            print('run', run_iter, i, 'cnt_avg', cnt_avg, 'cnt_any', cnt_any, '\n')
        
        n = args.task_end_index - args.task_start_index
        print(cnt_avg / n, cnt_any / n)
        print('usage_so_far', gpt_usage(args.backend))


def parse_args():
    args = argparse.ArgumentParser()
    args.add_argument('--backend', type=str, choices=['gpt-4', 'gpt-3.5-turbo', 'gpt-3.5-turbo-16k'], default='gpt-3.5-turbo')
    args.add_argument('--temperature', type=float, default=0.7)
    args.add_argument('--num_rum', type=int, default=1)

    args.add_argument('--task', type=str, required=True, choices=['shortest_path'], default='shortest_path')
    args.add_argument('--graph_encoding', type=str, required=True, 
                      choices=['vallina','edge_description','graph_modeling_language'], 
                      default='graph_modeling_language')
    args.add_argument('--task_file_path', type=str, required=True)
    args.add_argument('--task_start_index', type=int, default=0) # text: start from 900 and end by 1000
    args.add_argument('--task_end_index', type=int, default=100)
    args.add_argument('--difficulty', type=str, default='easy')
    args.add_argument('--thought_steps', type=int, default=2)

    args.add_argument('--naive_run', action='store_true')
    args.add_argument('--tot', action='store_true')
    args.add_argument('--shot', type=str, choices=['5-shot', '1-shot', '0-shot'])
    args.add_argument('--eval_one_by_one', action='store_true') 

    # only used when method_generate = sample, or naive_run
    # in rebuttal the reviewer also raise the questions if CoT can work with TP, thus, we set ['standard', 'cot'] 
    # also, since CoT prompting is longer than IO prompting, we additionally introduce eval-one-by-one to avoid exceeding token limits
    args.add_argument('--prompt_sample', type=str, choices=['standard', 'cot', 'bog'])  
    args.add_argument('--prompt_difficulty', type=str, default='easy') 

    # tot params not used in the shortest path reasoning task.
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
    GRAPH_ENCODING = args.graph_encoding
    run(args)