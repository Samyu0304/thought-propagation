import json
import os
import numpy as np
Path = 'path to your json file that saves the results of thought propagation'
Iter_list = ['0', '1', '2']

def load_results_from_path(path, iter_list):
    f = open(path)
    data = json.load(f)
    num_data = len(data)

    total_cost = data[-1]['usage_so_far']['cost']

    for iter_key in iter_list:
        length_consistency_count = 0
        valid_path_count = 0
        success_path_count = 0
        exceed_count = 0
        optimal_rate = 0

        for i in range(num_data):
            one_data = data[i][iter_key]
            results = one_data['test_output']

            if results['r'] != 'Fail':
                valid_path_count += 1
                if results['r'] == 0:
                    optimal_rate += 1

                exceed_count += results['r']
                if results['length_consistency']:
                    length_consistency_count += 1
    
        print(optimal_rate/ num_data, valid_path_count / num_data, exceed_count / valid_path_count)
    
load_results_from_path(Path, Iter_list)