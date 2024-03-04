import re
import os
import sympy
import pandas as pd
from tasks.base import Task, DATA_PATH
# prompts
#from run import GRAPH_ENCODING
GRAPH_ENCODING = 'graph_modeling_language'
if GRAPH_ENCODING == 'vallina':
    from prompts.shortest_path import *
elif GRAPH_ENCODING == 'edge_description':
    from prompts.shortest_path_edge_description import *
elif GRAPH_ENCODING == 'graph_modeling_language':
    from prompts.shortest_path_graph_modeling_language import *

import json
import networkx as nx

class ShortestPath(Task):
    def __init__(self, promblem_difficulty = 'easy', prompt_difficulty = 'easy', shot = '5-shot', steps=2):
        self.dir = 'data/shortest_path/' + promblem_difficulty
        self.prompt_difficulty = prompt_difficulty
        self.shot = shot
        self.name = 'shortest_path'
        self.file_list = self.get_json_list()
        self.n = len(self.file_list)
        #self.cache = {}
        self.idx = None
        self.times = 0
        self.steps = steps
        #self.prompt_status_cache = {}
        self.graph_encoding = GRAPH_ENCODING
            
    def get_json_list(self):
        file_list = os.listdir(self.dir)
        file_list.sort()
        return file_list

    def __len__(self):
        return self.n
    
    def get_shortest_dist(self, idx: int):
        path = str(idx) + '.json'
        json_path = os.path.join(self.dir, path)
        f = open(json_path)
        data = json.load(f)
        f.close()
        distance = data["shortest_length"]
        
        return distance
    
    def get_pairwise_path(self, path_str: str):
        path_str = path_str.replace('[', '')
        path_str = path_str.replace(']', '')
        path_list = path_str.split(',')
        print(path_list)
        path_list = [int(i) for i in path_list]

        source_path = path_list[0]
        target_path = path_list[-1]
        path_length = len(path_list)
        pairwise_path_list = []
        for i in range(path_length-1):
            if path_list[i]<path_list[i+1]:
                pairwise_path_list.append([path_list[i], path_list[i+1]])
            else:
                pairwise_path_list.append([path_list[i+1], path_list[i]])
        
        return source_path, target_path, pairwise_path_list
  
    def check_feasible(self, idx: int, path_str: str):
        # a path is feasible iff all edges exist in original graph and from source to target
        path = str(idx) + '.json'
        json_path = os.path.join(self.dir, path)
        f = open(json_path)
        data = json.load(f)
        f.close()
        edges = data["edges"]
        nodes = data["nodes"]
        source_node = min(nodes)
        target_node = max(nodes)
        # check source and target
        source_path, target_path, pairwise_path_list = self.get_pairwise_path(path_str)
        source_match = source_node == source_path

        target_match = target_node == target_path
        edge_match = [edge_pair in edges for edge_pair in pairwise_path_list]
        edge_match = False in edge_match
        edge_match = not edge_match

        return edge_match & source_match & target_match

    def get_true_length(self, idx, path_str):
        _, _, pairwise_path_list = self.get_pairwise_path(path_str)
        path = str(idx) + '.json'
        json_path = os.path.join(self.dir, path)
        f = open(json_path)
        data = json.load(f)
        f.close()

        edge_set = data['edges']
        distances_set = data['distance']

        path_length = 0
        for pair_edge in pairwise_path_list:
            if pair_edge[0]>pair_edge[1]:
                pair_edge = [pair_edge[1], pair_edge[0]]

            pair_index = edge_set.index(pair_edge)
            path_length += distances_set[pair_index]
        
        return path_length

    def get_input(self, idx: int):
        path = str(idx) + '.json'
        json_path = os.path.join(self.dir, path)
        f = open(json_path)
        data = json.load(f)
        f.close()

        node_set = data['nodes']
        source_node = min(node_set)
        target_node = max(node_set)
        edge_set = data['edges']
        distances_set = data['distance']
        input_str = self.stringrize_graph_input(node_set, edge_set, distances_set, source_node, target_node)
        
        return input_str

    def stringrize_graph_input(self, node_set, edge_set, distances_set, source_node, target_node):
        if self.graph_encoding == 'vallina':
            output_string = self.cvt_input_to_vallina(node_set, edge_set, distances_set, source_node, target_node)
        elif self.graph_encoding == 'edge_description':
            output_string = self.cvt_input_to_edge_description(node_set, edge_set, distances_set, source_node, target_node)
        elif self.graph_encoding == 'graph_modeling_language':
            output_string = self.cvt_input_to_graph_modeling_language(node_set, edge_set, distances_set, source_node, target_node)
        else:
            raise AssertionError('Graph Encoding Method not Implemented.')

        return output_string
    
    def cvt_input_to_vallina(self, node_set, edge_set, distances_set, source_node, target_node):
        blank_space = ' '
        output_string = 'Node Set:' + blank_space + str(node_set) + blank_space + 'Edge Set:' + blank_space + str(edge_set) + blank_space + 'Edge distance:' + blank_space + str(distances_set) + blank_space + 'Source Node:' + str(source_node) + blank_space + 'Target Node:' + str(target_node) + blank_space

        return output_string
    
    def cvt_input_to_edge_description(self, node_set, edge_set, distances_set, source_node, target_node):
        node_set = node_set
        edge_set = edge_set
        edge_distance_set = distances_set

        # source and target
        source_node = source_node
        target_node = target_node

        output_string = "In an undirected graph, the nodes are numbered from 0 to {},".format(max(node_set))
        output_string += " and the edges are:\n"

        for i, edge in enumerate(edge_set):
            output_string += "an edge between node {} and node {} with distance {},\n".format(edge[0], edge[1], edge_distance_set[i])

        output_string = output_string[:-2]  # 去除最后一个逗号
        output_string += ".\n\n"
        output_string += "Source Node: {}\n".format(source_node)
        output_string += "Target Node: {}".format(target_node)

        return output_string
    
    def cvt_input_to_graph_modeling_language(self, node_set, edge_set, distances_set, source_node, target_node):
        node_set = node_set
        edge_set = edge_set
        edge_distances_set = distances_set
        source_node = source_node
        target_node = target_node
        output_string = "Input:\ngraph[\n    comment \"This is an undirected graph.\"\n"
        for node in node_set:
            output_string += f"    node [id {node}]\n"
        
        for i, edge in enumerate(edge_set):
            output_string += f"    edge [label \"Edge between node {edge[0]} and node {edge[1]} with distance {edge_distances_set[i]}\"]\n"
            
        output_string += "]\n\n"
        output_string += "Source Node: {}\n".format(source_node)
        output_string += "Target Node: {}\n".format(target_node)

        return output_string

    
    @staticmethod
    def standard_prompt_wrap(x: str, y:str='', prompt_difficulty='easy', shot='5-shot') -> str:
        if prompt_difficulty == 'easy':
            if shot == '5-shot':
                return standard_prompt_easy_5shot.format(input=x) + y
            elif shot == '1-shot':
                return standard_prompt_easy_1shot.format(input=x) + y
            elif shot == '0-shot':
                return standard_prompt_easy_zeroshot.format(input=x) + y
    
    @staticmethod
    def cot_prompt_wrap(x: str, y:str='', prompt_difficulty='easy', shot='5-shot') -> str:
        if prompt_difficulty == 'easy':
            if shot == '5-shot':
                return cot_prompt_easy_5shot.format(input=x) + y
            elif shot == '1-shot':
                return cot_prompt_easy_1shot.format(input=x) + y
            elif shot == '0-shot':
                return cot_prompt_easy_zeroshot.format(input=x) + y
    
    @staticmethod
    def bog_prompt_wrap(x: str, y:str='', prompt_difficulty='easy', shot='1-shot') -> str:
        if prompt_difficulty == 'easy':
            if shot == '1-shot':
                return bog_prompt_easy_1shot.format(input=x) + y
            elif shot == '0-shot':
                return bog_prompt_easy_zeroshot.format(input=x) + y
            elif shot == '5-shot':
                return bog_prompt_easy_5shot.format(input=x) + y
    
    @staticmethod
    def neigborhood_evaluate_prompt_wrap(x: str, prompt_difficulty='easy', shot='0-shot') -> str:
        if prompt_difficulty == 'easy': 
            if shot == '0-shot':
                return neigborhood_evaluate_prompt_easy_zeroshot.format(input=x) 
            if shot == '1-shot':
                return neigborhood_evaluate_prompt_1shot.format(input=x)
            if shot == '5-shot':
                return neigborhood_evaluate_prompt_5shot.format(input=x)
    
    # mainly 3 steps in GoT pipeline, 1. find neighborhood problem; 2. solve neighborhood problem; 2. aggregate neighborhood solution to original problem.
    @staticmethod
    def neigborhood_propose_prompt_wrap(node_edge: str,  central_node: str, prompt_difficulty='easy') -> str:
        return neigborhood_propose_prompt.format(input=node_edge) + central_node
        
    @staticmethod
    def node_solution_prompt_warp(solution, source_node, target_node, prompt_type):  
        if prompt_type == 'cot':
            solution = solution.strip().split('\n')[-1].lower().replace('answer: ', '').split('=')[0]
            solution = solution.replace('thus, ', '')
            solution = solution.replace('therefore, ', '')
        
        solution = solution.replace('source node', 'source node ' + source_node)
        solution = solution.replace('target node', 'target node ' + target_node)

        return solution
       
    @staticmethod
    def one_by_one_neighborhood_aggregation_input_warp(neighborhood_solution_list, x, node_and_edge_and_dist_desc, source_node, target_node):
        
        source_node_desc = 'source node ' + source_node
        target_node_desc = 'target node ' + target_node
        neighborhood_prompt_warp_list = []

        for neighborhood_solution in neighborhood_solution_list:
            neighborhood_prompt_warp = neighborhood_one_by_one_aggregation_prompt_solve.format(
                input=node_and_edge_and_dist_desc, neighborhood=neighborhood_solution, 
                source_node_placeholder_1=source_node_desc,target_node_placeholder_1=target_node_desc,
                source_node_placeholder_2=source_node_desc,target_node_placeholder_2=target_node_desc)
            neighborhood_prompt_warp_list.append(neighborhood_prompt_warp)
        
        return neighborhood_prompt_warp_list

    @staticmethod
    def one_by_one_neighborhood_aggregation_eval_warp(neighborhood_output_list, x, node_and_edge_and_dist_desc, source_node, target_node):
        
        source_node_desc = 'source node ' + source_node
        target_node_desc = 'target node ' + target_node

        warped_neighborhood_eval = ''
        for i, y in enumerate(neighborhood_output_list, 1):
            warped_neighborhood_eval += f'Solution {i}:\n{y}\n'
        
        warped_prompt = neighborhood_one_by_one_aggregation_prompt_eval_2.format(
            input=node_and_edge_and_dist_desc, source_node=source_node_desc, 
            target_node = target_node_desc, candidate_solutions=warped_neighborhood_eval)

        warped_prompt = neighborhood_one_by_one_aggregation_prompt_eval_1 + warped_prompt

        return warped_prompt

    @staticmethod
    def neighborhood_aggregation_prompt_warp(neighborhood_solution_list, x, node_and_edge_and_dist_desc, source_node, target_node):

        pre_dec = node_and_edge_and_dist_desc + 'The hints are: '

        for solution in neighborhood_solution_list:
            pre_dec += solution + ' '
        pre_dec += 'Use the above hint to find the shortest path from the source node '+ source_node + 'to the target node ' + target_node + '.'

        return neighborhood_aggregation_prompt.format(input=pre_dec)
    
    @staticmethod
    def readout_prompt_warp(x, node_and_edge_and_dist_desc, key, target_node, original_solution, aggregated_solution):
        # replace the original target node in x with the altered target node
        if 'Target Node:'+target_node in x:
            x_with_alter_target = x.replace('Target Node:'+target_node, 'Target Node:'+key)
        else:
            x_with_alter_target = x.replace('Target Node: '+target_node, 'Target Node: '+key)

        solution_1 = 'Solution 1: ' + original_solution + ' '
        solution_2 = 'Solution 2: ' + aggregated_solution
        readout_input = node_and_edge_and_dist_desc + x_with_alter_target + solution_1 + solution_2

        return readout_prompt.format(input=readout_input)
    
    @staticmethod
    def warp_readout_output(solution):
        # flag = re.IGNORECASE 
        parse_solution = re.findall(r"shortest path from the source node(.+)", solution)
        if parse_solution != []:
            parse_solution = parse_solution[-1]
            parse_solution = 'The shortest path from the source node' + parse_solution
            return parse_solution
        else:
            return None
    
    @staticmethod
    def vote_outputs_unwrap(vote_outputs: list, n_candidates: int) -> list:
        vote_results = [0] * n_candidates
        for vote_output in vote_outputs:
            pattern_1 = r".*best solution is .*(\d+).*"
            pattern_2 = r".*most promising solution is .*(\d+).*"
            match_1 = re.match(pattern_1, vote_output, re.DOTALL)
            match_2 = re.match(pattern_2, vote_output, re.DOTALL)
            if match_1:
                vote = int(match_1.groups()[0]) - 1
                if vote in range(n_candidates):
                    vote_results[vote] += 1
            elif match_2:
                vote = int(match_2.groups()[0]) - 1
                if vote in range(n_candidates):
                    vote_results[vote] += 1
            else:
                print(f'vote no match: {[vote_output]}')
        return vote_results
    
    @staticmethod
    def warp_got_output(solution, source_node, target_node):
        solution = solution.replace('source node ' + source_node, 'source node')
        solution = solution.replace('target node ' + target_node, 'target node')
        return solution

    def test_output(self, idx: int, output: str):
        # parse the output for evaluation
        expression = output.strip().split('\n')[-1].lower().replace('answer: ', '').split('=')[0]
        print(expression)

        if re.findall(r'\[(.+?)\]', expression) != []:
            path = re.findall(r'\[(.+?)\]', expression)[0]

            try:
                is_valid = self.check_feasible(idx, path)
            except ValueError as e:
                return {'r': 'Fail'}
            
            if is_valid:

                length = re.findall(r'the shortest distance is (.*).', expression)
                if length != []:
                    length = length[0]
                elif re.findall(r'distance of (.*).', expression) != []:
                    length = re.findall(r'distance of (.*).', expression)[0]
                else:
                    length = 'Not Specified'
                try:
                    num_length = int(length)
                    true_length = self.get_true_length(idx, path)
                    optimal_distance = self.get_shortest_dist(idx)
                    optimal_rate = (true_length - optimal_distance) / optimal_distance
                    return {'r': optimal_rate, 'length_consistency': true_length==num_length, 'path': path}
                except ValueError as e:
                    return {'r': 'Fail'}
            
            else:
                return {'r': 'Fail'}
        
        else:
            return {'r': 'Fail'}
 