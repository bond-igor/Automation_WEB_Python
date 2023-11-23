from Task2.Task_02 import check_id
import pytest

def test_id(required_id, token):
	assert required_id in check_id(token)


if __name__ == "__main__":
	pytest.main(['-vv'])
