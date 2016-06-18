# Generated from teste.g4 by ANTLR 4.5.3
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\17")
        buf.write("W\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\5\2\"\n\2\3\3\3\3\3\4\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\3\5\3\5\5\5/\n\5\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\5\b@\n\b\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3")
        buf.write("\13\5\13Q\n\13\3\f\3\f\3\r\3\r\3\r\2\2\16\2\4\6\b\n\f")
        buf.write("\16\20\22\24\26\30\2\2P\2!\3\2\2\2\4#\3\2\2\2\6%\3\2\2")
        buf.write("\2\b.\3\2\2\2\n\60\3\2\2\2\f\66\3\2\2\2\16?\3\2\2\2\20")
        buf.write("A\3\2\2\2\22G\3\2\2\2\24P\3\2\2\2\26R\3\2\2\2\30T\3\2")
        buf.write("\2\2\32\"\5\20\t\2\33\34\7\3\2\2\34\35\5\2\2\2\35\36\7")
        buf.write("\4\2\2\36\"\3\2\2\2\37\"\5\n\6\2 \"\5\4\3\2!\32\3\2\2")
        buf.write("\2!\33\3\2\2\2!\37\3\2\2\2! \3\2\2\2\"\3\3\2\2\2#$\7\16")
        buf.write("\2\2$\5\3\2\2\2%&\5\4\3\2&\'\7\5\2\2\'(\7\16\2\2(\7\3")
        buf.write("\2\2\2)/\5\6\4\2*+\5\6\4\2+,\7\6\2\2,-\5\b\5\2-/\3\2\2")
        buf.write("\2.)\3\2\2\2.*\3\2\2\2/\t\3\2\2\2\60\61\7\7\2\2\61\62")
        buf.write("\5\b\5\2\62\63\7\3\2\2\63\64\5\2\2\2\64\65\7\4\2\2\65")
        buf.write("\13\3\2\2\2\66\67\5\6\4\2\678\5\26\f\289\5\6\4\29\r\3")
        buf.write("\2\2\2:;\5\f\7\2;<\5\30\r\2<=\5\16\b\2=@\3\2\2\2>@\5\f")
        buf.write("\7\2?:\3\2\2\2?>\3\2\2\2@\17\3\2\2\2AB\7\b\2\2BC\5\16")
        buf.write("\b\2CD\7\3\2\2DE\5\2\2\2EF\7\4\2\2F\21\3\2\2\2GH\5\6\4")
        buf.write("\2HI\7\13\2\2IJ\5\6\4\2J\23\3\2\2\2KQ\5\22\n\2LM\5\22")
        buf.write("\n\2MN\7\r\2\2NO\5\24\13\2OQ\3\2\2\2PK\3\2\2\2PL\3\2\2")
        buf.write("\2Q\25\3\2\2\2RS\7\n\2\2S\27\3\2\2\2TU\7\f\2\2U\31\3\2")
        buf.write("\2\2\6!.?P")
        return buf.getvalue()


class testeParser ( Parser ):

    grammarFileName = "teste.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'.'", "','", "'P'", "'S'", 
                     "<INVALID>", "<INVALID>", "'='", "<INVALID>", "'and'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NEWLINE", 
                      "COMPARISON_OP", "EQUAL", "BOOLEAN_OP", "AND", "ID", 
                      "WS" ]

    RULE_algebra_expr = 0
    RULE_tabela = 1
    RULE_coluna = 2
    RULE_condProjecao = 3
    RULE_projecao = 4
    RULE_t_s = 5
    RULE_condSelecao = 6
    RULE_selecao = 7
    RULE_t_theta = 8
    RULE_condJuncaoTheta = 9
    RULE_comparison_op = 10
    RULE_boolean_op = 11

    ruleNames =  [ "algebra_expr", "tabela", "coluna", "condProjecao", "projecao", 
                   "t_s", "condSelecao", "selecao", "t_theta", "condJuncaoTheta", 
                   "comparison_op", "boolean_op" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    NEWLINE=7
    COMPARISON_OP=8
    EQUAL=9
    BOOLEAN_OP=10
    AND=11
    ID=12
    WS=13

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class Algebra_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def selecao(self):
            return self.getTypedRuleContext(testeParser.SelecaoContext,0)


        def algebra_expr(self):
            return self.getTypedRuleContext(testeParser.Algebra_exprContext,0)


        def projecao(self):
            return self.getTypedRuleContext(testeParser.ProjecaoContext,0)


        def tabela(self):
            return self.getTypedRuleContext(testeParser.TabelaContext,0)


        def getRuleIndex(self):
            return testeParser.RULE_algebra_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlgebra_expr" ):
                listener.enterAlgebra_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlgebra_expr" ):
                listener.exitAlgebra_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlgebra_expr" ):
                return visitor.visitAlgebra_expr(self)
            else:
                return visitor.visitChildren(self)




    def algebra_expr(self):

        localctx = testeParser.Algebra_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_algebra_expr)
        try:
            self.state = 31
            token = self._input.LA(1)
            if token in [testeParser.T__5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.selecao()

            elif token in [testeParser.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.match(testeParser.T__0)
                self.state = 26
                self.algebra_expr()
                self.state = 27
                self.match(testeParser.T__1)

            elif token in [testeParser.T__4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 29
                self.projecao()

            elif token in [testeParser.ID]:
                self.enterOuterAlt(localctx, 4)
                self.state = 30
                self.tabela()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TabelaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(testeParser.ID, 0)

        def getRuleIndex(self):
            return testeParser.RULE_tabela

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTabela" ):
                listener.enterTabela(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTabela" ):
                listener.exitTabela(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTabela" ):
                return visitor.visitTabela(self)
            else:
                return visitor.visitChildren(self)




    def tabela(self):

        localctx = testeParser.TabelaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_tabela)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(testeParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ColunaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tabela(self):
            return self.getTypedRuleContext(testeParser.TabelaContext,0)


        def ID(self):
            return self.getToken(testeParser.ID, 0)

        def getRuleIndex(self):
            return testeParser.RULE_coluna

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColuna" ):
                listener.enterColuna(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColuna" ):
                listener.exitColuna(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColuna" ):
                return visitor.visitColuna(self)
            else:
                return visitor.visitChildren(self)




    def coluna(self):

        localctx = testeParser.ColunaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_coluna)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.tabela()
            self.state = 36
            self.match(testeParser.T__2)
            self.state = 37
            self.match(testeParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CondProjecaoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def coluna(self):
            return self.getTypedRuleContext(testeParser.ColunaContext,0)


        def condProjecao(self):
            return self.getTypedRuleContext(testeParser.CondProjecaoContext,0)


        def getRuleIndex(self):
            return testeParser.RULE_condProjecao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondProjecao" ):
                listener.enterCondProjecao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondProjecao" ):
                listener.exitCondProjecao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondProjecao" ):
                return visitor.visitCondProjecao(self)
            else:
                return visitor.visitChildren(self)




    def condProjecao(self):

        localctx = testeParser.CondProjecaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_condProjecao)
        try:
            self.state = 44
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.coluna()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.coluna()
                self.state = 41
                self.match(testeParser.T__3)
                self.state = 42
                self.condProjecao()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProjecaoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condProjecao(self):
            return self.getTypedRuleContext(testeParser.CondProjecaoContext,0)


        def algebra_expr(self):
            return self.getTypedRuleContext(testeParser.Algebra_exprContext,0)


        def getRuleIndex(self):
            return testeParser.RULE_projecao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProjecao" ):
                listener.enterProjecao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProjecao" ):
                listener.exitProjecao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProjecao" ):
                return visitor.visitProjecao(self)
            else:
                return visitor.visitChildren(self)




    def projecao(self):

        localctx = testeParser.ProjecaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_projecao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(testeParser.T__4)
            self.state = 47
            self.condProjecao()
            self.state = 48
            self.match(testeParser.T__0)
            self.state = 49
            self.algebra_expr()
            self.state = 50
            self.match(testeParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class T_sContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def coluna(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(testeParser.ColunaContext)
            else:
                return self.getTypedRuleContext(testeParser.ColunaContext,i)


        def comparison_op(self):
            return self.getTypedRuleContext(testeParser.Comparison_opContext,0)


        def getRuleIndex(self):
            return testeParser.RULE_t_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_s" ):
                listener.enterT_s(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_s" ):
                listener.exitT_s(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_s" ):
                return visitor.visitT_s(self)
            else:
                return visitor.visitChildren(self)




    def t_s(self):

        localctx = testeParser.T_sContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_t_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.coluna()
            self.state = 53
            self.comparison_op()
            self.state = 54
            self.coluna()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CondSelecaoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def t_s(self):
            return self.getTypedRuleContext(testeParser.T_sContext,0)


        def boolean_op(self):
            return self.getTypedRuleContext(testeParser.Boolean_opContext,0)


        def condSelecao(self):
            return self.getTypedRuleContext(testeParser.CondSelecaoContext,0)


        def getRuleIndex(self):
            return testeParser.RULE_condSelecao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondSelecao" ):
                listener.enterCondSelecao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondSelecao" ):
                listener.exitCondSelecao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondSelecao" ):
                return visitor.visitCondSelecao(self)
            else:
                return visitor.visitChildren(self)




    def condSelecao(self):

        localctx = testeParser.CondSelecaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_condSelecao)
        try:
            self.state = 61
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.t_s()
                self.state = 57
                self.boolean_op()
                self.state = 58
                self.condSelecao()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.t_s()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SelecaoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condSelecao(self):
            return self.getTypedRuleContext(testeParser.CondSelecaoContext,0)


        def algebra_expr(self):
            return self.getTypedRuleContext(testeParser.Algebra_exprContext,0)


        def getRuleIndex(self):
            return testeParser.RULE_selecao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelecao" ):
                listener.enterSelecao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelecao" ):
                listener.exitSelecao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelecao" ):
                return visitor.visitSelecao(self)
            else:
                return visitor.visitChildren(self)




    def selecao(self):

        localctx = testeParser.SelecaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_selecao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(testeParser.T__5)
            self.state = 64
            self.condSelecao()
            self.state = 65
            self.match(testeParser.T__0)
            self.state = 66
            self.algebra_expr()
            self.state = 67
            self.match(testeParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class T_thetaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def coluna(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(testeParser.ColunaContext)
            else:
                return self.getTypedRuleContext(testeParser.ColunaContext,i)


        def EQUAL(self):
            return self.getToken(testeParser.EQUAL, 0)

        def getRuleIndex(self):
            return testeParser.RULE_t_theta

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_theta" ):
                listener.enterT_theta(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_theta" ):
                listener.exitT_theta(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_theta" ):
                return visitor.visitT_theta(self)
            else:
                return visitor.visitChildren(self)




    def t_theta(self):

        localctx = testeParser.T_thetaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_t_theta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.coluna()
            self.state = 70
            self.match(testeParser.EQUAL)
            self.state = 71
            self.coluna()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CondJuncaoThetaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def t_theta(self):
            return self.getTypedRuleContext(testeParser.T_thetaContext,0)


        def AND(self):
            return self.getToken(testeParser.AND, 0)

        def condJuncaoTheta(self):
            return self.getTypedRuleContext(testeParser.CondJuncaoThetaContext,0)


        def getRuleIndex(self):
            return testeParser.RULE_condJuncaoTheta

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondJuncaoTheta" ):
                listener.enterCondJuncaoTheta(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondJuncaoTheta" ):
                listener.exitCondJuncaoTheta(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondJuncaoTheta" ):
                return visitor.visitCondJuncaoTheta(self)
            else:
                return visitor.visitChildren(self)




    def condJuncaoTheta(self):

        localctx = testeParser.CondJuncaoThetaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_condJuncaoTheta)
        try:
            self.state = 78
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.t_theta()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                self.t_theta()
                self.state = 75
                self.match(testeParser.AND)
                self.state = 76
                self.condJuncaoTheta()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Comparison_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMPARISON_OP(self):
            return self.getToken(testeParser.COMPARISON_OP, 0)

        def getRuleIndex(self):
            return testeParser.RULE_comparison_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison_op" ):
                listener.enterComparison_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison_op" ):
                listener.exitComparison_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison_op" ):
                return visitor.visitComparison_op(self)
            else:
                return visitor.visitChildren(self)




    def comparison_op(self):

        localctx = testeParser.Comparison_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_comparison_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(testeParser.COMPARISON_OP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Boolean_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN_OP(self):
            return self.getToken(testeParser.BOOLEAN_OP, 0)

        def getRuleIndex(self):
            return testeParser.RULE_boolean_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean_op" ):
                listener.enterBoolean_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean_op" ):
                listener.exitBoolean_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_op" ):
                return visitor.visitBoolean_op(self)
            else:
                return visitor.visitChildren(self)




    def boolean_op(self):

        localctx = testeParser.Boolean_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_boolean_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(testeParser.BOOLEAN_OP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





