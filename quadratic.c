#include <stdio.h>
#include <math.h>

int getInteger();
double getDelta(int a, int b, int c);

void main()
{
    int a, b, c;
    double delta, root1, root2;
    printf("Let's solve a quadratic equation.\n");
    printf("\nPlease input a:");
    a = getInteger();

    printf("\nPlease input b:");
    b = getInteger();

    printf("\nPlease input c:");
    c = getInteger();

    delta = getDelta(a, b, c);

    root1 = (-b + delta) / (2 * a);
    root2 = (-b - delta) / (2 * a);

    printf("\nThe root1 = %.02lf\n", root1);
    printf("The root2 = %.02lf\n", root2);
    printf("Thanks for using our super equation solver!\n");
}

int getInteger()
{
    int i;
    scanf("%d", &i);
    return i;
}

double getDelta(int a, int b, int c)
{
    return sqrt(b * b - 4 * a * c);
}