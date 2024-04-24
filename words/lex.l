%{
#include <stdio.h>
int counter = 0;
int yywrap();
%}

%%
[a-zA-Z]+ {
    if (yyleng > counter) {
        counter = yyleng;
    }
}
%%

int yywrap() {
    return 1; 
}

int main() { 
    yylex(); 
    printf("largest: %d", counter); 
    printf("\n"); 
    return 0;
}
