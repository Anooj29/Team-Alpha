from manim import *
import numpy as np

class RocketLaunchAndIntegration(Scene):
    def construct(self):

        rocket = SVGMobject("rocket.svg").scale(0.5).set_color(WHITE)
        rocket.move_to(ORIGIN)
        
        self.play(rocket.animate.shift(UP * 3), run_time=2)
        self.play(FadeOut(rocket))


        axes = Axes(
            x_range=[0, 10, 1], y_range=[0, 20, 2], 
            x_length=7, y_length=5,
            axis_config={"color": WHITE}, tips=False
        )
        labels = axes.get_axis_labels(x_label="t (time)", y_label="v(t) (velocity)")
        
        self.play(Create(axes), Write(labels))
        

        graph = axes.plot(lambda t: 10 - 0.5 * t**2, color=GREEN, x_range=[0, 4])
        self.play(Create(graph))
        

        explanation_text1 = Text("Velocity-Time graph of the rocket launch is variable.", font_size=24).to_edge(UP)
        self.play(Write(explanation_text1))
        self.wait(2)
        
        explanation_text2 = Text("To find the total distance travelled, we need to determine the area under the curve.", font_size=24).next_to(explanation_text1, DOWN)
        self.play(Write(explanation_text2))
        self.wait(2)
        
        area = axes.get_area(graph, x_range=[0, 4], color=[GREEN, BLUE])
        self.play(FadeIn(area))
        self.wait(2)
        

        self.play(FadeOut(explanation_text1), FadeOut(explanation_text2))
        
        explanation_text3 = Text("The shape of the area is irregular,", font_size=24).to_edge(UP)
        explanation_text4 = Text("so we use integral calculus.", font_size=24).next_to(explanation_text3, DOWN)
        self.play(Write(explanation_text3), Write(explanation_text4))
        self.wait(2)
        
        self.play(FadeOut(explanation_text3), FadeOut(explanation_text4))
        
        explanation_text5 = Text("We divide the area into rectangles", font_size=24).to_edge(UP)
        explanation_text6 = Text("to approximate it.", font_size=24).next_to(explanation_text5, DOWN)
        self.play(Write(explanation_text5), Write(explanation_text6))
        self.wait(2)
        
        rects = axes.get_riemann_rectangles(graph, x_range=[0, 4], dx=0.5, input_sample_type="left")
        self.play(Create(rects))
        self.wait(2)
        
        explanation_text7 = Text("As the number of rectangles increases,", font_size=24).to_edge(UP)
        explanation_text8 = Text("the approximation improves.", font_size=24).next_to(explanation_text7, DOWN)
        self.play(Write(explanation_text7), Write(explanation_text8))
        self.wait(2)
        
        more_rects = axes.get_riemann_rectangles(graph, x_range=[0, 4], dx=0.2, input_sample_type="left")
        self.play(Transform(rects, more_rects))
        self.wait(2)

        even_more_rects = axes.get_riemann_rectangles(graph, x_range=[0, 4], dx=0.1, input_sample_type="left")
        self.play(Transform(rects, even_more_rects))
        self.wait(2)
        
        self.play(FadeOut(explanation_text7), FadeOut(explanation_text8))
        
        explanation_text9 = Text("As dx tends to 0, the area under", font_size=24).to_edge(UP)
        explanation_text10 = Text("the curve approaches the true value.", font_size=24).next_to(explanation_text9, DOWN)
        self.play(Write(explanation_text9), Write(explanation_text10))
        self.wait(2)
        
        self.play(FadeOut(rects), FadeOut(graph), FadeOut(axes), FadeOut(labels))
        
        # Step 5: Conclusion
        conclusion = Text("Integral Calculus helps find the exact area under the curve.", font_size=36).to_edge(DOWN)
        self.play(Write(conclusion))
        self.wait(2)
        self.play(FadeOut(conclusion))

