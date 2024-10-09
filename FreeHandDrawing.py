from kivy.graphics import Line
from Tool import Tool

class FreeHandDrawing(Tool):
	def __init__(self):
		self.name = "Free Hand Drawing"
		
	def on_touch_down(self, touch, root):
		if self.is_cursor_on_drawing_area(touch, root) == True:
			x, y = touch.x - root.ids.drawing_area.pos_hint["x"] * root.width, touch.y
			root.object_manager.objects.append(Line(points = [x, y], width = root.object_manager.drafting_tool.width))
			root.ids.drawing_area.canvas.add(root.object_manager.objects[-1])
		
	def on_touch_move(self, touch, root):
		if self.is_cursor_on_drawing_area(touch, root) == True:
			x, y = touch.x - root.ids.drawing_area.pos_hint["x"] * root.width, touch.y
			root.object_manager.objects[-1].points += [x, y]
		
	def on_touch_up(self, touch, root):
		pass
		
