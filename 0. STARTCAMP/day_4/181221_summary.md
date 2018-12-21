# 181221 SUM

## 1. FLASK 

* 'https://ide.c9.io/benjjarvis/startcamp'에서 / 뒤를 '라우트'라고 부른다.

  ('라우트'='루트'=길. 사용자가 특정 랜딩 페이지로 넘어갈 수 있도록 길을 뚫어주는 것을 말함)

* 라우팅할 때, 일일히 저 주소를 치기 귀찮으니 뭐라치든 특정 페이지로 연결될 수 있도록 변수 처리하는 방법(내가 이해한 게 맞나 모르겠음)

  ```python
  #1
  @app.route("/ide/<string:benjjarvis>/<string:workspace>")
  def benjjarvis_workspace():
      return 'benjjarvis & workspace'
  
  
  
  #2 
  @app.route("/ide/<string:benjjarvis>/<string:workspace>")
  def benjjarvis_workspace(benjjarvis, workspace):
      return "{}'s hot {}!".format(benjjarvis, workspace)
  
  # 그러면 주소창에 ide/apple/samsung이라 쳤을 때, 'apple's hot samsung!'이라는 것이 출력된다.
  ```

* 플라스크화 `from flask import Flask`

* 제이슨화 `from flask import jsonify`

* html 내부문서 링크화 `from flask import render_template`

  - 이때, 반드시 주의해야될 것은 새 폴더를 만들고,그것의 이름을 templates라고 반드시 명명한 후 그 아래 확장자가 .html인 파일을 만들어야 한다는 것.

  - 그런 다음 플라스크에서 html 내부 계층 문서를 호스팅하는 코드

    ```python
    from flask import Flask, jsonify, render_template
    
    @app.route("/") #끝에 슬래쉬만 입력하면 바로 뜨게. 
    def index(): #지시
        return render_template('index.html') 
    	#'index.html이란 파일의 템플릿을 보여줘라'
    ```

* 플라스크 내부에서 영상 호출하는 방법(html 호출X)

  ```python
  @app.route("/ide/<string:benjjarvis>/<string:a>") 
  	#뒤에 변수는 안 써도 상관X
  def benjjarvis_a(benjjarvis, a):
      url="https://youtu.be/kiTni5eERoY"
      return "<a href={}>내 영상!</a>".format(url)
      # a=print(webbrowser.open(url))
      # return "{}'s now watching {}!".format(benjjarvis, a)
      # return render_template()
  ```

* 플라스크 내 한국어 인식하도록 만들기

  ```
  # -*(astric)- coding: utf-8 -* #
  ```

* html 문서에 입력해 랜덤 플라스크 만들기

  ```python
  from random import sample
  import random
  
  @app.route("/")
  def index(): 
      lunch = random.choice(['20층','Diet']) 
          #꼭 하나의 리스트에 넣어줘야 함
          #.choice 모듈은 random 외장함수를 불러올 때 자동으로 따라오는 킷
          #따라서 굳이 따로 불러오거나 정의하지 않아도 됨
      return render_template('index.html', lunch = lunch)
  		#, 뒤는 변수
      	#좌변수는 html에 대기?하고 있는 변수. html에 보이는 변수.
          #우변수는 위에서 정의한 지역함수. 
          #일반적으로 우에서 좌로 입력이 되는 구조라고 함.
  ```

  while doing this, should also update .html file like, 

  ```html
  <h2>Lunch: {{lunch}}</h2>
  ```

  h2태그는 굳이 넣을 필요 없지만, 플라스크에서 작성한 랜덤 코드가 html에서 작동되게 하기 위해 **{{}}**를 반드시 써주어야 한다.





## 2. HTML extension

* Convention:

  1) =띄어쓰기 하지 않음.

  2) ""를 씀.

  3) /> 이전은 띄어쓰기 해야함.


1. 폼 형식 만드는 기능

   ```html
   <form> #form 태그는 일종의 가방이나 주머니 같은 걸로 사용자의 정보를 담는 역할만.
       <input type="text" name="name"/> 
       #일반적으로 text폼은 디폴트값이라 굳이 쓰지 않아도 상관은 없지만, 명시적인 것이라 	써주는 게 좋다고 함.
       #<~ /> 이런 태그를 self-closing 태그라고 함.
   </form>
   ```

2. 폼 인풋 기능

   * email폼 기능

     ```html
     <form>
         <input type="email" name="name"/> 
         #여기서 email로 타입을 지정해줘야
         <input type='submit'/> 
         #~@~ 형식으로만 폼 입력을 받을 수 있음.
     </form> 
     ```

     **또한, name="name"을 꼭 써주어야 나중에 B폼으로 이동시킬 수 있음.**
     **name에 타입값을 지정해주면 폼에 입력한 데이터가 주소창에 보임.**



   * color폼 기능

     ```html
     <form>
         <input type="color"/> #color picker폼 등장.
     </form> 
     ```

   * 달력폼 기능

     ```html
     <form>
         <input type="date" /> #달력폼 등장.
     </form>
     ```

   *  폼의 가이드라인 기능

     ```html
     <form>
         <input type="email" placeholder="이메일을 입력하세요." />
         #placeholder라는 태그를 쓰면 가이드라인처럼 글씨가 뜬다고 함.
     </form>
     ```

   * '제출'버튼 구문 변경

     ```html
     <form>
         <input type="email" name="name"/>
         <input type='submit' value="바보"/> 
         #value값을 변경해주면 됨.
         #또한, 다른 타입에도 value값을 지정해주면 입력하기 전에 글자가 보인다고.
     </form>
     ```

3. 버튼 기능

   ```html
   <a href="/type_A"> #버튼을 클릭하면서 넘어갈 페이지 링크를 먼저 넣고, 
   	<button> #이 태그를 그 안에 넣어주면 됨.
   		Type A
   	</button>
   </a>
   ```

4. 비디오 삽입 기능

   ```html
   <iframe width="850" height="650" 
       src="https://www.youtube.com/embed/kiTni5eERoY" 
       frameborder="0" 
       allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" 
       allowfullscreen>
   </iframe>
   ```

   * iframe 태그를 사용하면 된다.




## 3. HTML HREF FUNC USING FLASK & PYTHON

1. STEP I: 플라스크에 다음과 같이 입력

   ```python
   @app.route("/")
   def index():
       return render_template('choose_your_type.html')
       
   @app.route("/type_A")
   def type_A():
       return render_template('type_A.html')
   
   @app.route("/type_B")
   def type_B():
       return render_template('type_B.html')
   ```

   * 이 경우, choose_your_type.html, type_A.html, type_B.html 문서를 모두 만들어야 함.
   * 같은 폴더의 문서로 넘어가게 하려면, 반드시 다음과 같은 플라스크 코드를 입력해야 함.

2. STEP II: choose_your_type.html 문서 만들기

   ```html
   <h1>Wanna see your type?</h1>
   <p>
       <a href="/type_A">
           <button>
               Type A
           </button>
       </a>
   </p>
   <p>
       <a href="/type_B">
           <button>
               Type B
           </button>
       </a>
   </p>
   ```



3. STEP III: type_A(B).html 문서 만들기

   ```html
   <iframe width="850" height="650" 
       src="https://www.youtube.com/embed/kiTni5eERoY" 
       frameborder="0" 
       allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" 
       allowfullscreen>
   </iframe>
   ```




## 4. PING-PONG FUNC

1. STEP 1: 플라스크 입력

   ```python
   @app.route("/ping")
   def ping():
       return render_template('ping.html')
   
   
   @app.route("/pong")
   def pong():
       name = request.args.get('name') 
       color = request.args.get('color')
       #request = 사용자의 요청
       #args = 인자. 요청 중에 실제 넘어온 값.
       #get = ~에서 뽑을거야.
       return render_template('pong.html', name=name, color=color)
   ```


2. STEP 2: ping.html

   ```html
   <!DOCTYPE html>
   
   <html>
   <head>
   	<title> ping </title>
   </head>
   
   <body>
       <h1> ping! </h1>
       <form action="/pong">
           <input type="text" name="name"/>
           <input type="color" name="color"/>
           <input type="email" name="email"/>
           <input type="date" name="date"/>
           <input type="submit" />
       </form>
   </body>
   </html>
   ```


3. STEP 3: pong.html

   ```html
   <!DOCTYPE html>
   
   <html>
   <head>
       <title> pong </title>
   </head>
   
   <body>
       <h1> pong! </h1>
       {{name}}
       {{color}}
   </body>
   </html>
   ```
