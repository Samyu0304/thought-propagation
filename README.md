# [ICLR 2024] Thought Propagation: An analogical approach to complex reasoning with large language models.
This repo holds the code, data and instructions to reproduce the results in Thought Propagation (TP).
<<<<<<< HEAD
# Thought-Propagation (TP)
=======
# Introduction
## Thought-Propagation (TP)
>>>>>>> 63906db3a20a5467c16c0cfa292bbce2a50ca27d
Analogical reasoning is fundamental to human cognition as humans usually solve new problems by reusing experiences in handling similar problems. Motivated by such a reasoning process from humans, Thought Propagation (TP) teaches Large Language Models (LLMs) to explore analogous problems related to the input one and distill useful experience to facilitate input problem-solving.
## What is the thought in TP?
The thought usually refers to a solution to a sub-problem of the input problem. The solution to the input problem is produced by chaining such thoughts together. <b>However, the thought in TP refers to the solution to a problem instead of a sub-problem.</b>
## Why propagating thoughts?
Many prompt-based reasoning methods, such as <a href='https://arxiv.org/pdf/2005.14165.pdf'>IO prompting</a>, <a href='https://openreview.net/pdf?id=_VjQlMeSB_J'>Chain-of-Thought Prompting</a>, and etc, teach LLMs to reason from scratch. Thus, they cannot reuse the insights in solving similar problems to:
1. ease the difficulty of solving complex problems with the prior knowledge of such insights,
2. refine the initial solutions to input problems as reasoning from scratch is sensitive to the hallucinations and mistakes made by LLMs.
Thus, TP propagates the thoughts of solving similar problems (aka analogous problems) to amend the limitations of reasoning from scratch.
## How to produce and propagate thoughts?
<a href='https://arxiv.org/pdf/2305.05994.pdf'>Previous work</a> constructs external knowledge bases, such as knowledge graphs, to retrieve thoughts in terms of 'A is to B what C is to D' to instantiate analogical reasoning in relational learning tasks. Constructing external knowledge bases to query from is expensive for general problems. Thus, TP is equipped with the LLM Propose, LLM Solve, and LLM Aggregate modules to produce and propagate the thoughts of solving analogous problems.
1. LLM Propose:
2. LLM Solve:
3. LLM Aggregate:

The TP framework is inspired by the <a href='https://arxiv.org/pdf/1704.01212.pdf'>message-passing module</a> in deep graph learning. The code of TP benefits from <a href='https://github.com/princeton-nlp/tree-of-thought-llm'>ToT</a> and <a href='https://github.com/noahshinn/reflexion'>Reflexion</a>.

# Experiments
## Graph Algorithm Reasoning
### Data Preparation
First, you need to generate the undirected graphs for this task. Run the following commands to generate graphs:
```bat
cd graph-algorithm-reasoning/data
python data_generator.py
```
Change the params in `data_generator.py` to customize the generated graphs. You could also use our generated graphs located in `graph-algorithm-reasoning/data/shortest_path/easy/`.
### Prompt
The way to convert graphs into strings affects the performance of prompting methods. We use 3 ways (vallina, <a href='https://graphviewer.nl/graphlet/gml-technical-report.pdf'>graph-modeling-language</a>, <a href='https://arxiv.org/abs/2305.10037'>edge-description</a>). The prompts are located in `graph-algorithm-reasoning/prompts/`. 
### Run
To run IO, CoT, Build-a-Graphs prompting methods on this task, just run
```bat
cd graph-algorithm-reasoning
bash run_bash.sh
```
To run ToT prompting methods on this task, just run
```bat
cd graph-algorithm-reasoning
bash run_tot.sh
```
To run TP prompting methods on this task, just run
```bat
cd graph-algorithm-reasoning
bash run_tp.sh
```
### Evaluation
After running experiments, the results are saved in `graph-algorithm-reasoning/logs/`. Use two `.py` files to get evaluation results.



## Creative Writing
Coming soon.

## LLM-Agent Planning
Coming soon.


<<<<<<< HEAD


=======
>>>>>>> 63906db3a20a5467c16c0cfa292bbce2a50ca27d
