from manim import *

class DerivativeGraph(Scene):
    config.pixel_height = 1080
    config.pixel_width = 1920
    config.frame_height = 18.0
    config.frame_width = 32.0

    def construct(self):
              # Color codes
        red = "#FF893B"
        green = "#729CA2"
        lgreen = "#C4DCDF"
        white = "#ECF3F4"
        purple = "#454866"
        tred = "#E07A5F"
        pastel = "#81B29A"
        blue = "#5AAFDCE6"

        # Create axes
        axes = Axes(
            x_range=[-5, 5],
            y_range=[-5, 5],
            axis_config={"include_tip": False},
        )
        self.add(axes)

        # Define the function
        def func(x):
            return x**3

        # Create the function graph
        graph = axes.plot(func, color=purple)
        self.add(graph)

        # Create a dot moving along the graph
        dot = Dot(color=white)
        dot_tracker = ValueTracker(0)
        dot.add_updater(lambda d: d.move_to(axes.c2p(dot_tracker.get_value(), func(dot_tracker.get_value()))))
        self.add(dot)

        # Create the tangent line
        tangent = Line()
        tangent.set_stroke( width=6, color=pastel)
        self.add(tangent)

        def update_tangent(obj):
            x = dot_tracker.get_value()
            tangent.put_start_and_end_on(
                axes.c2p(x - 0.1, func(x - 0.1)),
                axes.c2p(x + 0.1, func(x + 0.1))
            )

        tangent.add_updater(update_tangent)

        group= VGroup(axes, graph, tangent, dot).scale(0.8).move_to(LEFT*4)

        self.play(dot_tracker.animate.set_value(3), run_time=5)

