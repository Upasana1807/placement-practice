#include <stdio.h>

int main() {
	// your code goes here
    int a;
    scanf("%d", &a);
    int n=0;
    while(a!=0){
        n= (n*10)+(a%10);
        a/=10;
    }
    printf("%d", n);
}

