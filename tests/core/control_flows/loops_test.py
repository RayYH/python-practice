def test_looping_through_dictionaries():
    knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    for k, v in knights.items():
        assert k in ['gallahad', 'robin']
        assert v in ['the pure', 'the brave']


def test_looping_through_sequences():
    index = 0
    for i, v in enumerate(['tic', 'tac', 'toe']):
        assert index == i
        assert v in ['tic', 'tac', 'toe']
        index += 1


def test_looping_over_two_or_mode_sequences():
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    for q, a in zip(questions, answers):
        assert q in questions
        assert a in answers


def test_looping_over_reversed_sequences():
    index = 9
    for i in reversed(range(1, 10, 2)):
        assert i == index
        index -= 2


def test_looping_over_sorted_sequences():
    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    my_list = ['apple', 'apple', 'banana', 'orange', 'orange', 'pear']
    for item in sorted(basket):
        assert item == my_list.pop(0)
