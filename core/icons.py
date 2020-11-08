#!/bin/python3
# -*- conding: utf-8 -*-

from core.colors import Colors

class Icons:
	warn = "{}[!]{} - ".format(Colors.red, Colors.end)
	tips = "{}(?){} - ".format(Colors.green, Colors.end)
	list = "{}(*){} - ".format(Colors.cyan, Colors.end)
	info = "{}(i){} - ".format(Colors.blue, Colors.end)
