import pytest
from singly_linked_list import Singly_Linked_List



a = Singly_Linked_List()
b = Singly_Linked_List()


def test_ssl_init() -> None:
    """initialization test for ssl"""
    assert list(a) == []
    assert len(a) == 0

    assert list(b) == [4]
    assert len(b) == 1

def test_ssl_append() -> None:
    a.append(3)
    assert list(a)==[3]
    assert len(a)==1

    with pytest.raises(ValueError):
        a.append(None)

def test_ssl_pop():
    assert a.pop() == 3
    assert len(a) == 0
    
    with pytest.raises(ValueError):
        a.pop()
