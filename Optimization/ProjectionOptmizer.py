from SQL_Parser.QueryTree import *


class ProjectionOptmizer:
    def __init__(self, tree):
        self.root = tree.root

    def optimize(self):
        if isinstance(self.root.children, ThetaJoinNode):
            return self.root

        projection = self.root
        # terms = projection.terms

        # unaries, binaries = self.__separate_terms(terms)
        # son = projection.children
        t = []
        tables = self._get_tables(projection, t)
        print(tables)
        l = self._get_attributes(projection, tables)
        print(l)

        return self.root

    def _optimizer(self):
        pass

    def _get_attributes(self, node, lista):

        if isinstance(node, Table):
            term = node.get_description()
        elif isinstance(node, SelectionNode):
            term = node.get_description()
            print(term)
            t = term
            print (t)
            dot = t.index('.')
            for elem in lista:
                if elem[0] == t[:dot]:
                    d = t.find(">")
                    if(d == -1):
                        d = t.find("<")
                    if(d == -1):
                        d = t.find("=")
                    if(d != -1):
                        new = t.replace(t[d:],"")
                        elem.append(new.split())

            lista = self._get_attributes(node.children, lista)
        elif isinstance(node, ProjectionNode):
            term = node.get_description()
            t = term
            dot = t.index('.')
            for elem in lista:
                if elem[0] == t[:dot]:
                    new = t.replace(",","")
                    elem.append(new.split())
            lista = self._get_attributes(node.children,lista)

        elif isinstance(node, ThetaJoinNode):
            left = node.children[0]
            right = node.children[1]
            lista = self._get_attributes(left, lista)
            lista = self._get_tables(right, lista)

            term = node.get_description()
            t = term
            dot = t.index('.')
            for elem in lista:
                if elem[0] == t[:dot]:
                    new = t.replace(",", "")
                    elem.append(new.split())

        else:
            print("DEU ERRO")

        return lista


    def _get_tables(self, node, tab):
        if isinstance(node, Table):
            new_table = node.get_description()
            l = [new_table]
            if len(tab) > 0:
                tab.append(l)
            else:
                tab = [l]

        elif isinstance(node, SelectionNode):
            tab = self._get_tables(node.children, tab)

        elif isinstance(node, ProjectionNode):
            tab = self._get_tables(node.children, tab)

        elif isinstance(node, ThetaJoinNode):
            left = node.children[0]
            right = node.children[1]
            tab = self._get_tables(left, tab)
            tab = self._get_tables(right, tab)

        else:
            print("DEU ERRO")

        return tab
