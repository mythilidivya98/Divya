#include <stdio.h>

void main()
{
    int a,temp,fact,n,m,sum,ab;
    for(int j=1;j<=100000;j++)
    {
        ab=j;
        sum=0;
        while(ab>0)
        {
            fact=1;
            n=ab%10;
            for(int i=1; i<=n;i++)
            {
                fact = fact * i;
            }
            sum=sum+fact;
            ab=ab/10;
        }
        if(sum==j)
        {
            printf("%d\t",j);
        }
        
    }
}
