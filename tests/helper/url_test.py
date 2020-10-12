from src.helper.url import build_sub_url


def test_build_sub_url():
    assert build_sub_url('/demo/') == '/demo'
    assert build_sub_url('/demo///') == '/demo'
    assert build_sub_url('/demo', {'age': 24, 'name': 'Ray'}) \
           == '/demo?age=24&name=Ray'
    assert build_sub_url('/demo', {'name': '洪月阳'}) \
           == '/demo?name=%E6%B4%AA%E6%9C%88%E9%98%B3'
