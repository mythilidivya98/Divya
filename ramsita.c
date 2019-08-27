 # include<stdio.h>
void main() 
{
    int a;
  	int count=0,coun=0;
    int n;
  	scanf("%d %d",&a,&n);
    int b[n];
  	while(a-- >0)
    {
      for(int i=0;i<n;i++)
      {
        scanf("%d",&b[i]);
      }
      for(int i=0;i<n;i++)
      {
        if(b[i]==1)
        {
          count=count+1;
        }
        if(b[i]==0)
        {
          coun=coun+1;
          
        }}
      printf("SITA:%d",count);
      printf("RAM:%d\n",coun);
      count=0;
      coun=0;
}}
