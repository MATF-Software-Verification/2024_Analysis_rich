def test_panel_fit():
    from rich.panel import Panel
    
    panel = Panel.fit("sadrzaj", title="Test")
    
    assert panel.expand == False
    assert panel.title == "Test"
    assert panel.renderable == "sadrzaj"