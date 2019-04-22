class MicrowaveBase:
    def __init__(self):
        self.s = 0
        self.m = 0
        self.defect_digit = ''

class Microwave1(MicrowaveBase):
    def __init__(self):
        super().__init__()
        self.defect_digit = 0

class Microwave2(MicrowaveBase):
    def __init__(self):
        super().__init__()
        self.defect_digit = 4

class Microwave3(MicrowaveBase):
    def __init__(self):
        super().__init__()


class RemoteControl:
    def __init__(self, unit):
        self.unit = unit

    def check_time(self, time):
        """
        Check if time is in the limits and set it to memory
        """
        if time[-1] == 's':
            s = int(time[:-1]) % 60 + self.unit.s
            m = int(time[:-1]) // 60 + self.unit.m
        elif time[-1] == 'm':
            m = int(time[:-1]) + self.unit.m
            s = self.unit.s
            
        if m*60 + s > 5400:
            self.unit.s = 0
            self.unit.m = 90
            return
        if s < 0:
            s = 0
        if m < 0:
            m = 0
        self.unit.s = s
        self.unit.m = m

    def set_time(self, time):
        m, s = map(int, time.split(':'))
        time = str(m*60 + s)+ 's'
        self.check_time(time)
        
    def add_time(self, time):
        self.check_time(time)

    def del_time(self, time):
        time = '-' + time
        self.check_time(time)

    def show_time(self):
        s = str(self.unit.s)
        m = str(self.unit.m)
        if len(m) == 1:
            m = '0'+m
        if len(s) == 1:
            s = '0'+s
        if self.unit.defect_digit == '':
            return f'{m}:{s}'
        else:
            time = m+':'+s
            return time[:self.unit.defect_digit] + '_' + time[1+self.unit.defect_digit:]



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    microwave_1 = Microwave1()
    rc_1 = RemoteControl(microwave_1)
    rc_1.set_time("05:33")
    print(rc_1.unit.m)
    print(rc_1.unit.s)
    rc_1.del_time("30s")
    print(rc_1.unit.m)
    print(rc_1.unit.s)
    rc_1.del_time("2m")
    print(rc_1.unit.m)
    print(rc_1.unit.s)
    rc_1.show_time()

    
    
