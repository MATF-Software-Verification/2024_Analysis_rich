def test_panel_creation():
    from rich.panel import Panel
    
    panel = Panel("Hello, World!")
    
    assert panel.renderable == "Hello, World!"
    assert panel.title is None
    assert panel.subtitle is None
    assert panel.expand == True
    assert panel.highlight == False