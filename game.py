"""
Chapitre 11.1

Classes pour représenter un personnage.
"""


import random

import utils


class Weapon:
	"""
	Une arme dans le jeu.

	:param name: Le nom de l'arme
	:param power: Le niveau d'attaque
	:param min_level: Le niveau minimal pour l'utiliser
	"""
	UNARMED_POWER = 20

	def __init__(self, name, power, min_level):
		self.__name = name
		self.power = power
		self.min_level = min_level

	@property
	def name(self):
		return self.__name

	@classmethod
	def make_unarmed(cls):
		return cls('Unarmed', cls.UNARMED_POWER, 1)


class Character:
	"""
	Un personnage dans le jeu

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param attack: Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage
	"""
	def __init__(self, name, max_hp, attack, defense, level):
		self.__name = name
		self.max_hp = max_hp
		self.attack = attack
		self.defense = defense
		self.level = level
		self.weapon = None
		self.hp = max_hp

	@property
	def name(self):
		return self.__name

	@property
	def weapon(self):
		return self.__weapon

	@weapon.setter
	def weapon(self, val):
		if val is None:
			val = Weapon.make_unarmed()
		if val.min_level > self.level:
			raise ValueError(Weapon)
		self.__weapon = val

	@property
	def hp(self):
		return self.__hp

	@hp.setter
	def hp(self, val):
		self.__hp = utils.clamp(val, 0, self.max_hp)

	def compute_damage(self, other):
		level_factor = 2*self.level/5 + 2
		power_factor = self.weapon.power
		ratio_factor = self.attack/other.defense
		critical = random.random() <= 1/16
		modifier = (2 if critical <= 1/16 else 1)*random.uniform(0.85,1)
		damage = (level_factor * power_factor * ratio_factor / 50 + 2)* modifier
		return int(round(damage)), critical

def deal_damage(attacker, defender):
	# TODO: Calculer dégâts
	damage, critic = Character.compute_damage(attacker, defender)
	defender.hp -= damage
	print(f"\t\t{attacker.name} a utilisé {attacker.weapon.name}")
	if critic:
		print("C'est un coup critique !")
	print(f"\t\t{defender.name} prend {damage} dommages\n")

def run_battle(c1, c2):
	# TODO: Initialiser attaquant/défendeur, tour, etc.
	attacker = c1
	defender = c2
	turns = 1
	print(f"{attacker.name} commence un combat contre {defender.name} !\n")
	print(f"\t{attacker.name}: Ça va chauffer bebewwww !\n")
	print(f"\t{defender.name} : Vas-y approche toi pour voir !\n")
	while True:
		deal_damage(attacker, defender)
		if defender.hp == 0:
			print(f"{defender.name} a donné sa langue au chat ... littéralement !")
			print(f"{attacker.name} a triomphé")
			break
		turns += 1
		attacker, defender = defender, attacker
	return turns



