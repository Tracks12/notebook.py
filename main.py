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
	warn = f"{Colors.red}[!]{Colors.end} - "
	tips = f"{Colors.green}(?){Colors.end} - "
	list = f"{Colors.cyan}(*){Colors.end} - "
	info = f"{Colors.blue}(i){Colors.end} - "

class Rep:
	def __init__(self, file):
		self.entries = []
		self.__path = f"reps/{file}.json"
		self.__loadJSON()
		self.menu()

	def __loadJSON(self):
		try:
			print(f"{Icons.info}Chargement du répertoire ...")

			with open(self.__path, "r", encoding = "utf-8") as inFile:
				self.entries = load(inFile)
				print(f"{Icons.info}Répertoire charger")

		except Exception:
			print(f"{Icons.warn}Répertoire introuvable")
			print(f"{Icons.info}Création du répertoire ...")

			with open(self.__path, "w", encoding = "utf-8") as outFile:
				dump([], outFile, sort_keys=True, indent=2)
				print(f"{Icons.info}Nouveau répertoire crée")

	def __saveJSON(self):
		print(f"{Icons.info}Sauvegarde du répertoire ...")

		with open(self.__path, "w", encoding = "utf-8") as outFile:
			dump(self.entries, outFile, sort_keys=True, indent=2)
			print(f"{Icons.info}Répertoire sauvegarder")

	def menu(self):
		menu = [
			f"{Colors.cyan}C{Colors.end}.\tCréer une nouvelle entrée",
			f"{Colors.cyan}D{Colors.end}.\tSupprimer une entrée correspondant à un nom donné",
			f"{Colors.cyan}A{Colors.end}.\tAfficher la fiche correspondant à un nom donné",
			f"{Colors.cyan}G{Colors.end}.\tAfficher toutes les fiches",
			f"{Colors.cyan}V{Colors.end}.\tFiches ayant une Valeur donnée pour un champ donné",
			f"{Colors.cyan}S{Colors.end}.\tFiches qui Satisfont un critère donné\n",
			f"{Colors.green}?{Colors.end}.\tAffichger le menu",
			f"{Colors.red}Q{Colors.end}.\tQuitter et sauvegarder le répertoire"
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
			name = str(input(f"Nom: {Colors.red}"))

			for key, item in enumerate(self.entries):
				if(item["name"] == name):
					self.entries.pop(key)
					print(f"\n{Icons.info}L'entrée à bien été supprimer")
					self.__saveJSON()

					return True

			print(f"{Icons.warn}Il y a pas d'entrée portant ce nom")

			return False

		except Exception:
			print(f"{Icons.warn}Guiguigui, ça marche po bordel !")

	def sortAll(self):
		for item in self.entries:
			self.display(item)
			print("")

	def sortOnceByName(self):
		try:
			name = str(input(f"Nom: {Colors.green}")).upper()
			print(f"{Colors.end}----")

			for item in self.entries:
				if(item["name"] in name):
					self.display(item)

		except Exception:
			print(f"{Icons.warn}Non non non, t'arrête ça de suite baptiste !")

	def insert(self):
		try:
			fields = {
				"name":     str(input(f"{Colors.end}Nom\t\t: {Colors.cyan}")).upper(),
				"fname":    str(input(f"{Colors.end}Prénom\t\t: {Colors.cyan}")).capitalize(),
				"age":      int(input(f"{Colors.end}Age\t\t: {Colors.cyan}")),
				"function": str(input(f"{Colors.end}Fonction\t: {Colors.cyan}")),
				"phone":    str(input(f"{Colors.end}Tel\t\t: {Colors.cyan}")),
				"mail":     str(input(f"{Colors.end}Mail\t\t: {Colors.cyan}")).lower(),
				"address":  str(input(f"{Colors.end}Adresse\t\t: {Colors.cyan}"))
			}

			if(self.add(fields)):
				print(f"\n{Icons.info}L'entrée à bien été enregistrer")
				self.__saveJSON()

				return True

			else:
				return False

		except Exception:
			print(f"{Icons.warn}On insère pas de la merde Kévin !")

	def display(self, item):
		print(f'Nom\t\t: {item["name"].upper()}')
		print(f'Prénom\t\t: {item["fname"].capitalize()}')
		print(f'Age\t\t: {item["age"]}')
		print(f'Fonction\t: {item["function"].capitalize()}')
		print(f'Tel\t\t: {item["phone"]}')
		print(f'Mail\t\t: {item["mail"].lower()}')
		print(f'Adresse\t\t: {item["address"].lower()}')
		print("-------")

def main(system = system()):
	if(len(argv) > 1):
		if(argv[1] in ("-l", "--load")):
			try:
				repo = Rep(argv[2])

			except Exception:
				print(f"{Icons.warn}Insérer le nom du fichier en argument")
				return(False)

	else:
		shell("clear" if(system == "Linux") else "cls")

		path = str(input(f"Entrer le nom du répertoire: {Colors.green}"))
		print(Colors.end)
		repo = Rep(path);

	while(True):
		try:
			entry = str(input(f"\n> {Colors.cyan}"))[0]
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
				print(f"{Icons.info}Fermeture du répertoire")
				break

		except Exception:
			print(f"{Icons.warn}Céléstin arrête tes carabistouilles !")

	print("Au revoir kheyou ;)")

	return(True)

if(__name__ == "__main__"):
	main()
