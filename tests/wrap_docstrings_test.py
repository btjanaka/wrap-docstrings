"""Tests for wrap_docstrings."""

from wrap_docstrings import wrap_docstrings


def test_single_arg():
    input_text = '''\
def f(x):
    """Does stuff.

    Args:
        x: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure do
    """
    return x
'''

    output_text = '''\
def f(x):
    """Does stuff.

    Args:
        x: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
            tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
            quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
            consequat. Duis aute irure do
    """
    return x
'''

    assert wrap_docstrings(input_text, width=88, indent=4) == output_text


def test_single_arg_with_return_section():
    input_text = '''\
def f(x):
    """Does stuff.

    Args:
        x: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure do

    Returns:
        Returns are not formatted (for now, at least).
    """
    return x
'''

    output_text = '''\
def f(x):
    """Does stuff.

    Args:
        x: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
            tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
            quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
            consequat. Duis aute irure do

    Returns:
        Returns are not formatted (for now, at least).
    """
    return x
'''

    assert wrap_docstrings(input_text, width=88, indent=4) == output_text


def test_multi_arg():
    input_text = '''\
def f(x, y):
    """Does stuff.

    Args:
        x: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure do
        y: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
            ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
            aliquip ex ea commodo consequat. Duis aute irure do
    """
    return x
'''

    output_text = '''\
def f(x, y):
    """Does stuff.

    Args:
        x: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
            tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
            quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
            consequat. Duis aute irure do
        y: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
            tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
            quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
            consequat. Duis aute irure do
    """
    return x
'''

    assert wrap_docstrings(input_text, width=88, indent=4) == output_text


def test_multi_arg_with_return_section():
    input_text = '''\
def f(x, y):
    """Does stuff.

    Args:
        x: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure do
        y: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
            ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
            aliquip ex ea commodo consequat. Duis aute irure do

    Returns:
        Returns are not formatted (for now, at least).
    """
    return x
'''

    output_text = '''\
def f(x, y):
    """Does stuff.

    Args:
        x: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
            tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
            quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
            consequat. Duis aute irure do
        y: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
            tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
            quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
            consequat. Duis aute irure do

    Returns:
        Returns are not formatted (for now, at least).
    """
    return x
'''

    assert wrap_docstrings(input_text, width=88, indent=4) == output_text
