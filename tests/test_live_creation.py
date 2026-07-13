def test_live_creation():
    from rich.live import Live
    
    live = Live()
    
    assert live.is_started == False
    assert live.auto_refresh == True
    assert live._nested == False
    assert live.transient == False