import math
class heaps(object):
	__slots__=['size','arr','index']
	def __init__(self,size,arr):
		self.size=size
		self.arr=arr
		self.index=[-1]+[i for i in range(1,self.size)]
		self.buildminheap()
	def minheapify(self,i):
		l=2*i
		r=2*i+1
		if(l<self.size and self.arr[l][1]<self.arr[i][1]):
			mini=l
		else:
			mini=i
		if(r<self.size and self.arr[r][1]<self.arr[mini][1]):
			mini=r
		if(mini!=i):
			self.index[i]=self.arr[mini][0]
			self.index[mini]=self.arr[i][0]
			self.arr[i],self.arr[mini]=self.arr[mini],self.arr[i]
			self.minheapify(mini)
	def buildminheap(self):
		hs=self.size//2
		for i in range(hs,0,-1):
			self.minheapify(i)
		# self.show()
		print(self.index)
	def extractmin(self):
		emin=self.arr[1]
		self.index[1]=self.index[self.size-1]

		mini=self.arr[1]
		self.arr[1]=self.arr[self.size-1]
		self.size-=1
		self.minheapify(1)
		return emin
	def decreasekey(self,i,key):
		if(self.arr[i][1]<key):
			# print("Can't do....key less")
			return
		self.arr[i][1]=key
		parent=i//2
		while(i>1 and self.arr[parent][1]>self.arr[i][1]):
			self.index[parent],self.index[i]=self.index[i],self.index[parent]
			self.arr[parent],self.arr[i]=self.arr[i],self.arr[parent]
			i=parent
			parent=parent//2
	def mininsert(self,key):
		self.size+=1
		new=self.arr+[0]
		self.arr=new
		self.arr[self.size-1]=math.inf
		self.decreasekey(self.size-1,key)
		self.show()
	def map(self,k):
		for i in range(1,self.size):
			if(self.index[i]==k):
				return i
	def show(self):
		print()
		print("Resultant array: ")
		for i in range(1,self.size):
			print(self.arr[i])
		print("Index array:")
		for i in range(self.size):
			print(self.index[i],end=',')
