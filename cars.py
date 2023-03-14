class Heap:
    def __init__(self):
        self.arr = []
        self.d = {}
    
    def change_d_values(self, i, j):
        self.d[self.arr[i][1]] = i
        self.d[self.arr[j][1]] = j

    def heap_top(self, i):
        while i != 0 and self.arr[(i-1)//2][0] > self.arr[i][0]:
            self.arr[(i-1)//2], self.arr[i] = self.arr[i], self.arr[(i-1)//2]
            self.change_d_values((i-1)//2, i)
            i = (i-1)//2
    
    def heap_bottom(self, i):
        while i * 2 + 1 < len(self.arr) - 1:
            min_son_index = i * 2 + 1
            if self.arr[min_son_index][0] > self.arr[i*2 + 2][0]:
                min_son_index = i*2 + 2
            if self.arr[i][0] > self.arr[min_son_index][0]:
                self.arr[i], self.arr[min_son_index] = self.arr[min_son_index], self.arr[i]
                self.change_d_values(min_son_index, i)
                i = min_son_index
            else:
                break

    def insert(self, time, car):
        self.arr.append((time, car))
        i = len(self.arr) - 1
        self.d[car] = i
        self.heap_top(i)
    
    def extract(self):
        ans = self.arr[0]
        self.arr[0] = self.arr[-1]
        i = 0
        self.heap_bottom(i)
        self.arr.pop()
        return ans

    def replace(self, new_time, car):
        i = self.d[car]
        self.arr[i] = (new_time, car)
        self.heap_bottom(i)
        self.heap_top(i)
        

with open('input.txt', 'r') as f:
    n, k, p = map(int, f.readline().split())
    cars = []
    times = {}
    for i in range(p):
        c = int(f.readline())
        cars.append(c)
        if c in times:
            times[c].append(i)
        else:
            times[c] = []


times_arr = [p] * p
for i in range(p):
    if times[cars[i]]:
        times_arr[i] = times[cars[i]].pop(0)

f = set()
h = Heap()
cnt = 0
for i in range(p):
    if cars[i] not in f and len(h.arr) < k:
        f.add(cars[i])
        h.insert(-times_arr[i], cars[i])
        cnt += 1
    elif cars[i] not in f:
        cnt += 1
        f.remove(h.extract()[1])
        h.insert(-times_arr[i], cars[i])
        f.add(cars[i])
    elif cars[i] in f:
        h.replace(-times_arr[i], cars[i])
print(cnt)
