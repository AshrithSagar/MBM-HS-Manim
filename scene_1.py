from manim import *


class CartesianProduct(Scene):
    def construct(self):
        square_1 = Square(color=BLUE, fill_opacity=0.7).shift(5 * LEFT).scale(0.5)
        square_2 = Square(color=BLUE, fill_opacity=0.7).shift(4 * LEFT).scale(0.5)
        square_3 = Square(color=BLUE, fill_opacity=0.7).shift(3 * LEFT).scale(0.5)
        square_4 = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT).scale(0.5)
        square_5 = Square(color=BLUE, fill_opacity=0.7).shift(LEFT).scale(0.5)
        square_6 = Square(color=BLUE, fill_opacity=0.7).shift(ORIGIN).scale(0.5)
        square_7 = Square(color=BLUE, fill_opacity=0.7).shift(RIGHT).scale(0.5)

        square_group = VGroup(square_1, square_2, square_3, square_4, square_5, square_6, square_7)
        
        text = Text("S  K  N  K  C  N  E", font_size=48).shift(2 * LEFT)
        text_group = VGroup(text)
        
        self.add(square_group, text_group)
        self.wait(0.5)

        sequence_1 = Tex("SKNKCNE")
        sequence_1.to_corner(UP + RIGHT)
        self.play(Transform(text_group, sequence_1))
        self.wait()
