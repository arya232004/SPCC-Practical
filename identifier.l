%{
#include <stdio.h> 
int yywrap();
%}

%%
[a-zA-Z_][a-zA-Z0-9_]* {
    printf("Valid Identifier\n");
}

. {
    printf("Invalid Identifier\n");
}

%%

int main() {
    yylex();
    return 0;
}

int yywrap() {
    return 1; // Indicate end of input
}
