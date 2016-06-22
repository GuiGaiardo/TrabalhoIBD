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
@after{
print("Found "+ str(number) + " conditions on where")
}: SELECT sl=clausulaSelect FROM  fr=clausulaFrom w=where {number = $w.number
projection = ProjectionNode($sl.columns)
selection = SelectionNode($w.terms, $w.conectors)
theta_join = $fr.tj
query_tree.set_root(projection)
node = query_tree.root
node.set_child(selection)
node = node.children
node.set_child(theta_join)
}
        ;


comparisonOp: '>='|'<='| '>'| '<' | '=';

conditionsWhere returns[number, terms, conectors]
: t=termo c=conector cnd=conditionsWhere {$number = $cnd.number + 1
$terms = $cnd.terms
$terms.append($t.term)
$conectors = $cnd.conectors
$conectors.append($c.text)}
| t=termo {$number = 1
print(str($t.term))
$terms = [$t.term]
$conectors = []} ;

where returns[number, terms, conectors]
: WHERE c=conditionsWhere {$number = $conditionsWhere.number
$terms = $c.terms
$conectors = $c.conectors}
   | {$number = 0};

clausulaSelect returns[columns] : c=COLUNA ',' c1=clausulaSelect {$columns = $c1.columns
$columns.append($c.text)}| COLUNA {$columns = [$text]};

conditionsJoin returns[terms, conectors] : c1=COLUNA '=' c2=COLUNA c=conector cnd=conditionsJoin {$terms = $cnd.terms
$terms.append($c1.text + "=" + $c2.text)
$conectors = $cnd.conectors
$conectors.append($c.text)}
| COLUNA '=' COLUNA {$terms = [$text]
$conectors = []};

joins returns[tj] : t1=TABELA JOIN t2=TABELA ON c=conditionsJoin j=joins_ {join1 = ThetaJoinNode(Table($t1.text), Table($t2.text), $c.terms, $c.conectors)
if ($j.table == None):
    $tj = join1
else:
    $tj = ThetaJoinNode(join1, $j.table, $j.terms, $j.conectors)};
joins_ returns[table, terms, conectors] : JOIN t=TABELA ON c=conditionsJoin {$table = $t.text
$terms = $c.terms, $conectors = $c.conectors}
| {$table = None
$terms = None
$conectors = None};

clausulaFrom returns[tj] : t1=TABELA ',' c=clausulaFrom {tab = Table($t1.text)
join = ThetaJoinNode(tab, $c.tj, [','], [])
$tj = join}
| j=joins {$tj = $j.tj}
| j=joins ',' c=clausulaFrom {$tj = ThetaJoinNode($j.tj, $c.tj, [','], [])}
| TABELA {table = Table($text)
$tj = table};

termo returns[term] : t1=COLUNA o=comparisonOp t2=COLUNA {$term = ($t1.text,$o.text,$t2.text)}
| t=COLUNA o=comparisonOp a=ATRIBUTO {$term = ($t.text,$o.text,$a.text)};
conector : ('and' | 'or');



WS: [ \n\t\r]+ -> channel(HIDDEN);



SELECT : S E L E C T;
FROM   : F R O M;
WHERE  : W H E R E;
JOIN   : J O I N;
ON     : O N;

ATRIBUTO : '\'' ('a'..'z' |'A'..'Z' )+ '\'' | ('0' .. '9')+ ('.' ('0' .. '9')+ | );
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
