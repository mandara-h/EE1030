#include <stdio.h>
#include <stdlib.h>

double **createMat(int m,int n) {
	int i;
	double **a;
	a = (double **)malloc(m * sizeof( *a));
	for (i=0; i<m; i++)
		a[i] = (double *)malloc(n * sizeof( *a[i]));
	return a;
}

int checkLin(){
	double A[3] = {-2,3,5}, B[3] = {1,2,3}, C[3] = {7,0,-1};
	double **M = createMat(2, 3);
	for(int i=0; i<3; i++){
		M[0][i] = B[i] - A[i];
		M[1][i] = C[i] - A[i];
	}
	double k = M[1][0] / M[0][0];
	for(int i=0; i<3; i++){
		M[1][i] -= k * M[0][i];
	}
	if(M[1][0]==0){
		if(M[1][1]==0){
			if(M[1][2]==0){
				printf("The given 3 points are collinear");
				return 1;
			}
		}
	}
	else{
		printf("The given 3 points are not collinear");
		return 0;
	}
}
