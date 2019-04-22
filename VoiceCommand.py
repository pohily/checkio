class VoiceCommand:
    def __init__(self, channel_list):
        self.channel_list = channel_list
        self.number = 0
        self.cur_channel = self.channel_list[self.number]
            
    def first_channel(self):
        self.number = 0
        self.cur_channel = self.channel_list[self.number]
        return self.cur_channel
    
    def last_channel(self):
        self.number = len(self.channel_list) - 1
        self.cur_channel = self.channel_list[self.number]
        return self.cur_channel
    
    def turn_channel(self, number):
        if number <= len(self.channel_list):
            self.number = number - 1
            self.cur_channel = self.channel_list[self.number]
        else:
            self.number = 0
            self.cur_channel = self.channel_list[self.number]
        return self.cur_channel
    
    def next_channel(self):
        if self.number == len(self.channel_list) - 1:
            self.number = 0
            self.cur_channel = self.channel_list[self.number]
            return self.cur_channel
        else:
            self.number += 1
            self.cur_channel = self.channel_list[self.number]
            return self.cur_channel

    def previous_channel(self):
        if self.number == 0:
            self.number = len(self.channel_list) - 1
            self.cur_channel = self.channel_list[self.number]
            return self.cur_channel
        else:
            self.number -= 1
            self.cur_channel = self.channel_list[self.number]
            return self.cur_channel

    def current_channel(self):
        return self.cur_channel

    def is_exist(self, quarry):
        if isinstance(quarry, int):
            if 0 < quarry < len(self.channel_list):
                return 'Yes'
            else:
                return 'No'
        else:
            if quarry in self.channel_list:
                return 'Yes'
            else:
                return 'No'

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    CHANNELS = ["BBC", "Discovery", "TV1000"]

    
    
    controller = VoiceCommand(CHANNELS)
    print(controller.turn_channel(3))
    print(controller.next_channel())
    print(controller.current_channel())
