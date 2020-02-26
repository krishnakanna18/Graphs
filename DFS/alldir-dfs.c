#include<stdio.h>
#include<string.h>
#include<stdlib.h>
struct node{
	char name[20];
	int visit;
	struct node *next;
};
struct node2
{
   char name[20];
   int visit;
   struct node *head;   	
}; 
typedef struct node2 *Adjlist;
struct node3{
	int vertices;
	Adjlist adjlist;
}; 

typedef struct node3 *Graph;
struct node* createNode(char *nm)
{
	struct node *temp=(struct node*)malloc(sizeof(struct node));
	strcpy(temp->name,nm);
	temp->visit=0;
	temp->next=NULL;
	return temp;
}
Adjlist createList(char *nm)
{
	Adjlist temp=(struct node2*)malloc(sizeof(struct node2));
	strcpy(temp->name,nm);
	temp->visit=0;
	temp->head=NULL;
	return temp;
}
Graph createGraph(int v)
{
   Graph graph=(struct node3*)malloc(sizeof(struct node3));
	graph->vertices=v;
	graph->adjlist=(struct node2*)malloc(v*sizeof(struct node2));
	for(int i=0; i<v; i++)
		graph->adjlist[i].visit=0;
	return graph;
}
Graph addEdge(Graph graph,char *nm1,char *nm2)
{   int pos1,pos2;
	for(int i=0; i<graph->vertices; i++)
	  if(strcmp(graph->adjlist[i].name,nm1)==0)
	    pos1=i;
	  else if(strcmp(graph->adjlist[i].name,nm2)==0)
	     pos2=i;
	printf("Creating Link From %s and %s\n",nm1,nm2);
    struct node *n1=createNode(nm2);
    n1->next=graph->adjlist[pos1].head;
    graph->adjlist[pos1].head=n1;
   printf(" %s\n",graph->adjlist[pos1].head->name);

   
     return graph;
}
void DFS(Graph graph,char *nm)
{   int pos;
    for(int i=0; i<graph->vertices; i++)
       if(strcmp(graph->adjlist[i].name,nm)==0)
           {
             pos=i;
             break;
            }
    
	if(graph->adjlist[pos].visit==0)
	  {  
	     graph->adjlist[pos].visit=1;
	     printf("%s ->",graph->adjlist[pos].name);
	     struct node *temp=graph->adjlist[pos].head;
	     while(temp!=NULL)
	     {
	        DFS(graph,temp->name);
	        temp=temp->next;
	     }
	     
	  }
}
void DFS_util(Graph graph)
{
  for(int i=0; i<graph->vertices; i++)
    { DFS(graph,graph->adjlist[i].name);
      printf("\n");
    }
}
void main()
{
	Graph graph;
	int v; char nm1[20],nm2[20],nm[20];
	printf("Enter the number of vertices");
	scanf("%d",&v);
	graph=createGraph(v);
	printf("Enter the names of all the vertices");
	for(int i=0; i<v; i++)
	 scanf(" %[^\n]",graph->adjlist[i].name);
	char ch;
	printf("\nAdd the edges\n");
	do
	{
       printf("Enter the names:\n");
       scanf(" %[^\n]",nm1);
       scanf(" %[^\n]",nm2);
       graph=addEdge(graph,nm1,nm2);
       printf("Do u wanna cntue:");
       scanf(" %c",&ch);
    }while(ch=='y');
   
    DFS_util(graph);
}
