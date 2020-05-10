from src.helpers import remove_pattern


def terraform_help(message):
	pattern = "terraform help: "
	error = remove_pattern(pattern, message)
	return error
