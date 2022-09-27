from manim import *


def sequenceBoxes(string):
    dimension = 2

    mainGroup = VGroup()
    textGroup = VGroup()
    for index, character in enumerate(string[::-1]):
        box = Square(
            fill_color=BLUE,
            fill_opacity=0.5,
            stroke_color=BLUE
        ).scale(0.5).shift((index-3) * LEFT)
        text = Text(character, font_size=24).move_to(box.get_center())
        mainGroup.add(box, text)
        textGroup.add(text)

    return mainGroup, textGroup


class CartesianProduct_2(Scene):
    def construct(self):
        sequence = "SKNKCNE"

        # [[position, AA_groups], ...]
        mutations = [[2, "NBCD"]]

        box_group, seq_group = sequenceBoxes(string=sequence)
        self.add(box_group)

        # seq_group.to_corner(UP)
        self.add(seq_group)

        # self.play(seq_group.animate.shift(3*DOWN))

        sequenceList = Tex("SKNKCNE")
        sequenceList.to_corner(UP + RIGHT)
        self.play(Transform(seq_group, sequenceList))
        self.wait()
