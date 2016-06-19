# Generated from SQL.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SQLParser import SQLParser
else:
    from SQLParser import SQLParser

from SQL_Parser.QueryTree import *
query_tree = QueryTree()


# This class defines a complete listener for a parse tree produced by SQLParser.
class SQLListener(ParseTreeListener):

    # Enter a parse tree produced by SQLParser#sql_expr.
    def enterSql_expr(self, ctx:SQLParser.Sql_exprContext):
        pass

    # Exit a parse tree produced by SQLParser#sql_expr.
    def exitSql_expr(self, ctx:SQLParser.Sql_exprContext):
        pass


    # Enter a parse tree produced by SQLParser#comparisonOp.
    def enterComparisonOp(self, ctx:SQLParser.ComparisonOpContext):
        pass

    # Exit a parse tree produced by SQLParser#comparisonOp.
    def exitComparisonOp(self, ctx:SQLParser.ComparisonOpContext):
        pass


    # Enter a parse tree produced by SQLParser#conditionsWhere.
    def enterConditionsWhere(self, ctx:SQLParser.ConditionsWhereContext):
        pass

    # Exit a parse tree produced by SQLParser#conditionsWhere.
    def exitConditionsWhere(self, ctx:SQLParser.ConditionsWhereContext):
        pass


    # Enter a parse tree produced by SQLParser#where.
    def enterWhere(self, ctx:SQLParser.WhereContext):
        pass

    # Exit a parse tree produced by SQLParser#where.
    def exitWhere(self, ctx:SQLParser.WhereContext):
        pass


    # Enter a parse tree produced by SQLParser#clausulaSelect.
    def enterClausulaSelect(self, ctx:SQLParser.ClausulaSelectContext):
        pass

    # Exit a parse tree produced by SQLParser#clausulaSelect.
    def exitClausulaSelect(self, ctx:SQLParser.ClausulaSelectContext):
        pass


    # Enter a parse tree produced by SQLParser#conditionsJoin.
    def enterConditionsJoin(self, ctx:SQLParser.ConditionsJoinContext):
        pass

    # Exit a parse tree produced by SQLParser#conditionsJoin.
    def exitConditionsJoin(self, ctx:SQLParser.ConditionsJoinContext):
        pass


    # Enter a parse tree produced by SQLParser#joins.
    def enterJoins(self, ctx:SQLParser.JoinsContext):
        pass

    # Exit a parse tree produced by SQLParser#joins.
    def exitJoins(self, ctx:SQLParser.JoinsContext):
        pass


    # Enter a parse tree produced by SQLParser#joins_.
    def enterJoins_(self, ctx:SQLParser.Joins_Context):
        pass

    # Exit a parse tree produced by SQLParser#joins_.
    def exitJoins_(self, ctx:SQLParser.Joins_Context):
        pass


    # Enter a parse tree produced by SQLParser#clausulaFrom.
    def enterClausulaFrom(self, ctx:SQLParser.ClausulaFromContext):
        pass

    # Exit a parse tree produced by SQLParser#clausulaFrom.
    def exitClausulaFrom(self, ctx:SQLParser.ClausulaFromContext):
        pass


    # Enter a parse tree produced by SQLParser#termo.
    def enterTermo(self, ctx:SQLParser.TermoContext):
        pass

    # Exit a parse tree produced by SQLParser#termo.
    def exitTermo(self, ctx:SQLParser.TermoContext):
        pass


    # Enter a parse tree produced by SQLParser#conector.
    def enterConector(self, ctx:SQLParser.ConectorContext):
        pass

    # Exit a parse tree produced by SQLParser#conector.
    def exitConector(self, ctx:SQLParser.ConectorContext):
        pass


