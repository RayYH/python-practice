class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


class CustomException(Exception):
    pass


class InputError(IOError):
    """Exception raised for errors in the input.

    Attributes:
    expression -- input expression in which the error occurred
    message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class TransitionError(RuntimeError):
    """Raised when an operation attempts a state transition that's not allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous_state, next_state, message):
        self.previous_state = previous_state
        self.next_state = next_state
        self.message = message
