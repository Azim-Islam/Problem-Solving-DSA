#include <stdio.h>

int main()
{
    char string[50];
    gets(string);
    for(int i = 0; string[i] != '\0' ; i++){
        if(string[i] == 32){
            string[i] = 45;
        }
        if(string[i] == 9){
            string[i] = 35;
        }
        if(string[i] >= 48 && string[i] <= 57){
            string[i] = 47;
        }
    }

    printf("%s", string);
}