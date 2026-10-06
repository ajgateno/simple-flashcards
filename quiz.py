from score_card import ScoreCard

class Quiz:

	def __init__(self, questions):
		self.questions = questions

	def take(self):
		score_card = ScoreCard()
		for i in range(len(self.questions)):
			self.questions[i].ask(i + 1, score_card)
		score_card.report_score()
		return score_card
