%{
    #include<stdio.h>
    int i;
    int flag;
    int yywrap();
%}

%%
[0-9]+ {
    flag=0;
    i=atoi(yytext);
    for (int j=2; j<i;j++){
        if(i % j == 0){
            flag=1;
            break;
        }
    }
    if(flag == 0){
        printf("Prime");
    }
    else{
        printf("Not a prime");
    }
}
%%
int yywrap(){
    return 1;
}

int main(){
    yylex();
    return 0;
}
