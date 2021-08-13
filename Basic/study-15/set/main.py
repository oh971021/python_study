class Klass() :
  def set_data(self, first, second) :
    self.first = first
    self.second = second

k = Klass()

k.set_data(1, 2)

print(k.__dict__)

print(k.first)