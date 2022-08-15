#include <stdio.h> // include standard input/output library

int main(int argc, char *argv[]) // create "main" function, the first function C programs run.
{ // This function needs to return an int, and takes in two parameters: an int, an array of chars
    int distance = 100; // variable declaration:    TYPE name = VALUE; 

    printf("You are %d miles away.\n", distance); // PRINTF can take multiple arguments
    return 0; // UNIX uses return codes
}

/* In order to run:

make filename
./filename

*/
