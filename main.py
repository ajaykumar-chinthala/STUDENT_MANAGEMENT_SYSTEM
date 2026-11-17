from fastapi import FastAPI,Request,Form,status
import fastapi
from fastapi.templating import Jinja2Templates
import sqlite3
from pydantic import BaseModel,Field
from fastapi.responses import RedirectResponse
templates=Jinja2Templates(
    directory="templates"
)

app=FastAPI()

class Student(BaseModel):
    name:str=Field(max_length=40,min_length=3)
    age:int=Field(le=60,ge=18)
    gender:str
    marks:int=Field(le=100,ge=1)
    course:str
    image:str
    status:bool


def get_db_connection():
    connection=sqlite3.connect(
        "students.db"
    )
    return connection
get_db_connection()


def create_table():
    connection=get_db_connection()
    cursor=connection.cursor()

    q="""
     CREATE TABLE IF NOT EXISTS STUDENTS(
     Id INTEGER PRIMARY KEY AUTOINCREMENT,
     Name TEXT NOT NULL,
     Age INTEGER,
     Gender TEXT,
     Marks INTEGER,
     Course TEXT,
     Image TEXT,
     Status INTEGER
     )
    """
    cursor.execute(q)
    connection.commit()
    connection.close()
create_table()



@app.get("/")
def get_home(req:Request):
    connection=get_db_connection()
    cursor=connection.cursor()
    q="SELECT * FROM STUDENTS"
    cursor.execute(q)
    students=cursor.fetchall()
    connection.close()
    return templates.TemplateResponse(
        request=req,
        name="home.html",
        context={"stds":students}
    )

@app.get("/student/add")
def get_student_form(req:Request):
    return templates.TemplateResponse(
        request=req,
        name="add-std.html",
        context={}
    )

@app.post("/student/add")
def get_details(req:Request,
    name=Form(),
    age=Form(),
    gender=Form(),
    marks=Form(),
    course=Form(),
    image=Form(),
    status=Form()):

    std_obj=Student(
        name=name,
        age=age,
        gender=gender,
        marks=marks,
        course=course,
        image=image,
        status=status
    )
    
    values=(std_obj.name,std_obj.age,std_obj.gender,std_obj.marks,std_obj.course,std_obj.image,std_obj.status)

    connection=get_db_connection()
    cursor=connection.cursor()
    q="""
     INSERT INTO STUDENTS(name,age,gender,marks,course,image,status) values(?,?,?,?,?,?,?)
     """
    cursor.execute(q,values)
    connection.commit()
    connection.close()
    
    return RedirectResponse(url="/",status_code=303)



@app.get("/std/{std_id}")
def get_single(req:Request,std_id:int):
    connection=get_db_connection()
    cursor=connection.cursor()

    q="SELECT * FROM STUDENTS Where id= ?"


    cursor.execute(q,(std_id,))
    stdinf=cursor.fetchone()
    connection.close()

    return templates.TemplateResponse(
        request=req,
        name="singlestd.html",
        context={
             "std":stdinf
        }
    )

@app.post("/std/delete/{std_id}")
def del_std(std_id:int):
    connection=get_db_connection()
    cursor=connection.cursor()
    q="delete from students where id=?"

    cursor.execute(q,(std_id,))
    connection.commit()
    connection.close()

    return RedirectResponse(url="/",status_code=303)


@app.get("/std/update/{std_id}")
def update_students(req:Request,std_id):
    connection=get_db_connection()
    cursor=connection.cursor()
    q="select * from students where id=?"
    cursor.execute(q,(std_id,))
    studentd=cursor.fetchone()
    print(studentd)
    return templates.TemplateResponse(
        request=req,
        name="update.html",
        context={
             "stds":studentd
        }
    )

@app.post("/std/update/{std_id}")
def upadte_student(req:Request,std_id,name=Form(),
    age=Form(),
    gender=Form(),
    marks=Form(),
    course=Form(),
    image=Form(),
    status=Form()):
    std_obj=Student(
            name=name,
            age=age,
            gender=gender,
            marks=marks,
            course=course,
            image=image,
            status=status
        )
    values=(std_obj.name,std_obj.age,std_obj.gender,std_obj.marks,std_obj.course,std_obj.image,std_obj.status,std_id)
    connection=get_db_connection()
    cursor=connection.cursor()
    q="""update students set
         name=?,age=?,gender=?,marks=?,course=?,image=?,status=? where id =?
    """

    cursor.execute(q,values)
    connection.commit()
    connection.close()
    return RedirectResponse(url="/",status_code=fastapi.status.HTTP_303_SEE_OTHER)