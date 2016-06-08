# Generated from teste.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .testeParser import testeParser
else:
    from TrabalhoIBD.testeParser import testeParser

# This class defines a complete listener for a parse tree produced by testeParser.
class testeListener(ParseTreeListener):

    # Enter a parse tree produced by testeParser#algebra_expr.
    def enterAlgebra_expr(self, ctx:testeParser.Algebra_exprContext):
        pass

    # Exit a parse tree produced by testeParser#algebra_expr.
    def exitAlgebra_expr(self, ctx:testeParser.Algebra_exprContext):
        pass


    # Enter a parse tree produced by testeParser#tabela.
    def enterTabela(self, ctx:testeParser.TabelaContext):
        pass

    # Exit a parse tree produced by testeParser#tabela.
    def exitTabela(self, ctx:testeParser.TabelaContext):
        pass


    # Enter a parse tree produced by testeParser#coluna.
    def enterColuna(self, ctx:testeParser.ColunaContext):
        pass

    # Exit a parse tree produced by testeParser#coluna.
    def exitColuna(self, ctx:testeParser.ColunaContext):
        pass


    # Enter a parse tree produced by testeParser#condProjecao.
    def enterCondProjecao(self, ctx:testeParser.CondProjecaoContext):
        pass

    # Exit a parse tree produced by testeParser#condProjecao.
    def exitCondProjecao(self, ctx:testeParser.CondProjecaoContext):
        pass


    # Enter a parse tree produced by testeParser#projecao.
    def enterProjecao(self, ctx:testeParser.ProjecaoContext):
        pass

    # Exit a parse tree produced by testeParser#projecao.
    def exitProjecao(self, ctx:testeParser.ProjecaoContext):
        pass


    # Enter a parse tree produced by testeParser#t_s.
    def enterT_s(self, ctx:testeParser.T_sContext):
        pass

    # Exit a parse tree produced by testeParser#t_s.
    def exitT_s(self, ctx:testeParser.T_sContext):
        pass


    # Enter a parse tree produced by testeParser#condSelecao.
    def enterCondSelecao(self, ctx:testeParser.CondSelecaoContext):
        pass

    # Exit a parse tree produced by testeParser#condSelecao.
    def exitCondSelecao(self, ctx:testeParser.CondSelecaoContext):
        pass


    # Enter a parse tree produced by testeParser#selecao.
    def enterSelecao(self, ctx:testeParser.SelecaoContext):
        pass

    # Exit a parse tree produced by testeParser#selecao.
    def exitSelecao(self, ctx:testeParser.SelecaoContext):
        pass


    # Enter a parse tree produced by testeParser#t_theta.
    def enterT_theta(self, ctx:testeParser.T_thetaContext):
        pass

    # Exit a parse tree produced by testeParser#t_theta.
    def exitT_theta(self, ctx:testeParser.T_thetaContext):
        pass


    # Enter a parse tree produced by testeParser#condJuncaoTheta.
    def enterCondJuncaoTheta(self, ctx:testeParser.CondJuncaoThetaContext):
        pass

    # Exit a parse tree produced by testeParser#condJuncaoTheta.
    def exitCondJuncaoTheta(self, ctx:testeParser.CondJuncaoThetaContext):
        pass


    # Enter a parse tree produced by testeParser#comparison_op.
    def enterComparison_op(self, ctx:testeParser.Comparison_opContext):
        pass

    # Exit a parse tree produced by testeParser#comparison_op.
    def exitComparison_op(self, ctx:testeParser.Comparison_opContext):
        pass


    # Enter a parse tree produced by testeParser#boolean_op.
    def enterBoolean_op(self, ctx:testeParser.Boolean_opContext):
        pass

    # Exit a parse tree produced by testeParser#boolean_op.
    def exitBoolean_op(self, ctx:testeParser.Boolean_opContext):
        pass


