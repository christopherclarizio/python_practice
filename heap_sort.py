import math

def heap_sort(arr):
	heapify(arr)

	end = len(arr)-1
	while(end > 0):
		swap(arr, 0, end)
		end = end-1
		sift_dowm(arr, 0, end)

def heapify(arr):
	start = parent(len(arr)-1)

	while(start >= 0):
		sift_dowm(arr, start, len(arr)-1)
		start = start-1

def sift_dowm(arr, start, end):
	root = start

	while(left_child(root) <= end):
		child = left_child(root)
		max_index = root
	
		if(arr[max_index] < arr[child]):
			max_index = child

		if(arr[child+1] <= end and arr[max_index] < arr[child+1]):
			max_index = child+1

		if(max_index == root):
			return
		else:
			swap(arr, max_index, root)
			root = max_index

def parent(i):
	return math.floor((i-1)/2)

def left_child(i):
	return 2*i+1

def right_child(i):
	return 2*i+2

def swap(arr, i0, i1):
	temp = arr[i0]
	arr[i0] = arr[i1]
	arr[i1] = temp


my_list = [1,3,2,5,4]
print(my_list)
heap_sort(my_list)
print(my_list)