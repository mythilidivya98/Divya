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
    if(d==l)
    {
    printf("Equal");
    }
    else
    {
        if(diff>0)
        {
            printf("1st string is greater than 2nd string");
        }
        else
        {
        printf("2nd string is greater than 1st string");
        }
    }
    
    
    
}
