standard_prompt = '''
Write a coherent passage of 4 short paragraphs. The end sentence of each paragraph must be: {input}
'''

cot_prompt = '''
Write a coherent passage of 4 short paragraphs. The end sentence of each paragraph must be: {input}

Make a plan then write. Your output should be of the following format:

Plan:
Your plan here.

Passage:
Your passage here.
'''


vote_prompt = '''Given an instruction and several choices, decide which choice is most promising. Analyze each choice in detail, then conclude in the last line "The best choice is {s}", where s the integer id of the choice.
'''

compare_prompt = '''Briefly analyze the coherency of the following two passages. Conclude in the last line "The more coherent passage is 1", "The more coherent passage is 2", or "The two passages are similarly coherent".
'''

score_prompt = '''Analyze the following passage, then at the last line conclude "Thus the coherency score is {s}", where s is an integer from 1 to 10.
'''



# GoT: 
# first generate and refine writing plans, and then write 4 paragraphs
# 1. generate neighborhood problems by rephrasing the given 4 sentences; 
# 2. aggregate neighborhood problems by comparing the writing plans that end with the given 4 sentences. 
# 3. readout: decide whether the accept the aggregated results or choose the original result.
# 4. Writing: write 4 paragraphs that ends with the given 4 sentences using the plans.

node_plan_prompt = '''Make a writing plan for a coherent passage of 4 short paragraphs. The end sentence of each paragraph must be: {input}

The plan contains a one-setence description on each paragraph. Your output should be of the following format:

Plan:
Your plan here.
'''

node_write_prompt = '''Following this plan: {plan} to write a coherent passage of 4 short paragraphs. The end sentence of each paragraph must be: {input}

Your output should be of the following format:

Passage:
Your passage here.
'''

neighborhood_propose_prompt = '''Please rephrase the input sentences but do not change their order or meaning. The input sentences are: {input}

Your output should be of the following format:

Output:
Your sentences here.
'''
# Given an instruction and several choices, decide which choice is most promising. 
neighborhood_aggregate_prompt = '''Given several writing plans, decide which writing plan is the most promising. Analyze each writing plan in detail, then conclude in the last line "The best choice is {s}", where s the integer id of the choice.
'''

neighborhood_readout_prompt = '''compare and then output the better one.
'''