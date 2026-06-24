def test_iter_syntax_lines_multiline():
    from rich.traceback import _iter_syntax_lines
    
    results = list(_iter_syntax_lines((1, 5), (3, 10)))
    
    assert results[0] == (1, 5, -1)   
    assert results[1] == (2, 0, -1)   
    assert results[2] == (3, 0, 10)   