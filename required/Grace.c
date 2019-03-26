#include <stdio.h>
#include <stdlib.h>
#define allo
#define oskour
#define FT(x) int main(){FILE *f = NULL; char *str = "#include <stdio.h>%c#include <stdlib.h>%c#define allo%c#define oskour%c#define FT(x) int main(){FILE *f = NULL; char *str = %c%s%c; f = fopen(%cGrace_kid.c%c, %cw%c); if (f){fprintf(f, str, 10, 10, 10, 10, 34, str, 34, 34, 34, 34, 34, 10, 10, 10, 10, 10);}}%c/*%c    42%c*/%cFT(x)%c"; f = fopen("Grace_kid.c", "w"); if (f){fprintf(f, str, 10, 10, 10, 10, 34, str, 34, 34, 34, 34, 34, 10, 10, 10, 10, 10);}}
/*
    42
*/
FT(x)
