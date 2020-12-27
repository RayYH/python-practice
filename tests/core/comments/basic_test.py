def test_comments():
    # this is the first comment
    spam = 1  # and this is the second comment
    # ... and now a third!
    text = "# This is not a comment because it's inside quotes."
    assert spam
    assert text
