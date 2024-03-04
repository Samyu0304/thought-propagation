def get_task(name, file=None, difficulty='easy', prompt_difficulty='easy', shot='5-shot', steps = 2):
    if name == 'text':
        from .text import TextTask
        return TextTask(file)
    else:
        raise NotImplementedError