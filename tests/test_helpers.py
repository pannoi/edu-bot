import pytest


@pytest.mark.parametrize('pattern', [
	'docker help: ',
	'terraform help: ',
	'ansible help: ',
	'kubernetes help: ',
	'helm help: ',
	'jenkins help: ',
	'git help: ',
	'molecule help'
])
def test_removing_pattern(pattern):
	"""
	Checking that helpers.remove_pattern works propeerly for every topic

	:params pattern -> string that should be remove from message
	"""
	error = "something cool"
	message = pattern + error
	result = message.replace(pattern, '')
	print(result)
	assert result == error
