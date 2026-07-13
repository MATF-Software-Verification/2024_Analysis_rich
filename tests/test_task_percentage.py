def test_task_percentage():
    from rich.progress import Task, TaskID
    import time
    
    task = Task(TaskID(0), "test", total=100.0, completed=50, _get_time=time.monotonic)
    
    assert task.percentage == 50.0