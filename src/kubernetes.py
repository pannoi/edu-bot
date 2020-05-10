from src.helpers import remove_pattern


def kubernetes_help(message):
	pattern = "kubernetes help: "
	error = remove_pattern(pattern, message)
	return error
