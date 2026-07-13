def test_panel_with_title():
    from rich.panel import Panel
    
    panel = Panel("sadrzaj", title="Moj Panel")
    
    assert panel.title == "Moj Panel"
    assert panel.title_align == "center"