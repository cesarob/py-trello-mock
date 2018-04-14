from expects import *
import trello
import trellomock

with description("TrelloClient"):
    with it("raises a ResourceUnavailable exception when a board doesn't exist"):
        client = trellomock.TrelloClient()
        expect(lambda: client.get_board('an_id')).to(raise_error(trello.exceptions.ResourceUnavailable))

    with it("gets all the boards"):
        client = trellomock.TrelloClient()
        client.add_board('a_board')

        boards = client.list_boards()

        expect(boards).to(have_len(1))
        expect(boards[0]).to(be_a(trello.Board))
        expect(boards[0].name).to(equal('a_board'))

    with it("gets an existant board"):
        client = trellomock.TrelloClient()
        client.add_board('a_board')
        board_id = client.list_boards()[0].id

        board = client.get_board(board_id)

        expect(board.name).to(equal('a_board'))
