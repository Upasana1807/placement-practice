#include <stdio.h>

int findLCM(int num1, int num2, int num3) {
    // Write your code here
    int max=0;
    max= (num1>num2)? ((num1>num3)? num1:num3): ((num2>num3)? num2:num3);
    for (int i = max; i <= num1*num2*num3; i+=max) {
        if (i % num1 == 0 && i % num2 == 0 && i % num3 == 0) {
            return i;
        }
    }
}

int main() {
    int num1, num2, num3;
    
    printf("Enter three numbers: ");
    scanf("%d %d %d", &num1, &num2, &num3);
    
    int lcm = findLCM(num1, num2, num3);
    
    printf("%d", lcm);
    
    return 0;
}