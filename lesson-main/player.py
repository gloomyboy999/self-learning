class Player:
    def __init__(self, name, ap):
        print("我誕生了")
        self.name = name
        self.hp = 100
        self.ap = ap
    def attack(self, target):
        print(self.name, "attacking", target.name)
        target.hp = target.hp - self.ap


p1 = Player("Player1", 5)
p2 = Player("Player1", 10)
p1.attack(p2)
print(p2.hp)