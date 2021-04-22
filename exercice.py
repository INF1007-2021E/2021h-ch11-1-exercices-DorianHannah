from game import *


def main():
	positive_vibes = Weapon("Énergies positives", 53, 4)
	rale = Weapon("Rallement", 40, 3)
	epee_de_feu = Weapon("Épée de feu", 63, 5)
	pain_choc = Weapon("Pain au chocolat", 48, 2)

	Titi = Character("Thibault le titan", 100, 65, 16, 6)
	Dodo = Character("Dodo la malice", 110, 52, 21 , 4)

	Titi.weapon = epee_de_feu
	Dodo.weapon = positive_vibes

	turns = run_battle(Dodo, Titi)
	print(f"Le combat s'est terminé en {turns} tours !")

if __name__ == "__main__":
	main()

