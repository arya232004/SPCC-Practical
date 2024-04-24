%{
    #include<stdio.h>
    int yywrap();
%}

%% 
[-+*/=<>!&|^]+  {printf("operators are: %s\n",yytext);}
.
%%

int yywrap(){
    return 1;
}


int main(){
    yylex();
    return 0;
}