import pytest

@pytest.fixture
def good_word():
	return "table"
@pytest.fixture
def bad_word():
	return "tabll"