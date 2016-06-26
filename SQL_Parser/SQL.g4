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
}
: SELECT sl=clausulaSelect FROM  fr=clausulaFrom[ [] ] w=where {projection = ProjectionNode($sl.columns)
theta_join = $fr.tj

selectingTables = [x.split('.')[0] for x in $sl.columns]
whereTables = [x[0].split('.')[0] for x in $w.terms]
valid_query = 1

for t in selectingTables:
    if(not t in $fr.tables):
        print("Selecting unknow table " + t)
        valid_query = 0
        projection = None

for t in whereTables:
    if(not t in $fr.tables):
        print("Unknown table " + t + " being used in where clause")
        valid_query = 0
        projection = None

if valid_query:
    if len($w.terms) > 0:
        selection = SelectionNode($w.terms, $w.conectors)
        selection.set_child(theta_join)
        projection.set_child(selection)

    else:
        projection.set_child(theta_join)

else:
    projection = None

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
$tables = [$t1.text, $t2.text]
if ($j.table == []):
    $tj = join1
else:
    last_join = join1
    for i in range(len($j.table)):
        print($j.terms[i])
        last_join = ThetaJoinNode(last_join, Table($j.table[i]), $j.terms[i], $j.conectors[i])
    $tj = last_join
    #$tj = ThetaJoinNode(join1, Table($j.table[i]), $j.terms, $j.conectors)
    #$tables += [$j.table]

for term in $c.terms:
    table1 = term[0].split('.')[0]
    table2 = term[2].split('.')[0]
    if table1 not in ($tablesSoFar + [$t1.text] + [$t2.text]):
        print("Unknown table " + table1 + " referenced in JOIN condition")
    if table2 not in ($tablesSoFar + [$t1.text] + [$t2.text]):
        print("Unknown table " + table2 + " referenced in JOIN condition")
};

joins_ [tablesSoFar] returns[table, terms, conectors]  : JOIN t=TABELA ON c=conditionsJoin j=joins_[$tablesSoFar + [$t.text]] {$table = $t.text
$terms = [$c.terms] + $j.terms
$conectors = [$c.conectors] + $j.conectors
$table = [$t.text] + $j.table
for term in $c.terms:
    table1 = term[0].split('.')[0]
    if table1 not in ($tablesSoFar + [$t.text]):
        print("Unknown table " + table1 + " referenced in JOIN condition")}
| {$table = []
$terms = []
$conectors = []};

clausulaFrom[tablesSoFar] returns[tj, tables] : t1=TABELA ',' c=clausulaFrom[$tablesSoFar + [$t1.text]]{tab = Table($t1.text)
join = ThetaJoinNode(tab, $c.tj, [','], [])
$tj = join
$tables = [$t1.text] + $c.tables}
| j=joins[$tablesSoFar] {$tj = $j.tj
$tables = $j.tables}
| j=joins[$tablesSoFar] ',' c=clausulaFrom[$j.tables + $tablesSoFar ] {$tj = ThetaJoinNode($j.tj, $c.tj, [','], [])
$tables = $j.tables + $c.tables}
| t=TABELA {table = Table($text)
$tj = table
$tables = [$t.text]};

termo returns[term] : t1=COLUNA o=comparisonOp t2=COLUNA {$term = ($t1.text,$o.text,$t2.text)}
| t=COLUNA o=comparisonOp a=ATRIBUTO {$term = ($t.text,$o.text,$a.text)};
conector : ('and' | 'or');



WS: [ \n\t\r]+ -> channel(HIDDEN);



SELECT : S E L E C T;
FROM   : F R O M;
WHERE  : W H E R E;
JOIN   : J O I N;
ON     : O N;

ATRIBUTO : ('\'' | '\"') ('a'..'z' |'A'..'Z' | ' ')+ ('\'' | '\"') | ('0' .. '9')+ ('.' ('0' .. '9')+ | );
COLUNA : ('a'..'z' |'A'..'Z' )('a'..'z' |'A'..'Z' | '0' .. '9')*'.'('a'..'z' |'A'..'Z' )('a'..'z' |'A'..'Z' | '0' .. '9')*;
TABELA : ('a'..'z' |'A'..'Z' )('a'..'z' |'A'..'Z' | '0' .. '9')*;


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
