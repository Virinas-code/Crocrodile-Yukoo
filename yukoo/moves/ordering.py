#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Yukoo - Move ordering module.

This module is used to order moves for Yukoo.
"""
import chess

import yukoo.evaluation


class MoveOrderer:
    """
    Base class for move ordering.

    Contains specific functions for each priority case.
    """

    def __init__(self, board: chess.Board) -> None:
        """
        Initialize orderer.

        Gets initial board.

        :param chess.Board board: Initial board.
        """
        self.board: chess.Board = board
        self.test_board: chess.Board | None = None
        self.move_list: list[chess.Move] = list(self.board.legal_moves)

    def is_checkmate(self, move: chess.Move) -> bool:
        """
        Check if move is checkmate.

        Used for first case: Checkmate.

        :return: True if checkmate, False else.
        :rtype: bool
        """
        return self.test_board.is_checkmate()

    def is_check(self, move: chess.Move) -> bool:
        """
        Check if move is check.

        Used for second case: Check.

        :return: True if check, False else.
        :rtype: bool
        """
        return self.test_board.is_check()
    
    def sort_material(self, moves: list[chess.Move]) -> list[chess.Move]:
        """
        Sort moves by material advantage.

        Used for second case: Check.

        :param list[chess.Move] moves: Unordered moves list.
        :return: Move list sorted by material advantage.
        :rtype: list[chess.Move]
        """
        result: list[chess.Move] = moves
        result.sort(key=self.eval_material)
        return result
    
    def eval_material(self, move: chess.Move) -> int:
        """
        Eval material advantage after moive.

        Used for second case: Check.

        :param chess.Move move: Move played.
        :return: Material advantage.
        :rtype: int
        """
        test_board: chess.Board = self.board.copy()
        test_board.push(move)
        return yukoo.evaluation.evaluate(test_board)

    def sort(self, result_dict: dict[str, list[chess.Move]]) -> dict[str, list[chess.Move]]:
        """
        Sort priorities with multiple moves.

        Wraps sort function for some priorities.

        :param dict[str, list[chess.Move]] result_dict: Unordered priorities dict.
        :return: Ordered priorities dict.
        :rtype: dict[str, list[chess.Move]]
        """
        result: dict[str, list[chess.Move]] = result_dict
        result["check"] = self.sort_material(result["check"])
        return result

    def join(self, result_dict: dict[str, list[chess.Move]]) -> list[chess.Move]:
        """
        Join moves sorted by priority.

        Used to render the final move list.

        :param dict[str, list[chess.Move]] result_dict: The priorities dict to parse.
        :return: Ordered list from priorities.
        :rtype: list[chess.Move]
        """
        result: list[chess.Move] = []
        result.extend(result_dict["checkmate"])
        result.extend(result_dict["check"])
        result.extend(result_dict["other"])
        return result

    def order(self) -> list[chess.Move]:
        """
        Get board's legal moves, ordered.

        Wraps all priority functions.

        :return: List of legal moves, ordered.
        :rtype: list[chess.Move]
        """
        result_dict: dict[str, list[chess.Move]] = {
                "checkmate": [],
                "check": [],
                "other": []
        }
        for move in self.move_list:
            self.test_board = self.board.copy()
            self.test_board.push(move)
            if self.is_checkmate(move):
                result_dict["checkmate"].append(move)
            elif self.is_check(move):
                result_dict["check"].append(move)
            else:
                result_dict["other"].append(move)
        result_dict = self.sort(result_dict)
        return self.join(result_dict)  # Join results to one list


def order_moves(board: chess.Board) -> list[chess.Move]:
    """
    Order moves for board.

    Wraps ordering objects.

    :param chess.Board board: Board to order moves.
    :return: List of legal moves, ordered.
    :rtype: list[chess.Move]
    """
    move_order: MoveOrderer = MoveOrderer(board)
    return move_order.order()
