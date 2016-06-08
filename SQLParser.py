# Generated from SQL.g4 by ANTLR 4.5.3
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\r")
        buf.write("D\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\34")
        buf.write("\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4)")
        buf.write("\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\5")
        buf.write("\6\67\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7B\n\7")
        buf.write("\3\7\2\2\b\2\4\6\b\n\f\2\2C\2\16\3\2\2\2\4\33\3\2\2\2")
        buf.write("\6(\3\2\2\2\b*\3\2\2\2\n\66\3\2\2\2\fA\3\2\2\2\16\17\7")
        buf.write("\7\2\2\17\20\b\2\1\2\20\21\5\4\3\2\21\22\7\b\2\2\22\23")
        buf.write("\5\f\7\2\23\3\3\2\2\2\24\25\7\f\2\2\25\26\7\3\2\2\26\27")
        buf.write("\5\4\3\2\27\30\b\3\1\2\30\34\3\2\2\2\31\32\7\f\2\2\32")
        buf.write("\34\b\3\1\2\33\24\3\2\2\2\33\31\3\2\2\2\34\5\3\2\2\2\35")
        buf.write("\36\7\f\2\2\36\37\7\4\2\2\37 \7\f\2\2 !\7\5\2\2!\"\5\6")
        buf.write("\4\2\"#\b\4\1\2#)\3\2\2\2$%\7\f\2\2%&\7\4\2\2&\'\7\f\2")
        buf.write("\2\')\b\4\1\2(\35\3\2\2\2($\3\2\2\2)\7\3\2\2\2*+\7\r\2")
        buf.write("\2+,\7\n\2\2,-\7\r\2\2-.\7\13\2\2./\5\6\4\2/\60\5\n\6")
        buf.write("\2\60\t\3\2\2\2\61\62\7\n\2\2\62\63\7\r\2\2\63\64\7\13")
        buf.write("\2\2\64\67\5\6\4\2\65\67\3\2\2\2\66\61\3\2\2\2\66\65\3")
        buf.write("\2\2\2\67\13\3\2\2\289\7\r\2\29:\7\3\2\2:B\5\f\7\2;B\5")
        buf.write("\b\5\2<=\5\b\5\2=>\7\3\2\2>?\5\f\7\2?B\3\2\2\2@B\7\r\2")
        buf.write("\2A8\3\2\2\2A;\3\2\2\2A<\3\2\2\2A@\3\2\2\2B\r\3\2\2\2")
        buf.write("\6\33(\66A")
        return buf.getvalue()


class SQLParser ( Parser ):

    grammarFileName = "SQL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'='", "'and'", "<INVALID>", "'SELECT'", 
                     "'FROM'", "'WHERE'", "'JOIN'", "'ON'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "WS", "SELECT", "FROM", "WHERE", "JOIN", "ON", "COLUNA", 
                      "TABELA" ]

    RULE_sql_expr = 0
    RULE_clausulaSelect = 1
    RULE_conditionsJoin = 2
    RULE_joins = 3
    RULE_joins_ = 4
    RULE_clausulaFrom = 5

    ruleNames =  [ "sql_expr", "clausulaSelect", "conditionsJoin", "joins", 
                   "joins_", "clausulaFrom" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    WS=4
    SELECT=5
    FROM=6
    WHERE=7
    JOIN=8
    ON=9
    COLUNA=10
    TABELA=11

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

        def SELECT(self):
            return self.getToken(SQLParser.SELECT, 0)

        def clausulaSelect(self):
            return self.getTypedRuleContext(SQLParser.ClausulaSelectContext,0)


        def FROM(self):
            return self.getToken(SQLParser.FROM, 0)

        def clausulaFrom(self):
            return self.getTypedRuleContext(SQLParser.ClausulaFromContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            localctx._SELECT = self.match(SQLParser.SELECT)
            print ((None if localctx._SELECT is None else localctx._SELECT.text))
                    localctx.lista += [1];print(localctx.lista)
            self.state = 14
            self.clausulaSelect()
            self.state = 15
            self.match(SQLParser.FROM)
            self.state = 16
            self.clausulaFrom()
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
            self._COLUNA = None # Token

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
        self.enterRule(localctx, 2, self.RULE_clausulaSelect)
        try:
            self.state = 25
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.match(SQLParser.COLUNA)
                self.state = 19
                self.match(SQLParser.T__0)
                self.state = 20
                localctx.c1 = localctx._clausulaSelect = self.clausulaSelect()
                print(self._input.getText((localctx.start, self._input.LT(-1))))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                localctx._COLUNA = self.match(SQLParser.COLUNA)
                print((None if localctx._COLUNA is None else localctx._COLUNA.text))
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
        self.enterRule(localctx, 4, self.RULE_conditionsJoin)
        try:
            self.state = 38
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.match(SQLParser.COLUNA)
                self.state = 28
                self.match(SQLParser.T__1)
                self.state = 29
                self.match(SQLParser.COLUNA)
                self.state = 30
                self.match(SQLParser.T__2)
                self.state = 31
                self.conditionsJoin()
                print(self._input.getText((localctx.start, self._input.LT(-1))))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.match(SQLParser.COLUNA)
                self.state = 35
                self.match(SQLParser.T__1)
                self.state = 36
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
        self.enterRule(localctx, 6, self.RULE_joins)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(SQLParser.TABELA)
            self.state = 41
            self.match(SQLParser.JOIN)
            self.state = 42
            self.match(SQLParser.TABELA)
            self.state = 43
            self.match(SQLParser.ON)
            self.state = 44
            self.conditionsJoin()
            self.state = 45
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
        self.enterRule(localctx, 8, self.RULE_joins_)
        try:
            self.state = 52
            token = self._input.LA(1)
            if token in [SQLParser.JOIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.match(SQLParser.JOIN)
                self.state = 48
                self.match(SQLParser.TABELA)
                self.state = 49
                self.match(SQLParser.ON)
                self.state = 50
                self.conditionsJoin()

            elif token in [SQLParser.EOF, SQLParser.T__0]:
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
        self.enterRule(localctx, 10, self.RULE_clausulaFrom)
        try:
            self.state = 63
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.match(SQLParser.TABELA)
                self.state = 55
                self.match(SQLParser.T__0)
                self.state = 56
                self.clausulaFrom()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.joins()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 58
                self.joins()
                self.state = 59
                self.match(SQLParser.T__0)
                self.state = 60
                self.clausulaFrom()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 62
                self.match(SQLParser.TABELA)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





