#!/usr/bin/python3

from DraftingTool import DraftingTool

class ObjectManager:
	#  Class to mange objects in the app
	def __init__(self):
		self.objects = []
		self.undone_objects = []
		self.drafting_tool = DraftingTool()
