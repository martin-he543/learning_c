#include <stdio.h>
#include <math.h>

void main(){
    char input[80];
    int x, a, b, c;
    printf("Please input your name!\n");
    scanf("%s", input);
    printf("Hello %s!\n", input);

    printf("Please input your age\n");
    scanf("%d", &x);
    printf("You are %d years old!\n", x);

    printf("%.02f\n", sqrt(x));
    


}
