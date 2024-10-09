#!/usr/bin/env python3
from os import system

system("clear")

from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.core.window import Window
from kivy.graphics import Line

from ObjectManager import ObjectManager

Window.size = (1920, 1080)

class MainLayout(RelativeLayout):
	def __init__(self, **kwargs):
		super(MainLayout, self).__init__(**kwargs)
		self.object_manager = ObjectManager()
	
	def on_touch_down(self, touch):
		self.object_manager.drafting_tool.active_tool.on_touch_down(touch, self)
		return super(MainLayout, self).on_touch_down(touch)
		
	def on_touch_move(self, touch):
		self.object_manager.drafting_tool.active_tool.on_touch_move(touch, self)
		return super(MainLayout, self).on_touch_move(touch)
		
	def on_touch_up(self, touch):
		self.object_manager.drafting_tool.active_tool.on_touch_up(touch, self)
		return super(MainLayout, self).on_touch_up(touch)


class VectorApp(App): # defining the app class
	def build(self): # using MyRelativeLayout in the app
		return MainLayout() # returning MyRelativeLayout

	def on_pause(self):
		# Method to do something when pausing the application
		return True

	def on_resume(self):
		# Method to do something when resuming the application
		pass

vector = VectorApp()
vector.run()
