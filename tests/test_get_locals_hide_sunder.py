def test_get_locals_hide_sunder():
    from rich.traceback import Traceback
    import sys
    
    try:
        _sunder_var = "skriven"
        normal_var = "vidljiv"
        raise ValueError("test")
    except ValueError:
        exc_type, exc_value, traceback = sys.exc_info()
        trace = Traceback.extract(
            exc_type,
            exc_value,
            traceback,
            show_locals=True,
            locals_hide_dunder=False,
            locals_hide_sunder=True,
        )
        for stack in trace.stacks:
            for frame in stack.frames:
                if frame.locals:
                    for key in frame.locals:
                        assert not key.startswith("_")