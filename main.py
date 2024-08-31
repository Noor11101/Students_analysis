from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

# إضافة ميدلوير CORS إلى التطبيق
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # السماح لجميع النطاقات
    allow_credentials=True,
    allow_methods=["*"],  # السماح بجميع طرق HTTP (GET, POST, PUT, DELETE, إلخ)
    allow_headers=["*"],  # السماح بجميع رؤوس الطلبات
)
# تعديل الاسم ليبدأ بحرف كبير وفقاً للعادات العامة لتسمية الأصناف في بايثون
class Student(BaseModel):  
    id: int
    name: str
    grade: int

# قائمة الطلاب تحتوي على كائنات من نوع Student
students = [
    Student(id=1, name="Noor", grade=8),
    Student(id=2, name="Ali", grade=9),
]

# تعريف دالة معالجة الطلب GET
@app.get("/students")
def read_students():
    return students

@app.post("/students/")
def create_student(new_student: Student):
    students.append(new_student)
    return new_student

@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    for student in students:
        if student.id == student_id:
            student.name = updated_student.name
            student.grade = updated_student.grade
            return updated_student
    return {"error": "Student not found"}

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student.id == student_id:
            del students[index]
            return {"message": "Student deleted"}
    return {"error": "Student not found"}

