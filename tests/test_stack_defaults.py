def test_stack_defaults():
    from rich.traceback import Stack
    
    stack = Stack(exc_type="ValueError", exc_value="test error")
    
    assert stack.exc_type == "ValueError"
    assert stack.exc_value == "test error"
    assert stack.is_group == False
    assert stack.frames == []
    assert stack.exceptions == []
    assert stack.is_cause == False
    assert stack.syntax_error is None