def test_live_is_started():
    from rich.live import Live
    from rich.console import Console
    
    console = Console(force_terminal=False)
    live = Live(console=console)
    
    assert live.is_started == False
    live.start()
    assert live.is_started == True
    live.stop()
    assert live.is_started == False