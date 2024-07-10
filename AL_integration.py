from manim import *

class IntegrationIntro(Scene):

	# config.pixel_height = 1080 
	# config.pixel_width = 1920
	# config.frame_height = 18
	# config.frame_width = 32


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
		)

		curve = axes.plot(
			lambda x: 0.2 * x * (X - x),
			x_range = [0,X],
			color = YELLOW
		)

		graph = VGroup(axes,curve)
		graph.move_to(ORIGIN).shift(UP * 0.5)
		self.play(Create(axes),Create(curve))
		self.wait(3)

		def makeRect(num_rects):
			rectangles = VGroup()
			dx = X / num_rects

			for i in range(1, num_rects):
				x = i * dx
				height = 0.2 * x * (X - x)
				rect = Rectangle(
					width = dx,
					height = height,
					color = RED,
					fill_color = RED,
					fill_opacity = 0.5,
					stroke_width = 0.5
				)
				rect.move_to(axes.c2p(x , height / 2))
				rectangles.add(rect)

			return rectangles
				
		rects_list = []

		for i in range(1,4):
			num_rects = 6 ** i
			rectangles = makeRect(num_rects)
			rects_list.append(rectangles)

			# self.play(Create(rectangles),run_time = 2)
			# self.wait(1)
			# self.play(FadeOut(rectangles))

		self.play(Create(rects_list[0]),run_time = 2)

		for i in range(1, len(rects_list)):

			self.play(Transform(rects_list[0],rects_list[i]),run_time = 2)
			self.wait(1)
