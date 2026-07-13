def test_live_update():
    from rich.live import Live
    from rich.console import Console
    from rich.text import Text
    
    console = Console(force_terminal=False)
    live = Live("pocetni tekst", console=console)
    
    live.update("novi tekst")
    
    assert isinstance(live._renderable, Text)
    assert str(live._renderable) == "novi tekst"