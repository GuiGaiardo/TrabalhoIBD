# Generated from teste.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .testeParser import testeParser
else:
    from TrabalhoIBD.testeParser import testeParser

# This class defines a complete generic visitor for a parse tree produced by testeParser.

class testeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by testeParser#algebra_expr.
    def visitAlgebra_expr(self, ctx:testeParser.Algebra_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by testeParser#tabela.
    def visitTabela(self, ctx:testeParser.TabelaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by testeParser#coluna.
    def visitColuna(self, ctx:testeParser.ColunaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by testeParser#condProjecao.
    def visitCondProjecao(self, ctx:testeParser.CondProjecaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by testeParser#projecao.
    def visitProjecao(self, ctx:testeParser.ProjecaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by testeParser#t_s.
    def visitT_s(self, ctx:testeParser.T_sContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by testeParser#condSelecao.
    def visitCondSelecao(self, ctx:testeParser.CondSelecaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by testeParser#selecao.
    def visitSelecao(self, ctx:testeParser.SelecaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by testeParser#t_theta.
    def visitT_theta(self, ctx:testeParser.T_thetaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by testeParser#condJuncaoTheta.
    def visitCondJuncaoTheta(self, ctx:testeParser.CondJuncaoThetaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by testeParser#comparison_op.
    def visitComparison_op(self, ctx:testeParser.Comparison_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by testeParser#boolean_op.
    def visitBoolean_op(self, ctx:testeParser.Boolean_opContext):
        return self.visitChildren(ctx)



del testeParser