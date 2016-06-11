grammar SQL;

options{
    language=Python3;
}

@header{
print("Helllo")
}


sql_expr locals [lista = []]
@init{
number = 0
print("Nasd")
}
@after{
print("Found "+ str(number) + " conditions on where")
}: SELECT {print ($SELECT.text);$lista += [1];print($lista)}  clausulaSelect FROM  clausulaFrom w=where {number = $w.number;print($w.bla)}
        ;


comparisonOp: '>='|'<='| '>'| '<' | '=';

conditionsWhere returns[number]
: (COLUNA | ATRIBUTO) comparisonOp (COLUNA | ATRIBUTO) 'and' c1=conditionsWhere {$number = $c1.number + 1}
|  (COLUNA | ATRIBUTO) comparisonOp (COLUNA | ATRIBUTO) 'or' c1=conditionsWhere  {$number = $c1.number + 1}
| (COLUNA | ATRIBUTO) comparisonOp (COLUNA | ATRIBUTO) {$number = 1} ;

where returns[number, bla]
: WHERE conditionsWhere {$number = $conditionsWhere.number
$bla = "asd"}
   | {$number = 0};

clausulaSelect : COLUNA ',' c1=clausulaSelect {print("Coluna " + $clausulaSelect.text)}| COLUNA;

conditionsJoin : COLUNA '=' COLUNA 'and' conditionsJoin {print($text)} | COLUNA '=' COLUNA {print($text)};

joins : TABELA JOIN TABELA ON conditionsJoin joins_ ;
joins_: JOIN TABELA ON conditionsJoin
        | ;

clausulaFrom : TABELA ',' clausulaFrom | joins | joins ',' clausulaFrom | TABELA;


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
