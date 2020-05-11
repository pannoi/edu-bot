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
	

	def get_solution(self, error) -> str:
		"""
		Identifying error by message.
		
		:param error -> cutted message without pattern
		"""
		if "to commit" in error.lower():
			return "You didn't make any changes, try to commit you code"
		return 'Sorry here I can\'t help, try to call @pannoi'


	def git_help(self, message) -> str:
		"""
		Function to return answer to student.

		:param message -> message provided by student
		"""
		pattern = "git help: "
		error = remove_pattern(pattern, message)
		answer = self.get_solution(error)
		return answer
