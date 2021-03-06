# Generated from SQL.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SQLParser import SQLParser
else:
    from SQLParser import SQLParser

from SQL_Parser.QueryTree import *
query_tree = QueryTree()


# This class defines a complete generic visitor for a parse tree produced by SQLParser.

class SQLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SQLParser#sql_expr.
    def visitSql_expr(self, ctx:SQLParser.Sql_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#comparisonOp.
    def visitComparisonOp(self, ctx:SQLParser.ComparisonOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#conditionsWhere.
    def visitConditionsWhere(self, ctx:SQLParser.ConditionsWhereContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#where.
    def visitWhere(self, ctx:SQLParser.WhereContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#clausulaSelect.
    def visitClausulaSelect(self, ctx:SQLParser.ClausulaSelectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#conditionsJoin.
    def visitConditionsJoin(self, ctx:SQLParser.ConditionsJoinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#joins.
    def visitJoins(self, ctx:SQLParser.JoinsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#joins_.
    def visitJoins_(self, ctx:SQLParser.Joins_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#clausulaFrom.
    def visitClausulaFrom(self, ctx:SQLParser.ClausulaFromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#termo.
    def visitTermo(self, ctx:SQLParser.TermoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#conector.
    def visitConector(self, ctx:SQLParser.ConectorContext):
        return self.visitChildren(ctx)



del SQLParser