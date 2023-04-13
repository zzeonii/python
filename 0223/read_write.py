파일 생성하기
입출력 방법이 꼭 input()과 print()만 있는 것X
파일을 통한 입출력도 가능


소스코드를 실행하면 프로그램을 실행한 디렉터리에 새로운 파일이 하나 생성ㅇ됨
파일을 생성하기 위해 파이썬 내장 함수 open사용
open()함수 : 파일을 생성하기 위해 사용

readline 함수 사용
f.open('새파일.txt','w')
    readline()사용해서 파일의 첫 번째 줄을 읽어 출력하는 코드
    
readlines()함수는 파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트로 반환.

f.read() 파일의 내용 전체를 문자열료 반환
data는 파일의 전체 내용

>>> f=open('새파일.txt','r')
>>> while True:
    line=f.readline()
    print(line)
    if not line:
        break

[[with문 사용법]]

:지금까지 파일을 열고 닫은 방법
:쓰기모드로 열었던 파일을 닫지 않고 다시 사용하면 오류가 발생하기 때문에,
close()를 사용해서 열려 있는 파일을 직접 닫아 주는 것이 좋음

>>> with open('foo.txt','w') as f:
    f.write('Life is too')
