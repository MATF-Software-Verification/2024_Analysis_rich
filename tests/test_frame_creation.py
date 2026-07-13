def test_frame_creation():
    from rich.traceback import Frame
    
    frame = Frame(filename="test.py", lineno=10, name="test_func")
    
    assert frame.filename == "test.py"
    assert frame.lineno == 10
    assert frame.name == "test_func"
    assert frame.line == ""
    assert frame.locals is None
    assert frame.last_instruction is None