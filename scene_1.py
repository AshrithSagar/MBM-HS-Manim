from manim import *
import itertools


def mutationBoxes(sequence, boxGroup, seqGroup, mutations):
    mainGroups, textGroups = [], []
    sequence_length = len(sequence)

    for mutation in mutations:
        position = mutation[0]
        string = mutation[1]
        CorrespondingBox = boxGroup[2*(sequence_length-position-1)]
        main_box_y = CorrespondingBox.get_y()

        mainGroup = VGroup()
        textGroup = VGroup()
        for index, character in enumerate(string):
            box = Square(
                fill_color=GREEN,
                fill_opacity=0.5,
                stroke_color=GREEN
            ).scale(0.5).shift((main_box_y-index) * UP)
            text = Text(character, font_size=48).move_to(box.get_center())
            mainGroup.add(box, text)
            textGroup.add(text)
        mainGroup.match_x(CorrespondingBox)
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
        ).scale(0.5).shift((index-3) * LEFT + UP)
        text = Text(character, font_size=48).move_to(box.get_center())
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
        self.add(seq_text_group)

        for mut_box_group in mut_box_groups:
            self.add(mut_box_group)
        for mut_text_group in mut_text_groups:
            self.add(mut_text_group)

        sequential_mutations = list(sequence)
        position_list = [x[0] for x in mutations]
        for index, character in enumerate(sequence):
            if index in position_list:
                characters = [x[1] for x in mutations if x[0] == index]
                sequential_mutations[index] = [x for x in characters[0]]
            else:
                sequential_mutations[index] = character
        print(sequential_mutations)

        seqs = itertools.product(*sequential_mutations)
        for seq in seqs:
            seq = "".join(seq)
            print(seq)
        #     self.play(seq_text_group.animate.shift(3*DOWN))

        #     sequenceList = Tex("SKNKCNE")
        #     sequenceList.to_corner(UP + RIGHT)
        #     self.play(Transform(seq_text_group, sequenceList))
        #     self.wait(0.2)
        # self.wait()
