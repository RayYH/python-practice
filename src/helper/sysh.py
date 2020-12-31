import sys


def python_version():
    vi = sys.version_info
    return vi.major * 100 + vi.minor * 10 + vi.micro * 1
