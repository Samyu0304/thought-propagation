import json
import os
import numpy as np
Dir = 'logs/shortest_path/standard/graph_modeling_language/5-shot/easy/promptlevel_easy'


def load_results_from_path(path):
    f = open(path)
    data = json.load(f)
    num_data = len(data)
    length_consistency_count = 0
    total_cost = data[-1]['usage_so_far']['cost']
    valid_path_count = 0
    success_path_count = 0
    exceed_count = 0
    optimal_rate = 0


    for i in range(num_data):
        one_data = data[i]
        results = one_data['infos'][0]
        #print(results)

        if results['r'] != 'Fail':
            valid_path_count += 1
            if results['r'] == 0:
                optimal_rate += 1

            exceed_count += results['r']
            if results['length_consistency']:
                length_consistency_count += 1
    
    return optimal_rate/ num_data, valid_path_count / num_data, exceed_count / valid_path_count, length_consistency_count / valid_path_count

json_files = [pos_json for pos_json in os.listdir(Dir) if pos_json.endswith('.json')]
val_path_rate_list, exceed_rate_list, optimal_rate_list = [], [], []

for file_name in json_files:
    path = os.path.join(Dir, file_name)
    optimal_rate, val_path_rate, exceed_rate, _ = load_results_from_path(path)
    val_path_rate_list.append(val_path_rate)
    exceed_rate_list.append(exceed_rate)
    optimal_rate_list.append(optimal_rate)

val_path_rate_list = np.array(val_path_rate_list)
exceed_rate_list = np.array(exceed_rate_list)
optimal_rate_list = np.array(optimal_rate_list)

print('OPtimal Rate (up):', np.mean(optimal_rate_list), '+-', np.std(optimal_rate_list))
print('Feasible Solution Rate (up):', np.mean(val_path_rate_list), '+-', np.std(val_path_rate_list))
print('Exceed Rate (low):', np.mean(exceed_rate_list), '+-', np.std(exceed_rate_list))
