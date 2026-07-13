def test_safe_str_with_broken_str():
    from rich.traceback import Traceback

    class BrokenStr:
        def __str__(self):
            raise RuntimeError("__str__ failed!")

    try:
        raise ValueError(BrokenStr())
    except ValueError:
        tb = Traceback()
        assert tb is not None
        