import kivy
from kivy.uix.floatlayout import FloatLayout

import SQL_Parser

kivy.require('1.9.1')

from kivy.uix.label import Label
from kivy.properties import ObjectProperty


class TreePrinter(FloatLayout):

    query_tree = ObjectProperty(None)
    close = ObjectProperty(None)
    pos_x = -50
    pos_y = 250

    def draw_tree(self):

        node = self.query_tree.root
        self.draw_node(node)

    def draw_node(self, node):

        if type(node) is SQL_Parser.QueryTree.ProjectionNode:

            lbl = Label(text="P", pos=(self.pos_x, self.pos_y))
            terms = Label(text=node.get_description(), pos=(self.pos_x, self.pos_y - 15))
            separator = Label(text="|", pos=(self.pos_x, self.pos_y - 45))
            separator.font_size = 36
            self.add_widget(separator)
            terms.font_size = 12
            self.add_widget(lbl)
            self.add_widget(terms)
            self.pos_y -= 80
            self.draw_node(node.children)
            self.pos_y += 80

        elif type(node) is SQL_Parser.QueryTree.SelectionNode:

            lbl = Label(text="S", pos=(self.pos_x, self.pos_y))
            terms = Label(text=node.get_description(), pos=(self.pos_x, self.pos_y - 15))
            separator = Label(text="|", pos=(self.pos_x, self.pos_y - 45))
            separator.font_size = 36
            terms.font_size = 12
            self.add_widget(separator)
            self.add_widget(lbl)
            self.add_widget(terms)
            self.pos_y -= 80
            self.draw_node(node.children)
            self.pos_y += 80

        elif type(node) is SQL_Parser.QueryTree.ThetaJoinNode:

            if node.get_description() == "X":
                lbl = Label(text=node.get_description(), pos=(self.pos_x, self.pos_y))
            else:
                lbl = Label(text="|X|", pos=(self.pos_x, self.pos_y))
                terms = Label(text=node.get_description(), pos=(self.pos_x, self.pos_y - 15))
                terms.font_size = 12
                self.add_widget(terms)

            separator = Label(text='__________________', pos=(self.pos_x, self.pos_y - 45))
            separator.font_size = 36
            self.add_widget(separator)
            separator2 = Label(text='|', pos=(self.pos_x, self.pos_y - 35))
            separator2.font_size = 36
            self.add_widget(separator2)
            self.add_widget(lbl)
            self.pos_x -= 145
            self.pos_y -= 80
            separator3 = Label(text='|', pos=(self.pos_x, self.pos_y + 15))
            separator3.font_size = 18
            self.add_widget(separator3)
            self.draw_node(node.children[0])
            self.pos_x += 289
            separator4 = Label(text='|', pos=(self.pos_x, self.pos_y + 15))
            separator4.font_size = 18
            self.add_widget(separator4)
            self.draw_node(node.children[1])
            self.pos_x -= 145
            self.pos_y += 80

        elif type(node) is SQL_Parser.QueryTree.Table:

            lbl = Label(text=node.get_description(), pos=(self.pos_x, self.pos_y))
            self.add_widget(lbl)