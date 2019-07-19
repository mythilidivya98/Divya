#include <stdio.h>

void main()
{
    
    int a,sum=0,g,b;
    scanf("%d",&a);
    g=a;
    while(a>0)
    {
    b=a%10;
    sum=sum+(b*b*b);
    a=a/10;
    }
    if(g==sum)
    {
        printf("AMSTRONG NUMBER");
    }
    else
    {
        printf("NOT A AMSTRONG NUMBER");
    }
}
