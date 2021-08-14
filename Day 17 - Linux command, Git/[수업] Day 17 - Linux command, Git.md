## Day 17
- Linux command
- Git

## Limux command
- `clear`
    - 화면 정리.
- `ls`
    - list의 줄임말. 현재 위치의 file list를 보여줌.
    - 옵션
        - `ls -a`
            - list all. 숨김파일까지 보여줌
        - `ls -l`
            - 만들어진 날짜 / 파일 크기 등 기타 정보도 보여줌. 
        - `ls -t`
            - 시간순 배열
        - `ls -alt` 등으로 여러 옵션을 한꺼번에 줄 수 있다.
- `cd`
    - change directory. 내가 원하는 디렉토리로 이동
    - `cd <내가 이동하고싶은 디렉토리 경로>`
        - ex) cd ~/Desktop 하면 바탕화면으로 이동
    - cf) ~ 은 홈 화면을 의미. 윈도우에서는 C:/Users/내 이름/ 이었던듯.
- `mkdir`
    - make directory. 디렉토리 생성
    - `mkdir <원하는 디렉토리 경로/이름>`
- `cp`
    - 파일 복사: `cp <from 경로> <to 경로>`
        - ex) cp love.txt ../love2.txt 하면 현재 디렉토리의 love.txt를 상위 폴더의 love2.txt로 복사
    - 디레토리 복사: `cp -r <from 경로> <to 경로>`
        - 디렉토리 복사.
        - 디렉토리를 복사하고싶으면 반드시 -r 옵션을 줘야 함.
- `mv`
    - move. 파일/디렉토리 이동 
    - `move <from 경로> <to 경로>`
- `rm`
    - remove
    - 파일 제거: `rm <삭제할 파일 경로>`
    - 디렉토리 제거: `rm -r <삭제할 디렉토리 경로>` 
    - 파일 삭제 전 yes or no 묻기: `-i` 옵션 주기
        - `rm -i 파일 경로`
        - `rm -ir 디렉토리 경로`
- python 프로그램 실행시키기
    - python *.py 하면 됨.


## Git
### Why Git?
- 코드의 version 관리
    - 매 수정마다 screenshot(commit) 을 남김
- 협업 용이
    - 여러 사람들의 수정이 동시에 반영이 가능
    - 다른 사람들이 어떻게 수정했는지 볼 수 있음
### 다운로드
- Git Bash
    - Windows 용: https://git-scm.com/download/win 에서 다운로드
    - 설치 후 Git bash 가 잘 실행되는지 체크
- GitHub Desktop
    - https://desktop.github.com/ 에서 설치
### 용어
- Local
    - 내 컴퓨터
    - client 느낌. Git server와 통신(?) 하는 내 컴퓨터, 혹은 collaborator 의 컴퓨터
- Repository
    - server 느낌. Git server의 코드 저장소
- Clone
    - Git server의 repository 를 local 로 복사해오는 행위
- Commit
    - Git 에서의 screenshot
    - 커밋 메세지와 커밋 내용 (수정 내용) 으로 구성됨
- Push
    - Local 에서 Git repository로 정보를 전달하는 행위
- Pull 
    - Git repository의 정보를 Local로 가져오는 행위 
### 간단한 사용방법
- 연동시키기
    - git clone 레포지토리주소
        - 레포지토리 주소는 각 레포지토리 홈화면에서 Clone or download 버튼을 누르면 나옴.
- 수정내용 업로드하기
    - add
        - `git add <수정한 파일 경로>`
        - `git add .` 하면 모든 수정된 파일이 add 됨.
    - commit
        - `git commit -m "commit 메세지"`
    - push
        - `git push`
- 수정내용 받아오기
    - `git pull`
