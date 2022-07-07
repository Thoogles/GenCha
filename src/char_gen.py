#!/usr/bin/python3

class Character():
    """Model of a character in Genesys RPG"""

    def __init__(self, name):
        """Initialize the attributes of a character"""
        self.name = name
        self.stats = {"Brawn": 2, "Agility": 2, "Intellect": 2, "Cunning": 2, "Willpower": 2, "Presence": 2}
        self.wounds = 0
        self.soak = 0
        self.skills = {"skills": {}}
        self.talents = {}
        self.items = []
        self.defense = {"Melee": 0, "Range": 0}

    def get_stats(self):
        """Returns the stats dictionary"""
        return self.stats

    def set_stats(self, stats={}):
        """Set stat values

        stats: Should be dictionary."""
        self.stats = stats

    def get_wounds(self):
        """Returns the wound threshold of character"""
        return self.wounds

    def set_wounds(self, wounds=0):
        """Sets the wounds threshold value of a character.
        wounds: has to be integer"""
        try:
            self.wounds = int(wounds)
        except ValueError:
            print("wound value must be integer")

class PlayerCharacter(Character):
    """Model of a player character in Genesys RPG"""

    def __init__(self, name):
        """Initilize the attributes of player character"""
        super().__init__(name)
        self.strain = 0
        self.species = ""
        self.career = ""
        self.current_experience = 0
        self.total_experience = 0

    def increase_stat(self, stat):
        """Increase one stat/characteristic of a character, and reduce their xp accordingly."""
        if self.stats[stat] < 5:
            self.stats[stat] += 1
            self.current_experience -= (self.stats[stat] + 1) * 10
        else:
            raise ValueError("Cannot raise characteristic over 5")

    def increase_wounds(self, increase):
        """Increase the player characters wound threshold"""
        self.wounds += increase

    def decrease_wounds(self, decrease):
        """Decrease the player characters wound threshold"""
        self.wounds -= decrease

    def increase_skill_rank(self, skill):
        """Increase skill ranks of the player character, but do not do so if they are at max rank (5)"""
        if self.skills[skill] < 5:
            self.skills[skill] += 1
            # If skill is career skill, experience cost is rank x 5
            if self.skills[skill]:
                self.current_experience -= (self.skills[skill] + 1) * 5
            # If skill is not career skill, experience cost is rank x 5 + 5
            else:
                self.current_experience -= ((self.skills[skill] + 1) * 5) + 5
        else:
            raise ValueError("Cannot raise skill rank over 5")


if __name__ == "__main__":
    pass
