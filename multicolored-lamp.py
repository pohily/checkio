class Lamp:
    def __init__(self):
        self.state = 'Yellow'

    def light(self):
        if self.state == 'Red':
            self.state = 'Blue'
            print(self.state)
            return 'Blue'
        elif self.state == 'Blue':
            self.state = 'Yellow'
            print(self.state)
            return 'Yellow'
        elif self.state == 'Yellow':
            self.state = 'Green'
            print(self.state)
            return 'Green'
        elif self.state == 'Green':
            self.state = 'Red'
            print(self.state)
            return 'Red'
        
lamp_1 = Lamp()
lamp_2 = Lamp()

lamp_1.light() #Green
lamp_1.light() #Red
lamp_2.light()



"""

    """


