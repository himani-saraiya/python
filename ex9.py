arr = [
	{
		"name": "Apple"
	},
	{
		"name": "Mango"
	},
	{
		"name": "Potato"
	},
	{
		"name": "Guava"
	},
	{
		"name": "Capsicum"
	}
]
a = {}
i=0
while i<len(arr):
    for j in arr[i]:
        if len(arr[i][j])>5:
            a["name"]=arr[i][j]
            a["type"]="vegetable"
        else:
            a["name"]=arr[i][j]
            a["type"]="fruit"
    i=i+1
    print(a)