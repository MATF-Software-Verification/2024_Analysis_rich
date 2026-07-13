def test_from_exception():
    from rich.traceback import Traceback
    
    try:
        raise ValueError("test")
    except ValueError as e:
        tb = Traceback.from_exception(type(e), e, e.__traceback__)
        assert tb is not None