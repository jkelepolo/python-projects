import Modules.Drops as Drop

class Enemy:
    def __init__(self, Name = "", Description = [], LevelRange = [1,10], BaseDamage = 10, Rarity = 1, Loot = [], Weights = [], Attacks = [], Defense = 10 ):
        
        self.name = Name
        self.description = Description
        self.levelrange = LevelRange
        self.basedamage = BaseDamage
        self.rarity = Rarity
        self.loot = Loot
        self.weights = Weights
        self.attacks = Attacks
        self.defense = Defense



# Generic Enemy

# Name = "Goblin"
# Description = "A creature who lives in most biomes with wrinkly green skin bearing yellowed sharp teeth stands before you...\nA Goblin."
# LevelRange = [1,10]
# BaseDamage = 10
# Rarity = 1
# Loot = [Drop.GoblinEye, Drop.Gold]
# Weights = [0.1, 0.5]
# Attacks = ["The Goblin"]
# Defense = 10

# Goblin = Enemy(Name, Description, LevelRange, BaseDamage, Rarity, Loot, Weights, Attacks, Defense)



# Goblin Eenemy

Name = "Goblin"
Description = ["A creature who lives in most biomes with wrinkly green skin bearing yellowed sharp teeth stands before you...\nA Goblin."]
LevelRange = [1,10]
BaseDamage = 10
Rarity = 1
Loot = [Drop.GoblinEye, Drop.Gold]
Weights = [0.1, 0.5]
Attacks = ["The **Goblin** shoots a bow and arrow at you",
           "With all the power he can muster the **Goblin** charges you",
           "The **Goblin** throws stones and rocks at you"]
Defense = 10

Goblin = Enemy(Name, Description, LevelRange, BaseDamage, Rarity, Loot, Weights, Attacks, Defense)