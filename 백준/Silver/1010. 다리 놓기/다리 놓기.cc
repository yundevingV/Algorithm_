#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

double fact(int n)
{
	if (n == 0)
		return 1;
	return n * fact(n - 1);
}

double result(int n, int m)
{
	return (fact(n) / (fact(m) * fact(n - m)));
}
	int main() {

		int n;
		int m;
		int a;
		scanf("%d", &a);
		for (int i = 0; i < a; i++)
		{
			scanf("%d %d", &n, &m);
			printf("%.lf\n", result(m, n));
		}
		return 0;
	}

