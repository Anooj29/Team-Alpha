from manim import *

class IntegralCalculusAnimation(Scene):
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


class RocketTrajectory(Scene):
    def construct(self):

        # Rocket trajectory
        rocket = SVGMobject("rocket.svg").scale(0.5)  # Ensure you have a rocket.svg file
        trajectory = ParametricFunction(
            lambda t: np.array([t, 0.2 * t * (9 - t), 0]),
            t_range=[0, 9],
            color=YELLOW
        )

        self.play(Create(trajectory)).move_to(ORIGIN)
        self.play(MoveAlongPath(rocket, trajectory), run_time=4)
        self.wait(2)

        # Save the rocket and trajectory for the next scene
        self.rocket = rocket
        self.trajectory = trajectory


class IntegrationIntro(Scene):

    def construct(self):

        # Recreate the final state from the previous scene
        integral_complete = Text("Integral").set_color(RED)
        calculus_complete = Text("Calculus").set_color(BLUE)
        
        combined_words = VGroup(integral_complete, calculus_complete).arrange(RIGHT, buff=0.5).move_to(ORIGIN).to_edge(UP)

        self.add(combined_words)

        self.wait(2)

        # CONSTANTS
        X = 9
        Y = 6 
        
        axes = Axes(
            x_range=[0, X + 1, 1],
            y_range=[0, Y, 1],
            x_length= X + 1,
            y_length= Y,
            axis_config={"color": BLUE, "include_ticks": False}
        )

        curve = axes.plot(
            lambda x: 0.2 * x * (X - x),
            x_range=[0, X],
            color=YELLOW
        )

        graph = VGroup(axes, curve)
        graph.move_to(ORIGIN)
        self.play(Create(axes), Create(curve))
        self.wait(3)

        def makeRect(num_rects):
            rectangles = VGroup()
            dx = X / num_rects

            for i in range(1, num_rects):
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
            num_rects = 6 ** i
            rectangles = makeRect(num_rects)
            rects_list.append(rectangles)

        self.play(Create(rects_list[0]), run_time=2)

        for i in range(1, len(rects_list)):
            self.play(Transform(rects_list[0], rects_list[i]), run_time=2)
            self.wait(1)
