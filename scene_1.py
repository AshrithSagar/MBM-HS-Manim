from manim import *


def mutationBoxes(sequence, boxGroup, seqGroup, mutations):
    mainGroups, textGroups = [], []
    sequence_length = len(sequence)
    for mutation in mutations:
        position = mutation[0]
        string = mutation[1]

        mainGroup = VGroup()
        textGroup = VGroup()
        for index, character in enumerate(string[::-1]):
            box = Square(
                fill_color=GREEN,
                fill_opacity=0.5,
                stroke_color=GREEN
            ).scale(0.5).shift((index-3) * UP)
            text = Text(character, font_size=36).move_to(box.get_center())
            mainGroup.add(box, text)
            textGroup.add(text)
        mainGroup.move_to(boxGroup[2*(sequence_length-position-1)].get_center())
        mainGroups.append(mainGroup)
        textGroups.append(textGroup)

    return mainGroups, textGroups


def sequenceBoxes(sequence):
    mainGroup = VGroup()
    textGroup = VGroup()
    for index, character in enumerate(sequence[::-1]):
        box = Square(
            fill_color=BLUE,
            fill_opacity=0.5,
            stroke_color=BLUE
        ).scale(0.5).shift((index-3) * LEFT)
        text = Text(character, font_size=36).move_to(box.get_center())
        mainGroup.add(box, text)
        textGroup.add(text)

    return mainGroup, textGroup


class CartesianProduct(Scene):
    def construct(self):
        sequence = "SKNKCNE"

        # [[position, AA_groups], ...]
        mutations = [[2, "NDAQ"], [4, "CALEG"]]

        seq_box_group, seq_text_group = sequenceBoxes(sequence)
        mut_box_groups, mut_text_groups = mutationBoxes(
            sequence, seq_box_group, seq_text_group, mutations)
        self.add(seq_box_group)

        # seq_text_group.to_corner(UP)
        self.add(seq_text_group)

        for mut_box_group in mut_box_groups:
            self.add(mut_box_group)
        for mut_text_group in mut_text_groups:
            self.add(mut_text_group)

        # self.play(seq_text_group.animate.shift(3*DOWN))

        sequenceList = Tex("SKNKCNE")
        sequenceList.to_corner(UP + RIGHT)
        self.play(Transform(seq_text_group, sequenceList))
        self.wait()
