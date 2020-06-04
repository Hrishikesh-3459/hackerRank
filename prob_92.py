# Enter your code here. Read input from STDIN. Print output to STDOUT
class Solution:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    
    def enqueue(self, x):
        self.s1.append(x)

    def dequeue(self):
        if (len(self.s2) == 0):
            while (len(self.s1) != 0):
                self.s2.append(self.s1.pop())
        self.s2.pop()

    def display(self):
        if (len(self.s2) != 0):
            print(self.s2[-1])
        else:
            print(self.s1[0])


q = Solution()
n = int(input())
for i in range(n):
    x = input().split()
    if (x[0] == '1'):
        q.enqueue(int(x[1]))
    elif (x[0] == '2'):
        q.dequeue()
    elif(x[0] == '3'):
        q.display()


