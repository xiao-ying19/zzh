from flask import request, render_template,redirect, flash, url_for, session
from courseselection.model import Students, Teacher,SelectedClass, TeacherInfo
import json
from . import app


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        session['username'] = username
        s = Students()
        flag, res = s.search(username)
        if flag == 1:
            if res[0].password == password:
                return redirect(url_for('middle'))
            else:
                flash("密码错误！")
        else:
            flash("用户信息不存在！")
        return redirect(url_for('login'))
    return render_template('mylogin.html')


@app.route("/login1", methods=['GET', 'POST'])
def login1():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        session['username2'] = username
        session['password2'] = password
        flag, res = TeacherInfo.searchID(username)

        if flag == 1:
            if res.password == password:
                session['name'] = res.name
                return redirect(url_for('addcourse'))
            else:
                flash("密码错误！")
        else:
            flash("用户信息不存在！")
        return redirect(url_for('login1'))
    return render_template('mylogin.html')


@app.route('/middle')
def middle():
    return render_template('middle.html')


@app.route('/courseslist',methods=['POST','GET'])
def courseslist():
    courses = Teacher.findall()
    if request.method == 'POST':
        data = request.data
        data1 = json.loads(data.decode("utf-8"))
        classID = data1[0]["classID"] # 获取输入的课程号
        username = session['username']
        courselist = SelectedClass.search(username)
        all = []
        for course in courselist: # 遍历该学生选的全部课程
            all.append(course.classID)
        if classID in all:
            return "你已经选择了该课程！"
        else:
            res = Teacher.search(classID)
            if res is not None:
                time1 = Teacher.search(classID).time  # 正在选的课的上课时间
                flag = 0
                for oneclass in all:
                    if Teacher.search(oneclass).time == time1:
                        break
                    else:
                        flag += 1
                if flag < len(all):
                    return "与其他课时间有冲突"
                else:
                    kwargs = {
                        'id': username,
                        'classID': classID
                    }
                    SelectedClass.add(**kwargs)
                    return "选课成功！"
            else:
                return "课程号不存在！"
    return render_template('mylist.html', courses=courses)


@app.route('/display', methods=['POST','GET'])
def display():
    username = session['username']
    result = SelectedClass.search(username)  # 课程号和学号
    classID = [r.classID for r in result]  # 全部课程号
    finalList = []
    for oneID in classID:
        finalList.append(Teacher.search(oneID))
    if request.method == 'POST':
        data = request.data
        data1 = json.loads(data.decode("utf-8"))
        selectedclassID = data1[0]["classID"] # 获取输入的课程号
        if selectedclassID not in classID:
            return("课程号输入错误！")
            #return redirect(url_for('display'))
        else:

            kwargs = {
                'id': username,
                'classID': selectedclassID
            }
            SelectedClass.delete(**kwargs)
            return "退选成功"
    return render_template('display.html', finalList=finalList)


@app.route('/addcourse',methods=['POST','GET'])
def addcourse():
    if request.method == 'POST':
        classID = request.form['classID']
        classname = request.form['classname']
        time = request.form['time']
        id = session['username2']
        password = session['password2']
        name = session['name']
        res = Teacher.search(classID)
        if res is not None:
            flash("课程号已存在！")
            return redirect(url_for('addcourse'))
        flash("添加成功！")
        kwargs = {
            'classID': classID,
            'classname': classname,
            'time': time,
            'id': id,
            'password': password,
            'name': name
        }
        Teacher.add(**kwargs)
    return render_template('addcourse.html')










if __name__ == '__main__':
    print("9")
    app.run(debug=True)