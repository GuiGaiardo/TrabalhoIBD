grammar SQL;

options{
    language=Python3;
}

@header{
from SQL_Parser.QueryTree import *
query_tree = QueryTree()
}


sql_expr locals []
@init{
number = 0
valid_query = False
projection = None
query_tree.set_root(None)
}
: SELECT sl=clausulaSelect FROM  fr=clausulaFrom[ [] ] w=where r=anythingElse {projection = ProjectionNode($sl.columns)
theta_join = $fr.tj

if($sl.columns is None):
    selectingTables = []
else:
    selectingTables = [x.split('.')[0] for x in $sl.columns]
if($w.terms is None):
    whereTables = []
else:
    whereTables = [x[0].split('.')[0] for x in $w.terms]
valid_query = 1


if($sl.columns is None):
    projection = None
    valid_query = 0

if($fr.tj is None):
    valid_query = 0
    projection = None

if(not $fr.tables is None):
    for t in selectingTables:
        if(not t in $fr.tables):
            msg = "Selecting unknow table " + t
            query_tree.set_error(msg)
            valid_query = 0
            projection = None

    for t in whereTables:
        if(not t in $fr.tables):
            msg = "Unknown table " + t + " being used in where clause"
            query_tree.set_error(msg)
            valid_query = 0
            projection = None


if($w.terms is None):
    valid_query = 0

if valid_query:
    if len($w.terms) > 0:
        selection = SelectionNode($w.terms, $w.conectors)
        selection.set_child(theta_join)
        projection.set_child(selection)

    else:
        projection.set_child(theta_join)

else:
    projection = None

if $r.trailing_str == None or $r.trailing_str.strip(" ") == "":
    pass
else:
    projection = None
    msg = "Not viable input at " + $r.trailing_str
    query_tree.set_error(msg)



query_tree.set_root(projection)};


comparisonOp: '>='|'<='| '>'| '<' | '=';

conditionsWhere returns[terms, conectors]
: t=termo c=conector cnd=conditionsWhere {$terms = $cnd.terms
$terms.append($t.term)
$conectors = $cnd.conectors
$conectors.append($c.text)}
| t=termo {$terms = [$t.term]
$conectors = []} ;

where returns[terms, conectors]
: WHERE c=conditionsWhere {$terms = $c.terms
$conectors = $c.conectors}
   | {$terms = []
$conectors = []};

clausulaSelect returns[columns] : c=COLUNA ',' c1=clausulaSelect {$columns = $c1.columns
$columns.append($c.text)}
| COLUNA {$columns = [$text]}
;

conditionsJoin returns[terms, conectors] : c1=COLUNA '=' c2=COLUNA c=conector cnd=conditionsJoin {$terms = $cnd.terms
$terms.append(($c1.text,"=",$c2.text))
$conectors = $cnd.conectors
$conectors.append($c.text)}
| c1=COLUNA '=' c2=COLUNA {$terms = [($c1.text, "=", $c2.text)]
$conectors = []};

joins[tablesSoFar] returns[tj, tables] : t1=TABELA JOIN t2=TABELA ON c=conditionsJoin j=joins_[$tablesSoFar + [$t1.text] + [$t2.text]] {join1 = ThetaJoinNode(Table($t1.text), Table($t2.text), $c.terms, $c.conectors)
print($tablesSoFar)
$tables = [$t1.text, $t2.text] + $j.table
if ($j.table == []):
    $tj = join1
else:
    last_join = join1
    for i in range(len($j.table)):
        last_join = ThetaJoinNode(last_join, Table($j.table[i]), $j.terms[i], $j.conectors[i])
        $tj = last_join

for term in $c.terms:
    table1 = term[0].split('.')[0]
    table2 = term[2].split('.')[0]
    if table1 not in ($tablesSoFar + [$t1.text] + [$t2.text]):
        msg = "Unknown table " + table1 + " referenced in JOIN condition"
        query_tree.set_error(msg)
        $tj = None
    if table2 not in ($tablesSoFar + [$t1.text] + [$t2.text]):
        msg = "Unknown table " + table2 + " referenced in JOIN condition"
        query_tree.set_error(msg)
        $tj = None

if None in $j.table:
    $tj = None
};

joins_ [tablesSoFar] returns[table, terms, conectors]  : JOIN t=TABELA ON c=conditionsJoin j=joins_[$tablesSoFar + [$t.text]] {$table = $t.text
print($tablesSoFar)
$terms = [$c.terms] + $j.terms
$conectors = [$c.conectors] + $j.conectors
$table = [$t.text] + $j.table
for term in $c.terms:
    table1 = term[0].split('.')[0]
    table2 = term[2].split('.')[0]

    if table1 not in ($tablesSoFar + [$t.text]):
        msg = "Unknown table " + table1 + " referenced in JOIN condition"
        query_tree.set_error(msg)
        $table += [None]
    if table2 not in ($tablesSoFar + [$t.text]):
        msg = "Unknown table " + table2 + " referenced in JOIN condition"
        query_tree.set_error(msg)
        $table += [None]}
| {$table = []
$terms = []
$conectors = []};

//clausulaFrom[tablesSoFar] returns[tj, tables] : t1=TABELA ',' c=clausulaFrom[$tablesSoFar + [$t1.text]]{tab = Table($t1.text)
clausulaFrom[tablesSoFar] returns[tj, tables] : t1=TABELA ',' c=clausulaFrom[$tablesSoFar]{tab = Table($t1.text)

if $c.tj is None:
    join = None
else:
    join = ThetaJoinNode(tab, $c.tj, [','], [])
$tj = join
$tables = [$t1.text] + $c.tables}
| j=joins[$tablesSoFar] {$tj = $j.tj
$tables = $j.tables}
| j=joins[$tablesSoFar] ',' c=clausulaFrom[$j.tables + $tablesSoFar ] {

if $c.tj is None or $j.tj is None:
    $tj = None
else:
    $tj = ThetaJoinNode($j.tj, $c.tj, [','], [])
$tables = $j.tables + $c.tables}
| t=TABELA {table = Table($text)
$tj = table
$tables = [$t.text]};

termo returns[term] : t1=COLUNA o=comparisonOp t2=COLUNA {$term = ($t1.text,$o.text,$t2.text)}
| t=COLUNA o=comparisonOp a=ATRIBUTO {$term = ($t.text,$o.text,$a.text)};
conector : ('and' | 'or');


anythingElse returns[trailing_str] : t=.* {
$trailing_str = $t.text
 };



WS: [ \n\t\r]+ -> channel(HIDDEN);



SELECT : S E L E C T;
FROM   : F R O M;
WHERE  : W H E R E;
JOIN   : J O I N;
ON     : O N;

ATRIBUTO : ('\'' | '\"') ('a'..'z' |'A'..'Z' | ' ')+ ('\'' | '\"') | ('0' .. '9')+ ('.' ('0' .. '9')+ | );
COLUNA : ('a'..'z' |'A'..'Z' )('a'..'z' |'A'..'Z' | '0' .. '9'| '_' | '-')*'.'('a'..'z' |'A'..'Z' )('a'..'z' |'A'..'Z' | '0' .. '9'| '_' | '-')*;
TABELA : ('a'..'z' |'A'..'Z' )('a'..'z' |'A'..'Z' | '0' .. '9'| '_' | '-')*;





fragment A:('a'|'A');
fragment B:('b'|'B');
fragment C:('c'|'C');
fragment D:('d'|'D');
fragment E:('e'|'E');
fragment F:('f'|'F');
fragment G:('g'|'G');
fragment H:('h'|'H');
fragment I:('i'|'I');
fragment J:('j'|'J');
fragment K:('k'|'K');
fragment L:('l'|'L');
fragment M:('m'|'M');
fragment N:('n'|'N');
fragment O:('o'|'O');
fragment P:('p'|'P');
fragment Q:('q'|'Q');
fragment R:('r'|'R');
fragment S:('s'|'S');
fragment T:('t'|'T');
fragment U:('u'|'U');
fragment V:('v'|'V');
fragment W:('w'|'W');
fragment X:('x'|'X');
fragment Y:('y'|'Y');
fragment Z:('z'|'Z');
