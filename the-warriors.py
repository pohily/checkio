class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        
    @property
    def is_alive(self):
        return self.health > 0

class Knight(Warrior):
    def __init__(self):
        Warrior.__init__(self)
        self.attack = 7

class Defender(Warrior):
    def __init__(self):
        Warrior.__init__(self)
        self.health = 60
        self.attack = 3
        self.defense = 2
        
        
def fight(unit_1, unit_2):
    while unit_1.is_alive and unit_2.is_alive:
        if isinstance(unit_2, Defender):
            if unit_1.attack > unit_2.defense:
                unit_2.health -= (unit_1.attack - unit_2.defense)
            #print('1unit_2', unit_2.health)
        else:
            unit_2.health -= unit_1.attack
            #print('2unit_2', unit_2.health)
        if unit_2.is_alive:
            if isinstance(unit_1, Defender):
                if unit_2.attack > unit_1.defense:
                    unit_1.health -= (unit_2.attack - unit_1.defense)
                #print('1unit_1', unit_1.health)
            else:
                unit_1.health -= unit_2.attack
                #print('2unit_1', unit_1.health)
            
    return unit_1.is_alive

class Army():
    def __init__(self):
        self.army = []

    def add_units(self, unit, num):
        self.army += [unit() for i in range(num)]
        
class Battle():
    def fight(self, army1, army2):
        while army1.army and army2.army:
            x = army1.army[0]
            y = army2.army[0]
            if fight(x, y):
                army2.army.pop(0)
            else:
                army1.army.pop(0)
        return True if army1.army else False




        
rog = Warrior()
lancelot = Defender()
print(fight(lancelot, rog))
print(lancelot.is_alive)

"""
def fight(unit_1, unit_2):
    flag=1
    while unit_1.health>0 and unit_2.health>0:
        if flag:
            attack=unit_1.attack - (unit_2.defense if hasattr(unit_2,'defense') else 0)
            unit_2.health-=attack if attack>0 else 0
            if unit_2.health<=0:unit_2.is_alive=False
            flag=0
        else: 
            attack=unit_2.attack - (unit_1.defense if hasattr(unit_1,'defense') else 0)
            unit_1.health-=attack if attack>0 else 0
            if unit_1.health<=0:unit_1.is_alive=False
            flag=1
    return unit_1.health>0


    def __str__(self):
        return f'{self.__class__.__name__} (health={self.health}, attack={self.attack}, defense={self.defense})'
    """


