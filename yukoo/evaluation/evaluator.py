#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Yukoo - Evaluation module.

Base object for evaluating positions.
"""
import chess

from yukoo.evaluation.constants import *


class Evaluator:
    """
    Base evaluation object.

    Use functions defined in module:yukoo.evaluation.
    """

    def __init__(self, board: chess.Board) -> None:
        """
        Initialize evaluator.

        :param chess.Board board: Board to evaluate.
        :return: Nothing, use evaluate() function.
        """
        self.board: chess.Board = board

    def evaluate(self) -> int:
        """
        Evaluate wrapper.

        Evaluate position and return result.
        Also do some mirror stuff.

        :return: Relative evaluation of position as centipawns.
        :rtype: int
        """
        if self.board.turn is chess.BLACK:
            self.board = self.board.mirror()
        score1: int = self.evaluate_position(self.board)
        score2: int = self.evaluate_position(self.board.mirror())
        return score1 - score2

    def evaluate_position(self, board: chess.Board) -> int:
        """
        Evaluate position.

        Evaluate:
        - Material advantage
        - more coming...

        :param chess.Board board: Board to evaluate.
        :return: White's evaluation as centipawns.
        :rtype: int
        """
        score: int = 0
        score += self.eval_material(board)
        return score

    def eval_material(self, board: chess.Board) -> int:
        """
        Evaluate material advantage.

        :return: White's material as centipawns.
        :rtype: int
        """
        score: int = 0
        piece_map: dict[chess.Square, chess.Piece] = board.piece_map()
        for piece in piece_map.values():
            score += PIECES_VALUES.get(piece.symbol(), 0)
        return score

