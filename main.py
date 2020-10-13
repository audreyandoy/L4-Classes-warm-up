class Pokemon:
    # name, type, HP, Level, powers
    def __init__(self, name, type, HP, level, power):
        self.name = name
        self.type = type
        self.HP = HP
        self.level = level
        self.power = power
        

pikachu = Pokemon("pikachu", "lighting", 100, 5, ["lightening bolt", "iron tail", "tail whip"])

print(pikachu.name)

print(pikachu.HP - 10)

squirtle = Pokemon("squirtle", "water", 100, 5, ["water splash", "tackle", "skullbash"])
print(squirtle.power)

print(vars(squirtle))