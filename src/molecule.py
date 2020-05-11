from src.helpers import remove_pattern


class molecule:
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
		if "docker daemon" in error.lower():
			return "Check if docker serivce is running, or you have propper access rights"
		return 'Sorry here I can\'t help, try to call @pannoi'


	def molecule_help(self, message) -> str:
		"""
		Function to return answer to student.

		:param message -> message provided by student
		"""
		pattern = "molecule help: "
		error = remove_pattern(pattern, message)
		answer = self.get_solution(error)
		return answer
