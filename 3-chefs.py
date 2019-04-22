class AbstractCook:
    def __init__(self):
        self.food = 0
        self.drink = 0
        self.food_name = 'food'
        self.drink_name = 'drink'

    def add_food(self, quantity, cost):
        self.food += quantity * cost
        

    def add_drink(self, quantity, cost):
        self.drink += quantity * cost
        

    def total(self):
        return f'{self.food_name}: {self.food}, {self.drink_name}: {self.drink}, Total: {self.food + self.drink}'

class JapaneseCook(AbstractCook):
    def __init__(self):
        super().__init__()
        self.food_name = 'Sushi'
        self.drink_name = 'Tea'

class RussianCook(AbstractCook):
    def __init__(self):
        super().__init__()
        self.food_name = 'Dumplings'
        self.drink_name = 'Compote'

class ItalianCook(AbstractCook):
    def __init__(self):
        super().__init__()
        self.food_name = 'Pizza'
        self.drink_name = 'Juice'



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    client_1 = JapaneseCook()
    client_1.add_food(2, 30)
    client_1.add_food(3, 15)
    client_1.add_drink(2, 10)

    client_2 = RussianCook()
    client_2.add_food(1, 40)
    client_2.add_food(2, 25)
    client_2.add_drink(5, 20)

    client_3 = ItalianCook()
    client_3.add_food(2, 20)
    client_3.add_food(2, 30)
    client_3.add_drink(2, 10)

    print(client_1.total())
    print(client_2.total())
    print(client_3.total())
    assert client_1.total() == "Sushi: 105, Tea: 20, Total: 125"
    assert client_2.total() == "Dumplings: 90, Compote: 100, Total: 190"
    assert client_3.total() == "Pizza: 100, Juice: 20, Total: 120"


"""
class Cook:
    
    def __init__(self, food='', drink=''):
        self.fprice, self.dprice = 0, 0
        self.food, self.drink = food, drink
        
    def add_food(self, amount, price):
        self.fprice += amount * price
        
    def add_drink(self, amount, price):
        self.dprice += amount * price
        
    def total(self):
        return f"{self.food}: {self.fprice}, {self.drink}: {self.dprice}, Total: {self.fprice + self.dprice}"

class JapaneseCook(Cook):
    def __init__(self): super().__init__('Sushi', 'Tea')

class RussianCook(Cook):
    def __init__(self): super().__init__('Dumplings', 'Compote')

class ItalianCook(Cook):
    def __init__(self): super().__init__('Pizza', 'Juice')
"""               



