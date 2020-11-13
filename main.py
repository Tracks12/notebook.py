#!/bin/python3
# -*- conding: utf-8 -*-

"""
----------------------
 TD: Carnet d'adresse
----------------------
"""

from json import dump, load
from os import system as shell
from platform import system
from sys import argv
from time import sleep

class Colors:
	red   = "\033[31m"
	blue  = "\033[34m"
	green = "\033[32m"
	cyan  = "\033[36m"

	end   = "\033[0m"

class Icons:
	warn = "{}[!]{} - ".format(Colors.red, Colors.end)
	tips = "{}(?){} - ".format(Colors.green, Colors.end)
	list = "{}(*){} - ".format(Colors.cyan, Colors.end)
	info = "{}(i){} - ".format(Colors.blue, Colors.end)

class Rep:
	def __init__(self, file):
		self.entries = []
		self.__path = "reps/{}.json".format(file)
		self.__loadJSON()
		self.menu()

	def __loadJSON(self):
		try:
			print("{}Chargement du répertoire ...".format(Icons.info))

			with open(self.__path) as inFile:
				self.entries = load(inFile)
				print("{}Répertoire charger".format(Icons.info))

		except Exception:
			print("{}Répertoire introuvable".format(Icons.warn))
			print("{}Création du répertoire ...".format(Icons.info))

			with open(self.__path, 'w') as outFile:
				dump([], outFile, sort_keys=True, indent=2)
				print("{}Nouveau répertoire crée".format(Icons.info))

	def __saveJSON(self):
		print("{}Sauvegarde du répertoire ...".format(Icons.info))

		with open(self.__path, 'w') as outFile:
			json.dump(self.entries, outFile, sort_keys=True, indent=2)
			print("{}Répertoire sauvegarder".format(Icons.info))

	def menu(self):
		menu = [
			"{}C{}.\tCréer une nouvelle entrée".format(Colors.cyan, Colors.end),
			"{}D{}.\tSupprimer une entrée correspondant à un nom donné".format(Colors.cyan, Colors.end),
			"{}A{}.\tAfficher la fiche correspondant à un nom donné".format(Colors.cyan, Colors.end),
			"{}G{}.\tAfficher toutes les fiches".format(Colors.cyan, Colors.end),
			"{}V{}.\tFiches ayant une Valeur donnée pour un champ donné".format(Colors.cyan, Colors.end),
			"{}S{}.\tFiches qui Satisfont un critère donné\n".format(Colors.cyan, Colors.end),
			"{}?{}.\tAffichger le menu".format(Colors.green, Colors.end),
			"{}Q{}.\tQuitter et sauvegarder le répertoire".format(Colors.red, Colors.end)
		]

		print("\nRépertoire:")
		print("-----------\n")

		for item in menu:
			print(item)
			sleep(.025)

		return True

	def add(self, fields):
		self.entries.append(fields)

		return True

	def rem(self):
		try:
			name = str(input("Nom: {}".format(Colors.red)))

			for key, item in enumerate(self.entries):
				if(item["name"] == name):
					self.entries.pop(key)
					print("\n{}L'entrée à bien été supprimer".format(Icons.info))
					self.__saveJSON()

					return True

			print("{}Il y a pas d'entrée portant ce nom".format(Icons.warn))

			return False

		except Exception:
			print("{}Guiguigui, ça marche po bordel !".format(Icons.warn))

	def sortAll(self):
		for item in self.entries:
			self.display(item)
			print("")

	def sortOnceByName(self):
		try:
			name = str(input("Nom: {}".format(Colors.green)))
			print("{}----".format(Colors.end))

			for item in self.entries:
				if(item["name"] in name):
					self.display(item)

		except Exception:
			print("{}Non non non, t'arrête ça de suite baptiste !".format(Icons.warn))

	def insert(self):
		try:
			fields = {
				"name":     str(input("{}Nom\t\t: {}".format(Colors.end, Colors.cyan))),
				"fname":    str(input("{}Prénom\t\t: {}".format(Colors.end, Colors.cyan))),
				"age":      int(input("{}Age\t\t: {}".format(Colors.end, Colors.cyan))),
				"function": str(input("{}Fonction\t: {}".format(Colors.end, Colors.cyan))),
				"phone":    str(input("{}Tel\t\t: {}".format(Colors.end, Colors.cyan))),
				"mail":     str(input("{}Mail\t\t: {}".format(Colors.end, Colors.cyan))),
				"address":  str(input("{}Adresse\t\t: {}".format(Colors.end, Colors.cyan)))
			}

			if(self.add(fields)):
				print("\n{}L'entrée à bien été enregistrer".format(Icons.info))
				self.__saveJSON()

				return True

			else:
				return False

		except Exception:
			print("{}On insère pas de la merde Kévin !".format(Icons.warn))

	def display(self, item):
		print("Nom\t\t: {}".format(item["name"].capitalize()))
		print("Prénom\t\t: {}".format(item["fname"].capitalize()))
		print("Age\t\t: {}".format(item["age"]))
		print("Fonction\t: {}".format(item["function"].capitalize()))
		print("Tel\t\t: {}".format(item["phone"]))
		print("Mail\t\t: {}".format(item["mail"].lower()))
		print("Adresse\t\t: {}".format(item["address"].lower()))
		print("-------")

def main(system = system()):
	if(len(argv) > 1):
		if(argv[1] in ("-l", "--load")):
			try:
				repo = Rep(argv[2])

			except Exception:
				print("{}Insérer le nom du fichier en argument".format(Icons.warn))
				return(False)

	else:
		shell("clear" if(system == "Linux") else "cls")

		path = str(input("Entrer le nom du répertoire: {}".format(Colors.green)))
		print(Colors.end)
		repo = Rep(path);

	while(True):
		try:
			entry = input("\n> {}".format(Colors.cyan))[0]
			print(Colors.end)

			commands = (
				("Cc", lambda:repo.insert()),
				("Dd", lambda:repo.rem()),
				("Aa", lambda:repo.sortOnceByName()),
				("Gg", lambda:repo.sortAll()),
				("?", lambda:repo.menu()),
			)

			for command in commands:
				if(entry in command[0]):
					command[1]()

			if(entry in "Qq"):
				print("{}Fermeture du répertoire".format(Icons.info))
				break

		except Exception:
			print("{}Céléstin arrête tes carabistouilles !".format(Icons.warn))

	print("Au revoir kheyou ;)")

	return(True)

if(__name__ == '__main__'):
	main()
