from fastapi import FastAPI,HTTPException
from pydantic import Field,BaseModel


app = FastAPI(title="Student Management APP",version="3.1518",description="Student Management App,Control student details")


student = [
    {"id": 1, "name": "Rahim", "roll": 710256, "age": 21, "department": "cse", "gpa": 3.75, "status": "Pass"},
    {"id": 2, "name": "Karim", "roll": 710257, "age": 22, "department": "eee", "gpa": 1.80, "status": "Fail"},
    {"id": 3, "name": "Sadia", "roll": 710258, "age": 20, "department": "cse", "gpa": 3.90, "status": "Pass"},
    {"id": 4, "name": "Nayeem", "roll": 710259, "age": 22, "department": "civil", "gpa": 2.85, "status": "Pass"},
    {"id": 5, "name": "Tania", "roll": 710260, "age": 21, "department": "eee", "gpa": 1.50, "status": "Fail"},
    {"id": 6, "name": "Rakib", "roll": 710261, "age": 23, "department": "mech", "gpa": 3.20, "status": "Pass"},
    {"id": 7, "name": "Mehedi", "roll": 710262, "age": 22, "department": "eee", "gpa": 3.50, "status": "Pass"},
    {"id": 8, "name": "Jannat", "roll": 710263, "age": 20, "department": "cse", "gpa": 3.85, "status": "Pass"},
    {"id": 9, "name": "Sabbir", "roll": 710264, "age": 22, "department": "civil", "gpa": 1.90, "status": "Fail"},
    {"id": 10, "name": "Farhana", "roll": 710265, "age": 21, "department": "eee", "gpa": 3.40, "status": "Pass"},
    {"id": 11, "name": "Tanvir", "roll": 710266, "age": 23, "department": "mech", "gpa": 2.60, "status": "Pass"},
    {"id": 12, "name": "Mitu", "roll": 710267, "age": 20, "department": "cse", "gpa": 1.75, "status": "Fail"},
    {"id": 13, "name": "Shakil", "roll": 710268, "age": 22, "department": "eee", "gpa": 3.10, "status": "Pass"},
    {"id": 14, "name": "Nusrat", "roll": 710269, "age": 21, "department": "civil", "gpa": 3.65, "status": "Pass"},
    {"id": 15, "name": "Arif", "roll": 710270, "age": 23, "department": "mech", "gpa": 1.60, "status": "Fail"},
    {"id": 16, "name": "Sumaiya", "roll": 710271, "age": 20, "department": "cse", "gpa": 3.95, "status": "Pass"},
    {"id": 17, "name": "Hasan", "roll": 710272, "age": 22, "department": "eee", "gpa": 2.45, "status": "Pass"},
    {"id": 18, "name": "Riya", "roll": 710273, "age": 21, "department": "civil", "gpa": 1.85, "status": "Fail"},
    {"id": 19, "name": "Imran", "roll": 710274, "age": 23, "department": "mech", "gpa": 3.30, "status": "Pass"},
    {"id": 20, "name": "Maliha", "roll": 710275, "age": 20, "department": "cse", "gpa": 3.70, "status": "Pass"}
]

# 03.student list data post
@app.post("/student",status_code=201)
def student_create(new_student:dict):
     new_student["id"] =len(student) +1
     student.append(new_student)
     return {"massage":"Student Created","data":new_student}

# 01 . get all student 
@app.get("/student")
def student_get():
     return {"massage":"student get successfully","student":student}

# 07. get pass student
@app.get("/student/pass")
def student_pass():
     pass_list = []
     for stud in student:
          if stud["gpa"] >= 2.00:
               pass_list.append(stud)
     if pass_list:
          return {"message":"Pass student list","total":len(pass_list)}
     raise HTTPException(status_code=404,detail="No pass student found")

# 08 get fail student
@app.get("/student/fail")
def student_fail():
     fail_list =[]
     for stud in student:
          if stud["gpa"] < 2.00:
               fail_list.append(stud)
     if fail_list:
          return {"message":"Fail student list","total":len(fail_list)}
     raise HTTPException(status_code=404,detail="No fail student found")

# 02. one id student list get student data
@app.get("/student/{student_id}")
def get_student_one_item(student_id:int):
     for stud in student:
          if stud["id"] == student_id:
               return stud
     raise HTTPException(status_code=404, detail="Student not found")
               
# 04.put student 
@app.put("/student/{student_id}")
def student_update(student_id:int,student_update:dict):
     for stud in student:
          if stud["id"] == student_id:
               stud.clear()
               stud.update(student_update)
               stud["id"] = student_id
               return {"message":"student updaded","data":stud}
     raise HTTPException(status_code=404,detail="student not found")

# 06.patch student item
@app.patch("/student/{student_id}")
def student_patch(student_id:int,student_data:dict):
     for stud in student:
          if stud["id"] == student_id:
               stud.update(student_data)
               stud["id"] = student_id
               return {"message":"student partilly update","data":stud}
     raise HTTPException(status_code=404,detail="Student not found")     

# 05. delete student item
@app.delete("/student/{student_id}")
def student_delete(student_id:int):
     for stud in student:
          if stud["id"] == student_id:
               student.remove(stud)
               return {"message":"student delete","data":stud}
     raise HTTPException(status_code=404,detail="student not found")    



































