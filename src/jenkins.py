from src.helpers import remove_pattern


def docker_help(message):
	pattern = "jenkins help: "
	error = remove_pattern(pattern, message)
	return error
