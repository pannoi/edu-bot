import pytest


@pytest.mark.parametrize('error', [
	'Nothing to commit',
	'No files to commit'
])
def test_get_solution(error):
	""" Positive test of _soltuins. """
	if "to commit" in error:
		result = "You didn't make any changes"
	else:
		result = "Sorry here I can't help, please call @pannoi"
	
	assert result == "You didn't make any changes"


@pytest.mark.parametrize('error', [
	'Unknowown error',
	'Something illigable',
	'123'
])
def test_get_solution_negative(error):
	""" Testing unreal error to get unknow answer. """
	if "to commit" in error:
		result = "You didn't make any changes"
	else:
		result = "Sorry here I can't help, please call @pannoi"

	assert result == "Sorry here I can't help, please call @pannoi"
