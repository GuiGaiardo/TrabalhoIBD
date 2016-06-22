from SQL_Parser.QueryTree import *
class SelectionOptimizer:
    def __init__(self, tree):
        self.root = tree.root

    def optimize(self):
        selection = self.root.children
        if type(selection.children) == Table:
            return self.root

        terms = selection.terms
        terms.reverse()
        conectors = selection.conectors
        conectors.reverse()

        if 'or' in conectors:
            left_over_terms = terms[conectors.index('or'):]
            terms = terms[:conectors.index('or')]
            left_over_conectors = conectors[conectors.index('or'):]
            conectors = conectors[:conectors.index('or')]

            if len(terms) == 0:
                return self.root
        else:
            left_over_terms = []
            left_over_conectors = []

        unaries, binaries = self.__separate_terms(terms)
        son = selection.children
        tables, unaries, binaries = self._optimize(son, unaries, binaries)

        for term in binaries:
            left_over_terms.append(term)

        if len(left_over_terms) == 0:
            self.root.children = son

        else:
            selection.terms = left_over_terms
            n_conectors = len(selection.terms) - len(left_over_conectors) - 1
            selection.conectors = ["and" for i in range(n_conectors)] + left_over_conectors

        return self.root



#lidar com os unarios, achar posicao (acima da tabela)
#lidar com os binarios, achar posicao (acima da juncao)

    def _optimize(self, node, unaries, binaries):
        left = node.children[0]
        right = node.children[1]
        if isinstance(left, Table):
            left_table = left.get_description()
            tables = [left_table]
            terms = []
            for term in unaries:
                if term[0] == left_table:
                    terms.append(unaries.pop(unaries.index(term))[1])


            if len(terms) > 0:
                new_selection = SelectionNode(terms, ['and' for i in range(len(terms)-1)])
                new_selection.set_child(left)
                node.children[0] = new_selection

        elif isinstance(left, ThetaJoinNode):
            tables, unaries, binaries = self._optmize(left, unaries, binaries)

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
        print(right)
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





    #Separa os termos que utilizam apenas uma tabela dos que utilizam duas tabelas distintas
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