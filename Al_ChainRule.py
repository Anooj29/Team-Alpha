from typing_extensions import runtime
from manim import *
from moderngl_window.meta import scene

class AxesPlot(Scene):
	config.pixel_height=1080
	config.pixel_width=1920
	config.frame_height=18
	config.frame_width=32
	def construct(self, font_size=50):

		config.pixel_height=1080
		config.pixel_width=1920
		config.frame_height=18
		config.frame_width=32

		axes = Axes(
			x_range=[0,5,1],
			y_range=[-4,5,1],
			color=GRAY)

		self.play(Create(axes))
		self.remove(axes)

		text=MathTex("\\frac{d}{dx}f(x)g(x)=",
		"f(x)\\frac{d}{dx}g(x)",
		"+",
		"g(x)\\frac{d}{dx}f(x)", font_size=100)
		self.play(Write(text))

		brace1 = Brace(text[1], UP, buff = SMALL_BUFF, color=BLUE)
		brace2 = Brace(text[3],  buff = SMALL_BUFF, color=RED)
		t1 = brace1.get_text("$g'f$")
		t2 = brace2.get_text("$f'g$")
		self.play(
			GrowFromCenter(brace1),
			FadeIn(t1)
			)
		self.wait()
		self.play(
			ReplacementTransform(brace1,brace2),
			ReplacementTransform(t1,t2)
			)
		self.wait()
		self.wait(3)
        