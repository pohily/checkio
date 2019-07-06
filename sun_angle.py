def sun_angle(time):
    time_min = int(time[:2])*60 + int(time[3:])
    if time_min < 360 or time_min > 1080:
        return "I don't see the sun!"
    else:
        return (time_min - 360) / 4
    
    
    
print(sun_angle("12:15"))

"""
import unittest

def sun_angle(time):
    h, m = map(int, time.split(':'))
    day_part = h + m / 60 - 6
    return day_part / 12 * 180 if 0 <= day_part <= 12 else "I don't see the sun!"

td = {'06:00':0,
      '12:00':90,
      '18:00':180,
      '07:00':15,
      '01:23':"I don't see the sun!"}

class TestSolution(unittest.TestCase):
    def test_1(self):
        for d in td:
            self.assertEqual(sun_angle(d), td[d])




hour, minu = time.split(":")

hours, mins = map(int, time.split(":"))
    """


