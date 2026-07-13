def test_exception_group_traceback():
    import sys
    import pytest
    
    if sys.version_info < (3, 11):
        pytest.skip("ExceptionGroup requires Python 3.11+")
    
    from rich.traceback import Traceback
    
    try:
        raise ExceptionGroup("multiple errors", [
            ValueError("error 1"),
            TypeError("error 2"),
        ])
    except ExceptionGroup:
        tb = Traceback()
        assert tb is not None