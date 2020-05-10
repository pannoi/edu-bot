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
	error = "something cool"
	message = pattern + error
	result = message.replace(pattern, '')
	print(result)
	assert result == error
