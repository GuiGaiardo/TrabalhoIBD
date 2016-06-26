from SQL_Parser.QueryTree import *


class SelectionOptimizer:
    def __init__(self, tree):
        self.root = tree.root

    def optimize(self):
        if isinstance(self.root.children, ThetaJoinNode) or isinstance(self.root.children, Table):
            return self.root

        selection = self.root.children
        if 'or' in selection.conectors or isinstance(selection.children, Table):
            return self.root

        terms = selection.terms

        unaries, binaries = self.__separate_terms(terms)
        son = selection.children
        tables, unaries, binaries = self._optimize(son, unaries, binaries)

        if len(binaries) > 0:
            selection.terms = binaries
            n_conectors = len(selection.terms) - 1
            selection.conectors = ["and" for i in range(n_conectors)]

        else:
            self.root.children = son

        return self.root

    def _optimize(self, node, unaries, binaries):
        left = node.children[0]
        right = node.children[1]
        if isinstance(left, Table):
            left_table = left.get_description()
            tables = [left_table]
            terms = []
            for term in unaries:
                if term[0] == left_table:
                    terms.append(term[1])

            if len(terms) > 0:
                new_selection = SelectionNode(terms, ['and' for i in range(len(terms)-1)])
                new_selection.set_child(left)
                node.children[0] = new_selection

        elif isinstance(left, ThetaJoinNode):
            tables, unaries, binaries = self._optimize(left, unaries, binaries)

            terms = []
            for term in binaries:
                t1 = term[0][0]
                t2 = term[0][1]
                if (t1 in tables) and (t2 in tables):
                    terms.append(binaries.pop(binaries.index(term))[1])

            if len(terms) > 0:
                new_selection = SelectionNode(terms, ['and' for i in range(len(terms) - 1)])
                new_selection.set_child(left)
                node.children[0] = new_selection

        else:
            print("deu merda")

        if isinstance(right, Table):
            right_table = right.get_description()
            tables.append(right_table)
            terms = []
            for term in unaries:
                if term[0] == right_table:
                    terms.append(unaries.pop(unaries.index(term))[1])

            if len(terms) > 0:
                new_selection1 = SelectionNode(terms, ['and' for i in range(len(terms) - 1)])
                new_selection1.set_child(right)
                node.children[1] = new_selection1

        elif isinstance(right, ThetaJoinNode):
            t, unaries, binaries = self._optimize(right, unaries, binaries)
            tables += t

            terms = []
            for term in binaries:
                t1 = term[0][0]
                t2 = term[0][1]
                if (t1 in tables) and (t2 in tables):
                    terms.append(binaries.pop(binaries.index(term))[1])

            if len(terms) > 0:
                new_selection = SelectionNode(terms, ['and' for i in range(len(terms) - 1)])
                new_selection.set_child(left)
                node.children[1] = new_selection

        else:
            print("DEU RUIM!")

        return tables, unaries, binaries

    # Separa os termos que utilizam apenas uma tabela dos que utilizam duas tabelas distintas
    def __separate_terms(self, terms):
        unaries = []
        binaries = []
        for term in terms:
            tables = self.__get_tables(term)
            if len(tables) == 1:
                unaries.append((tables[0], term))
            else:
                binaries.append((tables, term))
        return unaries, binaries

    def __get_tables(self, term):
        table1 = term[0]
        dot = table1.index('.')
        table1 = table1[:dot]
        if '.' not in term[2]:
            return [table1]
        else:
            table2 = term[2]
            dot = table2.index('.')
            table2 = table2[:dot]

        return [table1, table2]
