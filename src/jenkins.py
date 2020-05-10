from src.helpers import remove_pattern


def jenkins_help(message):
	pattern = "jenkins help: "
	error = remove_pattern(pattern, message)
	return error
