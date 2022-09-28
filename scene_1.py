from manim import *
import itertools


def mutationBoxes(sequence, boxGroup, seqGroup, mutations):
    mutMainGroups, mutBoxGroups, mutTextGroups = [], [], []
    sequence_length = len(sequence)

    for mutation in mutations:
        position = mutation[0]
        string = mutation[1]
        CorrespondingBox = boxGroup[sequence_length-position-1]
        main_box_y = CorrespondingBox.get_y()

        mutBoxGroup = VGroup()
        mutTextGroup = VGroup()
        mutMainGroup = VGroup()

        for index, character in enumerate(string):
            box = Square(
                fill_color=GREEN,
                fill_opacity=0.5,
                stroke_color=GREEN
            ).scale(0.5).shift((main_box_y-index) * UP)
            text = Text(character, font_size=48).move_to(box.get_center())

            mutBoxGroup.add(box)
            mutTextGroup.add(text)
            mutMainGroup.add(box, text)

        mutBoxGroup.match_x(CorrespondingBox)
        mutTextGroup.match_x(CorrespondingBox)
        mutMainGroups.append(mutMainGroup)
        mutBoxGroups.append(mutBoxGroup)
        mutTextGroups.append(mutTextGroup)

    return mutMainGroups, mutBoxGroups, mutTextGroups


def sequenceBoxes(sequence):
    boxGroup = VGroup()
    textGroup = VGroup()
    for index, character in enumerate(sequence[::-1]):
        box = Square(
            fill_color=BLUE,
            fill_opacity=0.5,
            stroke_color=BLUE
        ).scale(0.5).shift((index-3) * LEFT + UP)
        text = Text(character, font_size=48).move_to(box.get_center())
        boxGroup.add(box)
        textGroup.add(text)

    return boxGroup, textGroup


class CartesianProduct(Scene):
    def construct(self):
        sequence = "SKNKCNE"

        # [[position, AA_groups], ...]
        mutations = [[2, "NDAQ"], [4, "CEG"]]

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

        sequenceList = VGroup()
        sequence_text = Text(sequence)
        sequence_text.to_corner(UP + RIGHT)
        sequenceList.add(sequence_text)
        sequenceList.to_corner(UP + RIGHT)

        for index, seq in enumerate(seqs):
            seq = "".join(seq)

            seq_box_group, seq_text_group = sequenceBoxes(seq)
            mut_main_groups, mut_box_groups, mut_text_groups = mutationBoxes(
                    seq, seq_box_group, seq_text_group, mutations)

            self.add(seq_box_group)
            self.add(seq_text_group)
            self.add(*[mut_box_group for mut_box_group in mut_box_groups])
            self.add(*[mut_text_group for mut_text_group in mut_text_groups])

            sequence_text = Text(seq, font_size=36)
            sequence_text.align_to(sequenceList[-1], UR).shift(0.5 * DOWN)
            sequenceList.add(sequence_text)
            self.play(Transform(seq_text_group, sequence_text), run_time=1)
            self.wait(0.5)

            self.play(mut_main_groups[0].animate.shift(UP))

            self.remove(*seq_box_group)
            box_list = [box for box in 
                [mut_box_group for mut_box_group in mut_box_groups]]
            text_list = [text for text in 
                [mut_text_group for mut_text_group in mut_text_groups]]
            self.remove(*box_list)
            self.remove(*text_list)
