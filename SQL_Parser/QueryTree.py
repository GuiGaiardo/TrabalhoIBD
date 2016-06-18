

class QueryTree():
    def __init__(self):
        return


    def set_root(self, node):
        self.root = node





class SelectionNode():
    def __init__(self, terms, conectors):
        self.terms = terms
        self.conectors = conectors
        self.children = None


    def __str__(self):
        text = "S"
        if (len(self.terms) == 1):
            text += " " + self.terms[0]

        else:
            for i in range(len(self.terms)-1):
                text += " " + self.terms[i] + " " + self.conectors[i]

            text += " " + self.terms[i+1]

        text += " (" + str(self.children) + ")"

        return text


    def set_child(self, child):
        self.children = child


class ProjectionNode():
    def __init__(self, columns):
        self.columns = columns
        self.children = None

    def __str__(self):
        text = "P "

        text += self.columns[0]
        for column in self.columns[1:]:
            text += ", " + column

        text += "(" + str(self.children) + ")"

        return text

    def set_child(self, child):
        self.children = child


class ThetaJoinNode():
    def __init__(self, child1, child2, terms, conectors):
        self.children = [child1, child2]
        self.terms = terms
        self.conectors = conectors

    def __str__(self):
        text = "(" + str(self.children[0]) + ")"
        text += " |X|"

        if (len(self.terms) == 1):
            if (self.terms[0] == ','):
                pass
            else:
                text += " " + self.terms[0]

        else:
            for i in range(len(self.terms)-1):
                text += " " + self.terms[i] + " " + self.conectors[i]

            text += " " + self.terms[i+1]

        text += " (" + str(self.children[1]) + ")"

        return text


class Table():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name