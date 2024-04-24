%{
#include <stdio.h> 
#include <y.tab.h>
%}
%token NUMBER 
%%
program: { printf("Result: %d\n", $2); }
expr: expr '+' term { $$ = $1 + $3; } 
    | term { $$ = $1; }
term: NUMBER { $$ = $1; }
%%
int yywrap() {
    return 1;
}

int main() {
    yyparse();
    return 0;
}
