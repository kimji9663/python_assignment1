

prompt = '''
*** 파이썬 과제 1 ***
	1. while 실습문제
	2. fileio 실습문제
	9. 과제 실행 테스트 끝내기
'''
def menu():
    while True:
        print(prompt)

        no = int(input('메뉴 선택 : '))
        if no == 1:
            wm.sungjuk_process()
        if no == 2:
            fm.emp_process()

        print()
        return
    
import fileio.fileio_mission as fm
import loop.while_mission as wm

if __name__ == '__main__':
    menu()
    print('-----------종료-----------')