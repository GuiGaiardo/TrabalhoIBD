import sys

from SQLLexer import SQLLexer
from antlr4 import *

from SQLParser import *
from SQLListener import SQLListener

# from SQL.SQLListener import

class KeyPrinter(SQLListener):
    # Enter a parse tree produced by SQLParser#sql_expr.
    def enterSql_expr(self, ctx: SQLParser.Sql_exprContext):
        pass

    # Exit a parse tree produced by SQLParser#sql_expr.
    def exitSql_expr(self, ctx: SQLParser.Sql_exprContext):
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

    print(str(query_tree.root))


#
# print("\n\n")
# print(tree.getChildCount())
#
# print("\n\n")

# visitor = MyVisitor()
# visitor.visit(tree)


if __name__ == '__main__':
    main(sys.argv)
