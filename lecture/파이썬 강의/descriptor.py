# 커맨드가 제일 앞에 있어야 한다.
# 다른모듈에서 사용 할 때, 디스크립터만 관리하는 모듈을 만들고 
# 다른 곳에서는 import 하면 된다.
class descriptor2:
    
    # 디스크립터 내에서 타입체크
    def __init__(self,types):
        self.datatype = types
    
    # 속성명을 가지고와서 변수명을 자동으로 설정하도록 바꿔주는 속성
    # 클래스에서 디스크립터 할당을 할때 변수 명을 가지고 오기 때문에 owner는 상관없다.
    # name은 내가 할당한 변수를 가지고 온다.
    def __set_name__(self, owner, name ):
        print("set_name", owner, name)
        self.name = "_"+ name
        
    def __get__(self, instance, owner):
        print('get', instance)
        return instance.__dict__.get(self.name,0) 
    
    def __set__(self, instance, value):
        print('set')
        # 타입이 아니면 에러를 발생시킨다.
        if type(value) == self.datatype :            
            instance.__dict__[self.name] = value
        else:
            raise TypeError("자료형 불일치")
