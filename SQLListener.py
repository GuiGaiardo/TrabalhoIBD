# Generated from SQL.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SQLParser import SQLParser
else:
    from TrabalhoIBD.SQLParser import SQLParser

# This class defines a complete listener for a parse tree produced by SQLParser.
class SQLListener(ParseTreeListener):

    # Enter a parse tree produced by SQLParser#sql_expr.
    def enterSql_expr(self, ctx:SQLParser.Sql_exprContext):
        pass

    # Exit a parse tree produced by SQLParser#sql_expr.
    def exitSql_expr(self, ctx:SQLParser.Sql_exprContext):
        pass


    # Enter a parse tree produced by SQLParser#clausulaSelect.
    def enterClausulaSelect(self, ctx:SQLParser.ClausulaSelectContext):
        pass

    # Exit a parse tree produced by SQLParser#clausulaSelect.
    def exitClausulaSelect(self, ctx:SQLParser.ClausulaSelectContext):
        pass


