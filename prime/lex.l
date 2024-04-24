%{
#include <stdio.h>
int yywrap();
#include <stdlib.h>
%}

%%
[0-9]+ {
    int c = atoi(yytext);
    int flag = 0; // Initialize flag
    if (c == 2) {
        printf("\n Prime number");
    } else if (c == 0 || c == 1) {
        printf("\n Not a Prime number");
    } else {
        for (int j = 2; j < c; j++) {
            if (c % j == 0) {
                flag = 1;
                break;
            }
        }
        if (flag == 1) {
            printf("\n Not a prime number");
        } else {
            printf("\n Prime number");
        }
    }
}
. {
    printf("\n Invalid input"); // Handle non-numeric input
}
%%
int yywrap() {
    return 1; 
}
int main() {
    yylex();
    return 0;
}
