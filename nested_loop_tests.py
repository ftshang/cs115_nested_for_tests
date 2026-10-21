"""Answer checks for CS 115 Nested For Loops, Section 1."""


def _normalize(answer):
    """Ignore blank lines around an answer and trailing spaces on each line."""
    if not isinstance(answer, str):
        raise AssertionError("Write your prediction as a multiline string.")
    lines = [line.rstrip() for line in answer.splitlines()]
    while lines and not lines[0]:
        lines.pop(0)
    while lines and not lines[-1]:
        lines.pop()
    return "\n".join(lines)


def _check(answer, expected):
    assert _normalize(answer) == _normalize(expected), (
        "Incorrect output. Check your loop tracing and try again!"
    )
    print("All tests passed!")


def test_1_1(answer):
    _check(answer, "0 1 2 3\n0 1 2 3\n0 1 2 3")


def test_1_2(answer):
    _check(answer, "1 2 3 4\n2 4 6 8\n3 6 9 12")


def test_1_3(answer):
    _check(answer, "1\n22\n333\n4444")


def test_1_4(answer):
    _check(answer, "*---\n-*--\n--*-")


def test_1_5(answer):
    _check(answer, "7 5 3\n9 7 5\n11 9 7")
