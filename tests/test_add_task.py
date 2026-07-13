def test_add_task():
    from rich.progress import Progress
    
    progress = Progress()
    task_id = progress.add_task("test", total=100)
    
    assert len(progress.tasks) == 1
    assert progress.tasks[0].description == "test"
    assert progress.tasks[0].total == 100
    assert progress.tasks[0].completed == 0
    assert progress.finished == False