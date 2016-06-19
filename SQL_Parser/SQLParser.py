# Generated from SQL.g4 by ANTLR 4.5.3
# encoding: utf-8
from antlr4 import *
from io import StringIO


from SQL_Parser.QueryTree import *
query_tree = QueryTree()

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\23")
        buf.write("s\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\5\4,\n\4\3\5\3\5\3\5\3\5\3\5\5\5\63\n\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\5\6<\n\6\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\5\7I\n\7\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\tZ\n\t\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5")
        buf.write("\nk\n\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\2\2\r\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\2\5\3\2\3\7\3\2\21\22\3\2\t\no\2\30")
        buf.write("\3\2\2\2\4\37\3\2\2\2\6+\3\2\2\2\b\62\3\2\2\2\n;\3\2\2")
        buf.write("\2\fH\3\2\2\2\16J\3\2\2\2\20Y\3\2\2\2\22j\3\2\2\2\24l")
        buf.write("\3\2\2\2\26p\3\2\2\2\30\31\7\f\2\2\31\32\5\n\6\2\32\33")
        buf.write("\7\r\2\2\33\34\5\22\n\2\34\35\5\b\5\2\35\36\b\2\1\2\36")
        buf.write("\3\3\2\2\2\37 \t\2\2\2 \5\3\2\2\2!\"\5\24\13\2\"#\5\26")
        buf.write("\f\2#$\5\6\4\2$%\b\4\1\2%,\3\2\2\2&\'\7\22\2\2\'(\5\4")
        buf.write("\3\2()\t\3\2\2)*\b\4\1\2*,\3\2\2\2+!\3\2\2\2+&\3\2\2\2")
        buf.write(",\7\3\2\2\2-.\7\16\2\2./\5\6\4\2/\60\b\5\1\2\60\63\3\2")
        buf.write("\2\2\61\63\b\5\1\2\62-\3\2\2\2\62\61\3\2\2\2\63\t\3\2")
        buf.write("\2\2\64\65\7\22\2\2\65\66\7\b\2\2\66\67\5\n\6\2\678\b")
        buf.write("\6\1\28<\3\2\2\29:\7\22\2\2:<\b\6\1\2;\64\3\2\2\2;9\3")
        buf.write("\2\2\2<\13\3\2\2\2=>\7\22\2\2>?\7\7\2\2?@\7\22\2\2@A\5")
        buf.write("\26\f\2AB\5\f\7\2BC\b\7\1\2CI\3\2\2\2DE\7\22\2\2EF\7\7")
        buf.write("\2\2FG\7\22\2\2GI\b\7\1\2H=\3\2\2\2HD\3\2\2\2I\r\3\2\2")
        buf.write("\2JK\7\23\2\2KL\7\17\2\2LM\7\23\2\2MN\7\20\2\2NO\5\f\7")
        buf.write("\2OP\5\20\t\2PQ\b\b\1\2Q\17\3\2\2\2RS\7\17\2\2ST\7\23")
        buf.write("\2\2TU\7\20\2\2UV\5\f\7\2VW\b\t\1\2WZ\3\2\2\2XZ\b\t\1")
        buf.write("\2YR\3\2\2\2YX\3\2\2\2Z\21\3\2\2\2[\\\7\23\2\2\\]\7\b")
        buf.write("\2\2]^\5\22\n\2^_\b\n\1\2_k\3\2\2\2`a\5\16\b\2ab\b\n\1")
        buf.write("\2bk\3\2\2\2cd\5\16\b\2de\7\b\2\2ef\5\22\n\2fg\b\n\1\2")
        buf.write("gk\3\2\2\2hi\7\23\2\2ik\b\n\1\2j[\3\2\2\2j`\3\2\2\2jc")
        buf.write("\3\2\2\2jh\3\2\2\2k\23\3\2\2\2lm\7\22\2\2mn\5\4\3\2no")
        buf.write("\t\3\2\2o\25\3\2\2\2pq\t\4\2\2q\27\3\2\2\2\b+\62;HYj")
        return buf.getvalue()


class SQLParser ( Parser ):

    grammarFileName = "SQL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'>='", "'<='", "'>'", "'<'", "'='", "','", 
                     "'and'", "'or'" ]

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
    RULE_termo = 9
    RULE_conector = 10

    ruleNames =  [ "sql_expr", "comparisonOp", "conditionsWhere", "where", 
                   "clausulaSelect", "conditionsJoin", "joins", "joins_", 
                   "clausulaFrom", "termo", "conector" ]

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
            self.sl = None # ClausulaSelectContext
            self.fr = None # ClausulaFromContext
            self.w = None # WhereContext

        def SELECT(self):
            return self.getToken(SQLParser.SELECT, 0)

        def FROM(self):
            return self.getToken(SQLParser.FROM, 0)

        def clausulaSelect(self):
            return self.getTypedRuleContext(SQLParser.ClausulaSelectContext,0)


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




    def sql_expr(self):

        localctx = SQLParser.Sql_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sql_expr)

        number = 0

        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(SQLParser.SELECT)
            self.state = 23
            localctx.sl = self.clausulaSelect()
            self.state = 24
            self.match(SQLParser.FROM)
            self.state = 25
            localctx.fr = self.clausulaFrom()
            self.state = 26
            localctx.w = self.where()
            number = localctx.w.number
            projection = ProjectionNode(localctx.sl.columns)
            selection = SelectionNode(localctx.w.terms, localctx.w.conectors)
            theta_join = localctx.fr.tj
            query_tree.set_root(projection)
            node = query_tree.root
            node.set_child(selection)
            node = node.children
            node.set_child(theta_join)

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




    def comparisonOp(self):

        localctx = SQLParser.ComparisonOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_comparisonOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
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
            self.terms = None
            self.conectors = None
            self.t = None # TermoContext
            self.c = None # ConectorContext
            self.cnd = None # ConditionsWhereContext

        def termo(self):
            return self.getTypedRuleContext(SQLParser.TermoContext,0)


        def conector(self):
            return self.getTypedRuleContext(SQLParser.ConectorContext,0)


        def conditionsWhere(self):
            return self.getTypedRuleContext(SQLParser.ConditionsWhereContext,0)


        def COLUNA(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.COLUNA)
            else:
                return self.getToken(SQLParser.COLUNA, i)

        def comparisonOp(self):
            return self.getTypedRuleContext(SQLParser.ComparisonOpContext,0)


        def ATRIBUTO(self):
            return self.getToken(SQLParser.ATRIBUTO, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_conditionsWhere

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionsWhere" ):
                listener.enterConditionsWhere(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionsWhere" ):
                listener.exitConditionsWhere(self)




    def conditionsWhere(self):

        localctx = SQLParser.ConditionsWhereContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_conditionsWhere)
        self._la = 0 # Token type
        try:
            self.state = 41
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                localctx.t = self.termo()
                self.state = 32
                localctx.c = self.conector()
                self.state = 33
                localctx.cnd = self.conditionsWhere()
                localctx.number = localctx.cnd.number + 1
                localctx.terms = localctx.cnd.terms
                localctx.terms.append((None if localctx.t is None else self._input.getText((localctx.t.start,localctx.t.stop))))
                localctx.conectors = localctx.cnd.conectors
                localctx.conectors.append((None if localctx.c is None else self._input.getText((localctx.c.start,localctx.c.stop))))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.match(SQLParser.COLUNA)
                self.state = 37
                self.comparisonOp()
                self.state = 38
                _la = self._input.LA(1)
                if not(_la==SQLParser.ATRIBUTO or _la==SQLParser.COLUNA):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                localctx.number = 1
                localctx.terms = [self._input.getText((localctx.start, self._input.LT(-1)))]
                localctx.conectors = []
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
            self.terms = None
            self.conectors = None
            self.c = None # ConditionsWhereContext
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




    def where(self):

        localctx = SQLParser.WhereContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_where)
        try:
            self.state = 48
            token = self._input.LA(1)
            if token in [SQLParser.WHERE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.match(SQLParser.WHERE)
                self.state = 44
                localctx.c = localctx._conditionsWhere = self.conditionsWhere()
                localctx.number = localctx._conditionsWhere.number
                localctx.terms = localctx.c.terms
                localctx.conectors = localctx.c.conectors

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
            self.columns = None
            self.c = None # Token
            self.c1 = None # ClausulaSelectContext

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




    def clausulaSelect(self):

        localctx = SQLParser.ClausulaSelectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_clausulaSelect)
        try:
            self.state = 57
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                localctx.c = self.match(SQLParser.COLUNA)
                self.state = 51
                self.match(SQLParser.T__5)
                self.state = 52
                localctx.c1 = self.clausulaSelect()
                localctx.columns = localctx.c1.columns
                localctx.columns.append((None if localctx.c is None else localctx.c.text))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.match(SQLParser.COLUNA)
                localctx.columns = [self._input.getText((localctx.start, self._input.LT(-1)))]
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
            self.terms = None
            self.conectors = None
            self.c1 = None # Token
            self.c2 = None # Token
            self.c = None # ConectorContext
            self.cnd = None # ConditionsJoinContext

        def COLUNA(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.COLUNA)
            else:
                return self.getToken(SQLParser.COLUNA, i)

        def conector(self):
            return self.getTypedRuleContext(SQLParser.ConectorContext,0)


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




    def conditionsJoin(self):

        localctx = SQLParser.ConditionsJoinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_conditionsJoin)
        try:
            self.state = 70
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                localctx.c1 = self.match(SQLParser.COLUNA)
                self.state = 60
                self.match(SQLParser.T__4)
                self.state = 61
                localctx.c2 = self.match(SQLParser.COLUNA)
                self.state = 62
                localctx.c = self.conector()
                self.state = 63
                localctx.cnd = self.conditionsJoin()
                localctx.terms = localctx.cnd.terms
                localctx.terms.append((None if localctx.c1 is None else localctx.c1.text) + "=" + (None if localctx.c2 is None else localctx.c2.text))
                localctx.conectors = localctx.cnd.conectors
                localctx.conectors.append((None if localctx.c is None else self._input.getText((localctx.c.start,localctx.c.stop))))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.match(SQLParser.COLUNA)
                self.state = 67
                self.match(SQLParser.T__4)
                self.state = 68
                self.match(SQLParser.COLUNA)
                localctx.terms = [self._input.getText((localctx.start, self._input.LT(-1)))]
                localctx.conectors = []
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
            self.tj = None
            self.t1 = None # Token
            self.t2 = None # Token
            self.c = None # ConditionsJoinContext
            self.j = None # Joins_Context

        def JOIN(self):
            return self.getToken(SQLParser.JOIN, 0)

        def ON(self):
            return self.getToken(SQLParser.ON, 0)

        def TABELA(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.TABELA)
            else:
                return self.getToken(SQLParser.TABELA, i)

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




    def joins(self):

        localctx = SQLParser.JoinsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_joins)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            localctx.t1 = self.match(SQLParser.TABELA)
            self.state = 73
            self.match(SQLParser.JOIN)
            self.state = 74
            localctx.t2 = self.match(SQLParser.TABELA)
            self.state = 75
            self.match(SQLParser.ON)
            self.state = 76
            localctx.c = self.conditionsJoin()
            self.state = 77
            localctx.j = self.joins_()
            join1 = ThetaJoinNode(Table((None if localctx.t1 is None else localctx.t1.text)), Table((None if localctx.t2 is None else localctx.t2.text)), localctx.c.terms, localctx.c.conectors)
            if (localctx.j.table == None):
                localctx.tj = join1
            else:
                localctx.tj = ThetaJoinNode(join1, localctx.j.table, localctx.j.terms, localctx.j.conectors)
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
            self.table = None
            self.terms = None
            self.conectors = None
            self.t = None # Token
            self.c = None # ConditionsJoinContext

        def JOIN(self):
            return self.getToken(SQLParser.JOIN, 0)

        def ON(self):
            return self.getToken(SQLParser.ON, 0)

        def TABELA(self):
            return self.getToken(SQLParser.TABELA, 0)

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




    def joins_(self):

        localctx = SQLParser.Joins_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_joins_)
        try:
            self.state = 87
            token = self._input.LA(1)
            if token in [SQLParser.JOIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.match(SQLParser.JOIN)
                self.state = 81
                localctx.t = self.match(SQLParser.TABELA)
                self.state = 82
                self.match(SQLParser.ON)
                self.state = 83
                localctx.c = self.conditionsJoin()
                localctx.table = (None if localctx.t is None else localctx.t.text)
                localctx.terms = localctx.c.terms, localctx.conectors = localctx.c.conectors

            elif token in [SQLParser.EOF, SQLParser.T__5, SQLParser.WHERE]:
                self.enterOuterAlt(localctx, 2)
                localctx.table = None
                localctx.terms = None
                localctx.conectors = None

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
            self.tj = None
            self.t1 = None # Token
            self.c = None # ClausulaFromContext
            self.j = None # JoinsContext

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




    def clausulaFrom(self):

        localctx = SQLParser.ClausulaFromContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_clausulaFrom)
        try:
            self.state = 104
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                localctx.t1 = self.match(SQLParser.TABELA)
                self.state = 90
                self.match(SQLParser.T__5)
                self.state = 91
                localctx.c = self.clausulaFrom()
                tab = Table((None if localctx.t1 is None else localctx.t1.text))
                join = ThetaJoinNode(tab, localctx.c.tj, [','], [])
                localctx.tj = join
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                localctx.j = self.joins()
                localctx.tj = localctx.j.tj
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 97
                localctx.j = self.joins()
                self.state = 98
                self.match(SQLParser.T__5)
                self.state = 99
                localctx.c = self.clausulaFrom()
                localctx.tj = ThetaJoinNode(localctx.j.tj, localctx.c.tj, [','], [])
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 102
                self.match(SQLParser.TABELA)
                table = Table(self._input.getText((localctx.start, self._input.LT(-1))))
                localctx.tj = table
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TermoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLUNA(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.COLUNA)
            else:
                return self.getToken(SQLParser.COLUNA, i)

        def comparisonOp(self):
            return self.getTypedRuleContext(SQLParser.ComparisonOpContext,0)


        def ATRIBUTO(self):
            return self.getToken(SQLParser.ATRIBUTO, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_termo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermo" ):
                listener.enterTermo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermo" ):
                listener.exitTermo(self)




    def termo(self):

        localctx = SQLParser.TermoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_termo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(SQLParser.COLUNA)
            self.state = 107
            self.comparisonOp()
            self.state = 108
            _la = self._input.LA(1)
            if not(_la==SQLParser.ATRIBUTO or _la==SQLParser.COLUNA):
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

    class ConectorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SQLParser.RULE_conector

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConector" ):
                listener.enterConector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConector" ):
                listener.exitConector(self)




    def conector(self):

        localctx = SQLParser.ConectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_conector)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            _la = self._input.LA(1)
            if not(_la==SQLParser.T__6 or _la==SQLParser.T__7):
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





