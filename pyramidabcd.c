#include <stdio.h>
int main()
{
    int a,b=1;
    char k=65;
    scanf("%d",&a);
    for(int i=0;i<=a;i++)
    {
        for(int j=0;j<i;j++)
        {
            printf("\t");
        }
        for(int j=1;j<=a-i;j++)
        {
            printf("%c\t",k);
            k++;
            
            
        }
        k--;
        for(int j=a-i-1;j>=1;j--)
        {
            k--;
            printf("%c\t",k) ; 
           
        }
        printf("\n");
        
    }
}
