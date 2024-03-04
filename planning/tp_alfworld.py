import os
import json
import argparse
#print (os.path.abspath('.'))
import openai
from alfworld_runs.alfworld_trial import run_got_trial
from alfworld_runs.generate_reflections import update_memory
from alfworld_runs.perception import update_successful_trail, update_message

from typing import Any, List, Dict



def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--num_trials", type=int, help="The number of trials to run", default=7) # 
    parser.add_argument("--num_envs", type=int, help="The number of environments per trial", default=134) # set 1 to debug
    parser.add_argument("--run_name", type=str, help="The name of the run", default='tp_run_logs') # when start new run change it
    parser.add_argument("--use_memory", action='store_true', help="Allow the Agent to use memory")
    parser.add_argument("--use_simulation", action='store_true', help="if use_simulation, run 2 plans, if not, eval plans with llm")
    parser.add_argument("--is_resume", action='store_true', help="To resume run")
    parser.add_argument("--resume_dir", type=str, help="If resume, the logging directory", default='tp_run_logs') # when start new run change it.
    parser.add_argument("--start_trial_num", type=int, help="If resume, the start trial num", default=2)
    parser.add_argument("--num_neighbor", type=int, help="number of neighborhood senarios", default=2)
    parser.add_argument("--model", type=str, default="text-davinci-003")

    args = parser.parse_args()

    assert args.num_trials > 0, "Number of trials should be positive"
    assert args.num_envs > 0, "Number of environments should be positive"

    return args

def main(args) -> None:
    if args.is_resume:
        if not os.path.exists(args.resume_dir):
            raise ValueError(f"Resume directory `{args.resume_dir}` does not exist")
        logging_dir = args.resume_dir

        # load environment configs
        env_config_path: str = os.path.join(args.resume_dir, f'env_results_trial_{args.start_trial_num - 1}.json')
        if not os.path.exists(env_config_path):
            raise ValueError(f"Environment config file `{env_config_path}` does not exist")
        with open(env_config_path, 'r') as rf:
            env_configs: List[Dict[str, Any]] = json.load(rf)
    else:
        # Create the run directory
        if not os.path.exists(args.run_name):
            os.makedirs(args.run_name)
        logging_dir = args.run_name

        # initialize environment configs
        env_configs: List[Dict[str, Any]] = []
        for i in range(args.num_envs):
            env_configs += [{
                'name': f'env_{i}',
                'memory': [],
                'is_success': False,
                'skip': False
            }]
    
    world_log_path: str = os.path.join(logging_dir, 'world.log')
    # print start status to user
    if args.is_resume:
        print(f"""
    -----
    Resuming run with the following parameters:
    Run name: {logging_dir}
    Number of trials: {args.num_trials}
    Number of environments: {args.num_envs}
    Use memory: {args.use_memory}
    Resume trial number: {args.start_trial_num}

    Sending all logs to `{args.run_name}`
    -----
    """)
    else:
        print(f"""
    -----
    Starting run with the following parameters:
    Run name: {logging_dir}
    Number of trials: {args.num_trials}
    Number of environments: {args.num_envs}
    Use memory: {args.use_memory}

    Sending all logs to `{args.run_name}`
    -----
    """)

    # run trials
    # tp follows the trial 0 of reflexion to: 1. save cost, and 2. keep consistent performance with reflexion at trial 0.
    trial_idx = args.start_trial_num
    while trial_idx < args.num_trials:
        with open(world_log_path, 'a') as wf:
            wf.write(f'\n\n***** Start Trial #{trial_idx} *****\n\n')

        # set paths to prior log files for compute neighborhood messages
        prior_trail_log_path: str = os.path.join(args.run_name, f'trial_{trial_idx-1}.log')
        # set path to store the computed messages
        message_log_path: str = os.path.join(args.run_name, f'message_{trial_idx-1}.json')

        # set paths to log files
        trial_log_path: str = os.path.join(args.run_name, f'trial_{trial_idx}.log')

        # the successful_trail save the pure trails and filter out the few_shot prompt and memory prompts
        successful_trail_path: str = os.path.join(args.run_name, f'successful_trial_{trial_idx-1}.json')
        updated_successful_trail_path: str = os.path.join(args.run_name, f'successful_trial_{trial_idx}.json')

        trial_env_configs_log_path: str = os.path.join(args.run_name, f'env_results_trial_{trial_idx}.json')
        if os.path.exists(trial_log_path):
            open(trial_log_path, 'w').close()
        if os.path.exists(trial_env_configs_log_path):
            open(trial_env_configs_log_path, 'w').close()
        if os.path.exists(updated_successful_trail_path):
            open(trial_env_configs_log_path, 'w').close()

        # compute neighborhood message and prevent additional cost in calling llms.
        if trial_idx == 1:
            with open('./alfworld/tp_run_logs/message_0.json') as f:
                neighbor_message_dict = json.load(f)
                f.close()
        else:
            neighbor_message_dict = update_message(prior_trail_log_path, successful_trail_path, args.num_neighbor, args.use_simulation) # neighbor_message is a dict
            with open(message_log_path, 'w') as wf:
                json.dump(neighbor_message_dict, wf, indent=4)
                wf.close()
            with open(message_log_path) as f:
                neighbor_message_dict = json.load(f)
                f.close()

        # run trial
        #print('-----test load success-----')
        #if trial_idx != 1:
        run_got_trial(trial_log_path, world_log_path, neighbor_message_dict, trial_idx, env_configs, args.use_memory, args.model)
        #print('-----end run-----')

        # update the successful trail using trail_log_path and successful_trail_path
        successful_trail = update_successful_trail(trial_log_path, successful_trail_path)
        with open(updated_successful_trail_path, 'w') as wf:
            json.dump(successful_trail, wf, indent=4)

        # update memory if needed
        if args.use_memory:
            env_configs: List[Dict[str, Any]] = update_memory(trial_log_path, env_configs)

        # log env configs for trial
        with open(trial_env_configs_log_path, 'w') as wf:
            json.dump(env_configs, wf, indent=4)

        # log world for trial
        with open(world_log_path, 'a') as wf:
            wf.write(f'\n\n***** End Trial #{trial_idx} *****\n\n')

        trial_idx += 1


if __name__ == '__main__':
    args = get_args()
    main(args)