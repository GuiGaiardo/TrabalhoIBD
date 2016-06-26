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
    pos_y = 100


    def draw_tree(self):
        self.size_hint = (1, 1.3)
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


#
# import kivy
# kivy.require('1.9.1')
#
# from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.button import Button
# from kivy.properties import ObjectProperty
# from SQL_Parser.QueryTree import *
# from kivy.graphics import Color, Rectangle
#
#
#
# class TreePrinter(FloatLayout):
#     query_tree = ObjectProperty(None)
#     close = ObjectProperty(None)
#
#     def __make_node_widget(self, description, level, right, divisions):
#         bt = Button(text=description, pos_hint={'top': 1-level*(.05), 'right': right}, size_hint=(1/(2**divisions), 0.05))
#         bt.text_size_hint = bt.size_hint
#         return bt
#
#     def __make_box_widget(self, widget, level, right):
#         v_box1 = FloatLayout(pos_hint={'top': 1-((level+1)*0.1), 'right': 0.25}, size_hint=(0.5,1-((level+1)*0.1)))
#         v_box2 = FloatLayout(pos_hint={'top': 1-((level+1)*0.1), 'right': 0.75}, size_hint=(0.5, 1 - ((level + 1) * 0.1)))
#         v_box1.add_widget(Button(text="1"))
#         bt = Button(text="2")
#         bt.pos = (bt.pos[0] + 200, bt.pos[1])
#         v_box2.add_widget(bt)
#
#         widget.add_widget(v_box1)
#         widget.add_widget(v_box2)
#
#         return v_box1, v_box2
#
#     def draw_tree(self):
#         self.size_hint = (None, None)
#         root = self.query_tree.root
#         print(self.size)
#         print(self.pos)
#         print(self.pos_hint)
#         # self.add_widget(Button(text="Teste", pos_hint={'top': 1-0*(.1), 'right': 1}, size_hint=(1, 0.1)))
#         self._draw_tree(root, self, 0, 1, 0)
#
#     def _draw_tree(self, node, widget, level, right, divisions):
#         if isinstance(node, ProjectionNode):
#             button = self.__make_node_widget(node.get_description(), level, right, divisions)
#             widget.add_widget(button)
#             print(node.get_description(), "| ", node.children)
#             self._draw_tree(node.children, widget, level+1, right, divisions)
#
#         elif isinstance(node, SelectionNode):
#             button = self.__make_node_widget(node.get_description(), level)
#             print(node.get_description(), "| ", node.children)
#             widget.add_widget(button)
#             self._draw_tree(node.children,widget, level+1, right, divisions)
#
#         elif isinstance(node, ThetaJoinNode):
#             button = self.__make_node_widget(node.get_description(), level, right, divisions)
#             widget.add_widget(button)
#             # box1, box2 = self.__make_box_widget(widget, level, right, divisions)
#             level += 1
#             #recursao pro filho da esquerda
#             print(node.get_description(), "|", node.children[0], "|", node.children[1])
#             self._draw_tree(node.children[0], widget, level, right-1/(2**(divisions+1)), divisions+1)
#             #recursao pro filho da direita
#             self._draw_tree(node.children[1], widget, level, right, divisions+1)
#
#         elif isinstance(node, Table):
#             button = self.__make_node_widget(node.get_description(), level, right, divisions)
#             widget.add_widget(button)
#
#         else:
#             print("Erro ao desenhar a arvore")
#
#         return
