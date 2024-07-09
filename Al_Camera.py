from manim import *

class Crazy(ThreeDScene):
    config.pixel_width = 3840
    config.pixel_width = 2160
    config.frame_height = 32
    config.frame_width = 32
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-180 * DEGREES)  
        self.begin_ambient_camera_rotation(2)
        Disp_array= VMobject(200)
        for x in range(-10, 10):
            for y in range(-3, 3):
                for z in range(-3, 3):
                    dot = Dot(point=(x, y, z), color=RED)
                    Disp_array.add(dot)
        [Disp_array.submobjects[i].set_color(BLUE) for i in range(0,100)]
        self.add(Disp_array)
        self.wait(20)
