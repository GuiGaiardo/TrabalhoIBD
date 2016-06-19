import kivy
kivy.require('1.9.1')

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty


class TreePrinter(BoxLayout):
    query_tree = ObjectProperty(None)
    close = ObjectProperty(None)

#CHEIO DE COISA INUTIL, NAO LEVAR EM CONSIDERACAO
    def draw_tree(self):
        node = self.query_tree.root
        lbl = Label(text=node.get_description())
        self.add_widget(lbl)

        node = node.children
        lbl2 = Label(text=node.get_description())
        self.add_widget(lbl2)

        node = node.children
        lblx = Label(text=node.get_description())
        self.add_widget(lblx)

        child1 = node.children[0]
        child2 = node.children[1]
        lbl3 = Label(text=child1.get_description())
        self.add_widget(lbl3)

        lbl4 = Label(text=child2.get_description())
        self.add_widget(lbl4)