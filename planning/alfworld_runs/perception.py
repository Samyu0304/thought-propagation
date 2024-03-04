'''
This file contains neighborhood problem proposal (seaching relevant problem)
For each problem in the same type of environments, the LLm outputs a score ranging from 0-10 (low to high relevance)
The top-k relevant problems with successful decision trails are employed to help LLM to generate some reflections.
Then, the generated reflections, together with self-reflecion, are fed into LLM to rethink it stategies for decition-making.
'''
from alfworld_runs.utils import get_completion # as what we did before, get completion is a 
from typing import List, Dict, Any
import json
from operator import itemgetter

# a mapping dict maps the env_idx into 6 categories.
# we first consider finding relevant envs of the same category.
SPLIT_DICT = {
    'put': [3, 7, 13, 15, 16, 18, 32, 34, 35, 39, 44, 48, 53, 55, 65, 70, 76, 83, 86, 95, 97, 102, 126, 127], 
    'clean': [1, 2, 4, 17, 29, 41, 43, 46, 47, 54, 56, 58, 60, 63, 64, 67, 68, 79, 82, 101, 103, 107, 108, 109, 110, 111, 114, 118, 124, 125, 132], 
    'heat': [5, 11, 19, 20, 24, 26, 27, 28, 36, 37, 38, 52, 57, 59, 75, 77, 90, 100, 104, 106, 116, 123, 131], 
    'cool': [0, 9, 10, 12, 14, 22, 30, 31, 49, 50, 66, 69, 81, 84, 87, 88, 89, 94, 96, 98, 128], 
    'examine': [6, 8, 21, 25, 45, 71, 78, 85, 91, 92, 93, 117, 119, 121, 122, 129, 130, 133], 
    'puttwo': [23, 33, 40, 42, 51, 61, 62, 72, 73, 74, 80, 99, 105, 112, 113, 115, 120]
    }

with open("./alfworld_runs/reflexion_few_shot_examples.txt", 'r') as f:
    FEW_SHOT_EXAMPLES = f.read()

with open('OB_DICT.json', 'r') as f:
    OB_DICT = json.load(f)

with open('./alfworld_runs/got_message_few_shot_examples.txt', 'r') as f:
    GOT_FEW_SHOT_EXAMPLES = f.read()


def _get_nei_senarios(env_id: int, num_nei: int, success_list: List[int]) -> List:

    similar_env_name = str()
    for key, value in SPLIT_DICT.items():
        if env_id in value:
            similar_env_name = key

    similar_env_collection = SPLIT_DICT[similar_env_name]
    similar_env_collection = [str(i) for i in similar_env_collection]
    # filter out successful solved envs
    # print(success_list)
    intersection_envs = list(set(success_list) & set(similar_env_collection))
    # intersection_envs.remove(env_id)
    # print(intersection_envs)
    cur_env_ob = OB_DICT[str(env_id)]

    score_list = []

    for i in intersection_envs:
        nei_env_ob = OB_DICT[str(i)]
        query: str = f"""Evaluate the similarity score between these two cases. The similarity score should be an integer bewteen 0 and 10. 0 indicates least similarity and 10 indicates most similarity.
Case 1:
{cur_env_ob}
Case 2:
{nei_env_ob}
The output format should be: The similarity score is:
"""
        query = get_completion(query)
        #print(query)
        if query.endswith('.'):
            score = query[-2]
        else:
            score = query[-1]
        try:
        
            score = int(score)
        except:
            score = 0
        
        score_list.append(score)
    
    #print(score_list)
    
    num_score = len(score_list)
    num_sample = min(num_score, num_nei)
    index_val_tuple = list(sorted(enumerate(score_list), key = itemgetter(1)))[-num_sample:]
    index = [i[0] for i in index_val_tuple]
    # use the index to retrive
    selected_env_id = [intersection_envs[i] for i in index]
    selected_env_ob = [OB_DICT[i] for i in selected_env_id]

    return selected_env_id, selected_env_ob


def _generate_message(env_id: int, log_str: str, env_logs: List, success_list: List[int], successful_trail_dict, num_nei: int, use_simulation: bool) -> str:
    """Allows the Agent to reflect upon a past experience."""
    # env_id: int, num_nei: int, success_list: List[int]
    selected_env_id, selected_env_ob = _get_nei_senarios(env_id, num_nei, success_list)
    #print(selected_env_id, selected_env_ob)
    # get source problem and enigbhorhood successful problem
    message_list = []
    for nei_env_id, nei_env_senario in zip(selected_env_id, selected_env_ob):
        nei_success_log = successful_trail_dict[nei_env_id]

        query: str = f"""You will be given a successful case where you successfully complete the task. Then you will be given a failure case where you fail to complete the task. Do not summarize these two cases, but rather use the successful case to think about the strategy and path you took to attempt to complete the task in the failure case. Devise a concise, new plan of action that accounts for your mistake with reference to specific actions that you should have taken. For example, if you tried A and B but forgot C, then devise a plan to achieve C with environment-specific actions. You will need this later to solve the failure case. Give your plan after "Plan".
Success Case:
{nei_success_log}
Failure Case:
{log_str}
Plan:
"""
        one_message = get_completion(query)
        # print(one_message)
        message_list.append(one_message)
    # message_list
    summarized_message = []
    if len(message_list) > 0:
        #summarized_message += '\n\nPlans from successful attempts in similar tasks:\n'
        for i, m in enumerate(message_list):
            summarized_message.append('\n\nPlans from successful attempts in similar tasks:\n' + f'Plan #{i}: {m}\n')

    if not use_simulation: # eval the best plan using llms.
        # evaluate then output
        if len(message_list) > 1:

            stringrize_message = summarized_message[0]
            num_plans = len(stringrize_message)
            for i in range(1, num_plans):
                stringrize_message += stringrize_message[i]

            query: str = f"""You once fail to accomplish the following task.
            The task is: {log_str}
            Here are several plans to accomplish the task:
            {stringrize_message}
            Output the most promising plan to accomplish the task, but do not output any irrelevant messages. Your answer goes after Plan:.
            Plan:
            """
        summarized_message = [get_completion(query)]
    #query += '\n\nNew plan:'
    
    print(selected_env_id)
    print(summarized_message)
    return selected_env_id, summarized_message


def update_message(trial_log_path: str, successful_trail_path: str, num_nei: int, use_simulation: bool) -> List[Dict[str, Any]]:
    """Updates the given env_config with the appropriate reflections."""
    with open(trial_log_path, 'r') as f:
        full_log: str = f.read()
        
    env_logs: List[str] = full_log.split('#####\n\n#####')
    # read successful_mask
    env_num = len(env_logs)
    success_list = []
    neighborhood_message_dict = {}

    with open(successful_trail_path) as f:
        successful_trail_dict = json.load(f)
        f.close()
    
    for key, val in successful_trail_dict.items():
        if val != []:
            success_list.append(key)
    
    #print(success_list)
    
    for i, env in enumerate(env_logs):
        # if unsolved, get reflection and update env config
        
        #print(env)
        if str(i) not in success_list:
            try:
                neighborhood_idx, neighborhood_message = _generate_message(i, env_logs[i], env_logs, success_list, successful_trail_dict, num_nei, use_simulation)
                #print(neighborhood_idx)
                #print(neighborhood_message)
                neighborhood_message_dict[i] = {}
                neighborhood_message_dict[i]['nei_message'] = neighborhood_message
                neighborhood_message_dict[i]['nei_idx'] = neighborhood_idx
            except:
                neighborhood_message_dict[i] = {}
                neighborhood_message_dict[i]['nei_message'] = 'PASS'

        
        else:
            neighborhood_message_dict[i] = {}
            neighborhood_message_dict[i]['nei_message'] = 'SUCCESS'

                
    return neighborhood_message_dict


def update_successful_trail(trial_log_path, successful_trail_path):
    with open(trial_log_path, 'r') as f:
        new_trail = f.read()
        new_trail = new_trail.split('#####\n\n#####')
    
    # read successful trails
    f = open(successful_trail_path)
    successful_trail = json.load(f)
    f.close()

    # merge the successful trail
    for i in range(0, 134):
    #trail_dict[i] = []
        if 'STATUS: OK' in new_trail[i]:
            target_str = new_trail[i].split('\n\n')[-3]
            output_list = target_str.split('\n')
            try:
                answer_start_idx = output_list.index('Here is the task:')
                answer_list = output_list[answer_start_idx+1:]
                answer_output = str()
                for s in answer_list:
                    answer_output += s + '\n'
                #print(answer_output)
                successful_trail[i] = answer_output
            except:
                successful_trail[i] = []

    return successful_trail



    
