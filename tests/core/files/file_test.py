TEST_FILE_RELATIVE_PATH = "/tmp/pytest.txt"

global file_handler


def test_open_file():
    # Opens a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
    f = open(TEST_FILE_RELATIVE_PATH, "w")
    f.close()
    f = open(TEST_FILE_RELATIVE_PATH)
    f.close()
    # Opens a file for reading. (default)
    f = open(TEST_FILE_RELATIVE_PATH, "r")
    f.close()
    try:
        # Opens a file for exclusive creation. If the file already exists, the operation fails.
        open(TEST_FILE_RELATIVE_PATH, "x")
        assert False
    except FileExistsError:
        assert True
    # Opens a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
    f = open(TEST_FILE_RELATIVE_PATH, "a")
    f.close()
    # Opens in text mode. (default)
    f = open(TEST_FILE_RELATIVE_PATH, "rt")
    f.close()
    # Opens in binary mode.
    f = open(TEST_FILE_RELATIVE_PATH, "rb")
    f.close()
    # Opens a file for updating (reading and writing)
    f = open(TEST_FILE_RELATIVE_PATH, "r+b")
    f.close()
    # Moreover, the default encoding is platform dependent. In windows, it is cp1252 but utf-8 in Linux.
    # So, we must not also rely on the default encoding or else our code will behave differently in different platforms.
    f = open(TEST_FILE_RELATIVE_PATH, mode='r', encoding='utf-8')
    f.close()


def test_safe_close_file():
    global file_handler
    try:
        file_handler = open(TEST_FILE_RELATIVE_PATH, mode='r', encoding='utf-8')
        # perform file operations
    finally:
        file_handler.close()
    # or, we can use with statement - file will be closed internally.
    with open(TEST_FILE_RELATIVE_PATH, mode='r', encoding='utf-8') as file_handler:
        assert file_handler


def test_writing_and_reading_file():
    with open(TEST_FILE_RELATIVE_PATH, mode="w", encoding="utf-8") as f:
        f.write("First Line\n")
        f.write("Second Line\n")
        f.write("Third Line\n")
    with open(TEST_FILE_RELATIVE_PATH, mode="r", encoding="utf-8") as f:
        assert f.read(5) == "First"
        assert f.tell() == 5
        f.seek(0)
        assert f.tell() == 0
        assert f.read() == "First Line\nSecond Line\nThird Line\n"
    lists = [
        "First Line\n",
        "Second Line\n",
        "Third Line\n",
    ]
    with open(TEST_FILE_RELATIVE_PATH, mode="r", encoding="utf-8") as f:
        index = 0
        for line in f:
            assert line == lists[index]
            index = index + 1
    with open(TEST_FILE_RELATIVE_PATH, mode="r", encoding="utf-8") as f:
        for value in lists:
            assert value == f.readline()
        f.seek(0)
        assert f.readlines() == lists
    # truncate file contents
    with open(TEST_FILE_RELATIVE_PATH, mode="w", encoding="utf-8") as f:
        f.close()
