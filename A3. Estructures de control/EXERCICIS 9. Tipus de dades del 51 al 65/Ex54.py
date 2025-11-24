vector = [1,2,30,4,5,6,7,8,9,10]
ultim = vector[len(vector)-1]

for i in range(len(vector)-1,0,-1):
    
    vector[i] = vector[i-1]

vector[0] = ultim

print(vector)