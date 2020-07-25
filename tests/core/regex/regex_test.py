import re


def test_regex():
    # any five letter string starting with a and ending with s.
    pattern = '^a...s$'
    assert not re.match(pattern, 'abs')
    assert not re.match(pattern, 'Alias')
    assert not re.match(pattern, 'An abacus	')
    assert re.match(pattern, 'alias')
    assert re.match(pattern, 'abyss')
    # Square brackets specifies a set of characters you wish to match.
    pattern = '[abc]'
    # [a-e] is the same as [abcde].
    # [1-4] is the same as [1234].
    # [0-39] is the same as [01239].
    # [^abc] means any character except a or b or c.
    # [^0-9] means any non-digit character.
    assert len(re.findall(pattern, 'a')) == 1
    assert len(re.findall(pattern, 'ac')) == 2
    assert len(re.findall(pattern, 'Hey Jude')) == 0
    assert len(re.findall(pattern, 'abc de ca')) == 5
    # A period matches any single character (except newline '\n').
    pattern = '..'
    assert len(re.findall(pattern, 'a')) == 0
    assert len(re.findall(pattern, 'ac')) == 1
    assert len(re.findall(pattern, 'acd')) == 1
    assert len(re.findall(pattern, 'room')) == 2
    # The caret symbol ^ is used to check if a string starts with a certain character.
    pattern = '^a'
    assert re.match(pattern, 'a')
    assert re.match(pattern, 'abc')
    assert not re.match(pattern, 'bac')
    pattern = '^ab'
    assert re.match(pattern, 'abc')
    assert not re.match(pattern, 'bac')
    # see https://docs.python.org/3/howto/regex.html#match-versus-search
    # The dollar symbol $ is used to check if a string ends with a certain character.
    pattern = '.*oo$'
    assert re.match(pattern, 'foo')
    assert re.match(pattern, 'hello oo')
    assert not re.match(pattern, 'foobar')
    # The star symbol * matches zero or more occurrences of the pattern left to it.
    pattern = '.*ma*n'
    assert re.match(pattern, 'mn')
    assert re.match(pattern, 'man')
    assert re.match(pattern, 'maaan')
    assert re.match(pattern, 'woman')
    assert not re.match(pattern, 'main')
    # The plus symbol + matches one or more occurrences of the pattern left to it.
    pattern = '.*ma+n'
    assert not re.match(pattern, 'mn')
    assert re.match(pattern, 'man')
    assert re.match(pattern, 'maaan')
    assert re.match(pattern, 'woman')
    assert not re.match(pattern, 'main')
    # The question mark symbol ? matches zero or one occurrence of the pattern left to it.
    pattern = '.*ma?n'
    assert re.match(pattern, 'mn')
    assert re.match(pattern, 'man')
    assert not re.match(pattern, 'maaan')
    assert re.match(pattern, 'woman')
    assert not re.match(pattern, 'main')
    # Consider this code: {n,m}. This means at least n, and at most m repetitions of the pattern left to it.
    pattern = 'a{2,3}'
    assert len(re.findall(pattern, 'abc dat')) == 0
    assert len(re.findall(pattern, 'abc daat')) == 1
    assert len(re.findall(pattern, 'aabc daaat')) == 2
    assert len(re.findall(pattern, 'aabc daaaat')) == 2
    pattern = '[0-9]{2,4}'
    assert len(re.findall(pattern, 'ab123csde')) == 1
    assert len(re.findall(pattern, '12 and 345673')) == 3
    assert len(re.findall(pattern, '1 and 2')) == 0
    # Vertical bar | is used for alternation (or operator).
    pattern = 'a|b'
    assert len(re.findall(pattern, 'cde')) == 0
    assert len(re.findall(pattern, 'ade')) == 1
    assert len(re.findall(pattern, 'acdbea')) == 3
    # Parentheses () is used to group sub-patterns.
    pattern = '(a|b|c)xz'
    assert len(re.findall(pattern, 'ab xz')) == 0
    assert len(re.findall(pattern, 'abxz')) == 1
    assert len(re.findall(pattern, 'axz cabxz')) == 2
    # \A - Matches if the specified characters are at the start of a string.
    pattern = r'\Athe'
    assert len(re.findall(pattern, 'the sun')) == 1
    assert len(re.findall(pattern, 'In the sun')) == 0
    # \b - Matches if the specified characters are at the beginning or end of a word.
    pattern = r'\bfoo'
    assert len(re.findall(pattern, 'football')) == 1
    assert len(re.findall(pattern, 'a football')) == 1
    assert len(re.findall(pattern, 'afootball')) == 0
    pattern = r'foo\b'
    assert len(re.findall(pattern, 'the foo')) == 1
    assert len(re.findall(pattern, 'the afoo test')) == 1
    assert len(re.findall(pattern, 'the afootest')) == 0
    # \B - Opposite of \b. Matches if the specified characters are not at the beginning or end of a word.
    pattern = r'\Bfoo'
    assert len(re.findall(pattern, 'football')) == 0
    assert len(re.findall(pattern, 'a football')) == 0
    assert len(re.findall(pattern, 'afootball')) == 1
    pattern = r'foo\B'
    assert len(re.findall(pattern, 'the foo')) == 0
    assert len(re.findall(pattern, 'the afoo test')) == 0
    assert len(re.findall(pattern, 'the afootest')) == 1
    # \d - Matches any decimal digit. Equivalent to [0-9]
    pattern = r'\d'
    assert len(re.findall(pattern, '12abc3')) == 3
    assert len(re.findall(pattern, 'Python')) == 0
    # \D - Matches any non-decimal digit. Equivalent to [^0-9]
    pattern = r'\D'
    assert len(re.findall(pattern, '1ab34"50')) == 3
    assert len(re.findall(pattern, '1345')) == 0
    # \s - Matches where a string contains any whitespace character. Equivalent to [ \t\n\r\f\v].
    pattern = r'\s'
    assert len(re.findall(pattern, 'Python RegEx')) == 1
    assert len(re.findall(pattern, 'PythonRegEx')) == 0
    # \S - Matches where a string contains any non-whitespace character. Equivalent to [^ \t\n\r\f\v].
    pattern = r'\S'
    assert len(re.findall(pattern, 'a b')) == 2
    assert len(re.findall(pattern, '  ')) == 0
    # \w - Matches any alphanumeric character (digits and alphabets). Equivalent to [a-zA-Z0-9_].
    pattern = r'\w'
    assert len(re.findall(pattern, '12&": ;c')) == 3
    assert len(re.findall(pattern, '%"> !)')) == 0
    # \W - Matches any non-alphanumeric character. Equivalent to [^a-zA-Z0-9_]
    pattern = r'\W'
    assert len(re.findall(pattern, '1a2%c')) == 1
    assert len(re.findall(pattern, 'Python')) == 0
    # \Z - Matches if the specified characters are at the end of a string.
    pattern = r'Python\Z'
    assert len(re.findall(pattern, 'I like Python')) == 1
    assert len(re.findall(pattern, 'I like Python Programming')) == 0
    assert len(re.findall(pattern, 'Python is fun')) == 0


def test_re_methods():
    string = 'hello 12 hi 89. Howdy 34'
    pattern = r'\d+'
    result = re.findall(pattern, string)
    assert result == ['12', '89', '34']
    string = 'Twelve:12 Eighty nine:89.'
    pattern = r'\d+'
    result = re.split(pattern, string)
    assert result == ['Twelve:', ' Eighty nine:', '.']
    string = 'Twelve:12 Eighty nine:89 Nine:9.'
    pattern = r'\d+'
    # max_split = 1
    # split only at the first occurrence
    result = re.split(pattern, string, 1)
    assert result == ['Twelve:', ' Eighty nine:89 Nine:9.']
    # multiline string
    string = 'abc 12\
    de 23 \n f45 6'
    # matches all whitespace characters
    pattern = r'\s+'
    # empty string
    replace = ''
    new_string = re.sub(pattern, replace, string)
    assert new_string == 'abc12de23f456'
    # multiline string
    string = 'abc 12\
    de 23 \n f45 6'
    # matches all whitespace characters
    pattern = r'\s+'
    replace = ''
    new_string = re.sub(r'\s+', replace, string, 1)
    assert new_string == "abc12    de 23 \n f45 6"
    # multiline string
    string = 'abc 12\
    de 23 \n f45 6'
    # matches all whitespace characters
    pattern = r'\s+'
    # empty string
    replace = ''
    new_string = re.subn(pattern, replace, string)
    assert new_string == ('abc12de23f456', 5)
    string = "Python is fun"
    # check if 'Python' is at the beginning
    assert re.search(r'\APython', string)
    string = '39801 356, 2102 1111'
    # Three digit number followed by space followed by two digit number
    pattern = r'(\d{3}) (\d{2})'
    # match variable contains a Match object.
    match = re.search(pattern, string)
    assert match.group() == "801 35"
    assert match.group(1) == "801"
    assert match.group(2) == "35"
    assert match.group(1, 2) == ('801', '35')
    # The start() function returns the index of the start of the matched substring.
    # Similarly, end() returns the end index of the matched substring.
    assert match.start() == 2
    assert match.end() == 8
    assert match.span() == (2, 8)
    assert match.re == re.compile('(\\d{3}) (\\d{2})')
    assert match.string == string
    string = '\n and \r are escape sequences.'
    result = re.findall(r'[\n\r]', string)
    assert result == ['\n', '\r']
