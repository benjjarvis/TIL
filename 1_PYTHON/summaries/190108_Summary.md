# 190108 Summary

## 1. git

1. vcs: version control system. 여러가지 버전을 컨트롤하는 시스템. 대표적인 게 git. 거의 모든 운영체제를 컨트롤할 수 있음.

2. git init: git이라는 기능을 가진 플러그인을 달겠다. 

   - 단, 이 명령어를 사용할 때는 해당 디렉토리에 들어가 있는 상태여야 한다.

3. repository: directory가 기능을 가지게 되면 이게 됨. 굳이 한국어로 번역하자면 특정 기능을 가지고 있는 '저장소'? 줄여서 repo라고 부르고, 정확히 말하자면 remote repository(원격; 로컬에 있는 리포가 아니기 때문에).

   - git init을 하면 자동으로 repo로 변경

   - 한번 설정하면 프롬프트($) 이전에 master라고 뜸.

   - repo를 삭제하고 원상복구하는 방법: .git/을 삭제해주면 됨.

     ```bash
     rm -rf .git/
     ```

4. config: configuration. 설정

   - 예) .gitconfig

5. git add . : 현재 디렉토리 내 상황을 찍는 것

6. git status : 현재 디렉토리 내 변경사항을 확인하는 것

7. git commit: 변경된 사항을 확인하고,  stage에 올리는 것. 

8. -m: (leave) message

   - git repository에 무언가를 올릴 때 commit과 함께 씀.

   - 반드시 변경사항이 있는 폴더에서 쓰는 것이 좋음.

   - 현재형, 명령형, 깔끔하게.

   - 활용 예:

     ```bash
     git commit -m 'first commit'
     ```

9. git log: git의 version을 찍어볼 수 있음.

* 이런 식으로 계속 깃 커밋을 하면, 나 학부나 대학원때 플젝 수행해서 여러 버전으로 저장한 것처럼 파일이 여러 버전으로 쌓여서 저장됨. 나는 합쳐서 변경하여 저장했지만, 막상 이 커밋이 저장된 곳에서 변경사항을 찾아보면 1줄(1) + 2줄 추가(2) + 3줄 추가(3) 이런 식으로 저장돼 있다고 함... 

10. git remote: 깃이 날아가서 연동될 위치를 가리키는 것.

    - 활용 예:

      ```bash
      git remote add origin https://github.com/benjjarvis/learn_git.git
      ```

    - git remote -v : 컨텐츠와 위치의 버전을 알아보는 것. 

      ```bash
      $ git remote -v
      
      origin  https://github.com/benjjarvis/learn_git.git (fetch)
      origin  https://github.com/benjjarvis/learn_git.git (push)
      ```

      * 보통은 fetch와 push의 위치가 같아야 함.

11. git push: 연동될 위치로 깃을 실질적으로 보내는 것.

    - 활용 예:

      ```bash
      $ git push -u origin master
      ```

      * 처음에만 -u(upstream)를 붙이고 이후로는 git push만(원래는 이게 full command라서 항상 이렇게 써야 하는데, 그냥 생략해도 자동으로 보내준다고 함).

