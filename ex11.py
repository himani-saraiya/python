arr = [
	{
		"name": "Jay",
		"age": 60
	},
	{
		"name": "Gloria",
		"age": 36
	},
	{
		"name": "Manny",
		"age": 16
	},
	{
		"name": "Joe",
		"age": 9
	}
]
i=0
sum=0
while i<len(arr):
    for j in arr[i]:
        print(arr[i][j])
        if arr[i][j]==str:
            pass
        else:
            sum=sum+arr[i][j]
    i=i+1
   