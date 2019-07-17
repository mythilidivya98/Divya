#include <stdio.h>

void main()
{
  int a,b;
  scanf("%d %d",&a,&b);
  printf("BEFORE SWAPPING\n");
  printf("%d %d",a,b);
  a=a+b;
  b=a-b;
  a=a-b;
  printf("\nAFTER SWAPPING\n");
  printf("%d %d",a,b);
        
 
}
