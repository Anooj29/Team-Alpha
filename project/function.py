from manim import *

class Function(Scene):
    # Correcting the configuration
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
        
        title = Text("Calculus Introduction").scale(1.5)
        title.set_color(white)

        # Create the introductory text
        intro_text = Text("A function is a mathematical expression defining the relationship between two variables.")

        # Create the second part of the introductory text
        intro_text2 = Text("A Derivative of this function is another function describing the slope of the curve at each point on the curve.")

        self.play(Write(title))
        title.next_to(intro_text, UP, buff=1)
        self.play(title.animate.next_to(intro_text,UP*5,buff=1))
        intro_text.next_to(title, DOWN, buff=1)
        self.wait(1)

        intro_text.set_color(green)
        intro_text.set_color_by_t2c({"function": white, "variables": white})
        intro_text2.next_to(intro_text, DOWN, buff=1)
        intro_text2.set_color(green)
        intro_text2.set_color_by_t2c({"Derivative": white, "slope": white})

        self.play(FadeIn(intro_text))
        self.wait(1)
        self.play(FadeIn(intro_text2))
        self.wait(2)

        func = MathTex("f(x) = x^2")
        func.next_to(intro_text2, DOWN,buff=1)
        self.play(Write(func))

        tangent_line = MathTex("f'(x) = 2x")
        tangent_line.next_to(func, DOWN, buff=1.5 )
        self.play(Write(tangent_line))

        self.wait(2)
        self.play(FadeOut(intro_text), FadeOut(intro_text2), FadeOut(func), FadeOut(tangent_line))

        group_fumction= VGroup(func,tangent_line).set_color(white).move_to(UP+LEFT)

        plane = NumberPlane(
            x_range=[-4,4],
            y_range=[-2,10],
            background_line_style={
                "stroke_color": blue ,
                "stroke_width": 1,
                "stroke_opacity": 1
            },
            axis_config={
                "stroke_color": purple,
                "stroke_width": 2
            },
            faded_line_ratio=2
        )
        plane2 = NumberPlane(
            x_range=[-4,4],
            y_range=[-2,10],
            background_line_style={
                "stroke_color": blue,
                "stroke_width": 1,
                "stroke_opacity": 1
            },
            axis_config={
                "stroke_color": purple,
                "stroke_width": 2
            },
            faded_line_ratio=2
        )


        graph1 = Axes(
            x_range=[-3, 3],
            y_range=[-1, 9],
            axis_config={"color": red}
        )
        
        graph_labels = graph1.get_axis_labels(x_label="x", y_label="f(x)")
        parabola = graph1.plot(lambda x: x**2, color=green)
        parabola_label = graph1.get_graph_label(parabola, label="x^2")
        self.play(Create(plane))
        self.play(Create(graph1), Write(graph_labels))
        self.play(Create(parabola), Write(parabola_label))
        
        dot = Dot().move_to(graph1.coords_to_point(1,1))
        dot.set_color(lgreen)
        dot_2 = Dot().move_to(graph1.coords_to_point(2,4))
        dot_label = MathTex("A(1,1)").next_to(dot, RIGHT)
        dot_label2 = MathTex("B(2,4)").next_to(dot_2, RIGHT)


        x_tracker = ValueTracker(-3)

        def update_slope(dot):
            x = x_tracker.get_value()
            y = x**2
            dot.move_to(graph1.c2p(x,y))

        tangent_line = always_redraw(
            lambda: TangentLine(
                parabola, 
                alpha=(x_tracker.get_value() + 3) / 6, 
                length=4,
                color=tred
            )
        )
        tangent_line.move_to(graph1.coords_to_point(1,1))

        self.play(FadeIn(dot, dot_2, scale=0.5), Write(dot_label), Write(dot_label2))
       
        self.wait(3)

        
        group1 = VGroup(graph1,graph_labels,parabola,parabola_label,dot_2,dot,dot_label,dot_label2,tangent_line,plane).shift(LEFT*5).scale(1)



        graph2 = Axes(
            x_range=[-3, 3],
            y_range=[-1, 9],
            axis_config={"color": red})
        graph_labels2 = graph2.get_axis_labels(x_label="x", y_label="f'(x)")
        derivative = graph2.plot(lambda x:2*x, color=green)
        derivative_label = graph2.get_graph_label(derivative, label="2x")
        xx_tracker = ValueTracker(-3)
        dot_3 = Dot(color=lgreen).move_to(graph2.coords_to_point(0,0))

        def update_dot(dot):
            x = xx_tracker.get_value()
            y = 2*x
            dot.move_to(graph2.c2p(x, y))


        group2 = VGroup(graph2, graph_labels2, derivative, derivative_label,dot_3, plane2).next_to(group1, RIGHT, buff = 1).scale(1)

        self.play(group1.animate.next_to(group2, LEFT, buff = 4))

        self.play(Create(plane2))
        self.play(Create(graph2), Write(graph_labels2))
        self.play(Create(derivative), Write(derivative_label))
        self.clear()

        self.play(Create(group1), Create(group2))
        self.wait(3)

        dot.add_updater(update_slope)
        dot_3.add_updater(update_dot)


        self.play(x_tracker.animate.set_value(3), xx_tracker.animate.set_value(3), run_time =10, rate_func = linear)
        self.wait(2) 
        
