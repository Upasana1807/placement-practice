#include <stdio.h>

int main() {
	// your code goes here
    int a,a1;
    scanf("%d", &a);
    int n=0;
    a1=a;
    while(a!=0){
        n= (n*10)+(a%10);
        a/=10;
    }
    if(n==a1){
        printf("Palindrome");
    }
    else{
        printf("Not Palindrome");
    }
}

