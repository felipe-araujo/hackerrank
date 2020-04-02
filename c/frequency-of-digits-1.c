#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    char num[10001];
    scanf("%s", num);
    int freq[10];
    for(int i = 0; i< 10; i++){
        freq[i] = 0;
    }

    for(int i=0; i<strlen(num); i++) {
        char c = num[i];
        if(c>=48 && c <=57){
            int j = c-48;
            freq[j] +=1;
        }
        
    }

    for(int i = 0; i< 10; i++){
        printf("%d ", freq[i]);
    }

    return 0;
}
