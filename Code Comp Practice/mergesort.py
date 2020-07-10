def merge(arr, low, mid, high):
	cpy = arr[:]
	ptr = low
	lPtr = low
	hPtr = mid

	while lPtr <= mid - 1 and hPtr <= high:
		if cpy[lPtr] < cpy[hPtr]:
			arr[ptr] = cpy[lPtr]
			lPtr += 1
		else:
			arr[ptr] = cpy[hPtr]
			hPtr += 1
		ptr += 1

	while lPtr <= mid - 1:
		arr[ptr] = cpy[lPtr]
		lPtr += 1
		ptr += 1

	while hPtr <= high:
		arr[ptr] = cpy[hPtr]
		hPtr += 1
		ptr += 1

def sort(arr, low, high):
	# Base case
	if low - high == 0:
		return
	# Find pivot in middle
	pivot = (high - low + 1) // 2 + low

	# Sort subarrays
	sort(arr, low, pivot - 1)
	sort(arr, pivot, high)

	# Merge arrays
	merge(arr, low, pivot, high)

arr = [5,9,1,2,6,3,7,8,8,8,8]
sort(arr, 0, len(arr) - 1)
print(arr)
