# [ICLR 2024] Thought Propagation: An analogical approach to complex reasoning with large language models.
This repo holds the code, data, and instructions to reproduce the <a href='https://openreview.net/forum?id=SBoRhRCzM3&referrer=%5Bthe%20profile%20of%20Junchi%20Yu%5D(%2Fprofile%3Fid%3D~Junchi_Yu1)'>Thought Propagation (TP)</a> results.
# Introduction
## Thought-Propagation (TP)
Analogical reasoning is fundamental to human cognition as humans usually solve new problems by reusing experiences in handling similar problems. Motivated by such a reasoning process from humans, Thought Propagation (TP) teaches Large Language Models (LLMs) to explore analogous problems related to the input one and distill useful experience to facilitate input problem-solving.
## What is the thought in TP?
The thought usually refers to a solution to a sub-problem of the input problem. The solution to the input problem is produced by chaining such thoughts together. <b>However, the thought in TP refers to the solution to a problem instead of a sub-problem.</b>
## Why propagating thoughts?
Many prompt-based reasoning methods, such as <a href='https://arxiv.org/pdf/2005.14165.pdf'>IO prompting</a>, <a href='https://openreview.net/pdf?id=_VjQlMeSB_J'>Chain-of-Thought Prompting</a>, and etc, teach LLMs to reason from scratch. Thus, they cannot reuse the insights in solving similar problems to:
1. ease the difficulty of solving complex problems with the prior knowledge of such insights,
2. refine the initial solutions to input problems as reasoning from scratch is sensitive to the hallucinations and mistakes made by LLMs.
Thus, TP propagates the thoughts of solving similar problems (aka analogous problems) to amend the limitations of reasoning from scratch.

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
After running experiments, the results are saved in `graph-algorithm-reasoning/logs/`. Use two `.py` files to get evaluation results.


## Creative Writing
Follow the instructions below to run experiments:
```bat
cd creative-writing
bash bfs.sh (ToT)
bash tp.sh (TP)
bash cot_sampling.sh (CoT)
bash standard_sampling.sh (IO)
```

## LLM-Agent Planning
First, follow this <a href='https://github.com/alfworld/alfworld'>repo</a> to install Alfworld. Then move `planning` to the Alfworld directory. 
<b>Notice: I failed to run this experiment on a Macbook with M2 Pro. But I managed to run it on a Macbook with Intel Core i5. This phenomenon is mostly due to the dependency of the Alfworld environment.</b>

Run Reflexion:
```bat
python reflexion_alfworld.py
```
Run TP:
```bat
python tp_alfworld.py --use_memory --use_simulation
```
To activate/deactivate memory and simulation result in 4 variant models of TP.

# Cite
Please cite this work if you find it helpful:
```bat
@inproceedings{yu2023thought,
  title={THOUGHT PROPAGATION: AN ANALOGICAL APPROACH TO COMPLEX REASONING WITH LARGE LANGUAGE MODELS},
  author={Yu, Junchi and He, Ran and Ying, Zhitao},
  booktitle={The Twelfth International Conference on Learning Representations},
  year={2024}
}
```
