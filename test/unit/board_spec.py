from expects import *
import trellomock

with description("Board"):

    with it("adds a label"):
        client = trellomock.TrelloClient()
        board = trellomock.Board(client)

        board.add_label('a_label', 'red')

        labels = board.get_labels()
        expect(labels).to(have_len(1))
        expect(labels[0].name).to(equal('a_label'))
        expect(labels[0].color).to(equal('red'))
