#Stack -> LIFO
#Queue -> FIFO


def Stack_ByList(arr, action=None, data=None):

	if action == 'Add' and data is not None:
		print("The following element " + str(data) + " has been added in the Stack")
		arr.insert(0, data)

	if action == 'Remove':
		if len(arr) == 0:
			print("The Stack is Empty")
			return None


		print("The following element " + str(arr[0]) + " has been removed from the Stack")
		arr.pop(0)



def Queue_ByList(arr, action=None, data=None):

	if action == 'Add' and data is not None:
		print("The following element " + str(data) + " has been added in the Queue")
		arr.append(data)

	if action == 'Remove':
		if len(arr) == 0:
			print("The Queue is Empty")
			return None


		print("The following element " + str(arr[0]) + " has been removed from the Queue")
		arr.pop(0)



print("-------------------------------------------")
print('STACK IMPLEMENTATION USING ARRAY')
print("-------------------------------------------")
arr = [1, 2, 3, 4]
print("The Initial Array is ", arr)
print()

Stack_ByList(arr, 'Add', 0)
print(arr)
print()

Stack_ByList(arr, 'Remove')
print(arr)
print()

Stack_ByList(arr, 'Add', 3)
print(arr)
print()

Stack_ByList(arr, 'Add', 5)
print(arr)
print()

Stack_ByList(arr, 'Remove')
print(arr)
print()

Stack_ByList(arr, 'Remove')
print(arr)
print()


print()
print()
print("-------------------------------------------")
print('QUEUE IMPLEMENTATION USING ARRAY')
print("-------------------------------------------")
arr = [1, 2, 3, 4]
print("The Initial Array is ", arr)
print()

Queue_ByList(arr, 'Add', 0)
print(arr)
print()

Queue_ByList(arr, 'Remove')
print(arr)
print()

Queue_ByList(arr, 'Add', 3)
print(arr)
print()

Queue_ByList(arr, 'Add', 5)
print(arr)
print()

Queue_ByList(arr, 'Remove')
print(arr)
print()

Queue_ByList(arr, 'Remove')
print(arr)
print()
