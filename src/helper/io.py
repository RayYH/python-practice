import sys
from contextlib import contextmanager
from io import StringIO
import io


@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


def to_string(out):
    if hasattr(out, 'getvalue'):
        return out.getvalue().strip()
    return str(out).strip()


def normalize(input_params):
    return '\n'.join(str(x) for x in input_params)


def stdin(monkeypatch, input_params):
    monkeypatch.setattr('sys.stdin', io.StringIO(normalize(input_params)))
