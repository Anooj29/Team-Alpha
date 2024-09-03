from manim import *

class ScreenGraph(Scene):
    config.pixel_height = 1080
    config.pixel_width = 1920
    config.frame_height = 18.0
    config.frame_width = 32.0
    
    def construct(self):    
        positions = [
            LEFT * 4 + UP * 2,       
            RIGHT * 4 + UP * 2,      
            LEFT * 4 + DOWN * 2,     
            RIGHT * 4 + DOWN * 2    
        ]

        for i, pos in enumerate(positions):

            dot = Dot(point=ORIGIN, color=WHITE)
                        
            screen = Rectangle(width=36, height=21, color=WHITE)
            screen.scale(0.1)
            screen.move_to(dot.get_center())

            self.play(Create(dot))            
            self.play(Transform(dot, screen))
            
            axes = Axes(
                x_range=[-3.5, 3.5, 1], y_range=[-1, 1, 0.5],
                axis_config={"color": WHITE}
            )
            graph = axes.plot(lambda x: np.sin(x), color=YELLOW)
            
            graph_group = VGroup(axes, graph).scale(0.2)  
            graph_group.move_to(screen.get_center())

            self.play(Create(graph_group))

            screen_struct = VGroup(graph_group,screen)
            
            self.play(screen_struct.animate.scale(1.0).move_to(pos),Uncreate(dot))

        self.wait(2)