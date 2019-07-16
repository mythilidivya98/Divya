/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>
struct Node
{
    int data;
    struct Node* next;
    
};
struct Node* root;
/*int length()
{
    int count=0;
    struct Node *temp;
    temp=root;
    while(temp!=NULL)
    {
        count++;
        temp=temp->link;
    }
    printf("%d",count);
}*/
void create()
{
    struct Node* temp;
    temp=(struct Node*)malloc(sizeof(struct Node));
    printf("Enter the data");
    scanf("%d",temp->data);
    if(temp==NULL)
    {
        root=temp;
    }
    else
    {
        struct Node* p;
        p=root;
        while(p->next==NULL)
        {
            p=p->next;
        }
        p->next=temp;
    }
}
void main()
{
    int a,b,c;
    struct Node* head=NULL;
    struct Node* second=NULL;
    struct Node* third=NULL;
    head=(struct Node*)malloc(sizeof(struct Node));
    second=(struct Node*)malloc(sizeof(struct Node));
    third=(struct Node*)malloc(sizeof(struct Node));
    scanf("%d %d %d",&a,&b,&c);
    head->data=a;
    head->next=second;
    second->data=b;
    second->next=third;
    third->data=c;
    third->next=NULL;
    printf("%d %d %d",head->data,second->data,third->data);
    create();
}
