# Generated from SQL.g4 by ANTLR 4.5.3
# encoding: utf-8
from antlr4 import *
from io import StringIO


print("Helllo")

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\23")
        buf.write("i\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\62\n\4\3\5\3\5\3\5\3")
        buf.write("\5\3\5\5\59\n\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6A\n\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7N\n\7\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\5\t\\\n\t\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\ng\n\n\3\n\2\2\13")
        buf.write("\2\4\6\b\n\f\16\20\22\2\4\3\2\3\7\3\2\21\22h\2\24\3\2")
        buf.write("\2\2\4\34\3\2\2\2\6\61\3\2\2\2\b8\3\2\2\2\n@\3\2\2\2\f")
        buf.write("M\3\2\2\2\16O\3\2\2\2\20[\3\2\2\2\22f\3\2\2\2\24\25\7")
        buf.write("\f\2\2\25\26\b\2\1\2\26\27\5\n\6\2\27\30\7\r\2\2\30\31")
        buf.write("\5\22\n\2\31\32\5\b\5\2\32\33\b\2\1\2\33\3\3\2\2\2\34")
        buf.write("\35\t\2\2\2\35\5\3\2\2\2\36\37\t\3\2\2\37 \5\4\3\2 !\t")
        buf.write("\3\2\2!\"\7\b\2\2\"#\5\6\4\2#$\b\4\1\2$\62\3\2\2\2%&\t")
        buf.write("\3\2\2&\'\5\4\3\2\'(\t\3\2\2()\7\t\2\2)*\5\6\4\2*+\b\4")
        buf.write("\1\2+\62\3\2\2\2,-\t\3\2\2-.\5\4\3\2./\t\3\2\2/\60\b\4")
        buf.write("\1\2\60\62\3\2\2\2\61\36\3\2\2\2\61%\3\2\2\2\61,\3\2\2")
        buf.write("\2\62\7\3\2\2\2\63\64\7\16\2\2\64\65\5\6\4\2\65\66\b\5")
        buf.write("\1\2\669\3\2\2\2\679\b\5\1\28\63\3\2\2\28\67\3\2\2\29")
        buf.write("\t\3\2\2\2:;\7\22\2\2;<\7\n\2\2<=\5\n\6\2=>\b\6\1\2>A")
        buf.write("\3\2\2\2?A\7\22\2\2@:\3\2\2\2@?\3\2\2\2A\13\3\2\2\2BC")
        buf.write("\7\22\2\2CD\7\7\2\2DE\7\22\2\2EF\7\b\2\2FG\5\f\7\2GH\b")
        buf.write("\7\1\2HN\3\2\2\2IJ\7\22\2\2JK\7\7\2\2KL\7\22\2\2LN\b\7")
        buf.write("\1\2MB\3\2\2\2MI\3\2\2\2N\r\3\2\2\2OP\7\23\2\2PQ\7\17")
        buf.write("\2\2QR\7\23\2\2RS\7\20\2\2ST\5\f\7\2TU\5\20\t\2U\17\3")
        buf.write("\2\2\2VW\7\17\2\2WX\7\23\2\2XY\7\20\2\2Y\\\5\f\7\2Z\\")
        buf.write("\3\2\2\2[V\3\2\2\2[Z\3\2\2\2\\\21\3\2\2\2]^\7\23\2\2^")
        buf.write("_\7\n\2\2_g\5\22\n\2`g\5\16\b\2ab\5\16\b\2bc\7\n\2\2c")
        buf.write("d\5\22\n\2dg\3\2\2\2eg\7\23\2\2f]\3\2\2\2f`\3\2\2\2fa")
        buf.write("\3\2\2\2fe\3\2\2\2g\23\3\2\2\2\b\618@M[f")
        return buf.getvalue()


class SQLParser ( Parser ):

    grammarFileName = "SQL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'>='", "'<='", "'>'", "'<'", "'='", "'and'", 
                     "'or'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "WS", "SELECT", "FROM", "WHERE", "JOIN", 
                      "ON", "ATRIBUTO", "COLUNA", "TABELA" ]

    RULE_sql_expr = 0
    RULE_comparisonOp = 1
    RULE_conditionsWhere = 2
    RULE_where = 3
    RULE_clausulaSelect = 4
    RULE_conditionsJoin = 5
    RULE_joins = 6
    RULE_joins_ = 7
    RULE_clausulaFrom = 8

    ruleNames =  [ "sql_expr", "comparisonOp", "conditionsWhere", "where", 
                   "clausulaSelect", "conditionsJoin", "joins", "joins_", 
                   "clausulaFrom" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    WS=9
    SELECT=10
    FROM=11
    WHERE=12
    JOIN=13
    ON=14
    ATRIBUTO=15
    COLUNA=16
    TABELA=17

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class Sql_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.lista =  []
            self._SELECT = None # Token
            self.w = None # WhereContext

        def SELECT(self):
            return self.getToken(SQLParser.SELECT, 0)

        def clausulaSelect(self):
            return self.getTypedRuleContext(SQLParser.ClausulaSelectContext,0)


        def FROM(self):
            return self.getToken(SQLParser.FROM, 0)

        def clausulaFrom(self):
            return self.getTypedRuleContext(SQLParser.ClausulaFromContext,0)


        def where(self):
            return self.getTypedRuleContext(SQLParser.WhereContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_sql_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSql_expr" ):
                listener.enterSql_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSql_expr" ):
                listener.exitSql_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSql_expr" ):
                return visitor.visitSql_expr(self)
            else:
                return visitor.visitChildren(self)




    def sql_expr(self):

        localctx = SQLParser.Sql_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sql_expr)

        number = 0
        print("Nasd")

        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            localctx._SELECT = self.match(SQLParser.SELECT)
            print ((None if localctx._SELECT is None else localctx._SELECT.text));localctx.lista += [1];print(localctx.lista)
            self.state = 20
            self.clausulaSelect()
            self.state = 21
            self.match(SQLParser.FROM)
            self.state = 22
            self.clausulaFrom()
            self.state = 23
            localctx.w = self.where()
            number = localctx.w.number;print(localctx.w.bla)
            self._ctx.stop = self._input.LT(-1)

            print("Found "+ str(number) + " conditions on where")

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ComparisonOpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SQLParser.RULE_comparisonOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonOp" ):
                listener.enterComparisonOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonOp" ):
                listener.exitComparisonOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonOp" ):
                return visitor.visitComparisonOp(self)
            else:
                return visitor.visitChildren(self)




    def comparisonOp(self):

        localctx = SQLParser.ComparisonOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_comparisonOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SQLParser.T__0) | (1 << SQLParser.T__1) | (1 << SQLParser.T__2) | (1 << SQLParser.T__3) | (1 << SQLParser.T__4))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConditionsWhereContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.number = None
            self.c1 = None # ConditionsWhereContext

        def comparisonOp(self):
            return self.getTypedRuleContext(SQLParser.ComparisonOpContext,0)


        def COLUNA(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.COLUNA)
            else:
                return self.getToken(SQLParser.COLUNA, i)

        def ATRIBUTO(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.ATRIBUTO)
            else:
                return self.getToken(SQLParser.ATRIBUTO, i)

        def conditionsWhere(self):
            return self.getTypedRuleContext(SQLParser.ConditionsWhereContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_conditionsWhere

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionsWhere" ):
                listener.enterConditionsWhere(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionsWhere" ):
                listener.exitConditionsWhere(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionsWhere" ):
                return visitor.visitConditionsWhere(self)
            else:
                return visitor.visitChildren(self)




    def conditionsWhere(self):

        localctx = SQLParser.ConditionsWhereContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_conditionsWhere)
        self._la = 0 # Token type
        try:
            self.state = 47
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                _la = self._input.LA(1)
                if not(_la==SQLParser.ATRIBUTO or _la==SQLParser.COLUNA):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 29
                self.comparisonOp()
                self.state = 30
                _la = self._input.LA(1)
                if not(_la==SQLParser.ATRIBUTO or _la==SQLParser.COLUNA):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 31
                self.match(SQLParser.T__5)
                self.state = 32
                localctx.c1 = self.conditionsWhere()
                localctx.number = localctx.c1.number + 1
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                _la = self._input.LA(1)
                if not(_la==SQLParser.ATRIBUTO or _la==SQLParser.COLUNA):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 36
                self.comparisonOp()
                self.state = 37
                _la = self._input.LA(1)
                if not(_la==SQLParser.ATRIBUTO or _la==SQLParser.COLUNA):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 38
                self.match(SQLParser.T__6)
                self.state = 39
                localctx.c1 = self.conditionsWhere()
                localctx.number = localctx.c1.number + 1
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 42
                _la = self._input.LA(1)
                if not(_la==SQLParser.ATRIBUTO or _la==SQLParser.COLUNA):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 43
                self.comparisonOp()
                self.state = 44
                _la = self._input.LA(1)
                if not(_la==SQLParser.ATRIBUTO or _la==SQLParser.COLUNA):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                localctx.number = 1
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WhereContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.number = None
            self.bla = None
            self._conditionsWhere = None # ConditionsWhereContext

        def WHERE(self):
            return self.getToken(SQLParser.WHERE, 0)

        def conditionsWhere(self):
            return self.getTypedRuleContext(SQLParser.ConditionsWhereContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_where

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhere" ):
                listener.enterWhere(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhere" ):
                listener.exitWhere(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhere" ):
                return visitor.visitWhere(self)
            else:
                return visitor.visitChildren(self)




    def where(self):

        localctx = SQLParser.WhereContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_where)
        try:
            self.state = 54
            token = self._input.LA(1)
            if token in [SQLParser.WHERE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.match(SQLParser.WHERE)
                self.state = 50
                localctx._conditionsWhere = self.conditionsWhere()
                localctx.number = localctx._conditionsWhere.number
                localctx.bla = "asd"

            elif token in [SQLParser.EOF]:
                self.enterOuterAlt(localctx, 2)
                localctx.number = 0

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ClausulaSelectContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.c1 = None # ClausulaSelectContext
            self._clausulaSelect = None # ClausulaSelectContext

        def COLUNA(self):
            return self.getToken(SQLParser.COLUNA, 0)

        def clausulaSelect(self):
            return self.getTypedRuleContext(SQLParser.ClausulaSelectContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_clausulaSelect

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClausulaSelect" ):
                listener.enterClausulaSelect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClausulaSelect" ):
                listener.exitClausulaSelect(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClausulaSelect" ):
                return visitor.visitClausulaSelect(self)
            else:
                return visitor.visitChildren(self)




    def clausulaSelect(self):

        localctx = SQLParser.ClausulaSelectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_clausulaSelect)
        try:
            self.state = 62
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.match(SQLParser.COLUNA)
                self.state = 57
                self.match(SQLParser.T__7)
                self.state = 58
                localctx.c1 = localctx._clausulaSelect = self.clausulaSelect()
                print("Coluna " + self._input.getText((localctx.start, self._input.LT(-1))))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.match(SQLParser.COLUNA)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConditionsJoinContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLUNA(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.COLUNA)
            else:
                return self.getToken(SQLParser.COLUNA, i)

        def conditionsJoin(self):
            return self.getTypedRuleContext(SQLParser.ConditionsJoinContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_conditionsJoin

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionsJoin" ):
                listener.enterConditionsJoin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionsJoin" ):
                listener.exitConditionsJoin(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionsJoin" ):
                return visitor.visitConditionsJoin(self)
            else:
                return visitor.visitChildren(self)




    def conditionsJoin(self):

        localctx = SQLParser.ConditionsJoinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_conditionsJoin)
        try:
            self.state = 75
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.match(SQLParser.COLUNA)
                self.state = 65
                self.match(SQLParser.T__4)
                self.state = 66
                self.match(SQLParser.COLUNA)
                self.state = 67
                self.match(SQLParser.T__5)
                self.state = 68
                self.conditionsJoin()
                print(self._input.getText((localctx.start, self._input.LT(-1))))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.match(SQLParser.COLUNA)
                self.state = 72
                self.match(SQLParser.T__4)
                self.state = 73
                self.match(SQLParser.COLUNA)
                print(self._input.getText((localctx.start, self._input.LT(-1))))
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class JoinsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TABELA(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.TABELA)
            else:
                return self.getToken(SQLParser.TABELA, i)

        def JOIN(self):
            return self.getToken(SQLParser.JOIN, 0)

        def ON(self):
            return self.getToken(SQLParser.ON, 0)

        def conditionsJoin(self):
            return self.getTypedRuleContext(SQLParser.ConditionsJoinContext,0)


        def joins_(self):
            return self.getTypedRuleContext(SQLParser.Joins_Context,0)


        def getRuleIndex(self):
            return SQLParser.RULE_joins

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJoins" ):
                listener.enterJoins(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJoins" ):
                listener.exitJoins(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJoins" ):
                return visitor.visitJoins(self)
            else:
                return visitor.visitChildren(self)




    def joins(self):

        localctx = SQLParser.JoinsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_joins)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(SQLParser.TABELA)
            self.state = 78
            self.match(SQLParser.JOIN)
            self.state = 79
            self.match(SQLParser.TABELA)
            self.state = 80
            self.match(SQLParser.ON)
            self.state = 81
            self.conditionsJoin()
            self.state = 82
            self.joins_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Joins_Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def JOIN(self):
            return self.getToken(SQLParser.JOIN, 0)

        def TABELA(self):
            return self.getToken(SQLParser.TABELA, 0)

        def ON(self):
            return self.getToken(SQLParser.ON, 0)

        def conditionsJoin(self):
            return self.getTypedRuleContext(SQLParser.ConditionsJoinContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_joins_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJoins_" ):
                listener.enterJoins_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJoins_" ):
                listener.exitJoins_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJoins_" ):
                return visitor.visitJoins_(self)
            else:
                return visitor.visitChildren(self)




    def joins_(self):

        localctx = SQLParser.Joins_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_joins_)
        try:
            self.state = 89
            token = self._input.LA(1)
            if token in [SQLParser.JOIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.match(SQLParser.JOIN)
                self.state = 85
                self.match(SQLParser.TABELA)
                self.state = 86
                self.match(SQLParser.ON)
                self.state = 87
                self.conditionsJoin()

            elif token in [SQLParser.EOF, SQLParser.T__7, SQLParser.WHERE]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ClausulaFromContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TABELA(self):
            return self.getToken(SQLParser.TABELA, 0)

        def clausulaFrom(self):
            return self.getTypedRuleContext(SQLParser.ClausulaFromContext,0)


        def joins(self):
            return self.getTypedRuleContext(SQLParser.JoinsContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_clausulaFrom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClausulaFrom" ):
                listener.enterClausulaFrom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClausulaFrom" ):
                listener.exitClausulaFrom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClausulaFrom" ):
                return visitor.visitClausulaFrom(self)
            else:
                return visitor.visitChildren(self)




    def clausulaFrom(self):

        localctx = SQLParser.ClausulaFromContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_clausulaFrom)
        try:
            self.state = 100
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self.match(SQLParser.TABELA)
                self.state = 92
                self.match(SQLParser.T__7)
                self.state = 93
                self.clausulaFrom()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self.joins()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 95
                self.joins()
                self.state = 96
                self.match(SQLParser.T__7)
                self.state = 97
                self.clausulaFrom()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 99
                self.match(SQLParser.TABELA)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





