def test_reader_next():
    import io
    import tempfile
    import os
    from rich.progress import Progress, _Reader
    
   
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(b"line one\nline two\nline three\n")
        temp_path = f.name
    
    try:
        with Progress() as progress:
            task_id = progress.add_task("reading", total=100)
            
            with open(temp_path, "rb") as f:
                reader = _Reader(f, progress, task_id)
                
               
                line = next(reader)
                
                assert line == b"line one\n"
                assert progress.tasks[0].completed > 0
    finally:
        os.unlink(temp_path)