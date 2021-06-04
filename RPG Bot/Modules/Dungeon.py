import Modules.Enemy as Enemy
import Modules.Drops as Drops

class Dungeon:
    def __init__(self, Name = "", Enemies = [], Beginning = [], Smells = [], Sights = [], Sounds = [], Touch = [], Taste = [], Feelings = [], Movement = [], End = [], Death = [], Loot = []):
        self.name = Name
        self.enemies = Enemies
        self.beginning = Beginning
        self.smells = Smells
        self.sights = Sights
        self.sounds = Sounds
        self.touch = Touch
        self.taste = Taste
        self.feelings = Feelings
        self.movement = Movement
        self.end = End
        self.death = Death
        self.loot = Loot


# Generic Dungeon
# Name = "GenericDungeon"
# Enemies = []
# Beginning = []
# Smells = []
# Sights = []
# Sounds = []
# Touch = []
# Taste = []
# Feelings = []
# Movement = []
# End = []
# Death = []
# Loot = []
# GenericDungeon = Dungeon(Name, Enemies, Beginning, Smells, Sights, Sounds, Touch, Taste, Feelings, Movement, End, Death, Loot)




# Plains Dungeon
Name = "Plains"
Enemies = [Enemy.Goblin]
Beginning = ["You peer across the great plains and prepare to take on what ever comes your way",
             "The great plains lay before you wanderer, proceed with caution",
             "You see grassy fields ahead of you, there is also a sense of danger"]
Smells = []
Sights = []
Sounds = []
Touch = []
Taste = []
Feelings = []
Movement = []
End = []
Death = []
Loot = []
PlainsDungeon = Dungeon(Name, Enemies, Beginning, Smells, Sights, Sounds, Touch, Taste, Feelings, Movement, End, Death, Loot)

































