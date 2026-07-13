def test_progress_creation():
    from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn
    
    progress = Progress(
        TextColumn("test text"),
        BarColumn(),
        TimeRemainingColumn(),
    )
    
    assert progress.finished == True      
    assert progress.disable == False      
    assert len(progress.columns) == 3     
    assert progress.expand == False       