#include <stdio.h>
void main()
{
   int a=0,b=1,c,k,l;
   printf("ENTER THE STARTING AND ENDING POSITION:");
   scanf("%d %d",&k,&l);
   for(int i=k;(a+b)<l;i++)
   {
       c=a+b;
       printf("%d\t",c);
       a=b;
       b=c;
   }
   
}
