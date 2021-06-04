# import random
# random.choices(['one', 'two', 'three'], [0.2, 0.3, 0.5], k=10)
# ['three', 'two', 'three', 'three', 'three',
#  'three', 'three', 'two', 'two', 'one']




class Drops:
    def __init__(self, ItemName = "", Description = "", Emote = "", ItemType = "", CountRange = [1,5] ):
        self.itemname = ItemName
        self.description = Description
        self.emote = Emote
        self.itemtype = ItemType
        self.countrange = CountRange



# Gold

Gold = Drops( "Gold", "The shiny currency of Grimm RPG", ":coin:", "Gold", [25,50] )


# Goblin Eye

GoblinEye = Drops ("Goblin's Eye", "Torn from an evil goblin", ":eye:", "Drop", [1,2])