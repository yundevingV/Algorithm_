#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int main() {
	
	int a;
	int b, c; 
	scanf("%d", &a);

	for (int i = 0; a > i; i++)
	{
		scanf("%d %d", &b, &c);
		printf("%d\n", b + c);

	}

	return 0;
}

