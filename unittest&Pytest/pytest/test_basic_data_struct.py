import pytest
import functools

@pytest.fixture
def origin_data(request):
    print("\nGetting data types by {}".format(request.node))
    return {
        'list': ['a', 'sd', 'ss'],
        'tuple': (1, 2, 3),
        'set': {'Masha', 'Pasha', 'Sasha'},
        'dict': {'first_name': 'Alex', 'last_name': 'Lesli'},
        'str': 'Test String',
        'int': 1337,
    }

@pytest.fixture(scope='session')
def session_fixture(request):
    print("{} fixture output - start\n-----".format(request.scope))
    yield
    print("\n-----\n{} fixture output - finish".format(request.scope))




@pytest.fixture(scope='module')
def module_fixture(request):
    print("{} fixture output - start\n-----".format(request.scope))

    def module_finalizer():
        print("\n-----\n{} fixture output - finish".format(request.scope))

    request.addfinalizer(module_finalizer)



def test_1_list_length(session_fixture, module_fixture, origin_data):
    """
    Check len of given list
    :param session_fixture: fixture for test session
    :param module_fixture: fixture for the module
    :param origin_data: function fixture to prepare and get test data
    :return:
    """
    assert len(origin_data['list']) == 3


def test_2_tuple_value(session_fixture, module_fixture, origin_data):
    """
    Check if the first element of the given tuple is equal to 1
    :param session_fixture: fixture for test session
    :param module_fixture: fixture for the module
    :param origin_data: function fixture to prepare and get test data
    :return:
    """
    assert origin_data['tuple'][0] == 1


def test_3_sum_list_values(session_fixture, module_fixture, origin_data):
    """
    Check if the sum of given list values numbers is equal to 6
    :param session_fixture: fixture for test session
    :param module_fixture: fixture for the module
    :param origin_data: function fixture to prepare and get test data
    :return:
    """
    assert ''.join(origin_data['list']) == 'asdss'


def test_4_dict_name_check(session_fixture, module_fixture, origin_data):
    """
    Check if the given dictionary contains the name Alex
    :param session_fixture: fixture for test session
    :param module_fixture: fixture for the module
    :param origin_data: function fixture to prepare and get test data
    :return:
    """
    assert 'Alex' == origin_data['dict']['first_name']


def test_5_dict_items_len(session_fixture, module_fixture, origin_data):
    """
    Check if the given dictionary contains at least 2 values
    :param session_fixture: fixture for test session
    :param module_fixture: fixture for the module
    :param origin_data: function fixture to prepare and get test data
    :return:
    """
    assert len(origin_data['dict'].values()) >= 2


def test_6_dict_check_fullname(session_fixture, module_fixture, origin_data):
    """
    Check if the fullname from dict is equal to Alex Lesli
    :param session_fixture: fixture for test session
    :param module_fixture: fixture for the module
    :param origin_data: function fixture to prepare and get test data
    :return:
    """
    fullname = '{first_name} {last_name}'.format(**origin_data['dict'])
    assert fullname == 'Alex Ivanov'


def test_7_str_check_word(session_fixture, module_fixture, origin_data):
    """
    Check if given string contains the Test word
    :param session_fixture: fixture for test session
    :param module_fixture: fixture for the module
    :param origin_data: function fixture to prepare and get test data
    :return:
    """
    assert 'Test' in origin_data['str']


def test_8_is_integer_odd(session_fixture, module_fixture, origin_data):
    """
    Check if the given number is idd
    :param session_fixture: fixture for test session
    :param module_fixture: fixture for the module
    :param origin_data: function fixture to prepare and get test data
    :return:
    """
    assert origin_data['int'] % 2 != 0


def test_9_check_set_difference(session_fixture, module_fixture, origin_data):
    """
    Check if there is at least one difference between two sets
    :param session_fixture: fixture for test session
    :param module_fixture: fixture for the module
    :param origin_data: function fixture to prepare and get test data
    :return:
    """
    assert len(origin_data['set'].difference({"Sasha", 3})) == 2


def test_10_check_set_intersection(session_fixture, module_fixture, origin_data):
    """
    Check if number of intersecting values of sets is equal to 2
    :param session_fixture: fixture for test session
    :param module_fixture: fixture for the module
    :param origin_data: function fixture to prepare and get test data
    :return:
    """
    assert len(origin_data['set'].intersection({"Masha", "Pasha"})) == 2