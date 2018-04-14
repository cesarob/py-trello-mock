# -*- coding: utf-8 -*-
from uuid import uuid4
import trello
import trello.trelloclient as trelloclient
from .board import Board


class ResourceUnavailable(trello.exceptions.ResourceUnavailable):
    def __init__(self, type, id):

        class HttpResponse:
            status_code = 400

        super().__init__("Invalid %s id %s " % (type, id), HttpResponse())


class TrelloClient(trelloclient.TrelloClient):

    def __init__(self):
        self.boards = []
        self.organizations = []

    def info_for_all_boards(self, actions):
        """
        Use this if you want to retrieve info for all your boards in one swoop
        """
        # TODO I think this operation has a bug in py-trello it is not returning anything
        raise NotImplementedError()

    def logout(self):
        raise NotImplementedError()

    def list_boards(self, board_filter="all"):
        """
        Returns all boards for your Trello user

        :return: a list of Python objects representing the Trello boards.
        :rtype: list of Board

        Each board has the following noteworthy attributes:
            - id: the board's identifier
            - name: Name of the board
            - desc: Description of the board (optional - may be missing from the
                    returned JSON)
            - closed: Boolean representing whether this board is closed or not
            - url: URL to the board
        """
        # TODO We are not applying filtering
        return self.boards

    def list_organizations(self):
        """
        Returns all organizations for your Trello user

        :return: a list of Python objects representing the Trello organizations.
        :rtype: list of Organization

        Each organization has the following noteworthy attributes:
            - id: the organization's identifier
            - name: Name of the organization
            - desc: Description of the organization (optional - may be missing from the
                    returned JSON)
            - closed: Boolean representing whether this organization is closed or not
            - url: URL to the organization
        """
        return self.organizations

    def get_organization(self, organization_id):
        """Get organization

        :rtype: Organization
        """
        # TODO I think this operation has a bug in py-trello it is not returning anything
        raise NotImplementedError()

    def get_board(self, board_id):
        """Get board

        :rtype: Board
        """
        # TODO check py-treo iface
        board = None
        for board in self.boards:
            if board_id == board.id:
                return board
        if board is None:
            raise ResourceUnavailable(self.__class__.__name__, board_id)

    def add_board(self, board_name, source_board=None, organization_id=None, permission_level='private'):
        """Create board
        :param board_name: Name of the board to create
        :param source_board: Optional Board to copy
        :param permission_level: Permission level, defaults to private
        :rtype: Board
        """
        board = Board(client=self, board_id=str(uuid4()), name=board_name)
        self.boards.append(board)
        return board

    def get_member(self, member_id):
        """Get member

        :rtype: Member
        """
        raise NotImplementedError()

    def get_card(self, card_id):
        """Get card

        :rtype: Card
        """
        raise NotImplementedError()

    def get_list(self, list_id):
        """Get list

        :rtype: List
        """
        raise NotImplementedError()

    def get_label(self, label_id, board_id):
        """Get Label

        Requires the parent board id the label is on

        :rtype: Label
        """
        raise NotImplementedError()

    def fetch_json(
            self,
            uri_path,
            http_method='GET',
            headers=None,
            query_params=None,
            post_args=None,
            files=None):
        raise NotImplementedError()

    def list_hooks(self, token=None):
        raise NotImplementedError()

    def create_hook(self, callback_url, id_model, desc=None, token=None):
        raise NotImplementedError()

    def search(self, query, partial_match=False, models=[],
               board_ids=[], org_ids=[], card_ids=[]):
        """
        Search trello given a query string.

        :param str query: A query string up to 16K characters
        :param bool partial_match: True means that trello will look for
                content that starts with any of the words in your query.
        :param list models: Comma-separated list of types of objects to search.
                This can be 'actions', 'boards', 'cards', 'members',
                or 'organizations'.  The default is 'all' models.
        :param list board_ids: Comma-separated list of boards to limit search
        :param org_ids: Comma-separated list of organizations to limit search
        :param card_ids: Comma-separated list of cards to limit search

        :return: All objects matching the search criterial.  These can
            be Cards, Boards, Organizations, and Members.  The attributes
            of the objects in the results are minimal; the user must call
            the fetch method on the resulting objects to get a full set
            of attributes populated.
        :rtype list:
        """
        # TODO
        raise NotImplementedError()
