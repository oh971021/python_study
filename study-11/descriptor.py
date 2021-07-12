class Descriptor:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        print("get")
        return self.value

    def __set__(self, instance, value):
        print("set")
        self.value = value

    def __delete__(self, instance):
        print("delete")
        del self.value