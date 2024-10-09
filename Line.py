from kivy.graphics import Line as kv_Line
from Tool import Tool

class Line(Tool):
	def __init__(self):
		self.name = "Line"
		
	def on_touch_down(self, touch, root):
		if self.is_cursor_on_drawing_area(touch, root) == True:
			x, y = touch.x - root.ids.drawing_area.pos_hint["x"] * root.width, touch.y
			root.object_manager.objects.append(kv_Line(points = [x, y, x, y], width = root.object_manager.drafting_tool.width))
			root.ids.drawing_area.canvas.add(root.object_manager.objects[-1])
			
	def on_touch_move(self, touch, root):
		if self.is_cursor_on_drawing_area(touch, root) == True:
			x, y = touch.x - root.ids.drawing_area.pos_hint["x"] * root.width, touch.y
			root.object_manager.objects[-1].points = [root.object_manager.objects[-1].points[0], root.object_manager.objects[-1].points[1], x, y]
		
	def on_touch_up(self, touch, root):
		pass
		
