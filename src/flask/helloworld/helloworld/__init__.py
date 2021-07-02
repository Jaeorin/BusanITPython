from werkzeug.routing import BaseConverter
from models import Board
from database import db_session
from flask import Flask, url_for, request, render_template, session, redirect
from bs4 import BeautifulSoup
import requests


# 2
class BoardView(BaseConverter):
    def to_python(self, value):
        record = db_session.query(Board).filter(Board.id == value).first()
        return record

    def to_url(self, record):
        return record.id


app = Flask(__name__, template_folder="templates")

# 3. 디버깅 여부
# 설명
# 여기에 3번 수업내용 설명
# 현재 appStart.py 에서 매개변수로 디버깅 여부를 전달 중이므로 주석 처리
# app.debug = True

# 2
app.url_map.converters["board"] = BoardView

# 8
app.secret_key = "iot_key"


@app.route("/")
def http_prepost_response():
    iot: str = "Hello KITTY<br><img src=\"https://www.google.com/images/branding/googlelogo/1x" \
               "/googlelogo_color_272x92dp.png\"><br> "
    return iot


# 1
@app.before_first_request
def before_first_request():
    print("앱 기동하고 맨 처음 요청만 응답")


@app.before_request
def before_request():
    print("매 요청마다 실행")


@app.after_request
def after_request(response):
    print("매 요청 처리되고 나서 실행")
    return response


@app.teardown_request
def teardown_request(exception):
    if exception is not None:
        print(exception)
    print("브라우저가 응답하고 실행")


@app.teardown_appcontext
def teardown_app_context(exception):
    if exception is not None:
        print(exception)
    print("HTTP 요청 애플리케이션 컨텍스트가 종료될 때 실행")


# 2
@app.route("/board/<board:record>", endpoint="view")
def board_view_route(record):
    return url_for("view", record=record)


# 4 ~ 5.
@app.route("/boardList")
def board_list():
    print("boardList")
    return "<img src=\"https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png\">"


@app.route("/staticImage")
def static_image_response():
    return "<img src=" + url_for("static", filename="1.jpg") + ">"


# 6.
@app.route("/getPost", methods=["GET"])
def board_list_get():
    return ""


@app.route("/getPost", methods=["POST"])
def board_list_post():
    return ""


# 7.
@app.route("/user/<username>")
def user_name(username):
    return "User name : %s" % username


@app.route("/user/<int:number>")
def user_number_id(number):
    return "ID Number : %d" % number


# 7. GET  8. POST  9. Session_check
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session_check = request.form.get("username", None)
        if session_check is None:
            if "logged_in" in session:
                if session["logged_in"]:
                    return session["username"] + "님 환영합니다"
        if (request.form["username"] == "iot"
                and request.form["password"] == "2019"):
            session["logged_in"] = True
            session["username"] = request.form["username"]
            return request.form["username"] + "님 환영합니다"
        else:
            return "로그인 실패"
    else:
        try:
            if session["logged_in"]:
                return session["username"] + "님 환영합니다"
            else:
                return login_page()
        except session["logged_in"] as exception:
            print(exception)
            return login_page()


@app.route("/getLoginTest", methods=["GET"])
def get_login_test():
    if request.method == "GET":
        if (request.args.get("username") == "iot"
                and request.args.get("password") == "2019"):
            return request.args.get("username") + "님 환영합니다"
        else:
            return "로그인 실패"
    else:
        return "다시 시도해 주세요"


@app.route("/log")
def log():
    test_value = 20190211
    app.logger.debug("디버깅 시행 중")
    app.logger.warning(str(test_value) + "=====")
    app.logger.error("에러발생")
    return "로거 끝"


# 8. 
@app.route("/loginPage")
def login_page():
    return render_template("login.html")


# 9
@app.route("/logout", methods=["POST", "GET"])
def logout():
    session["logged_in"] = False
    session.pop("uname", None)
    return "로그아웃 되셨습니다"


@app.route("/template")
@app.route("/template/")
@app.route("/template/<number>")
def template(number=None):
    members = ["최성주", "주수홍", "최재원"]
    return render_template("template.html", number=number, members=members)


# 10.
@app.route("/multiplication")
@app.route("/multiplication/")
@app.route("/multiplication/<int:number>")
def multiplication(number=None):
    return render_template("multiplication.html", number=number)


@app.route("/calculation", methods=["POST"])
def calculation():
    if request.method == "POST":
        if "" == request.form["number"]:
            calculation_number = None
        else:
            calculation_number = request.form["number"]
    else:
        calculation_number = None
    return redirect(url_for("multiplication", number=calculation_number))


@app.route("/iotPage")
@app.route("/iotPage/")
def iot_page():
    result_req = requests.get("https://busanit.ac.kr/p/?j=41")
    result_txt = result_req.text
    if result_req.ok:
        obj_soup = BeautifulSoup(result_txt, "html.parser")
        data = obj_soup.select("#ej-tbl > tbody > tr > td > a")
        return render_template("main.html", data=data)
    else:
        return "가져오기 실패"


@app.route("/iotPage2")
@app.route("/iotPage2/")
def iot_page2():
    result_req = requests.get("https://media.daum.net/")
    result_txt = result_req.text
    if result_req.ok:
        obj_soup = BeautifulSoup(result_txt, "html.parser")
        data = obj_soup.select("div.box_headline > ul.list_headline > li > strong.tit_g > a")
        return render_template("main.html", data=data)
    else:
        return "가져오기 실패"


@app.route("/iotPage3")
@app.route("/iotPage3/")
def iot_page3():
    result_req = requests.get("https://media.daum.net/ranking/bestreply/")
    result_txt = result_req.text
    if result_req.ok:
        obj_soup = BeautifulSoup(result_txt, "html.parser")
        data = obj_soup.select("div.cont_thumb > strong.tit_thumb > a")
        return render_template("main.html", data=data)
    else:
        return "가져오기 실패"


@app.route("/iotPage4")
@app.route("/iotPage4/")
def iot_page4():
    result_req = requests.get("https://sports.news.naver.com/index.nhn")
    result_txt = result_req.text
    if result_req.ok:
        obj_soup = BeautifulSoup(result_txt, "html.parser")
        data = obj_soup.select("div.main_article_box > ul.main_article_list > li > a")
        return render_template("main.html", data=data)
    else:
        return "가져오기 실패"
