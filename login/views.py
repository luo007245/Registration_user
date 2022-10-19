from django.shortcuts import render
import mysql.connector as sql
email=''
pwd=''

# Create your views here.
def login(request):
    global email,pwd
    print("run")
    if request.method == 'POST':
        toSql=sql.connect(host='localhost',user='root',password='ankush123',database='web')
        cursor=toSql.cursor()
        dataValue = request.POST
        for key, value in dataValue.items():
            if key == 'email':
                email = value
            if key == 'password':
                pwd = value
        values ="select * from userdata where Email='{}' and Password='{}'".format(email,pwd)
        cursor.execute(values)
        tupleData = tuple(cursor.fetchall())
        print(tupleData)
        if tupleData==():
            return render(request, 'welcome.html')
        else:
            return render(request, 'error.html')
    return render(request, 'login/login_page.html')
