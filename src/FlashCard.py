class FlashCard:
    
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    
    # pour un affichage plus adapté
    def __repr__(self):
        return f"Question: {self.question} \n 
                Answer : {self.answer}"
    
    def ShowAnswer(self):
        return self.answer
    
    def ShowQuestion(self):
        return self.question