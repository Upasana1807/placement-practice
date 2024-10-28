#include <stdio.h>

int main() {
	// your code goes here
    int a;
    scanf("%d", &a);
    int sum=0;
    while(a!=0){
        sum+= (a%10);
        a/=10;
    }
    printf("%d", sum);
}

