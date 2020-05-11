from src.helpers import remove_pattern


class git:
	def __init__(self):
		"""
		Class constructor.

		:param messsage -> message what gives the student
		"""
		self.answer = ""


	def __repr__(self) -> str:
		"""Represent object."""
		return self.answer

	
	def git_help(self, message):
		"""Function to return answer to student."""
		pattern = "git help: "
		error = remove_pattern(pattern, message)
		return error
	