from quiz import Quiz
from quiz_question import QuizQuestion
from card import Card

if __name__ == "__main__":
	content = ""
	with open("quiz.txt", "r") as content_file:
		content = content_file.read()
	content = [line for line in content.split("\n") if len(line) > 0]
	questions = [QuizQuestion(i, Card(1, content[i].split(',')[0], content[i].split(',')[1]), 100) for i in range(len(content))]
	quiz = Quiz(questions)
	quiz.take()
