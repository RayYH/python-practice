def create(x, y):
    """
    x: simple number
    y: a dictionary
    """
    def set_x(new_x):
        nonlocal x
        x = new_x

    def modify_content(foo):
        y["foo"] = foo

    def get_x():
        return x

    def get_y():
        return y

    return {
        "set_x": set_x,
        "modify_content": modify_content,
        "get_x": get_x,
        "get_y": get_y
    }


def test_create():
    instance = create(10, {})
    assert instance['get_x']() == 10
    assert instance['set_x'].__closure__
    instance['set_x'](100)
    assert instance['get_x']() == 100
    assert instance['modify_content'].__closure__
    instance['modify_content'](30)
    assert instance['get_y']() == {"foo": 30}
