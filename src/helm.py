from src.helpers import remove_pattern


def helm_help(message):
	pattern = "helm help: "
	error = remove_pattern(pattern, message)
	return error
