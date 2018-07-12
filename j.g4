//	Define a grammar called J
grammar j;

compilationUnit:
	 ('package' qualifiedIdentifier ';')? ('import' qualifiedIdentifier ';')* (type2Declaration)* EOF
	;

qualifiedIdentifier:
	ID (',' ID)*
	;

type2Declaration:
	modifiers classDeclaration
	;

modifiers:
	 ('public' | 'protected' | 'private' | 'static' | 'abstratc')*
	;

classDeclaration:
	'class' ID ('extends' qualifiedIdentifier)? classBody
	;

classBody:
	'{' (modifiers memberDecl)* '}'
	;

memberDecl:
	ID formalParameters block  // construtor
	| ('void' | 'type2') ID formalParameters (block | ';') // metodo
	| type2 variableDeclarators ';' // campos
	;

block:
	'{' (blockStatement)* '}'
	;

blockStatement:
	localVariableDeclarationStatement
	| statement
	;

statement:
	block
	| ID ':' statement
	| 'if' parExpression statement ('else' statement)?
	| 'while' parExpression statement
	| 'return' (expression)? ';'
	| ';'
	| statementExpression  ';'
	;

formalParameters:
	'(' (formalParameter (',' formalParameter)*)?  ')'
	;

formalParameter:
	type2 ID
	;

parExpression:
	'(' expression ')'
	;

localVariableDeclarationStatement:
	type2 variableDeclarators ';'
	;

variableDeclarators:
	variableDeclarator (',' variableDeclarator)*
	;

variableDeclarator:
	ID ('=' variableInitializer)?
	;

variableInitializer:
	arrayInitializer
	| expression
	;

arrayInitializer:
	'{' (variableInitializer (',' variableInitializer)*)? '}'
	;

arguments:
	'(' (expression (',' expression)*)? ')'
	;

type2:
	referenceType
	| basicType
	;

basicType:
	'boolean'
	| 'char'
	| 'int'
	;

referenceType:
	basicType '[' ']' ('[' ']')*
	| qualifiedIdentifier ('[' ']')*
	;

statementExpression:
	expression
	;

expression:
	assignmentExpression
	;

assignmentExpression:
	conditionalAndExpression (('=' | '+=') assignmentExpression)?
	;

conditionalAndExpression:
	equalityExpression ('&&' equalityExpression)*
	;

equalityExpression:
	relationalExpression ('==' relationalExpression)*
	;

relationalExpression:
	additiveExpression (('>' | '<=') additiveExpression | 'instanceof' referenceType)?
	;

additiveExpression:
	multiplicativeExpression (('+' | '-') multiplicativeExpression)*
	;

multiplicativeExpression:
	unaryExpression ('*' unaryExpression)*
	;

unaryExpression:
	'++' unaryExpression
	| '-' unaryExpression
	| simpleUnaryExpression
	;

simpleUnaryExpression:
	'!' unaryExpression
	| '(' basicType ')' unaryExpression
	| '(' referenceType ')' simpleUnaryExpression
	| postfixExpression
	;

postfixExpression:
	primary (selector)* ('--')*
	;

selector:
	'.' qualifiedIdentifier (arguments)?
	| '[' expression ']'
	;

primary:
	parExpression
	| 'this' (arguments)?
	| 'super' (arguments | '.' ID (arguments)?)
	;

creator:
	(basicType | qualifiedIdentifier) '(' arguments | '[' ']' ('[' ']')* (arrayInitializer)? | newArrayDeclarator ')'
	;

newArrayDeclarator:
	'[' expression ']' ('[' expression ']')* ('[' ']')*
	;

literal:
	INT_LITERAL
	| CHAR_LITERAL
	| STRING_LITERAL
	| 'true'
	| 'false'
	| 'null'
	;

fragment DIGIT: [0-9] ;
NUMBER: DIGIT+ ([.,] DIGIT+)? ;
ID : ('a'..'z'|'A'..'Z')+  ;
INT_LITERAL: '0' | [1-9][0-9]* ;
CHAR_LITERAL: ;
STRING_LITERAL: ;
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines