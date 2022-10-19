from django.shortcuts import render
import mysql.connector as sql
username=''
name=''
email=''
gender=''
pwd=''
enname =''
desc = ''

# Create your views here.
def signup(request):
    global username,name,email,gender,pwd
    if request.method == 'POST':
        toSql=sql.connect(host='localhost',user='root',password='ankush123',database='web')
        cursor=toSql.cursor()
        dataValue = request.POST
        for key, value in dataValue.items():
            if key == 'username':
                username = value
            if key == 'name':
                name = value
            if key == 'email':
                email = value
            if key == 'sex':
                gender = value
            if key == 'password':
                pwd = value
        values = "INSERT INTO userdata values('{}','{}','{}','{}','{}')".format(username,name,gender,email,pwd)
        cursor.execute(values)
        toSql.commit()
    return render(request, 'signup/signup_page.html')

def contact(request):
    global enname,desc
    if request.method == 'POST':
        toSql=sql.connect(host='localhost',user='root',password='ankush123',database='web')
        cursor=toSql.cursor()
        dataValue = request.POST
        for key, value in dataValue.items():
            if key == 'name':
                enname = value
            if key == 'desc':
                desc = value
        values = "INSERT INTO enquiry values('{}','{}')".format(enname,desc)
        cursor.execute(values)
        toSql.commit()
    return render(request, 'contectUsPage.html')