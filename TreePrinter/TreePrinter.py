import kivy
kivy.require('1.9.1')

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from SQL_Parser.QueryTree import *
from kivy.graphics import Color, Rectangle



class TreePrinter(FloatLayout):
    query_tree = ObjectProperty(None)
    close = ObjectProperty(None)

    def __make_node_widget(self, description, level, right, divisions):
        bt = Button(text=description, pos_hint={'top': 1-level*(.1), 'right': right}, size_hint=(1/(2**divisions), 0.1))
        return bt

    def __make_box_widget(self, widget, level, right):
        v_box1 = FloatLayout(pos_hint={'top': 1-((level+1)*0.1), 'right': 0.25}, size_hint=(0.5,1-((level+1)*0.1)))
        v_box2 = FloatLayout(pos_hint={'top': 1-((level+1)*0.1), 'right': 0.75}, size_hint=(0.5, 1 - ((level + 1) * 0.1)))
        v_box1.add_widget(Button(text="1"))
        bt = Button(text="2")
        bt.pos = (bt.pos[0] + 200, bt.pos[1])
        v_box2.add_widget(bt)

        widget.add_widget(v_box1)
        widget.add_widget(v_box2)

        return v_box1, v_box2

    def draw_tree(self):
        root = self.query_tree.root
        print(self.size)
        print(self.pos)
        print(self.pos_hint)
        # self.add_widget(Button(text="Teste", pos_hint={'top': 1-0*(.1), 'right': 1}, size_hint=(1, 0.1)))
        self._draw_tree(root, self, 0, 1, 0)

    def _draw_tree(self, node, widget, level, right, divisions):
        if isinstance(node, ProjectionNode):
            button = self.__make_node_widget(node.get_description(), level, right, divisions)
            widget.add_widget(button)
            print(node.get_description(), "| ", node.children)
            self._draw_tree(node.children, widget, level+1, right, divisions)

        elif isinstance(node, SelectionNode):
            button = self.__make_node_widget(node.get_description(), level)
            print(node.get_description(), "| ", node.children)
            widget.add_widget(button)
            self._draw_tree(node.children,widget, level+1, right, divisions)

        elif isinstance(node, ThetaJoinNode):
            button = self.__make_node_widget(node.get_description(), level, right, divisions)
            widget.add_widget(button)
            # box1, box2 = self.__make_box_widget(widget, level, right, divisions)
            level += 1
            #recursao pro filho da esquerda
            print(node.get_description(), "|", node.children[0], "|", node.children[1])
            self._draw_tree(node.children[0], widget, level, right-1/(2**(divisions+1)), divisions+1)
            #recursao pro filho da direita
            self._draw_tree(node.children[1], widget, level, right, divisions+1)

        elif isinstance(node, Table):
            button = self.__make_node_widget(node.get_description(), level, right, divisions)
            widget.add_widget(button)

        else:
            print("Erro ao desenhar a arvore")

        return
