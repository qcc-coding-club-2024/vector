from kivy.geometry import circumcircle
from Tool import Tool

class Ellipse(Tool):
	def __init__(self):
		self.name = "Ellipse"
	def on_touch_down(self, touch, root):
		if self.is_cursor_on_drawing_area(touch, root) == True:
			x, y = touch.x - root.ids.drawing_area.pos_hint["x"] * root.width, touch.y
			
