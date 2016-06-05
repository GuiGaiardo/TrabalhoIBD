import kivy
kivy.require('1.0.6')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

import os


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
        #faz as analises
        try:
            #query_tree = QueryChecker(self.text_input.text)
            self.is_valid = True
        except QueryLexicalError:
            self.is_valid = False
            #msg de erro lexico
        except QuerySyntaxError:
            self.is_valid = False


    def show_tree(self):
        if self.is_valid:
            pass
            #show tree

    def show_optimized_tree(self):
        if self.is_valid:
            pass
            #optimize and show




class QueryTree(App):
    pass



Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)

if __name__ == '__main__':
    QueryTree().run()