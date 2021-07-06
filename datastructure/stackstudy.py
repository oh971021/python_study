class stack :
    def __init__(self) :
        self.data = []
    def push(self,value) :
        self.data.insert(0,value)
    def pop(self) :
        self.data.pop(0)
    def top(self) :
        return self.data[0]
    def empty(self) :
        return not (len(self.data) > 0)

s = stack()
s.push(1); s.push(2); s.push(3); s.push(4); 
print(s.__dict__)
s.pop();
print(s.__dict__)
s.pop();
print(s.__dict__)

print("현재 스택의 가장 최상위에 있는 데이터의 값은 : ", s.top())
print("스택 꽉찼나요? ", s.empty())