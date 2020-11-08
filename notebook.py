#!/bin/python3
# -*- conding: utf-8 -*-

"""
----------------------
 TD: Carnet d'adresse
----------------------
"""

from platform import system
import os, sys

from core.colors import Colors as color
from core.icons import Icons as icon
from core.rep import Rep

def main():
	if(len(sys.argv) > 1):
		if(sys.argv[1] in ("-l", "--load")):
			try:
				repo = Rep(sys.argv[2])

			except Exception:
				print("{}Insérer le nom du fichier en argument".format(icon.warn))
				exit()

	else:
		os.system("clear" if(system == "Linux") else "cls")

		path = input("Entrer le nom du répertoire: {}".format(color.green))
		print(color.end)
		repo = Rep(path);

	while(True):
		try:
			command = input("\n> {}".format(color.cyan))[0]
			print(color.end)

			if(command in "Cc"): repo.insert()
			elif(command in "Dd"): repo.rem()
			elif(command in "Aa"): repo.sortOnceByName()
			elif(command in "Gg"): repo.sortAll()
			elif(command in "?"): repo.menu()

			elif(command in "Qq"):
				print("{}Fermeture du répertoire".format(icon.info))
				break

		except Exception:
			print("{}Céléstin arrête tes carabistouilles !".format(icon.warn))

if(__name__ == '__main__'):
	system = system()

	main()
	print("Au revoir kheyou ;)")
