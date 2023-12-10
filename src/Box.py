class Box:

    def __init__(self, nb):
        self.number = nb
        # content stores the cards in the box
        self.content = []
        self.length = 0
        self.period = getPeriodFromNumber(nb)

    def AddCard(self, card):
        self.content.append(card)

    def RemoveCard(self, card):
        self.content.remove(card)
    
    def GetNumberOfCards(self):
        return len(self.content)

    def getPeriodFromNumber(nb):
        """Retrieves the period of the box (in days) from its number"""
        match nb:
            case 1 | 2:
                return nb
            case 3:
                return 5
            case 4:
                return 9
            case 5:
                return 14
            case 6:
                return 21
            case 7:
                return 30
            case _:
                raise ValueError("The boxes are numbered from 1 to 7 inclusive")
    