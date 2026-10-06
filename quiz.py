from score_card import ScoreCard

class Quiz:

	def __init__(self, questions):
		self.questions = questions

	def take(self):
		score_card = ScoreCard()
		for question in self.questions:
			question.ask(score_card)
		score_card.report_score()
		return score_card
