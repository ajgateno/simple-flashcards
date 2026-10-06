
class ScoreCard:

	def __init__(self):
		self.score = 0
		self.total = 0

	def add_score(self, question, correct):
		if correct:
			self.score += question.score
		self.total += question.score

	def report_score(self):
		print(f"Final score: {self.score} / {self.total}")
