class Heap:
    def __init__(self):
        self.arr = []
    
    def insert(self, val):
        self.arr.append(val)
        i = len(self.arr) - 1
        while i != 0 and self.arr[(i-1)//2] < self.arr[i]:
            self.arr[(i-1)//2], self.arr[i] = self.arr[i], self.arr[(i-1)//2]
            i = (i-1)//2
    
    def extract(self):
        if not self.arr:
            return 'Error'
        ans = self.arr[0]
        self.arr[0] = self.arr[-1]
        i = 0
        while i * 2 + 1 < len(self.arr) - 1:
            min_son_index = i * 2 + 1
            if self.arr[min_son_index] < self.arr[i*2 + 2]:
                min_son_index = i*2 + 2
            
            if self.arr[i] < self.arr[min_son_index]:
                self.arr[i], self.arr[min_son_index] = self.arr[min_son_index], self.arr[i]
                i = min_son_index
            else:
                break
        self.arr.pop()
        return ans
            



heap = Heap()
with open('input.txt', 'r') as f:
    n = int(f.readline())
    for _ in range(n):
        args = f.readline().split()

        if args[0] == '0':
            heap.insert(int(args[1]))
        else:
            print(heap.extract())
