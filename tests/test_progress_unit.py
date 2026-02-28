import pytest
from rich.progress import Progress, BarColumn, TextColumn

def test_progress_percent_completion():
    progress = Progress(TextColumn("{task.percentage:>3.0f}%"), BarColumn())
    task_id = progress.add_task("Test task", total=100)

    # update task do 50%
    progress.update(task_id, advance=50)
    task = progress.tasks[0]
    assert task.percentage == 50

    # update do 100%
    progress.update(task_id, advance=50)
    task = progress.tasks[0]
    assert task.percentage == 100