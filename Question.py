
class Question():
    
    def __init__(self, text, answer):
        self.text = text
        if(answer == "True"):
            self.answer = True
        else:
            self.answer = False