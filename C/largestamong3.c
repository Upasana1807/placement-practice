#include <stdio.h>

int main() {
	// your code goes here
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    printf("%d", ((a>b)?((a>c)?a:c):((b>c)?b:c)));
}

