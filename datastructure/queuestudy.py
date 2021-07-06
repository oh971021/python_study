class queue :
  def __init__(self) :
    self.data = []
    
  def put(self,value) :
    self.data.insert(0,value)
  
  def get(self) :
    self.data.pop(-1)

q = queue()
q.put(20)
print(q.__dict__)
q.put(30)
print(q.__dict__)
q.put(40)
print(q.__dict__)
q.put(50)
print(q.__dict__)
print("여기까지가 데이터 넣는 과정")
q.get()
print(q.__dict__)
q.get()
print(q.__dict__)
