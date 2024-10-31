import random
# List of random responses to be given after each answer
responses = [
	"Cool!",
	"Nice!",
	"Wow, great!"
]
# Function to ask a question and provide a random response
def ask_question (question):
	answer = input(question + " ")
	print(random.choice(responses))
	print()  # For spacing between questions

# List of questions to be filled in by students
questions = [
	"What's your favorite hobby?",	# Example question
	"What's your favorite movie?",  
]

# Function to randomly select and ask two questions
def icebreaker():
	print("Let's break the ice! I'll ask you two random questions:")
	selected_questions = random.sample(questions, 2)  # Randomly select 2 questions
	for question in selected_questions:
		ask_question(question)
# Call the icebreaker function to start the program
icebreaker()

