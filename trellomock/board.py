# -*- coding: utf-8 -*-
import trello.board as board


class Board(board.Board):
    def get_last_activity(self):
        return []
