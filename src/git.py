from src.helpers import remove_pattern


def git_help(message):
	pattern = "git help: "
	error = remove_pattern(pattern, message)
	return error
