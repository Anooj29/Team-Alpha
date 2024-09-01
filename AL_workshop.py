from manim import *


class IntegralCalculusAnimation(Scene):

    config.pixel_height = 1080
    config.pixel_width = 1920
    config.frame_height = 18.0
    config.frame_width = 32.0
    def construct(self):

        integral_text = "Integral"
        calculus_text = "Calculus"

        integral_letters = VGroup(*[Text(letter) for letter in integral_text])
        calculus_letters = VGroup(*[Text(letter) for letter in calculus_text])

        for letter in integral_letters:
            letter.shift(np.random.uniform(-5, 5) * RIGHT + np.random.uniform(-3, 3) * UP )
        
        for letter in calculus_letters:
            letter.shift(np.random.uniform(-5, 5) * RIGHT + np.random.uniform(-3, 3) * UP)
        
        self.add(integral_letters, calculus_letters)  

        self.wait(2)  

        integral_complete = Text("Integral").scale(1.3)
        calculus_complete = Text("Calculus").scale(1.3)
        
        combined_words = VGroup(integral_complete, calculus_complete).arrange(RIGHT, buff=0.5).move_to(ORIGIN)

        self.play(
            *[
                letter.animate.move_to(integral_complete[i].get_center())
                for i, letter in enumerate(integral_letters)
            ],
            *[
                letter.animate.move_to(calculus_complete[i].get_center())
                for i, letter in enumerate(calculus_letters)
            ],
            run_time=3
        )

        self.remove(integral_letters, calculus_letters)
        self.add(integral_complete, calculus_complete)

        self.play(
            integral_complete.animate.set_color(RED),
            calculus_complete.animate.set_color(BLUE),
            run_time=2
        )

        self.play(combined_words.animate.to_edge(UP * 3))

        # Save the final state for continuation
        self.integral_complete = integral_complete
        self.calculus_complete = calculus_complete
        self.combined_words = combined_words

        self.wait(2)

class IntegrationRocket(Scene):

    config.pixel_height = 1080
    config.pixel_width = 1920
    config.frame_height = 18.0
    config.frame_width = 32.0

    def construct(self):
        # Title
        integral_complete = Text("Integral").scale(1.3).set_color(RED)
        calculus_complete = Text("Calculus").scale(1.3).set_color(BLUE)

        # Use these recreated elements in your scene
        combined_words = VGroup(integral_complete, calculus_complete).arrange(RIGHT, buff=0.5).move_to(ORIGIN)
        self.add(combined_words.to_edge(UP * 3))

        # Introduction text
        intro_text = Text(
            "Imagine a rocket launching. \nWe monitor its velocity over time."
        ).scale(0.8).move_to(ORIGIN)
        self.play(Write(intro_text))
        self.wait(3)
        self.play(FadeOut(intro_text))

        self.wait(2)

        # Constants for graph
        X = 9
        Y = 6
        
        axes = Axes(
            x_range=[0, X + 1, 1],
            y_range=[0, Y, 1],
            x_length=X + 1,
            y_length=Y,
            axis_config={"color": BLUE, "include_ticks": False}
        )

        curve = axes.plot(
            lambda x: 0.2 * x * (X - x),
            x_range=[0, X],
            color=YELLOW
        )

        graph = VGroup(axes, curve)
        graph.move_to(ORIGIN).shift(UP * 0.5).move_to(ORIGIN).shift(LEFT * 4)
        self.play(Create(axes), Create(curve))
        self.wait(3)

        # Explanation text
        explanation_text = Text(
            "To determine the distance traveled in a given time, \nwe plot the velocity function and find the area under the curve."
        ).scale(0.8).next_to(graph, RIGHT, buff=1)
        self.play(Write(explanation_text))
        self.wait(3)
        self.play(FadeOut(explanation_text))

        # Explain irregular area
        explanation_text = Text(
            "The area under the curve is irregular, \nmaking it difficult to calculate with standard formulas."
        ).scale(0.8).next_to(graph, RIGHT, buff=1)
        self.play(Write(explanation_text))
        self.wait(3)
        self.play(FadeOut(explanation_text))

        # Explain rectangle approximation
        explanation_text = Text(
            "We divide the area into small rectangles with equal width (dx). \nEach rectangle approximates the area under the curve."
        ).scale(0.8).next_to(graph, RIGHT, buff=1)
        self.play(Write(explanation_text))
        self.wait(3)
        self.play(FadeOut(explanation_text))

        def makeRect(num_rects):
            rectangles = VGroup()
            dx = X / num_rects

            for i in range(num_rects):
                x = i * dx
                height = 0.2 * x * (X - x)
                rect = Rectangle(
                    width=dx,
                    height=height,
                    color=RED,
                    fill_color=RED,
                    fill_opacity=0.5,
                    stroke_width=0.5
                )
                rect.move_to(axes.c2p(x, height / 2))
                rectangles.add(rect)

            return rectangles

        rects_list = []

        for i in range(1, 4):
            num_rects = 4 ** i
            rectangles = makeRect(num_rects)
            rects_list.append(rectangles)

        self.play(Create(rects_list[0]), run_time=2)
        self.wait(1)

        for i in range(1, len(rects_list)):
            explanation_text = Text(f"Increasing to {4**(i+1)} rectangles").scale(0.8).next_to(graph, RIGHT, buff=1)
            self.play(Write(explanation_text))
            self.wait(1)
            
            self.play(Transform(rects_list[0], rects_list[i]), run_time=2)
            self.wait(1)
            
            self.play(FadeOut(explanation_text))

        explanation_text = Text(
            "As the number of rectangles increases, \nthe approximation becomes closer to the true area."
        ).scale(0.8).next_to(graph, RIGHT, buff=1)
        self.play(Write(explanation_text))
        self.wait(3)
        self.play(FadeOut(explanation_text))

        explanation_text = Text(
            "When dx approaches 0, \nthe sum of the areas of the rectangles \ngives the exact area under the curve."
        ).scale(0.8).next_to(graph, RIGHT, buff=1)
        self.play(Write(explanation_text))
        self.wait(3)
        self.play(FadeOut(explanation_text))

        integral_text = MathTex(
            r"\text{Area} = \int_a^b f(t) \, dt"
        ).scale(0.8).next_to(graph, RIGHT, buff=1)
        self.play(Write(integral_text))
        self.wait(3)
        self.play(FadeOut(integral_text))

