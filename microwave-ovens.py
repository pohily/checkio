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

    def check_time(self, m, s):
        """
        Check if time is in the limits and set it to memory
        """
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
        self.check_time(m, s)
        
    def add_time(self, time):
        if time[-1] == 's':
            t = self.unit.s + self.unit.m * 60 + int(time[:-1])
            s = t % 60 
            m = t // 60
        elif time[-1] == 'm':
            t = self.unit.s + self.unit.m * 60 + int(time[:-1]) * 60
            s = t % 60 
            m = t // 60
        self.check_time(m, s)

    def del_time(self, time):
        if time[-1] == 's':
            t = self.unit.s + self.unit.m * 60 - int(time[:-1])
            if t < 0:
                s = - (t % 60)
                m = int(t / 60)
            else:
                s = t%60
                m = t // 60
        elif time[-1] == 'm':
            t = self.unit.s + self.unit.m * 60 - int(time[:-1]) * 60
            s = t % 60 
            m = t // 60
        self.check_time(m, s)

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

    

    microwave_3 = Microwave3()
    rc_3 = RemoteControl(microwave_3)
    print(rc_3.unit.m)
    print(rc_3.unit.s)
    rc_3.del_time("90s")
    print(rc_3.unit.m)
    print(rc_3.unit.s)
    rc_3.del_time("6m")
    print(rc_3.unit.m)
    print(rc_3.unit.s)
    rc_3.add_time("2m")
    print(rc_3.unit.m)
    print(rc_3.unit.s)
    rc_3.show_time()
