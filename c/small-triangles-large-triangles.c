#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct triangle
{
	int a;
	int b;
	int c;
};

typedef struct triangle triangle;


double area(triangle *t){
    double p = (t->a+t->b+t->c)/2;
    double arg = p*(p-t->a)*(p-t->b)*(p-t->c); 
    return sqrt(arg);
}

int cmpfunc (const void* a, const void* b) {
    return area((triangle*)a) - area((triangle*)b);
   //return ( *(int*)a - *(int*)b );
}

void sort_by_area(triangle* tr, int n) {
	/**
	* Sort an array a of the length n
	*/
    qsort(tr, n, sizeof(triangle), cmpfunc);
}

int main()
{
	int n;
	scanf("%d", &n);
	triangle *tr = malloc(n * sizeof(triangle));
	for (int i = 0; i < n; i++) {
		scanf("%d%d%d", &tr[i].a, &tr[i].b, &tr[i].c);
	}
	sort_by_area(tr, n);
	for (int i = 0; i < n; i++) {
		printf("%d %d %d\n", tr[i].a, tr[i].b, tr[i].c);
	}
	return 0;
}