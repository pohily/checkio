VOWELS = "aeiou"

class Chat:
    def __init__(self):
        self.dialogue = []

    def connect_human(self, name):
        name.chat = self
    
    def connect_robot(self, name):
        name.chat = self

    def show_human_dialogue(self):
        dialog = ''
        for line in self.dialogue:
            dialog += f'{line[0]} said: {line[1]}\n'
        print(dialog)
        return dialog[:-1]

    def show_robot_dialogue(self):
        dialog = ''
        for line in self.dialogue:
            tmp = ''
            for letter in line[1].lower():
                if letter in VOWELS:
                    tmp += '0'
                else:
                    tmp += '1'
            dialog += f'{line[0]} said: {tmp}\n'
        print(dialog)
        return dialog[:-1]

class Human():
    def __init__(self, name):
        self.name = name
        self.chat = None

    def send(self, text):
        self.chat.dialogue.append((self.name, text))

Robot = Human


chat = Chat()
karl = Human("Karl")
bot = Robot("R2D2")
chat.connect_human(karl)
chat.connect_robot(bot)
karl.send("Hi! What's new?")
bot.send("Hello, human. Could we speak later about it?")
assert chat.show_human_dialogue() == """Karl said: Hi! What's new?
R2D2 said: Hello, human. Could we speak later about it?"""
assert chat.show_robot_dialogue() == """Karl said: 101111011111011
R2D2 said: 10110111010111100111101110011101011010011011"""

print("Coding complete? Let's try tests!")
"""

""" 
