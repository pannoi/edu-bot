from src.helpers import remove_pattern


class tf:
	def __init__(self):
		"""
		Class constructor.

		"""
		self.answer = ""

	
	def __repr__(self) -> str:
		"""Repesent object."""
		return self.answer


	def get_solution(self, error) -> str:
		"""
		Identifying error by message.
		
		:param error -> cutted message without pattern
		"""
		if "subscription" in error.lower():
			return "You're using wrong subscribtion, please check it and try again"
		return 'Sorry here I can\'t help, try to call @pannoi'


	def tf_help(self, message) -> str:
		"""
		Function to return answer to student.

		:param message -> message provided by student
		"""
		pattern = "terraform help: "
		error = remove_pattern(pattern, message)
		answer = self.get_solution(error)
		return answer
