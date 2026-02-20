#Making this probably took about 15 minutes all typed out by hand without any help from AI
#Note how we are using encapsulation to manage the character's stats
#Getters and setters are used to control access to the character's health and mana attributes
#This ensures that health and mana values remain within valid ranges

class GameCharacter:
    def __init__(self, name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1
    
    @property
    def name(self):
        return self._name
    
    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, new_health):
        if new_health < 0:
            self._health = 0
        elif new_health > 100:
            self._health = 100
        else:
            self._health = new_health
    
    @property
    def mana(self):
        return self._mana
    
    @mana.setter
    def mana(self, new_mana):
        if new_mana < 0:
            self._mana = 0
        elif new_mana > 50:
            self._mana = 50
        else:
            self._mana = new_mana

    @property
    def level(self):
        return self._level
    
    def level_up(self):
        self._level += 1
        self.mana = 50
        self.health = 100
        print(f"{self.name} leveled up to {self.level}!")
    
    def __str__(self):
        return (f'Name: {self.name}\nLevel: {self.level}\nHealth: {self.health}\nMana: {self.mana}')

kratos = GameCharacter('Kratos')
print(kratos)

kratos.health -= 30
kratos.mana -= 10
print(kratos)

kratos.level_up()