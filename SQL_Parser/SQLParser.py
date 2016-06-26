# Generated from SQL.g4 by ANTLR 4.5.3
# encoding: utf-8
from antlr4 import *
from io import StringIO


from SQL_Parser.QueryTree import *
query_tree = QueryTree()

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\23")
        buf.write("z\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5")
        buf.write("\4*\n\4\3\5\3\5\3\5\3\5\3\5\5\5\61\n\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\5\6:\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\5\7G\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\tY\n\t\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\nj")
        buf.write("\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\5\13v\n\13\3\f\3\f\3\f\2\2\r\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\2\4\3\2\3\7\3\2\t\nw\2\30\3\2\2\2\4\37\3\2\2\2\6)")
        buf.write("\3\2\2\2\b\60\3\2\2\2\n9\3\2\2\2\fF\3\2\2\2\16H\3\2\2")
        buf.write("\2\20X\3\2\2\2\22i\3\2\2\2\24u\3\2\2\2\26w\3\2\2\2\30")
        buf.write("\31\7\f\2\2\31\32\5\n\6\2\32\33\7\r\2\2\33\34\5\22\n\2")
        buf.write("\34\35\5\b\5\2\35\36\b\2\1\2\36\3\3\2\2\2\37 \t\2\2\2")
        buf.write(" \5\3\2\2\2!\"\5\24\13\2\"#\5\26\f\2#$\5\6\4\2$%\b\4\1")
        buf.write("\2%*\3\2\2\2&\'\5\24\13\2\'(\b\4\1\2(*\3\2\2\2)!\3\2\2")
        buf.write("\2)&\3\2\2\2*\7\3\2\2\2+,\7\16\2\2,-\5\6\4\2-.\b\5\1\2")
        buf.write(".\61\3\2\2\2/\61\b\5\1\2\60+\3\2\2\2\60/\3\2\2\2\61\t")
        buf.write("\3\2\2\2\62\63\7\22\2\2\63\64\7\b\2\2\64\65\5\n\6\2\65")
        buf.write("\66\b\6\1\2\66:\3\2\2\2\678\7\22\2\28:\b\6\1\29\62\3\2")
        buf.write("\2\29\67\3\2\2\2:\13\3\2\2\2;<\7\22\2\2<=\7\7\2\2=>\7")
        buf.write("\22\2\2>?\5\26\f\2?@\5\f\7\2@A\b\7\1\2AG\3\2\2\2BC\7\22")
        buf.write("\2\2CD\7\7\2\2DE\7\22\2\2EG\b\7\1\2F;\3\2\2\2FB\3\2\2")
        buf.write("\2G\r\3\2\2\2HI\7\23\2\2IJ\7\17\2\2JK\7\23\2\2KL\7\20")
        buf.write("\2\2LM\5\f\7\2MN\5\20\t\2NO\b\b\1\2O\17\3\2\2\2PQ\7\17")
        buf.write("\2\2QR\7\23\2\2RS\7\20\2\2ST\5\f\7\2TU\5\20\t\2UV\b\t")
        buf.write("\1\2VY\3\2\2\2WY\b\t\1\2XP\3\2\2\2XW\3\2\2\2Y\21\3\2\2")
        buf.write("\2Z[\7\23\2\2[\\\7\b\2\2\\]\5\22\n\2]^\b\n\1\2^j\3\2\2")
        buf.write("\2_`\5\16\b\2`a\b\n\1\2aj\3\2\2\2bc\5\16\b\2cd\7\b\2\2")
        buf.write("de\5\22\n\2ef\b\n\1\2fj\3\2\2\2gh\7\23\2\2hj\b\n\1\2i")
        buf.write("Z\3\2\2\2i_\3\2\2\2ib\3\2\2\2ig\3\2\2\2j\23\3\2\2\2kl")
        buf.write("\7\22\2\2lm\5\4\3\2mn\7\22\2\2no\b\13\1\2ov\3\2\2\2pq")
        buf.write("\7\22\2\2qr\5\4\3\2rs\7\21\2\2st\b\13\1\2tv\3\2\2\2uk")
        buf.write("\3\2\2\2up\3\2\2\2v\25\3\2\2\2wx\t\3\2\2x\27\3\2\2\2\t")
        buf.write(")\609FXiu")
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
            localctx.fr = self.clausulaFrom( [] )
            self.state = 26
            localctx.w = self.where()
            projection = ProjectionNode(localctx.sl.columns)
            theta_join = localctx.fr.tj

            selectingTables = [x.split('.')[0] for x in localctx.sl.columns]
            whereTables = [x[0].split('.')[0] for x in localctx.w.terms]
            valid_query = 1

            if(not localctx.fr.tables is None):
                for t in selectingTables:
                    if(not t in localctx.fr.tables):
                        print("Selecting unknow table " + t)
                        valid_query = 0
                        projection = None

                print("--->" , whereTables)
                for t in whereTables:
                    print(localctx.fr.tables)
                    if(not t in localctx.fr.tables):
                        print("Unknown table " + t + " being used in where clause")
                        valid_query = 0
                        projection = None

            if valid_query:
                if len(localctx.w.terms) > 0:
                    selection = SelectionNode(localctx.w.terms, localctx.w.conectors)
                    selection.set_child(theta_join)
                    projection.set_child(selection)

                else:
                    projection.set_child(theta_join)

            else:
                projection = None

            query_tree.set_root(projection)
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
        try:
            self.state = 39
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
                localctx.terms = localctx.cnd.terms
                localctx.terms.append(localctx.t.term)
                localctx.conectors = localctx.cnd.conectors
                localctx.conectors.append((None if localctx.c is None else self._input.getText((localctx.c.start,localctx.c.stop))))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                localctx.t = self.termo()
                localctx.terms = [localctx.t.term]
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
            self.terms = None
            self.conectors = None
            self.c = None # ConditionsWhereContext

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
            self.state = 46
            token = self._input.LA(1)
            if token in [SQLParser.WHERE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.match(SQLParser.WHERE)
                self.state = 42
                localctx.c = self.conditionsWhere()
                localctx.terms = localctx.c.terms
                localctx.conectors = localctx.c.conectors

            elif token in [SQLParser.EOF]:
                self.enterOuterAlt(localctx, 2)
                localctx.terms = []
                localctx.conectors = []

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
            self.state = 55
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                localctx.c = self.match(SQLParser.COLUNA)
                self.state = 49
                self.match(SQLParser.T__5)
                self.state = 50
                localctx.c1 = self.clausulaSelect()
                localctx.columns = localctx.c1.columns
                localctx.columns.append((None if localctx.c is None else localctx.c.text))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
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
            self.state = 68
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                localctx.c1 = self.match(SQLParser.COLUNA)
                self.state = 58
                self.match(SQLParser.T__4)
                self.state = 59
                localctx.c2 = self.match(SQLParser.COLUNA)
                self.state = 60
                localctx.c = self.conector()
                self.state = 61
                localctx.cnd = self.conditionsJoin()
                localctx.terms = localctx.cnd.terms
                localctx.terms.append(((None if localctx.c1 is None else localctx.c1.text),"=",(None if localctx.c2 is None else localctx.c2.text)))
                localctx.conectors = localctx.cnd.conectors
                localctx.conectors.append((None if localctx.c is None else self._input.getText((localctx.c.start,localctx.c.stop))))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                localctx.c1 = self.match(SQLParser.COLUNA)
                self.state = 65
                self.match(SQLParser.T__4)
                self.state = 66
                localctx.c2 = self.match(SQLParser.COLUNA)
                localctx.terms = [((None if localctx.c1 is None else localctx.c1.text), "=", (None if localctx.c2 is None else localctx.c2.text))]
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, tablesSoFar=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.tablesSoFar = None
            self.tj = None
            self.tables = None
            self.t1 = None # Token
            self.t2 = None # Token
            self.c = None # ConditionsJoinContext
            self.j = None # Joins_Context
            self.tablesSoFar = tablesSoFar

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




    def joins(self, tablesSoFar):

        localctx = SQLParser.JoinsContext(self, self._ctx, self.state, tablesSoFar)
        self.enterRule(localctx, 12, self.RULE_joins)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            localctx.t1 = self.match(SQLParser.TABELA)
            self.state = 71
            self.match(SQLParser.JOIN)
            self.state = 72
            localctx.t2 = self.match(SQLParser.TABELA)
            self.state = 73
            self.match(SQLParser.ON)
            self.state = 74
            localctx.c = self.conditionsJoin()
            self.state = 75
            localctx.j = self.joins_(localctx.tablesSoFar + [(None if localctx.t1 is None else localctx.t1.text)] + [(None if localctx.t2 is None else localctx.t2.text)])
            join1 = ThetaJoinNode(Table((None if localctx.t1 is None else localctx.t1.text)), Table((None if localctx.t2 is None else localctx.t2.text)), localctx.c.terms, localctx.c.conectors)
            localctx.tables = [(None if localctx.t1 is None else localctx.t1.text), (None if localctx.t2 is None else localctx.t2.text)] + localctx.j.table
            if (localctx.j.table == []):
                localctx.tj = join1
            else:
                last_join = join1
                for i in range(len(localctx.j.table)):
                    print(localctx.j.terms[i])
                    last_join = ThetaJoinNode(last_join, Table(localctx.j.table[i]), localctx.j.terms[i], localctx.j.conectors[i])
                localctx.tj = last_join
                #localctx.tj = ThetaJoinNode(join1, Table(localctx.j.table[i]), localctx.j.terms, localctx.j.conectors)
                #localctx.tables += [localctx.j.table]

            for term in localctx.c.terms:
                table1 = term[0].split('.')[0]
                table2 = term[2].split('.')[0]
                if table1 not in (localctx.tablesSoFar + [(None if localctx.t1 is None else localctx.t1.text)] + [(None if localctx.t2 is None else localctx.t2.text)]):
                    print("Unknown table " + table1 + " referenced in JOIN condition")
                if table2 not in (localctx.tablesSoFar + [(None if localctx.t1 is None else localctx.t1.text)] + [(None if localctx.t2 is None else localctx.t2.text)]):
                    print("Unknown table " + table2 + " referenced in JOIN condition")

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Joins_Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, tablesSoFar=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.tablesSoFar = None
            self.table = None
            self.terms = None
            self.conectors = None
            self.t = None # Token
            self.c = None # ConditionsJoinContext
            self.j = None # Joins_Context
            self.tablesSoFar = tablesSoFar

        def JOIN(self):
            return self.getToken(SQLParser.JOIN, 0)

        def ON(self):
            return self.getToken(SQLParser.ON, 0)

        def TABELA(self):
            return self.getToken(SQLParser.TABELA, 0)

        def conditionsJoin(self):
            return self.getTypedRuleContext(SQLParser.ConditionsJoinContext,0)


        def joins_(self):
            return self.getTypedRuleContext(SQLParser.Joins_Context,0)


        def getRuleIndex(self):
            return SQLParser.RULE_joins_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJoins_" ):
                listener.enterJoins_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJoins_" ):
                listener.exitJoins_(self)




    def joins_(self, tablesSoFar):

        localctx = SQLParser.Joins_Context(self, self._ctx, self.state, tablesSoFar)
        self.enterRule(localctx, 14, self.RULE_joins_)
        try:
            self.state = 86
            token = self._input.LA(1)
            if token in [SQLParser.JOIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.match(SQLParser.JOIN)
                self.state = 79
                localctx.t = self.match(SQLParser.TABELA)
                self.state = 80
                self.match(SQLParser.ON)
                self.state = 81
                localctx.c = self.conditionsJoin()
                self.state = 82
                localctx.j = self.joins_(localctx.tablesSoFar + [(None if localctx.t is None else localctx.t.text)])
                localctx.table = (None if localctx.t is None else localctx.t.text)
                localctx.terms = [localctx.c.terms] + localctx.j.terms
                localctx.conectors = [localctx.c.conectors] + localctx.j.conectors
                localctx.table = [(None if localctx.t is None else localctx.t.text)] + localctx.j.table
                for term in localctx.c.terms:
                    table1 = term[0].split('.')[0]
                    if table1 not in (localctx.tablesSoFar + [(None if localctx.t is None else localctx.t.text)]):
                        print("Unknown table " + table1 + " referenced in JOIN condition")

            elif token in [SQLParser.EOF, SQLParser.T__5, SQLParser.WHERE]:
                self.enterOuterAlt(localctx, 2)
                localctx.table = []
                localctx.terms = []
                localctx.conectors = []

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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, tablesSoFar=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.tablesSoFar = None
            self.tj = None
            self.tables = None
            self.t1 = None # Token
            self.c = None # ClausulaFromContext
            self.j = None # JoinsContext
            self.t = None # Token
            self.tablesSoFar = tablesSoFar

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




    def clausulaFrom(self, tablesSoFar):

        localctx = SQLParser.ClausulaFromContext(self, self._ctx, self.state, tablesSoFar)
        self.enterRule(localctx, 16, self.RULE_clausulaFrom)
        try:
            self.state = 103
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                localctx.t1 = self.match(SQLParser.TABELA)
                self.state = 89
                self.match(SQLParser.T__5)
                self.state = 90
                localctx.c = self.clausulaFrom(localctx.tablesSoFar + [(None if localctx.t1 is None else localctx.t1.text)])
                tab = Table((None if localctx.t1 is None else localctx.t1.text))
                join = ThetaJoinNode(tab, localctx.c.tj, [','], [])
                localctx.tj = join
                localctx.tables = [(None if localctx.t1 is None else localctx.t1.text)] + localctx.c.tables
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                localctx.j = self.joins(localctx.tablesSoFar)
                localctx.tj = localctx.j.tj
                localctx.tables = localctx.j.tables
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 96
                localctx.j = self.joins(localctx.tablesSoFar)
                self.state = 97
                self.match(SQLParser.T__5)
                self.state = 98
                localctx.c = self.clausulaFrom(localctx.j.tables + localctx.tablesSoFar )
                localctx.tj = ThetaJoinNode(localctx.j.tj, localctx.c.tj, [','], [])
                localctx.tables = localctx.j.tables + localctx.c.tables
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 101
                localctx.t = self.match(SQLParser.TABELA)
                table = Table(self._input.getText((localctx.start, self._input.LT(-1))))
                localctx.tj = table
                localctx.tables = [(None if localctx.t is None else localctx.t.text)]
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
            self.term = None
            self.t1 = None # Token
            self.o = None # ComparisonOpContext
            self.t2 = None # Token
            self.t = None # Token
            self.a = None # Token

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
        try:
            self.state = 115
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                localctx.t1 = self.match(SQLParser.COLUNA)
                self.state = 106
                localctx.o = self.comparisonOp()
                self.state = 107
                localctx.t2 = self.match(SQLParser.COLUNA)
                localctx.term = ((None if localctx.t1 is None else localctx.t1.text),(None if localctx.o is None else self._input.getText((localctx.o.start,localctx.o.stop))),(None if localctx.t2 is None else localctx.t2.text))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                localctx.t = self.match(SQLParser.COLUNA)
                self.state = 111
                localctx.o = self.comparisonOp()
                self.state = 112
                localctx.a = self.match(SQLParser.ATRIBUTO)
                localctx.term = ((None if localctx.t is None else localctx.t.text),(None if localctx.o is None else self._input.getText((localctx.o.start,localctx.o.stop))),(None if localctx.a is None else localctx.a.text))
                pass


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
            self.state = 117
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





