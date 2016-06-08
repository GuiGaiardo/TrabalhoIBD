# Generated from SQL.g4 by ANTLR 4.5.3
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\t")
        buf.write("\25\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\2\5\2\13\n\2\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\5\3\23\n\3\3\3\2\2\4\2\4\2\2\24\2\n\3")
        buf.write("\2\2\2\4\22\3\2\2\2\6\7\7\5\2\2\7\b\b\2\1\2\b\13\5\4\3")
        buf.write("\2\t\13\7\6\2\2\n\6\3\2\2\2\n\t\3\2\2\2\13\3\3\2\2\2\f")
        buf.write("\r\7\b\2\2\r\16\7\3\2\2\16\17\5\4\3\2\17\20\b\3\1\2\20")
        buf.write("\23\3\2\2\2\21\23\7\b\2\2\22\f\3\2\2\2\22\21\3\2\2\2\23")
        buf.write("\5\3\2\2\2\4\n\22")
        return buf.getvalue()


class SQLParser ( Parser ):

    grammarFileName = "SQL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "<INVALID>", "'SELECT'", "'FROM'", 
                     "'WHERE'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "WS", "SELECT", "FROM", 
                      "WHERE", "COLUNA", "TABELA" ]

    RULE_sql_expr = 0
    RULE_clausulaSelect = 1

    ruleNames =  [ "sql_expr", "clausulaSelect" ]

    EOF = Token.EOF
    T__0=1
    WS=2
    SELECT=3
    FROM=4
    WHERE=5
    COLUNA=6
    TABELA=7

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
            self.state = 8
            token = self._input.LA(1)
            if token in [SQLParser.SELECT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 4
                localctx._SELECT = self.match(SQLParser.SELECT)
                print ((None if localctx._SELECT is None else localctx._SELECT.text))
                localctx.lista += [1]
                print(localctx.lista)
                self.state = 6
                self.clausulaSelect()

            elif token in [SQLParser.FROM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 7
                self.match(SQLParser.FROM)

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
        self.enterRule(localctx, 2, self.RULE_clausulaSelect)
        try:
            self.state = 16
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 10
                self.match(SQLParser.COLUNA)
                self.state = 11
                self.match(SQLParser.T__0)
                self.state = 12
                localctx.c1 = localctx._clausulaSelect = self.clausulaSelect()
                print(self._input.getText((localctx.start, self._input.LT(-1))))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 15
                self.match(SQLParser.COLUNA)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





