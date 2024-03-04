import os
import re
from tasks.base import Task, DATA_PATH
from prompts.text import *
from models import gpt


class TextTask(Task):
    """
    Input (x)   : a text instruction
    Output (y)  : a text generation
    Reward (r)  : # TODO
    Input Example: 
    Output Example: 
    """
    def __init__(self, file='data_100_random_text.txt'):
        """
        file: a text file, each line is some sentences
        """
        super().__init__()
        path = os.path.join(DATA_PATH, 'text', file)
        self.data = open(path).readlines()
        self.steps = 2
        self.name = 'text'
        self.stops = ['\nPassage:\n', None]

    def __len__(self) -> int:
        return len(self.data)
    
    def get_input(self, idx: int) -> str:
        return self.data[idx]
    
    def test_output(self, idx: int, output: str):
        output = output.split('Passage:\n')[-1]
        prompt = score_prompt + output
        score_outputs = gpt(prompt, n=5, model='gpt-4') # model = 'gpt-4' # 3.5-turbo
        scores = []
        for score_output in score_outputs:
            # print(score_output)
            pattern = r".*coherency score is (\d+).*"
            match = re.match(pattern, score_output, re.DOTALL)
            if match:
                score = int(match.groups()[0])
                scores.append(score)
            else:
                print(f'------------------score no match: {[score_output]}')
        print(scores)
        # print('------------')
        info = {'rs': scores, 'r': sum(scores) / len(scores) if scores else 0}
        return info
    
    @staticmethod
    def plan_output_warp(plans: str) -> str:
        # 1. 2. 3. 4.
        plan_1, plan_2, plan_3, plan_4 = '', '', '', ''
        plans = plans.split('\n')
        for plan in plans:
            if not plan.endswith('\n'):
                plan = plan + '\n'
            if plan.startswith('1.'):
                plan_1 = plan
            elif plan.startswith('2.'):
                plan_2 = plan
            elif plan.startswith('3.'):
                plan_3 = plan
            elif plan.startswith('4.'):
                plan_4 = plan
        plan_string = 'Plan:\n' + plan_1 +  plan_2 + plan_3 + plan_4

        return plan_string
    
    @staticmethod
    def node_passage_prompt_warp(x: str, warp_init_solution: str) -> str:
        return node_write_prompt.format(input = x, plan = warp_init_solution)
    
    @staticmethod
    def neigborhood_propose_prompt_wrap(sentences: str) -> str:
    
        return neighborhood_propose_prompt.format(input=sentences)
        
    @staticmethod
    def node_plan_prompt_warp(sentences: str, y = ' ') -> str:

        return node_plan_prompt.format(input=sentences) + y

    @staticmethod
    def neighborhood_aggregation_prompt_warp(plans) -> str:
        prompt = neighborhood_aggregate_prompt
        for i, y in enumerate(plans, 1):
            # y = y.replace('Plan:\n', '')
            # TODO: truncate the plan part?
            prompt += f'Choice {i}:\n{y}\n'
        return prompt
    
    @staticmethod
    def readout_prompt_warp(x, key, target_node, original_solution, aggregated_solution):
        pass

    
    @staticmethod
    def standard_prompt_wrap(x: str, y:str='') -> str:
        return standard_prompt.format(input=x) + y

    @staticmethod
    def cot_prompt_wrap(x: str, y:str='') -> str:
        return cot_prompt.format(input=x) + y

    @staticmethod
    def vote_prompt_wrap(x: str, ys: list) -> str:
        prompt = vote_prompt
        for i, y in enumerate(ys, 1):
            # y = y.replace('Plan:\n', '')
            # TODO: truncate the plan part?
            prompt += f'Choice {i}:\n{y}\n'
        return prompt
    
    @staticmethod
    def vote_outputs_unwrap(vote_outputs: list, n_candidates: int) -> list:
        vote_results = [0] * n_candidates
        for vote_output in vote_outputs:
            pattern_1 = r".*best choice is .*(\d+).*"
            pattern_2 = r".*most promising choice is .*(\d+).*"
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
    def compare_prompt_wrap(x: str, ys: list) -> str:
        assert len(ys) == 2, 'compare prompt only supports 2 candidates'
        ys = [y.split('Passage:\n')[-1] for y in ys]
        prompt = compare_prompt + f'Passage 1:\n{ys[0]}\n\nPassage 2:\n{ys[1]}\n'
        return prompt
    
    @staticmethod
    def compare_output_unwrap(compare_output: str):
        if 'more coherent passage is 1' in compare_output:
            return 0
        elif 'more coherent passage is 2' in compare_output:
            return 1
        elif 'two passages are similarly coherent' in compare_output:
            return 0.5
        else:
            print(f'-----------------compare no match: {[compare_output]}')
            return -1