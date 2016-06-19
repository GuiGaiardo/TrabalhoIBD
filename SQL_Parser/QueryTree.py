

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


    def get_description(self):
        description = ""

        if (len(self.terms) == 1):
            description += self.terms[0]

        else:
            for i in range(len(self.conectors)):
                description += " " + self.terms[i] + " " + self.conectors[i]

            description += " " + self.terms[i+1]

        return description


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

    def get_description(self):
        description = self.columns[0]
        for column in self.columns[1:]:
            description += ", " + column

        return description


class ThetaJoinNode():
    def __init__(self, child1, child2, terms, conectors):
        self.children = [child1, child2]
        self.terms = terms
        self.conectors = conectors

    def __str__(self):
        text = "(" + str(self.children[0]) + ")"

        if (self.terms[0] == ','):
            text += " X"
        else:
            text += " |X|"
            if (len(self.terms) == 1):
                text += " " + self.terms[0]
            else:
               for i in range(len(self.terms)-1):
                   text += " " + self.terms[i] + " " + self.conectors[i]

               text += " " + self.terms[i+1]

        text += " (" + str(self.children[1]) + ")"

        return text

    def get_description(self):
        description = ""

        if (len(self.terms) == 1):
            if (self.terms[0] == ','):
                description += "X"
            else:
                description += self.terms[0]

        else:
            for i in range(len(self.conectors)):
                description += " " + self.terms[i] + " " + self.conectors[i]

            description += " " + self.terms[i+1]

        return description


class Table():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def get_description(self):
        return self.name