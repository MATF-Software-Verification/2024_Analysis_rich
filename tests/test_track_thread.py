def test_track_thread_advances():
    import time
    from rich.progress import Progress, _TrackThread
    
    with Progress() as progress:
        task_id = progress.add_task("test", total=100)
        
        with _TrackThread(progress, task_id, update_period=0.1) as thread:
            thread.completed = 50  
            time.sleep(0.3)        
        
        assert progress.tasks[0].completed == 50