#!/bin/python3
# -*- conding: utf-8 -*-

"""
----------------------
 TD: Carnet d'adresse
----------------------
"""

from os import system as shell
from platform import system
from sys import argv

from core.colors import Colors as color
from core.icons import Icons as icon
from core.rep import Rep

def main(system = system()):
	if(len(argv) > 1):
		if(argv[1] in ("-l", "--load")):
			try:
				repo = Rep(argv[2])

			except Exception:
				print("{}Insérer le nom du fichier en argument".format(icon.warn))
				return(False)

	else:
		shell("clear" if(system == "Linux") else "cls")

		path = str(input("Entrer le nom du répertoire: {}".format(color.green)))
		print(color.end)
		repo = Rep(path);

	while(True):
		try:
			entry = input("\n> {}".format(color.cyan))[0]
			print(color.end)

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
				print("{}Fermeture du répertoire".format(icon.info))
				break

		except Exception:
			print("{}Céléstin arrête tes carabistouilles !".format(icon.warn))

	print("Au revoir kheyou ;)")

	return(True)

if(__name__ == '__main__'):
	main()
