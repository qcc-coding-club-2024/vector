from kivy.graphics import Line as kv_Line
from Tool import Tool

class Polyline(Tool):
	def __init__(self):
		self.name = "Polyline"
		self.is_first_point = True
		
	def on_touch_down(self, touch, root):
		if self.is_cursor_on_drawing_area(touch, root) == True:
			x, y = touch.x - root.ids.drawing_area.pos_hint["x"] * root.width, touch.y
			if self.is_first_point == True:
				root.object_manager.objects.append(kv_Line(points = [x, y, x, y], width = root.object_manager.drafting_tool.width))
				root.ids.drawing_area.canvas.add(root.object_manager.objects[-1])
			else:
				root.object_manager.objects[-1].points += [x, y]
			
	def on_touch_move(self, touch, root):
		x1, y1 = root.object_manager.objects[-1].points[0], root.object_manager.objects[-1].points[1]
		x2, y2 = touch.x - root.ids.drawing_area.pos_hint["x"] * root.width, touch.y
		if self.is_cursor_on_drawing_area(touch, root) == True:
			if self.is_first_point == True:
				root.object_manager.objects[-1].points = [x1, y1, x2, y2]
			else:
				root.object_manager.objects[-1].points = root.object_manager.objects[-1].points[0:-2]
				root.object_manager.objects[-1].points += [x2, y2]
			
	def on_touch_up(self, touch, root):
		if self.is_cursor_on_drawing_area(touch, root) == True:
			self.is_first_point = False
			
			x_final, y_final = touch.x - root.ids.drawing_area.pos_hint["x"] * root.width, touch.y
			
			if x_final == root.object_manager.objects[-1].points[0] and y_final == root.object_manager.objects[-1].points[1]:
				self.is_first_point = True
		
