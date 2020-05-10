from src.helpers import remove_pattern


def ansible_help(message):
	pattern = "ansible help: "
	error = remove_pattern(pattern, message)
	return error
