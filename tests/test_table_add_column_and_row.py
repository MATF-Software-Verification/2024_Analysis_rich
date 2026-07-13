def test_table_add_column_and_row():
    from rich.table import Table
    
    table = Table("Ime", "Godine", "Grad")
    table.add_row("Jovan", "28", "Beograd")
    
    assert len(table.columns) == 3
    assert table.row_count == 1
    assert table.columns[0].header == "Ime"
    assert table.columns[1].header == "Godine"
    assert table.columns[2].header == "Grad"