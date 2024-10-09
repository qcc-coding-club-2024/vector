#!/usr/bin/env python3

from FreeHandDrawing import FreeHandDrawing
from Line import Line
from Rectangle import Rectangle
from Polyline import Polyline
from Move import Move
from Delete import Delete

class DraftingTool:
	def __init__(self):
		self.free_hand_drawing = FreeHandDrawing()
		self.line = Line()
		self.rectangle = Rectangle()
		self.polyline = Polyline()
		self.move = Move()
		self.delete = Delete()
		
		self.active_tool = self.free_hand_drawing
		self.width = 2
