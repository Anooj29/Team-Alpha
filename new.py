from manim import *


class introIntegration(Scene):

	def construct(self):
		# Create letters for "Integral Calculus" spaced apart
		letters = VGroup(
			*[
				Text(letter).scale(1.5) for letter in "Integral Calculus"
				]
		).arrange(buff=2)

		# Position letters initially far apart horizontally
		for i, letter in enumerate(letters):
			letter.shift(LEFT * 6 + RIGHT * 0.6 * i)

		# Create the complete word "Integral Calculus"
		complete_word = Text("Integral Calculus").scale(1.5)

		# Animate the letters coming together to form the word
		self.play(
			Transform(letters,complete_word),
			run_time = 2
		)

       	# Move the word to the top of the screen
		self.play(complete_word.animate.to_edge(UP))

		self.wait(2)

