%{
  int counter=0;   
  int yywrap(); 
%}

%% 
[a-zA-Z]+ {
    if (yyleng > counter){
        counter=yyleng;
    }
}
%%

int yywrap(){
    return 1;
}

int main(){
    yylex();
    printf("Length is %d",counter);
    return 0;
}
