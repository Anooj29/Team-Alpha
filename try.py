from manim import *

class ChangingCameraWidthAndRestore(MovingCameraScene):
    def construct(self):
        # Create some text
        text = Text("Hello World").set_color(BLUE)
        self.add(text)

        # Save the current state of the camera frame
        self.camera.frame.save_state()

        # Zoom in on the text by adjusting the camera frame's width
        self.play(self.camera.frame.animate.scale(0.5).move_to(text))
        self.wait(0.3)

        # Restore the camera frame to its original state
        self.play(Restore(self.camera.frame))

# To run this script, save it to a file and run it using:
# manim -pql changing_camera.py ChangingCameraWidthAndRestore
