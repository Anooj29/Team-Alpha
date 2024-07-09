from manim import *

class Title(Scene):
	config.pixel_height=1080
	config.pixel_width=1920
	config.frame_height=18
	config.frame_width=32
	def construct(self):

		rect = Rectangle(color=BLUE, height=17, width=31, grid_xstep=2, grid_ystep=1)
		self.play(Create(rect))

		return super().construct()