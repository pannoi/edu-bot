from src.helpers import remove_pattern


def molecule_help(message):
	pattern = "molecule help: "
	error = remove_pattern(pattern, message)
	return error
