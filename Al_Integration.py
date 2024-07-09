from manim import *
from manim.utils.color.X11 import BLUE2

class IntegrationIntro(Scene):

	config.pixel_height = 1080 
	config.pixel_width = 1920
	config.frame_height = 18
	config.frame_width = 32


	def construct(self):

		# CONSTANTS
		X = 9
		Y = 6 
		
		axes = Axes(
			x_range=[0,X + 1,1],
			y_range=[0,Y,1],
			x_length= X + 1,
			y_length= Y,
			axis_config={"color":BLUE , "include_ticks": False}
		).add_coordinates()

		axes.add_background_rectangle(color=WHITE, opacity=0.2)

		curve = axes.plot(
			lambda x: 0.2 * x * (X - x),
			x_range = [0,X],
			color = YELLOW
		)

		graph = VGroup(axes,curve)
		graph.move_to(ORIGIN).shift(UP * 0.5)
		self.play(Create(axes),Create(curve))
		self.wait(1)

		def makeRect(num_rects):
			rectangles = VGroup()
			dx = X / num_rects

			for i in range(1, num_rects):
				x = i * dx
				height = 0.2 * x * (X - x)
				rect = Rectangle(
					width = dx,
					height = height,
					color = BLUE,
					fill_color = BLUE,
					fill_opacity = 0.5,
					stroke_width = 0.5
				)
				rect.move_to(axes.c2p(x , height / 2))
				rectangles.add(rect)

			return rectangles
				
		
		for i in range(1,4):
			num_rects = 6 ** i
			rectangles = makeRect(num_rects)
			

			self.play(Create(rectangles),run_time = 2)
			self.wait(1)
			self.play(FadeOut(rectangles))
			self.wait(1)

		area = axes.get_area(curve, x_range=(0, 9), color=BLUE)
		self.play(Create(area))
