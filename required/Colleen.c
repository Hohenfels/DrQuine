#include<stdio.h>
/*
	42
*/
int foo(){return (0);}
int main()
{
	/*
		allo
	*/
	char *str = "#include<stdio.h>%c/*%c%c42%c*/%cint foo(){return (0);}%cint main()%c{%c%c/*%c%c%callo%c%c*/%c%cchar *str = %c%s%c;%c%cprintf(str, 10, 10, 9, 10, 10, 10, 10, 10, 9, 10, 9, 9, 10, 9, 10, 9, 34, str, 34, 10, 9, 10, 10);%c}%c";
	printf(str, 10, 10, 9, 10, 10, 10, 10, 10, 9, 10, 9, 9, 10, 9, 10, 9, 34, str, 34, 10, 9, 10, 10);
}
