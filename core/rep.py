#!/bin/python3
# -*- conding: utf-8 -*-

import json
from time import sleep

from core.colors import Colors as color
from core.icons import Icons as icon

class Rep:
	def __init__(self, file):
		self.entries = []
		self.__path = "{}.json".format(file)
		self.loadJSON()
		self.menu()

	def menu(self):
		menu = [
			"{}C{}.\tCréer une nouvelle entrée".format(color.cyan, color.end),
			"{}D{}.\tSupprimer une entrée correspondant à un nom donné".format(color.cyan, color.end),
			"{}A{}.\tAfficher la fiche correspondant à un nom donné".format(color.cyan, color.end),
			"{}G{}.\tAfficher toutes les fiches".format(color.cyan, color.end),
			"{}V{}.\tFiches ayant une Valeur donnée pour un champ donné".format(color.cyan, color.end),
			"{}S{}.\tFiches qui Satisfont un critère donné\n".format(color.cyan, color.end),
			"{}?{}.\tAffichger le menu".format(color.green, color.end),
			"{}Q{}.\tQuitter et sauvegarder le répertoire".format(color.red, color.end)
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
			name = str(input("Nom: {}".format(color.red)))

			for key, item in enumerate(self.entries):
				if(item["name"] == name):
					self.entries.pop(key)
					print("\n{}L'entrée à bien été supprimer".format(icon.info))
					self.saveJSON()

					return True

			print("{}Il y a pas d'entrée portant ce nom".format(icon.warn))

			return False

		except Exception:
			print("{}Guiguigui, ça marche po bordel !".format(icon.warn))

	def sortAll(self):
		for item in self.entries:
			self.display(item)
			print("")

	def sortOnceByName(self):
		try:
			name = str(input("Nom: {}".format(color.green)))
			print("{}----".format(color.end))

			for item in self.entries:
				if(item["name"] in name):
					self.display(item)

		except Exception:
			print("{}Non non non, t'arrête ça de suite baptiste !".format(icon.warn))

	def insert(self):
		try:
			fields = {
				"name":     str(input("{}Nom\t\t: {}".format(color.end, color.cyan))),
				"fname":    str(input("{}Prénom\t\t: {}".format(color.end, color.cyan))),
				"age":      int(input("{}Age\t\t: {}".format(color.end, color.cyan))),
				"function": str(input("{}Fonction\t: {}".format(color.end, color.cyan))),
				"phone":    str(input("{}Tel\t\t: {}".format(color.end, color.cyan))),
				"mail":     str(input("{}Mail\t\t: {}".format(color.end, color.cyan))),
				"address":  str(input("{}Adresse\t\t: {}".format(color.end, color.cyan)))
			}

			if(self.add(fields)):
				print("\n{}L'entrée à bien été enregistrer".format(icon.info))
				self.saveJSON()

				return True

			else:
				return False

		except Exception:
			print("{}On insère pas de la merde Kévin !".format(icon.warn))

	def display(self, item):
		print("Nom\t\t: {}".format(item["name"].capitalize()))
		print("Prénom\t\t: {}".format(item["fname"].capitalize()))
		print("Age\t\t: {}".format(item["age"]))
		print("Fonction\t: {}".format(item["function"].capitalize()))
		print("Tel\t\t: {}".format(item["phone"]))
		print("Mail\t\t: {}".format(item["mail"].lower()))
		print("Adresse\t\t: {}".format(item["address"].lower()))
		print("-------")

	def loadJSON(self):
		try:
			print("{}Chargement du répertoire ...".format(icon.info))

			with open(self.__path) as inFile:
				self.entries = json.load(inFile)
				print("{}Répertoire charger".format(icon.info))

		except Exception:
			print("{}Répertoire introuvable".format(icon.warn))
			print("{}Création du répertoire ...".format(icon.info))

			with open(self.__path, 'w') as outFile:
				json.dump([], outFile, sort_keys=True, indent=2)
				print("{}Nouveau répertoire crée".format(icon.info))

	def saveJSON(self):
		print("{}Sauvegarde du répertoire ...".format(icon.info))

		with open(self.__path, 'w') as outFile:
			json.dump(self.entries, outFile, sort_keys=True, indent=2)
			print("{}Répertoire sauvegarder".format(icon.info))
