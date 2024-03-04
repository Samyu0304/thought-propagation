python run.py --tot --graph_encoding edge_description --task shortest_path --task_file_path shortest_path --shot 5-shot  --prompt_sample standard
python run.py --tot --graph_encoding edge_description --task shortest_path --task_file_path shortest_path --shot 1-shot  --prompt_sample standard
python run.py --tot --graph_encoding edge_description --task shortest_path --task_file_path shortest_path --shot 0-shot  --prompt_sample standard

python run.py --tot --graph_encoding vallina --task shortest_path --task_file_path shortest_path --shot 5-shot  --prompt_sample standard
python run.py --tot --graph_encoding vallina --task shortest_path --task_file_path shortest_path --shot 1-shot  --prompt_sample standard
python run.py --tot --graph_encoding vallina --task shortest_path --task_file_path shortest_path --shot 0-shot  --prompt_sample standard

python run.py --tot --graph_encoding graph_modeling_languagen --task shortest_path --task_file_path shortest_path --shot 5-shot  --prompt_sample standard
python run.py --tot --graph_encoding graph_modeling_language --task shortest_path --task_file_path shortest_path --shot 1-shot  --prompt_sample standard
python run.py --tot --graph_encoding graph_modeling_language --task shortest_path --task_file_path shortest_path --shot 0-shot  --prompt_sample standard