def test_live_nested():
    from rich.live import Live
    from rich.console import Console
    
    console = Console()
    
    with Live(console=console) as live1:
        
        live2 = Live(console=console)
        live2.start()
        
        assert live2._nested == True
        
        live2.stop()
