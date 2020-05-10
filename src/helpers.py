def remove_pattern(pattern, message):
	"""
	Removing pattern `help :` from message and returing clean message

	: param pattern -> contains theme + "help :"
	: param message -> contains message provided by student
	"""
	return message.replace(pattern, '')
