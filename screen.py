from manim import *

class ScreenDisplay(Scene):
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

        
        for pos in positions:
            
            dot = Dot(point=ORIGIN, color=WHITE)
            
            
            screen = Rectangle(width=36, height=21, color=WHITE)
            screen.scale(0.1)
            screen.move_to(dot.get_center())

            
            self.play(Create(dot))
            
            
            self.play(Transform(dot, screen))
            
            
            self.play(screen.animate.scale(1.0).move_to(pos),FadeOut(dot))
        self.wait(2)
