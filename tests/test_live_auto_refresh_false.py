def test_live_auto_refresh_false():
    from rich.live import Live
    from rich.console import Console
    
    console = Console(force_terminal=False)
    
    with Live("test", console=console, auto_refresh=False) as live:
        assert live.auto_refresh == False
        assert live._refresh_thread is None  
        live.update("novo")
    
    assert live.is_started == False