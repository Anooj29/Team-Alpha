from typing_extensions import runtime
from manim import *
from moderngl_window.meta import scene

class Select(Scene):
	config.pixel_width=1920
	config.pixel_height=1080
	config.frame_height=18
	config.frame_width = 32
	def construct(self):

		tex = Text("HELLo", stroke_width=10, font_size=50)

		self.play(Create(tex), runtime=3)
		self.wait(3)