# io/cot/build-a-graph prompting
python run.py --task shortest_path --task_file_path shortest_path  --shot 0-shot --prompt_sample cot  --thought_steps 2 --graph_encoding graph_modeling_language  --task_end_index 100 --naive_run
python run.py --task shortest_path --task_file_path shortest_path  --shot 1-shot --prompt_sample cot  --thought_steps 2 --graph_encoding graph_modeling_language  --task_end_index 100 --naive_run
python run.py --task shortest_path --task_file_path shortest_path  --shot 5-shot --prompt_sample cot  --thought_steps 2 --graph_encoding graph_modeling_language  --task_end_index 100 --naive_run

python run.py --task shortest_path --task_file_path shortest_path  --shot 0-shot --prompt_sample standard  --thought_steps 2 --graph_encoding graph_modeling_language  --task_end_index 100 --naive_run
python run.py --task shortest_path --task_file_path shortest_path  --shot 1-shot --prompt_sample standard  --thought_steps 2 --graph_encoding graph_modeling_language  --task_end_index 100 --naive_run
python run.py --task shortest_path --task_file_path shortest_path  --shot 5-shot --prompt_sample standard  --thought_steps 2 --graph_encoding graph_modeling_language  --task_end_index 100 --naive_run

python run.py --task shortest_path --task_file_path shortest_path  --shot 0-shot --prompt_sample bog  --thought_steps 2 --graph_encoding graph_modeling_language  --task_end_index 100 --naive_run
python run.py --task shortest_path --task_file_path shortest_path  --shot 1-shot --prompt_sample bog  --thought_steps 2 --graph_encoding graph_modeling_language  --task_end_index 100 --naive_run
python run.py --task shortest_path --task_file_path shortest_path  --shot 5-shot --prompt_sample bog  --thought_steps 2 --graph_encoding graph_modeling_language  --task_end_index 100 --naive_run

python run.py --task shortest_path --task_file_path shortest_path  --shot 0-shot --prompt_sample cot  --thought_steps 2 --graph_encoding vallina  --task_end_index 100 --naive_run
python run.py --task shortest_path --task_file_path shortest_path  --shot 1-shot --prompt_sample cot  --thought_steps 2 --graph_encoding vallina  --task_end_index 100 --naive_run
python run.py --task shortest_path --task_file_path shortest_path  --shot 5-shot --prompt_sample cot  --thought_steps 2 --graph_encoding vallina  --task_end_index 100 --naive_run

python run.py --task shortest_path --task_file_path shortest_path  --shot 0-shot --prompt_sample standard  --thought_steps 2 --graph_encoding vallina  --task_end_index 100 --naive_run
python run.py --task shortest_path --task_file_path shortest_path  --shot 1-shot --prompt_sample standard  --thought_steps 2 --graph_encoding vallina  --task_end_index 100 --naive_run
python run.py --task shortest_path --task_file_path shortest_path  --shot 5-shot --prompt_sample standard  --thought_steps 2 --graph_encoding vallina  --task_end_index 100 --naive_run

python run.py --task shortest_path --task_file_path shortest_path  --shot 0-shot --prompt_sample bog  --thought_steps 2 --graph_encoding vallina  --task_end_index 100 --naive_run
python run.py --task shortest_path --task_file_path shortest_path  --shot 1-shot --prompt_sample bog  --thought_steps 2 --graph_encoding vallina  --task_end_index 100 --naive_run
python run.py --task shortest_path --task_file_path shortest_path  --shot 5-shot --prompt_sample bog  --thought_steps 2 --graph_encoding vallina  --task_end_index 100 --naive_run

python run.py --task shortest_path --task_file_path shortest_path  --shot 0-shot --prompt_sample cot  --thought_steps 2 --graph_encoding edge_description  --task_end_index 100 --naive_run
python run.py --task shortest_path --task_file_path shortest_path  --shot 1-shot --prompt_sample cot  --thought_steps 2 --graph_encoding edge_description  --task_end_index 100 --naive_run
python run.py --task shortest_path --task_file_path shortest_path  --shot 5-shot --prompt_sample cot  --thought_steps 2 --graph_encoding edge_description  --task_end_index 100 --naive_run

python run.py --task shortest_path --task_file_path shortest_path  --shot 0-shot --prompt_sample standard  --thought_steps 2 --graph_encoding edge_description  --task_end_index 100 --naive_run
python run.py --task shortest_path --task_file_path shortest_path  --shot 1-shot --prompt_sample standard  --thought_steps 2 --graph_encoding edge_description  --task_end_index 100 --naive_run
python run.py --task shortest_path --task_file_path shortest_path  --shot 5-shot --prompt_sample standard  --thought_steps 2 --graph_encoding edge_description  --task_end_index 100 --naive_run

python run.py --task shortest_path --task_file_path shortest_path  --shot 0-shot --prompt_sample bog  --thought_steps 2 --graph_encoding edge_description  --task_end_index 100 --naive_run
python run.py --task shortest_path --task_file_path shortest_path  --shot 1-shot --prompt_sample bog  --thought_steps 2 --graph_encoding edge_description  --task_end_index 100 --naive_run
python run.py --task shortest_path --task_file_path shortest_path  --shot 5-shot --prompt_sample bog  --thought_steps 2 --graph_encoding edge_description  --task_end_index 100 --naive_run