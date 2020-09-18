while(1):
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break

'''
EOF 에러는 try.. except 문을 통해 처리할 수 있다.
try 블록 안에 평소와 같이 명령을 입력하고
except 블록에 예외 상황에 해당하는 오류 핸들러를 입력

try:
    실행할 코드
except:
    예외가 발생했을 때 처리하는 코드
    
'''
