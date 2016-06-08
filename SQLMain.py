import sys

from SQLLexer import SQLLexer
from SQLParser import SQLParser
from antlr4 import *

from TrabalhoIBD.SQLListener import SQLListener

# from SQL.SQLListener import

class KeyPrinter(SQLListener):
    # Enter a parse tree produced by SQLParser#sql_expr.
    def enterSql_expr(self, ctx: SQLParser.Sql_exprContext):
        pass

    # Exit a parse tree produced by SQLParser#sql_expr.
    def exitSql_expr(self, ctx: SQLParser.Sql_exprContext):
        print("Bla")
        pass


def main(argv):
    input = FileStream(argv[1])
    lexer = SQLLexer(input)
    stream = CommonTokenStream(lexer)
    parser = SQLParser(stream)
    tree = parser.sql_expr()
    printer = KeyPrinter()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)


#
# print("\n\n")
# print(tree.getChildCount())
#
# print("\n\n")

# visitor = MyVisitor()
# visitor.visit(tree)


if __name__ == '__main__':
    main(sys.argv)
