def test_table_grid():
    from rich.table import Table
    
    table = Table.grid("Kolona1", "Kolona2")
    
    assert table.show_header == False
    assert table.show_footer == False
    assert table.show_edge == False
    assert table.box is None