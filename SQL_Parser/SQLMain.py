import sys

from SQL_Parser.SQLLexer import SQLLexer
from antlr4 import *

from SQL_Parser.SQLParser import *
from SQL_Parser.SQLListener import SQLListener


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
    input_file = FileStream("tmp")
    lexer = SQLLexer(input_file)
    stream = CommonTokenStream(lexer)
    parser = SQLParser(stream)
    tree = parser.sql_expr()
    printer = KeyPrinter()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

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
