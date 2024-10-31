#include <stdio.h>

int *createMat(int x, int y, int z) { 
    static int coordinates[3];  // Static array to store coordinates

    coordinates[0] = x;
    coordinates[1] = y;
    coordinates[2] = z;

    return coordinates;
}
