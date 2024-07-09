from manim import *

class MovePointOnCurve(Scene):
    def construct(self):
        # Define the parametric curve
        curve = ParametricFunction(
            lambda t: np.array([t, np.sin(t), 0]),
            t_range = np.array([-PI, PI, 0.01]),
            color = BLUE
        )

        # Define a ValueTracker to keep track of the parameter 't'
        t_tracker = ValueTracker(-PI)

        # Create a Dot to represent the point on the curve
        dot = Dot(color=RED)
        
        # Define an updater function to update the dot's position along the curve
        def update_dot(dot):
            t = t_tracker.get_value()
            dot.move_to(curve.point_from_proportion((t + PI) / (2 * PI)))
        
        # Attach the updater function to the dot
        dot.add_updater(update_dot)

        # Add the curve and dot to the scene
        self.add(curve, dot)

        # Animate the movement of the point along the curve
        self.play(t_tracker.animate.set_value(PI), run_time=4, rate_func=linear)
        self.wait()

if __name__ == "__main__":
    scene = MovePointOnCurve()
    scene.render()
