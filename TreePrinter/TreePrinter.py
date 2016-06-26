import kivy
kivy.require('1.9.1')

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from SQL_Parser.QueryTree import *

class TreePrinter(FloatLayout):
    query_tree = ObjectProperty(None)
    close = ObjectProperty(None)

    def __make_node_widget(self, description, level):
        bt = Button(text=description, pos_hint={'top': 1-level*(.1)}, size_hint=(1, 0.1))
        return bt

    def __make_box_widget(self, level):
        v_box1 = FloatLayout(pos_hint={'top': 1-((level+1)*0.1), 'right': 1}, size_hint=(0.5,1-((level+1)*0.1)))
        v_box2 = FloatLayout(pos_hint={'top': 1-((level+1)*0.1), 'right': 0.5}, size_hint=(0.5,1-((level+1)*0.1)))
        self.add_widget(v_box1)
        self.add_widget(v_box2)

        return v_box1, v_box2

    def draw_tree(self):
        root = self.query_tree.root
        self._draw_tree(root, self, 0)


    def _draw_tree(self, node, widget, level):
        if isinstance(node, ProjectionNode):
            button = self.__make_node_widget(node.get_description(), level)
            widget.add_widget(button)
            self._draw_tree(node.children, widget, level+1)

        elif isinstance(node, SelectionNode):
            button = self.__make_node_widget(node.get_description(), level)
            widget.add_widget(button)
            self._draw_tree(node.children,widget, level+1)

        elif isinstance(node, ThetaJoinNode):
            button = self.__make_node_widget(node.get_description(), level)
            widget.add_widget(button)
            box1, box2 = self.__make_box_widget(level)
            level += 1
            #recursao pro filho da esquerda
            self._draw_tree(node.children[0], box1, 0)
            #recursao pro filho da direita
            self._draw_tree(node.children[1], box2, 0)

        elif isinstance(node, Table):
            button = self.__make_node_widget(node.get_description(), level)
            widget.add_widget(button)

        else:
            print("Erro ao desenhar a arvore")

        return
