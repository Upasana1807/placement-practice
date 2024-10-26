#include <stdio.h>

int main() {
	// your code goes here
    int a,a1;
    scanf("%d", &a);
    a1=a;
    int sum=0;
    int digit=0;
    while(a!=0){
        digit= a%10;
        int facto=1;
        while(digit!=0){
            facto*=digit;
            digit--;
        }
        sum+=facto;
        a/=10;
    }
    if(sum==a1){
        printf("Strong Number");
    }
    else{
        printf("Not Strong Number");
    }
}

