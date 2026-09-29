from lib.display_members import *

def test_when_list_empty_return_empty_string():
    result = display_members([])
    assert result == ""

def test_when_single_return_member():
    result = display_members(['bart'])
    assert result == 'bart'