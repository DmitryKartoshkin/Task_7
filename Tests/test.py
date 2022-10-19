from main import Stak
import pytest

@pytest.fixture
def new_class():
    l = ["s", 1, "qw"]
    stak = Stak(l)
    return stak

def test_isEmpty(new_class):
    result = new_class.isEmpty()
    assert result == True

def test_push(new_class):
    result = new_class.size()
    assert result == 3

def test_pop(new_class):
    result = new_class.pop()
    assert result == 'qw'

def test_peek(new_class):
    result = new_class.peek()
    assert result == "qw"
#
def test_is_correct_bracket(new_class):
    result = new_class.is_correct_bracket()
    assert result == "Несбалансированно"


