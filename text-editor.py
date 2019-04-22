class Text:
    def __init__(self, text='', font=''):
        self.text = text
        self.font = font

    def write(self, text):
        self.text += text

    def set_font(self, font):
        self.font = font

    def show(self):
        if self.font:
            return '[{0}]{1}[{0}]'.format(self.font, self.text)
        else:
            return self.text

    def restore(self, restored):
        self.font, self.text = restored 
        

class SavedText:
    def __init__(self):
        self.ver = 0
        self.version = {}
        
    def save_text(self, text):
        self.version[self.ver] = [text.font, text.text]
        self.ver += 1

    def get_version(self, number):
        return self.version[number][0], self.version[number][1]
        


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    text = Text()
    saver = SavedText()
    
    text.write("At the very beginning ")
    saver.save_text(text)
    text.set_font("Arial")
    saver.save_text(text)
    text.write("there was nothing.")

    assert text.show() == "[Arial]At the very beginning there was nothing.[Arial]"
    
    
    text.restore(saver.get_version(0))
  
    assert text.show() == "At the very beginning "

'''

'''
