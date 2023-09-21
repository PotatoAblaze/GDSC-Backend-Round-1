from QuestionsList import QuestionsList
from Question import Question
import time

class QuizManager():
    
    def __init__(self):
        self.questions_list = QuestionsList.question_data
        self.questions = []
        self.current_question = 0
        self.score = 0
        self.attempted_questions = 0
        self.correct_answers = 0
        
    def LoadQuestions(self):
        for question in self.questions_list:
            new_question = Question(question['text'], question['answer'])
            self.questions.append(new_question)
    
    def CheckForValidInput(self, valid_inputs : list, invalid_message):
        while True:
            prompt = input("Your Answer: ").lower()
            if(valid_inputs.count(prompt) > 0):
                return(prompt)
            else:
                print(invalid_message)
    
    def PrintStartingPrompt(self):
        print(f'''Welcome to the Juicer's Quiz!
Your goal is to answer {len(self.questions)} questions with an answer of either 'True' or 'False'.
(In place of 'True'; 'true', 'T' and 't' are also acceptable)
(In place of 'False'; 'false', 'F' and 'f' are also acceptable)
The scoring will be +2 for a correct answer and -1 for an incorrect answer.
It is not possible to go back to a question you already attempted or skipped.

Do you wish to START?
Enter 'Y' for yes and 'N' for no.''')
        
        user_prompt : str = self.CheckForValidInput(['y', 'n'], "That is an invalid input! Try again!\n'Y' for yes and 'N' for no.")
        
        if(user_prompt == 'y'):
            self.DisplayCurrentQuestion()
        else:
            print("It is a sad day for all of mankind, since you have missed the chance to attempt one of the greatest quizzes known to mankind.")
            quit()
        
        
    def DisplayCurrentQuestion(self):
        print(f'''

QUESTION {self.current_question + 1}
{self.questions[self.current_question].text}

COMMANDS
To Answer: Enter 'true' or 'false'
To go to next question: Enter 'next'
To see the number of questions answered: Enter 'attempt'
To see the number of questions remaining: Enter 'remain'
''')
        
        user_prompt : str = self.CheckForValidInput(['true', 't', 'false', 'f', 'next', 'attempt', 'remain'], "Invalid input!")
        print()
        
        if(user_prompt == 'true' or user_prompt == 't'):
            self.EvaluateQuestion(True)
        elif(user_prompt == 'false' or user_prompt == 'f'):
            self.EvaluateQuestion(False)
        elif(user_prompt == 'next'):
            print("Skipped this question!")
        elif(user_prompt == 'attempt'):
            print(f"You have attempted {self.attempted_questions} questions")
        elif(user_prompt == 'remain'):
            print(f"You have {len(self.questions) - self.current_question - 1} questions remaining!")
        
        print()
        input("Press Enter to proceed")
        if(user_prompt != 'remain' and user_prompt != 'attempt'):
            self.NextQuestion()
        else:
            self.DisplayCurrentQuestion()
            
    def NextQuestion(self):
        if(self.current_question == len(self.questions) - 1):
            self.EndQuiz()
        else:
            self.current_question += 1
            self.DisplayCurrentQuestion()
            
    def EndQuiz(self):
        print(f'''

You attempted all the questions! You are a national hero!
Your final score: {self.score}
Your attempted questions: {self.attempted_questions}
Your correct answers: {self.correct_answers}
Your incorrect answers: {self.attempted_questions - self.correct_answers}

THANK YOU FOR PLAYING! WE HOPE YOU COME FOR THE NEXT EDITION OF THE JUICER'S QUIZ!
''')
        quit()
        
    
    def EvaluateQuestion(self, given_answer):
        if(given_answer == self.questions[self.current_question].answer):
            print("You were correct! +1 added to score.")
            self.score += 2
            self.correct_answers += 1
        else:
            print("You were wrong! -1 deducted from score.")
            self.score -= 1
            
        self.attempted_questions += 1
        

if __name__ == "__main__":
    manager = QuizManager()
    manager.LoadQuestions()
    manager.PrintStartingPrompt()    
    
    