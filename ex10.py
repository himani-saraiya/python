from unicodedata import name


ob = [
  {
    "name"    : 'Tanay',
    "haveCycle" : True
  },
  {
    "name"    : 'Akanksha',
    "haveCycle"  : False
  },
  {
   "name"     : 'Tanvi',
    "haveCycle"  : True
  },
	{
    "name"    : 'Kanak',
    "haveCycle"  : False
  }
]
l = []
for i in ob: 
    for j in ob[i]:
        if ob[i][j] == True:
            l.append(ob[i].name())
        
print(l)