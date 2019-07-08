#include <stdio.h>

void main()
{
    char a[50];
    char b[20];
    int i,j,d,g=0,k=0,l,diff;
    scanf("%s",&a);
    scanf("%s",&b);
    for (i = 0; a[i] != '\0'; ++i)
    {
     g=i;
    }
    for (j = 0; b[j] != '\0'; ++j)
    {
     k=j;
    }
    l=g>k?g:k;
    for (d = 0; d < l;d++)
    {
      if(a[d]==b[d])
      {
          continue;
      }
      else
      {
          diff=a[d]-b[d];
          break;
      }
    }
    if(d==g)
    {
    printf("Equal");
    }
    else
    {
        printf("not equal=%d",diff);
    }
    
    
}
