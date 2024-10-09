from Tool import Tool

class Delete(Tool):
	def __init__(self):
		self.name = "Delete"
		self.slope = None
		
	def get_slope(self, x1, y1, x2, y2):
		return (y2-y1)/(x2-x1)
		
	def belongs_to_line(self, x, y, line):
		x1 = line.points[0]
		y1 = line.points[1]
		x2 = line.points[2]
		y2 = line.points[3]
		m = self.get_slope(x1, y1, x2, y2)
		n = -m * x1 + y1
		side1 = int(y)
		side2 = int(m * x + n)
		if (x > x1 and x < x2 and y > y1 and y < y2 and side1 == side2) or (x > x1 and x < x2 and y2 < y and y < y1 and side1 == side2):
			return True
		else:
			return False
			
	def delete_lines(self, touch, root):
		for line in root.object_manager.objects:
			if self.belongs_to_line(touch.x - root.ids.main_menu.size_hint[0] * root.size[0], touch.y, line):
				if line in root.ids.drawing_area.canvas.children:
					root.ids.drawing_area.canvas.remove(line)
					root.object_manager.objects.remove(line)
		
	def on_touch_down(self, touch, root):
		if self.is_cursor_on_drawing_area(touch, root) == True:
			x = touch.x / root.width
			y = touch.y / root.height
			root.ids.eraser_layout.pos_hint = {"center_x": x, "center_y": y}
			self.delete_lines(touch, root)
		
	def on_touch_move(self, touch, root):
		if self.is_cursor_on_drawing_area(touch, root) == True:
			x = touch.x / root.width
			y = touch.y / root.height
			root.ids.eraser_layout.pos_hint = {"center_x": x, "center_y": y}
			self.delete_lines(touch, root)
		
	def on_touch_up(self, touch, root):
		x = -1
		y = -1
		root.ids.eraser_layout.pos_hint = {"center_x": x, "center_y": y}
		
