%{
#include<stdio.h>
int yywrap();
%}

%%
^[a-zA-Z][a-zA-Z0-9]* {printf("valid");}
^[^a-zA-Z] {printf("invalid");}
if|else  {printf("keyword");}
%%

int yywrap(){
    return 1;
}

int main(){
    yylex();
    return 0;
}
