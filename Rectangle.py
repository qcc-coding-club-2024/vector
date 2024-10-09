from kivy.graphics import Line as kv_Line
from Tool import Tool

class Rectangle(Tool):
	def __init__(self):
		self.name = "Rectangle"
		
	def on_touch_down(self, touch, root):
		if self.is_cursor_on_drawing_area(touch, root) == True:
			x, y = touch.x - root.ids.drawing_area.pos_hint["x"] * root.width, touch.y
			root.object_manager.objects.append(kv_Line(points = [x, y], width = root.object_manager.drafting_tool.width))
			root.ids.drawing_area.canvas.add(root.object_manager.objects[-1])
			
	def on_touch_move(self, touch, root):
		if self.is_cursor_on_drawing_area(touch, root) == True:
			x1, y1 = root.object_manager.objects[-1].points[0], root.object_manager.objects[-1].points[1]
			x3, y3 = touch.x - root.ids.drawing_area.pos_hint["x"] * root.width, touch.y
			root.object_manager.objects[-1].points = touch.x, touch.y
			x2, y2 = x3, y1
			x4, y4 = x1, y3
			root.object_manager.objects[-1].points = [x1, y1, x2, y2, x3, y3, x4, y4, x1, y1]
		
	def on_touch_up(self, touch, root):
		pass
