vector = [1,2,30,4,5,6,7,8,9,10]
primer = vector[0]

for i in range(0,len(vector)-1):
    
    vector[i] = vector[i+1]

vector[len(vector)-1] = primer

print(vector)