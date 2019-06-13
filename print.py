#include<stdio.h>
int main()
{
int n1,a[10000],f=0;
scanf("%d",&n1);
for(int i=0;i<n1;i++)
scanf("%d",&a[i]);
for(int i=0;i<n1;i++)
{
if(a[i]==i)
{
  f=1;
printf("%d ",a[i]);
}
}
  if(f==0)
printf("-1");
}
