from quiz import Quiz
from quiz_question import QuizQuestion
from card import Card

if __name__ == "__main__":
	questions = [
		QuizQuestion(1, Card(1, "What is the capital of Panama?", "Panama City"), 100),
		QuizQuestion(2, Card(2, "What is the capital of Canada?", "Ottawa"), 100),
		QuizQuestion(3, Card(3, "What is the southernmost continent on Earth?", "Antarctica"), 100),
	]
	quiz = Quiz(questions)
	quiz.take()
