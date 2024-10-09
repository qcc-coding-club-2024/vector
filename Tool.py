class Tool:
	def __init__(self):
		pass
		
	def is_cursor_on_drawing_area(self,touch, root):
		x, y = touch.x, touch.y
		return x >= root.ids.drawing_area.pos[0] and x <= root.ids.drawing_area.pos[0] + root.ids.drawing_area.width and y >= root.ids.drawing_area.pos[1] and y <= root.ids.drawing_area.pos[1] + root.ids.drawing_area.height
		
