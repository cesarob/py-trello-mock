from expects import *
import trellomock

with description("Board"):
    with before.each:
        self.client = trellomock.TrelloClient()
        self.board = trellomock.Board(self.client)

    with it("adds a label"):
        self.board.add_label('a_label', 'red')

        labels = self.board.get_labels()
        expect(labels).to(have_len(1))
        expect(labels[0].name).to(equal('a_label'))
        expect(labels[0].color).to(equal('red'))

    with description("Once a list is added"):
        with before.each:
            self.list = self.board.add_list('a_list')
            self.list_id = self.list.id

        with it("is retrieved by id"):
            the_list = self.board.get_list(self.list_id)
            expect(the_list).to(be(self.list))

        with it("is contained in the board lists"):
            lists = self.board.get_lists(list_filter='all')
            expect(lists).to(have_len(1))
            expect(lists[0].name).to(equal('a_list'))
            expect(lists[0].id).to(equal(self.list.id))

        with it("is retrieved by id from the client"):
            list = self.client.get_list(self.list_id)
            expect(list).to(be(self.list))
