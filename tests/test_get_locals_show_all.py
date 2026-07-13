def test_get_locals_show_all():
    from rich.traceback import Traceback
    import sys
    
    try:
        my_var = "vidljiv"
        raise ValueError("test")
    except ValueError:
        exc_type, exc_value, traceback = sys.exc_info()
        trace = Traceback.extract(
            exc_type,
            exc_value,
            traceback,
            show_locals=True,
            locals_hide_dunder=False,
            locals_hide_sunder=False,
        )
        assert trace is not None