def test_task_defaults():
    from rich.progress import Task, TaskID
    import time
    
    task = Task(TaskID(0), "test task", total=100.0, completed=0, _get_time=time.monotonic)
    
    assert task.description == "test task"
    assert task.total == 100.0
    assert task.completed == 0
    assert task.finished == False
    assert task.visible == True