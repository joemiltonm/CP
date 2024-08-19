
stops = int(input())

passenger_count = []

for i in range(stops):
    exit, entry = list(map(int, input().split()))
    passenger_count.append((exit, entry))

max = -1
current_passengers = 0


for x,y in passenger_count:
    current_passengers -= x
    current_passengers += y
    if current_passengers > max:
        max = current_passengers
    
print(max)





