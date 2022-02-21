#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Yukoo - Main evaluation module.

Use easy functions.
"""
import chess

from yukoo.evaluation.evaluator import Evaluator


def evaluate(position: chess.Board) -> int:
    """
    Evaluate position.

    Wraps the Evaluator object.

    :param chess.Board position: Position to evaluate.
    :return: Relative advantage as centipawns.
    :rtype: int
    """
    evaluator: Evaluator = Evaluator(position)
    return evaluator.evaluate()

