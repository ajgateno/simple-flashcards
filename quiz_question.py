
class QuizQuestion:

	def __init__(self, card, score):
		self.card = card
		self.score = score

	def ask(self, number, score_card):
		print(f"Question {number}: {self.card.question}")
		answer = input()
		score_card.add_score(self, answer.strip().lower() == self.card.answer.lower())
