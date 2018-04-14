# -*- coding: utf-8 -*-
from uuid import uuid4

import trello.board as board
from .trellolist import List
from .label import Label


class Board(board.Board):

    def __init__(self, client=None, board_id=None, organization=None, name=''):
        super().__init__(client, board_id, organization, name)
        self.lists = []
        self.labels = {}

        # These ones were set in fetch operation
        self.description = None
        self.closed = False
        self.url = None

    def fetch(self):
        raise NotImplementedError()

    def save(self):
        # In this version changes always are synced
        pass

    def set_name(self, name):
        self.name = name

    def set_description(self, desc):
        self.description = desc

    def close(self):
        self.closed = True

    def open(self):
        self.closed = False

    def get_list(self, list_id):
        return self.client.get_list(list_id)

    def get_lists(self, list_filter):
        """Get lists from filter

        :rtype: list of List
        """
        # TODO check default return value if board is empty
        result = []
        if list_filter == 'all':
            result = self.lists
        elif list_filter == 'open':
            # TODO
            raise NotImplementedError()
        elif list_filter == 'closed':
            # TODO
            raise NotImplementedError()
        else:
            # # TODO Check what trello does here
            raise ValueError('Invalid List Filter: ' + list_filter)
        return result

    def get_labels(self, fields='all', limit=50):
        """Get label

        :rtype: list of Label
        """
        # TODO fields pending
        return list(self.labels.values())

    def get_checklists(self, cards='all'):
        """Get checklists

        :rtype: list of Checklist
        """
        raise NotImplementedError()

    def add_list(self, name, pos=None):
        """Add a list to this board

        :name: name for the list
        :pos: position of the list: "bottom", "top" or a positive number
        :return: the list
        :rtype: List
        """
        # TODO pending to manage the position of the list
        list = List(self, list_id=str(uuid4()), name=name)
        list.pos = pos
        self.client.add_list(list)
        self.lists.append(list)
        return list

    def add_label(self, name, color):
        """Add a label to this board

        :name: name of the label
        :color: the color, either green, yellow, orange
            red, purple, blue, sky, lime, pink, or black
        :return: the label
        :rtype: Label
        """
        label = Label(self.client, str(uuid4()), name, color)
        self.labels[label.id] = label
        return label

    def delete_label(self, label_id):
        """Delete a label from this board

        :label_id: the ID of the label to delete.
        :return: the label
        :rtype: json
        """
        # TODO review trello behaviour, probably if the label doesn't exist an exception is rised
        return self.labels.pop(label_id, None)

    def all_cards(self):
        """Returns all cards on this board

        :rtype: list of Card
        """
        filters = {
            'filter': 'all',
            'fields': 'all'
        }
        return self.get_cards(filters)

    def open_cards(self):
        """Returns all open cards on this board

        :rtype: list of Card
        """
        filters = {
            'filter': 'open',
            'fields': 'all'
        }
        return self.get_cards(filters)

    def closed_cards(self):
        """Returns all closed cards on this board

        :rtype: list of Card
        """
        filters = {
            'filter': 'closed',
            'fields': 'all'
        }
        return self.get_cards(filters)

    def get_cards(self, filters=None, card_filter=""):
        """
        :filters: dict containing query parameters. Eg. {'fields': 'all'}
        :card_filter: filters on card status ('open', 'closed', 'all')

        More info on card queries:
        https://trello.com/docs/api/board/index.html#get-1-boards-board-id-cards

        :rtype: list of Card
        """
        # TODO
        raise NotImplementedError()

    def get_members(self, filters=None):
        """Get members with filter

        :filters: dict containing query parameters.
            Eg. {'fields': 'all', 'filter': 'admins'}

        More info on possible filters:
        https://developers.trello.com/advanced-reference/board#get-1-boards-board-id-members

        :rtype: list of Member
        """
        raise NotImplementedError()

    # Add a member to a board
    def add_member(self, member, member_type="normal"):
        raise NotImplementedError()

    # Removes an existing member of a board
    def remove_member(self, member):
        raise NotImplementedError()

    def fetch_actions(self, action_filter, action_limit=50, before=None, since=None):
        """Returns all actions that conform to the given filters.

        :action_filter: str of possible actions separated by comma
            ie. 'createCard,updateCard'
        :action_limit: int of max items returned
        :before: datetime obj
        :since: datetime obj

        More info on action filter values:
        https://developers.trello.com/advanced-reference/board#get-1-boards-board-id-actions

        :rtype: json list of past actions
        """
        raise NotImplementedError()

    def get_last_activity(self):
        """Return the date of the last action done on the board.

        :rtype: datetime.datetime
        """
        # TODO
        return []
