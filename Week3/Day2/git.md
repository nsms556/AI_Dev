# Git

## 1. Git
  - 분산 버전관리 시스템

## 2. 명령어
  - git init : 로컬 리포지토리 생성
  - git add <file_name> : <file_name>을 스테이지에 추가(스테이징)
  - git reset
  - git commit -m "message" : 현재 스테이지를 로컬 리포지토리에 추가 
  - git log : 로그 조회
  - git branch 
    - <branch_name> : <branch_name>으로 브랜치 생성
    - -v : 리포지토리의 브랜치 목록 + 마지막 커밋
    - -d <branch_name> : <branch_name> 삭제
    - -M <branch_name> : 현재 브랜치의 이름을 <branch_name>으로 변경
  - git checkout <branch_name> : <branch_name>의 브랜치로 전환
  - git merge <branch_name> : <branch_name>을 현재 브랜치로 병합
  - git remote
    - add <nickname> <remote_repository> : <remote_repository>를 <nickname> 이름으로 등록
    - -v : 원격 리포지토리 목록
  - git push <remote_repo> <branch> : <branch>를 <remote_repo>에 푸시(업로드)
  - git fetch : 원격 리포지토리의 변경 내용을 다운로드
  - git pull 
    - 옵션 X : 원격 리포지토리의 변경 내용을 다운로드하여 현재 브랜치에 병합(fetch + merge)
    - <remote_repo> <branch_name> : <remote_repo>의 변경 내용을 <branch_name>에 병합
  - git status : 파일 상태를 확인, 커밋되지 않은 내용을 조회
  - git clone <remote_repo> : <remote_repo>를 <local_repo>로 복사하여 현재 디렉토리의 <remote_repo> 이름 폴더로 다운로드
    - <folder_name> : 현재 디렉토리의 <folder_name>으로 다운로드

## 3. 관련 용어
  - HEAD : 현재 작업 중인 브랜치
  - Fast-forward : 빨리 감기의 형태로 브랜치를 병합

## 4. Pull Request (PR)
  - 과정
    1) 오리지널 리포지토리를 내 <remote_repo>로 포크(fork)
    2) <remot_repo>를 클론하여 <local_repo>로 복사
    3) <local_repo>에서 브랜치를 생성하고 <remote_repo>로 푸시(push)
    4) <remote_repo>를 오리지널 리포지토리로 pull 요청(Pull request)  

  - Compare & Pull Request
    - base repository: 오리지널 리포지토리
      - base : PR의 대상 브랜치
    - head repository : 내 리포지토리
      - compare : Pull을 요청할 브랜치