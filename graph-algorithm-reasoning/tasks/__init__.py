def get_task(name, file=None, difficulty='easy', prompt_difficulty='easy', shot='5-shot', steps = 2):
    if name == 'shortest_path':
        from .shortest_path import ShortestPath
        return ShortestPath(difficulty, prompt_difficulty, shot, steps)
    else:
        raise NotImplementedError