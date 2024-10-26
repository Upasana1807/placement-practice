#include <stdio.h>

int main() {
	// your code goes here
    int a;
    scanf("%d", &a);
    if(((a%100==0) && (a%400==0) && (a%4!=0)) || ((a%4==0) && (a%100!=0))){
        printf("Leap Year");
    }
    else{
        printf("Not Leap Year");
    }
}

