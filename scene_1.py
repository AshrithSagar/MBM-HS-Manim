"""
Cartesian Product animation of Peptide mutater using Manim
"""
import itertools
from manim import *


def mutation_boxes(sequence, box_group, seq_group, mutations):
    """
    For the vertical boxes containing the mutations
    """
    mut_main_groups, mut_box_groups, mut_text_groups = [], [], []
    sequence_length = len(sequence)

    for mutation in mutations:
        position = mutation[0]
        mutation_string = mutation[1]
        corresponding_box = box_group[sequence_length-position-1]
        main_box_y = corresponding_box.get_y()

        mut_box_group = VGroup()
        mut_text_group = VGroup()
        mut_main_group = VGroup()

        for index, character in enumerate(mutation_string):
            box = Square(
                fill_color=GREEN,
                fill_opacity=0.5,
                stroke_color=GREEN
            ).scale(0.5).shift((main_box_y-index) * UP)
            text = Text(character, font_size=48).move_to(box.get_center())

            mut_box_group.add(box)
            mut_text_group.add(text)
            mut_main_group.add(box, text)

        mut_box_group.match_x(corresponding_box)
        mut_text_group.match_x(corresponding_box)
        mut_main_groups.append(mut_main_group)
        mut_box_groups.append(mut_box_group)
        mut_text_groups.append(mut_text_group)

    return mut_main_groups, mut_box_groups, mut_text_groups


def sequence_boxes(sequence):
    """
    Main horizontal sequence boxes
    """
    box_group = VGroup()
    text_group = VGroup()

    for index, character in enumerate(sequence[::-1]):
        box = Square(
            fill_color=BLUE,
            fill_opacity=0.5,
            stroke_color=BLUE
        ).scale(0.5).shift((index-3) * LEFT + UP)
        text = Text(character, font_size=48).move_to(box.get_center())
        box_group.add(box)
        text_group.add(text)

    return box_group, text_group


class CartesianProduct(Scene):
    """
    Main scene.
    Animation explaining the cartesian product of the peptide mutator.
    """
    def construct(self):
        sequence = "SKNKCNE"

        # [[position, AA_groups], ...]
        mutations = [[2, "NDAQ"], [4, "CEG"]]

        # Evaluate the Cartesian product
        sequential_mutations = list(sequence)
        position_list = [x[0] for x in mutations]
        for index, character in enumerate(sequence):
            if index in position_list:
                characters = [x[1] for x in mutations if x[0] == index]
                sequential_mutations[index] = list(characters[0])
            else:
                sequential_mutations[index] = character
        print(sequential_mutations)
        seqs = itertools.product(*sequential_mutations)

        # Sequence list on right side
        sequence_list = VGroup()
        sequence_text = Text(sequence)
        sequence_list.add(sequence_text)
        sequence_list.to_corner(UP + RIGHT)

        # Iterate over all sequences in the Cartesian product
        for index, seq in enumerate(seqs):
            seq = "".join(seq)

            seq_box_group, seq_text_group = sequence_boxes(seq)
            mut_main_groups, mut_box_groups, mut_text_groups = mutation_boxes(
                    seq, seq_box_group, seq_text_group, mutations)

            self.add(seq_box_group)
            # self.add(*mut_box_groups)
            # self.add(*mut_text_groups)
            self.add(seq_text_group)

            new_seq_text_group = seq_text_group.copy()
            self.add(new_seq_text_group)

            sequence_text = Text(seq, font_size=36)
            sequence_text.align_to(sequence_list[-1], UR).shift(0.5 * DOWN)
            sequence_list.add(sequence_text)
            self.play(Transform(seq_text_group, sequence_text), run_time=1)
            self.wait(0.5)

            # self.play(mut_main_groups[0].animate.shift(UP))

            self.remove(*seq_box_group)
            self.remove(*list(mut_box_groups))
            self.remove(*list(mut_text_groups))

            self.remove(*new_seq_text_group)
