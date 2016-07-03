import sys

from SQL_Parser.SQLLexer import SQLLexer
from antlr4 import *
from antlr4.Parser import DefaultErrorStrategy





from SQL_Parser.SQLParser import *
from SQL_Parser.SQLListener import SQLListener
# from SQLLexer import SQLLexer
# from antlr4 import *
# from SQLParser import *
# from SQLListener import SQLListener

class ERol(DefaultErrorStrategy):
    def recover(self, recognizer, e):
        query_tree.valid = False
        return super(ERol, self).recover(recognizer, e)

    def recoverInline(self, recognizer):
        query_tree.valid = False
        return super(ERol, self).recoverInline(recognizer)

    def sync(self, recognizer):
        super(ERol, self).sync(recognizer)


class KeyPrinter(SQLListener):
    # Enter a parse tree produced by SQLParser#sql_expr.
    def enterSql_expr(self, ctx: SQLParser.Sql_exprContext):
        pass

    # Exit a parse tree produced by SQLParser#sql_expr.
    def exitSql_expr(self, ctx: SQLParser.Sql_exprContext):
        pass


def main(input):
    with open("tmp", "w") as input_file:
        input_file.write(input)

    query_tree.valid = True
    input_file = FileStream("tmp")
    lexer = SQLLexer(input_file)
    stream = CommonTokenStream(lexer)
    parser = SQLParser(stream)
    parser._errHandler = ERol()
    tree = parser.sql_expr()
    printer = KeyPrinter()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    if(not query_tree.valid):
        query_tree.set_root(None)

    return query_tree


#
# print("\n\n")
# print(tree.getChildCount())
#
# print("\n\n")

# visitor = MyVisitor()
# visitor.visit(tree)


if __name__ == '__main__':
    main(sys.argv)
