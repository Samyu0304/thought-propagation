python run.py \
    --task text \
    --task_file_path data_100_random_text.txt \
    --task_start_index 0 \
    --task_end_index 100 \
    --naive_run \
    --backend gpt-4 \
    --prompt_sample standard \
    --n_generate_sample 10 \
    --temperature 1.0 \
    ${@}

python run.py \
    --task text \
    --task_file_path data_100_random_text.txt \
    --task_start_index 0 \
    --task_end_index 100 \
    --naive_run \
    --backend gpt-3.5-turbo-16k \
    --prompt_sample standard \
    --n_generate_sample 10 \
    --temperature 1.0 \
    ${@}