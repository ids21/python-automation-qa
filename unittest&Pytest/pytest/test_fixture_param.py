import pytest


@pytest.fixture(params=[11, 12, 13, 14])
def fixture_with_params(request):
    return request.param


@pytest.mark.parametrize("test_input", [1, 2, 3])
def test_one_2(test_input):
    print(test_input)


@pytest.mark.parametrize("test_input", [1, 2, 3])
class TestClassParametrized:

    def test_one(self, test_input):
        pass

    def test_two(self, test_input):
        pass

    def test_one_1(self,test_input, fixture_with_params):
        print(test_input, fixture_with_params)
