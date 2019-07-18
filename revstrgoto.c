#include <stdio.h>

void main()
{
    int i;
    char ch[4];
    scanf("%s",&ch);
    i=4;
    t1:
    if(i>=0)
    {
    printf("%c",ch[i]);
    i--;
    }
    if(i>=0)
    {
    goto t1;
    }
}
