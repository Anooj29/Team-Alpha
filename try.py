from manim import *

class IntegrationHistory(Scene):
    def construct(self):
        # CONSTANTS
        X = 9
        Y = 6 
        
        # Create axes
        axes = Axes(
            x_range=[0, X + 1, 1],
            y_range=[0, Y, 1],
            x_length=X + 1,
            y_length=Y,
            axis_config={"color": BLUE, "include_ticks": False}
        )
        
        # Labels for axes
        x_label = axes.get_x_axis_label(Tex("x"), edge=RIGHT, direction=UP)
        y_label = axes.get_y_axis_label(Tex("f(x)"), edge=UP, direction=RIGHT)
        
        # Define the curve
        curve = axes.plot(
            lambda x: 0.2 * x * (X - x),
            x_range=[0, X],
            color=YELLOW
        )
        
        # Label for the curve
        curve_label = axes.get_graph_label(curve, label=Tex("f(x)=0.2x(X-x)"))

        # Group the graph elements together and position
        graph = VGroup(axes, curve, x_label, y_label, curve_label)
        graph.move_to(ORIGIN).shift(UP * 0.5)
        
        # Animate creation of axes and curve
        self.play(Create(axes), Create(curve), Write(x_label), Write(y_label), Write(curve_label))
        self.wait(3)

        # Introduction Text
        intro_text = Text("How do we find the area under this curve?").to_edge(UP)
        self.play(Write(intro_text))
        self.wait(3)
        self.play(FadeOut(intro_text))

        def make_rects(num_rects):
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
                rect.move_to(axes.c2p(x + dx/2, height / 2))
                rectangles.add(rect)

            return rectangles
                
        rects_list = []
        num_rects_list = [6, 12, 24]

        for num_rects in num_rects_list:
            rectangles = make_rects(num_rects)
            rects_list.append(rectangles)

        # Rectangular Approximation Text
        approx_text = Text("Rectangular Approximation (Riemann Sums)").to_edge(UP)
        self.play(Write(approx_text))
        self.play(Create(rects_list[0]), run_time=2)
        for i in range(1, len(rects_list)):
            self.play(Transform(rects_list[0], rects_list[i]), run_time=2)
            self.wait(1)
        self.play(FadeOut(approx_text), FadeOut(rects_list[0]))
        
        # Trapezoidal Approximation
        def make_trapezoids(num_trapezoids):
            trapezoids = VGroup()
            dx = X / num_trapezoids

            for i in range(num_trapezoids):
                x = i * dx
                y1 = 0.2 * x * (X - x)
                y2 = 0.2 * (x + dx) * (X - (x + dx))
                trapezoid = Polygon(
                    axes.c2p(x, 0),
                    axes.c2p(x, y1),
                    axes.c2p(x + dx, y2),
                    axes.c2p(x + dx, 0),
                    color=GREEN,
                    fill_color=GREEN,
                    fill_opacity=0.5,
                    stroke_width=0.5
                )
                trapezoids.add(trapezoid)

            return trapezoids

        trapz_list = []
        for num_trapz in num_rects_list:
            trapezoids = make_trapezoids(num_trapz)
            trapz_list.append(trapezoids)

        # Trapezoidal Approximation Text
        trapz_text = Text("Trapezoidal Approximation").to_edge(UP)
        self.play(Write(trapz_text))
        self.play(Create(trapz_list[0]), run_time=2)
        for i in range(1, len(trapz_list)):
            self.play(Transform(trapz_list[0], trapz_list[i]), run_time=2)
            self.wait(1)
        self.play(FadeOut(trapz_text), FadeOut(trapz_list[0]))

        # Transition to Integral Calculus
        integral_text = Text("As the number of rectangles or trapezoids increases,").to_edge(UP)
        integral_text2 = Text("the approximation becomes more accurate.").next_to(integral_text, DOWN)
        integral_text3 = Text("This leads to the concept of integration.").next_to(integral_text2, DOWN)
        self.play(Write(integral_text))
        self.play(Write(integral_text2))
        self.play(Write(integral_text3))
        self.wait(3)
        self.play(FadeOut(integral_text), FadeOut(integral_text2), FadeOut(integral_text3))

        # Conclusion Text
        conclusion_text = Text("Integration is a fundamental concept in calculus that").to_edge(UP)
        conclusion_text2 = Text("allows us to find the exact area under a curve.").next_to(conclusion_text, DOWN)
        self.play(Write(conclusion_text))
        self.play(Write(conclusion_text2))
        self.wait(3)
        self.play(FadeOut(conclusion_text), FadeOut(conclusion_text2))
