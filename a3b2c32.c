#include <stdio.h>

void main()
{
   char a[20],b[20][20],c[20][20],d[20];
   int i,l,j=0,k=0,g=0,nc=0,cc=0,sc=0;
   scanf("%s",a);
   for (i = 0; a[i] != '\0'; i++)
    {
     l=i+1;
    }
   for (i = 0; i < l;i++)
    {
      if((a[i]>='a' && a[i]<='z') || (a[i]>='A' && a[i]<='Z'))
      {
        if((nc!=0 ||j!=0)&&(k==0))
        {
         c[nc][j]='\0';
         j=0;
        
         nc++;
        }
        b[sc][k]=a[i];
        k++;
      }
      else if(a[i]>='0' && a[i]<='9')
      {
          if(j==0)
          {
        b[sc][k]='\0';
        sc++;
        k=0;
          }
        c[nc][j]=a[i];
        j++;
      }
      /*else
      {
        b[sc][j]='\0';
        j=0;
        sc++;
        c[nc][k]='\0';
        nc++;
        k=0;
        d[g]=a[i];
        g++;
      }*/
    }
    d[g]='\0';
    b[sc][k]='\0';
    c[nc][j]='\0';
    printf("\nString\n");
    for(i=0;i<sc;i++)
    {
    printf("%s\t",b[i]);
    }
    printf("\nNumbers\n");
    for(i=0;i<=nc;i++)
    {
    printf("%s\t",c[i]);
    }
    printf("\n%s",d);
    for(k=0;k<=nc;k++)
    {
    for(i=0;i<atoi(c[k]);i++)
    {
        printf("\t%s",b[k]);
    }
    printf("\n");
    }
    
    
}
