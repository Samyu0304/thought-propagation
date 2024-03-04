python run.py \
    --task text \
    --task_file_path data_100_random_text.txt \
    --task_start_index 0 \
    --backend gpt-4 \
    --task_end_index 100 \
    --method_generate sample \
    --method_evaluate vote \
    --method_select greedy \
    --n_generate_sample 5 \
    --n_evaluate_sample 5 \
    --n_select_sample 1 \
    --prompt_sample standard \
    --temperature 1.0 \
    ${@}

python run.py \
    --task text \
    --task_file_path data_100_random_text.txt \
    --task_start_index 0 \
    --backend gpt-3.5-turbo-16k \
    --task_end_index 100 \
    --method_generate sample \
    --method_evaluate vote \
    --method_select greedy \
    --n_generate_sample 5 \
    --n_evaluate_sample 5 \
    --n_select_sample 1 \
    --prompt_sample standard \
    --temperature 1.0 \
    ${@}