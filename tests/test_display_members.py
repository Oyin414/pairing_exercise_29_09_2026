from lib.display_members import *

def test_when_list_empty_return_empty_string():
    result = display_members([])
    assert result == ""

def test_when_single_return_member():
    result = display_members(['bart'])
    assert result == 'bart'

def test_when_list_has_two_items_ampersand_separates_them_in_string():
    result = display_members(['bart', 'simpson'])
    assert result == 'bart & simpson'

def test_when_list_has_multiple_items_ampersand_separates_last_two_in_string():
    result = display_members(['bart', 'simpson', 'lisa', 'simpson'])
    assert result == 'bart, simpson, lisa & simpson'