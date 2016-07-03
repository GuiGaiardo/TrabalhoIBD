

class QueryTree():
    def __init__(self):
        self.root = None
        self.valid = True
        self.errors = []
        return

    def set_root(self, node):
        self.root = node

    def set_error(self, error):
        self.errors.append([error])




class SelectionNode():
    def __init__(self, terms, conectors):
        self.terms = terms
        self.conectors = conectors
        self.children = None



    def __str__(self):
        text = "S"
        if (len(self.terms) == 1):
            text += " " + self.terms[0][0] + self.terms[0][1] + self.terms[0][2]

        else:
            for i in range(len(self.conectors)):
                text += " " + self.terms[i][0] + self.terms[i][1] + self.terms[i][2] + " " + self.conectors[i]

            text += " " + self.terms[i+1][0] + self.terms[i+1][1] + self.terms[i+1][2]

        text += " (" + str(self.children) + ")"

        return text



    def get_description(self):
        description = "S("

        if (len(self.terms) == 1):
            description += self.terms[0][0] + self.terms[0][1] + self.terms[0][2]

        else:
            for i in range(len(self.conectors)):
                description += " " + self.terms[i][0] + self.terms[i][1] + self.terms[i][2] + " " + self.conectors[i]

            description += " " + self.terms[i+1][0] + self.terms[i+1][1] + self.terms[i+1][2]
        description += ")"
        
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
        description = "P(" + self.columns[0]
        for column in self.columns[1:]:
            description += ", " + column
        description += ")"

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

        elif (len(self.terms) == 1):
            text += " |X|"
            text += " " + self.terms[0][0] + self.terms[0][1] + self.terms[0][2]

        else:
            text += " |X|"
            for i in range(len(self.conectors)):
                text += " " + self.terms[i][0] + self.terms[i][1] + self.terms[i][2] + " " + self.conectors[i]

            text += " " + self.terms[i+1][0] + self.terms[i+1][1] + self.terms[i+1][2]

        text += " (" + str(self.children[1]) + ")"

        return text


    def get_description(self):
        text = ""

        if (self.terms[0] == ','):
            text += "X"

        elif (len(self.terms) == 1):
            text += " " + self.terms[0][0] + self.terms[0][1] + self.terms[0][2]

        else:
            for i in range(len(self.conectors)):
                text += " " + self.terms[i][0] + self.terms[i][1] + self.terms[i][2] + " " + self.conectors[i]

            text += " " + self.terms[i + 1][0] + self.terms[i + 1][1] + self.terms[i + 1][2]

        return text


class Table():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def get_description(self):
        return self.name