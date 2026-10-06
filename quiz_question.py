
class QuizQuestion:

	def __init__(self, number, card, score):
		self.number = number
		self.card = card
		self.score = score

	def ask(self, score_card):
		print(f"Question {self.number}: {self.card.question}")
		answer = input()
		score_card.add_score(self, answer.strip().lower() == self.card.answer.lower())
