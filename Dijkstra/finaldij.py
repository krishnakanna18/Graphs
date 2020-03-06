from gheap import *
from collections import defaultdict

def initialise(graph,dist,pre,src):
	dist[src][1]=0
	pre[src]=src
	dheap=heaps(len(vertices)+1,dist)
	return dheap
def path(graph,pre,i):
	if(pre[i]==i):
		# print(i,end='->')
		return
	else:
		path(graph,pre,pre[i])
		print(pre[i],end='->')
	# print(" Distance:",res[i])



def dijkstra(graph,dheap,src):
	global pre
	res=defaultdict()
	# result=heaps(dheap.size,[])
	while(dheap.size>1):
		min=dheap.extractmin()
		# res.append(min)
		d=min[1]
		res[min[0]]=d
		# dheap.show()
		# print("Min:",min,end=' ')
		# print(":",dheap.arr)
		for v in graph[min[0]]:
			if(dheap.map(v)!=None):
				if(min[1]+graph[min[0]][v]<dheap.arr[dheap.map(v)][1]):
					dheap.arr[dheap.map(v)][1]=min[1]+graph[min[0]][v]
					pre[v]=min[0]
					dheap.decreasekey(dheap.map(v),dheap.arr[v][1])
		# 			print(v,end=' ')
		# 			print(":",dheap.arr,":",dheap.index)
		# print()
	# print(pre,res)
	for i in range(1,len(pre)):
		if(res[i]!=math.inf):
			print("Path from",src,"to",i,end=':  ')
			path(graph,pre,i)
			print(i,end=' ')
			pr="Distance "+str(res[i])
			print(pr.rjust(30))
graph=defaultdict(dict)
vertices=[]
with open("inp.txt") as f:
	for line in f:
		(a,b,c)=(int(w) for w in line.split( ))
		if a not in graph:
			graph[a]=dict()
			graph[a][b]=c
		else:
			graph[a][b]=c
		if a not in vertices:
			vertices.append(a)
		if b not in vertices:
			vertices.append(b)
# print(graph,vertices)
(dist,pre)=([[i,math.inf] for i in range(len(vertices)+1)],[math.inf for i in range(len(vertices)+1)])
dist[0]=pre[0]=-1
dheap=initialise(graph,dist,pre,1)
# print(dist,pre)
dijkstra(graph,dheap,1)






