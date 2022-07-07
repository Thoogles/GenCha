#!/usr/bin/python3

import unittest
from src.char_gen import Character, PlayerCharacter

class TestPlayerCharacter(unittest.TestCase):
    """Tests for Player Character class methods"""

    def setUp(self):
        """Setup player character object for test cases"""
        self.pc =  PlayerCharacter("Mike")
        self.pc.experience = 100
        self.pc.wounds = 10
        self.pc.strain = 8

    def test_increase_characteristic_player(self):
        """Do the characteristics increase, and does xp get deducted"""
        self.pc.increase_stat("Brawn")
        self.assertEqual(self.pc.stats["Brawn"], 3)

    def test_set_experience(self):
        """Can you set new value for current experience"""
        self.pc.set_current_experience(160)
        self.assertEqual(self.pc.current_experience, 160)


unittest.main()
