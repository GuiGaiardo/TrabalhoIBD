import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
import os

from TreePrinter import TreePrinter
from SQL_Parser import SQLMain
from Optimization.SelectionOptmizer import *
from Optimization.ProjectionOptimizer import *

kivy.require('1.9.1')


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class Root(FloatLayout):
    loadfile = ObjectProperty(None)
    text_input = ObjectProperty(None)
    is_valid = False

    def dismiss_popup(self):
        self._popup.dismiss()



    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.75, 0.75))
        self._popup.open()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            self.text_input.text = stream.read()

        self.dismiss_popup()

    def parse_query(self):
        tree = SQLMain.main(self.text_input.text)
        if not tree.root:
            self.tree = None
            self.is_valid = False
        else:
            self.is_valid = True
            self.tree = tree
            print(str(tree.root))

    def show_tree(self):
        if self.is_valid:
            printer = TreePrinter.TreePrinter(query_tree=self.tree, close=self.dismiss_popup)
            printer.draw_tree()
            self._popup = Popup(title="Query Tree", content=printer)
            self._popup.open()

    def show_optimized_tree(self):
        if self.is_valid:
            optimized_tree = self.tree
            self.parse_query()
            s = SelectionOptimizer(optimized_tree)
            optimized_tree.root = s.optimize()
            p = ProjectionOptimizer(optimized_tree)
            optimized_tree.root = p.optimize()
            printer = TreePrinter.TreePrinter(query_tree=optimized_tree, close=self.dismiss_popup)
            printer.draw_tree()
            self._popup = Popup(title="Optimized Query Tree", content=printer)
            self._popup.open()



class QueryTree(App):
    pass


Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)
Factory.register('TreePrinter', cls=TreePrinter)

if __name__ == '__main__':
    QueryTree().run()
