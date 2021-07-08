iamGlobal = "안녕 나는 글로벌 변수야. 나는 모듈안에 있지롱"

# 함수를 만든다. 매개변수는 *args 로 여러개의 인자를 받는다.
def thisFunc(*args) :
  # 글로벌 변수 키워드를 지정해준다.
  # 가져와서 쓰겠다는 말씀.
  global iamGlobal

  # thisfunc 실행되는지 확인하기.
  print("thisFunc executed")
  # 글로벌 변수를 실행한다.
  # 잘가져왔는지 확인한다.
  print(iamGlobal)

  # 로컬 변수를 만들어준다.
  iamNonlocal = "안녕 나는 로컬변수야. 나는 thisfunc 안에있는 함수로 쓰일거야 ㅎㅎ"

  # 내부함수를 만든다. 매개변수는 외부함수와 같다.
  def thatFunc(*args) :
    # 리스트 변수를 하나 만들어준다.
    paras = [  ]
    # 지역 변수 키워드 지정해주기.
    # 외부함수에 있는 변수를 가져와서 쓰겠다 이말씀.
    nonlocal iamNonlocal

    # 함수 실행 되는지 확인하기.
    print("thatFunc executed")
    # 로컬변수한번 실행해주고,
    print(iamNonlocal)
    # 현재 들어와있는 인자가 어떤건지 확인하기.
    # 패킹된 모습 그대로를 출력해본다.
    print("you have entered : ", args, "as parameters.")

    # 인자 하나씪 yourParas 함수로 보내버린다.
    for i in args :
      # 언패킹해서 돌아온 인자들을 함수에 집어넣는다.
      paras.insert(0,i)

    return yourParas(paras)

  # 위의 for문에서 받은 인자를 대입시켜본다.
  def yourParas(paras):
    # 순서대로 처리되다보니 출력값은 거꾸로 출력된다.
    print("Inverse Your parameters: ", paras)
  # 받은걸 언패킹해서 for문으로 돌려보낸다.
  return thatFunc(*args)

# thisFunc 으로 1,2,3 을 매개변수로 넣어준다.
thisFunc(1,2,3)