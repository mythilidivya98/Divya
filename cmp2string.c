#include <stdio.h>

void main()
{
    char a[50];
    char b[20];
    int i,j,d,g=0,k=0;
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
    if(i==j)
    {
    for (d = 0; d < g;d++)
    {
      if(a[d]==b[d])
      {
          continue;
      }
    }
    printf("Equal");
    }
    else
    {
        if(g>k)
        {
            printf("1st String is Greater than 2nd");
        }
        else
        {
            printf("2nd String is Greater than 1st");
        }
        
    }
    
}
