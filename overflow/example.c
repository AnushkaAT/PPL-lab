#include<stdio.h>
void function(){
	int a;
	int *ret = &a + 30;
	(*ret) = 4199822;
}

void main(){
	int x=0;
	function();
	x=1; //skipped
	printf("%d\n", x);
}