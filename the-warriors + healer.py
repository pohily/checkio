class Warrior:
    def __init__(self):
        self.name = 'Warrior'
        self.health = 50
        self.attack = 5
        self.maxhealth = self.health
        self.hit = 0

    def __repr__(self):
        return f'{self.name},{self.hit} {self.health}/{self.maxhealth}'

    def self_damage(self, enemy):
        self.health -= enemy.attack
        self.hit +=1
        if isinstance(enemy, Vampire):
            enemy.health += enemy.attack * enemy.vampirism
    
    @property
    def is_alive(self):
        return self.health > 0

class Knight(Warrior):
    def __init__(self):
        Warrior.__init__(self)
        self.name = 'Knight'
        self.attack = 7

class Defender(Warrior):
    def __init__(self):
        Warrior.__init__(self)
        self.name = 'Defender'
        self.health = 60
        self.maxhealth = self.health
        self.attack = 3
        self.defense = 2

    def self_damage(self, enemy):
        if enemy.attack > self.defense:
            self.health -= enemy.attack - self.defense
            self.hit += 1
            if isinstance(enemy, Vampire):
                enemy.health += (enemy.attack - self.defense) * enemy.vampirism

class Vampire(Warrior):
    def __init__(self):
        Warrior.__init__(self)
        self.name = 'Vampire'
        self.health = 40
        self.maxhealth = self.health
        self.attack = 4
        self.vampirism = 0.5

class Lancer(Warrior):
    def __init__(self):
        Warrior.__init__(self)
        self.name = 'Lancer'
        self.health = 50
        self.maxhealth = self.health
        self.attack = 6

class Healer(Warrior):
    def __init__(self):
        Warrior.__init__(self)
        self.name = 'Healer'
        self.health = 60
        self.maxhealth = self.health
        self.attack = 0

    def heal(self, patient):
        patient.health += 2 
        if patient.health > patient.maxhealth:
            patient.health = patient.maxhealth

        
        
def fight(unit_1, unit_2, healer1=0, healer2=0):
    print()
    print('new fight', unit_1, unit_2)
    while unit_1.is_alive and unit_2.is_alive:
        # unit1 hit
        unit_2.self_damage(unit_1)
        
        # Healer heal
        if healer2:
            unit_2.health += 2
            if unit_2.health > unit_2.maxhealth:
                unit_2.health = unit_2.maxhealth
       
        # unit2 hit if alive
        if unit_2.is_alive:
            unit_1.self_damage(unit_2)
            
            # Healer heal
            if healer1:
                unit_1.health += 2
                if unit_1.health > unit_1.maxhealth:
                    unit_1.health = unit_1.maxhealth
            
        print(unit_1, unit_2)
    return unit_1.is_alive

class Army():
    def __init__(self):
        self.army = []

    def add_units(self, unit, num):
        self.army += [unit() for i in range(num)]
        
class Battle():
    def straight_fight(self, army1, army2):
        print()
        print('New Straight Battle')
        while army1.army and army2.army:
            
            for index in range(min(len(army1.army), len(army2.army))):
                
                fight(army1.army[index], army2.army[index])
            #remove the dead
            tmp = []        
            for i in army1.army:
                if i.is_alive:
                    tmp.append(i)
            army1.army = tmp[:]
            tmp = [] 
            for i in army2.army:
                if i.is_alive:
                    tmp.append(i)
            army2.army = tmp[:]
            print(army1.army)
            print(army2.army)
        
        return True if army1.army else False

    def fight(self, army1, army2):
        print()
        print('New Battle')
        while army1.army and army2.army:
            x = army1.army[0]
            y = army2.army[0]
            
            try:
                # check for healer
                healer1, healer2, lancer1, lancer2 = 0, 0, 0, 0
                if isinstance(army1.army[1], Healer):
                    healer1 = 1
                if isinstance(army2.army[1], Healer):
                    healer2 = 1

                # check for lancer. Remember number of hits before fight
                if isinstance(x, Lancer):
                    lancer1 = army2.army[0].hit
                if isinstance(y, Lancer):
                    lancer2 = army1.army[0].hit
            except IndexError:
                pass

            if fight(x, y, healer1, healer2):
                
                # if lancer. Change health of second unit by number of hits
                try:
                    if isinstance(x, Lancer):
                        lancer1 = army2.army[0].hit - lancer1
                        army2.army[1].health -= lancer1 * 3
                        if isinstance(army2.army[1], Defender) or isinstance(army2.army[2], Healer):
                                army2.army[1].health += lancer1 * 2
                        # check if next unit killed by lancer and one more is hit
                        if army2.army[1].health <= 0:
                            delta = abs(army2.army[1].health)
                            del army2.army[1]
                            if isinstance(army2.army[1], Defender) or isinstance(army2.army[2], Healer):
                                delta -= lancer1 * 2
                            army2.army[1].health -= delta
                    if isinstance(y, Lancer):
                        lancer2 = army1.army[0].hit - lancer2
                        army1.army[1].health -= lancer2 * 3
                        if isinstance(army1.army[1], Defender) or isinstance(army1.army[2], Healer):
                                army1.army[1].health += lancer2* 2
                        if army1.army[1].health <= 0:
                            delta = abs(army1.army[1].health)
                            del army1.army[1]
                            if isinstance(army1.army[1], Defender) or isinstance(army1.army[2], Healer):
                                delta -= lancer2 * 2
                            army1.army[1].health -= delta
                except IndexError:
                    pass
                print('l1', lancer1, 'l2', lancer2)
                army2.army.pop(0)
            else:
                # if lancer. Change health of second unit by number of hits
                try:
                    if isinstance(x, Lancer):
                        lancer1 = army2.army[0].hit - lancer1
                        army2.army[1].health -= lancer1 * 3
                        if isinstance(army2.army[1], Defender) or isinstance(army2.army[2], Healer):
                                army2.army[1].health += lancer1 * 2
                        # check if next unit killed by lancer and one more is hit
                        if army2.army[1].health <= 0:
                            delta = abs(army2.army[1].health)
                            del army2.army[1]
                            if isinstance(army2.army[1], Defender) or isinstance(army2.army[2], Healer):
                                delta -= lancer1 * 2
                            army2.army[1].health -= delta
                    if isinstance(y, Lancer):
                        lancer2 = army1.army[0].hit - lancer2
                        army1.army[1].health -= lancer2 * 3
                        if isinstance(army1.army[1], Defender) or isinstance(army1.army[2], Healer):
                                army1.army[1].health += lancer2* 2
                        if army1.army[1].health <= 0:
                            delta = abs(army1.army[1].health)
                            del army1.army[1]
                            if isinstance(army1.army[1], Defender) or isinstance(army1.army[2], Healer):
                                delta -= lancer2 * 2
                            army1.army[1].health -= delta
                except IndexError:
                    pass
                print('l1', lancer1, 'l2', lancer2)
                army1.army.pop(0)
        return True if army1.army else False

       

army_1 = Army()
army_2 = Army()
army_1.add_units(Lancer, 5)
army_1.add_units(Vampire, 3)
army_1.add_units(Warrior, 4)
army_1.add_units(Defender, 2)

army_2.add_units(Warrior, 4)
army_2.add_units(Defender, 4)
army_2.add_units(Vampire, 6)
army_2.add_units(Lancer, 5)
battle = Battle()
print(battle.straight_fight(army_1, army_2))
