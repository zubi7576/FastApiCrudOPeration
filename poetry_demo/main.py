from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Student(BaseModel):
    id: str
    name: str
    age:str
    Grade:str


students  = [
   {
      "id":"1",
      "name":"Zubair",
      "age":"25",
      "Grade":"A"
   },
   {
      "id":"2",
      "name":"Ahmad",
     "age":"23",
     "Grade":"A"
   },
   {
      "id":"3",
      "name":"Ali",
      "age":"20",
      "Grade":"A"
   },
   {
      "id":"4",
      "name":"ABC",
      "age":"21",
      "Grade":"A"
   }
]

#####Get All Students 
@app.get("/getStudent")
def getStudent():
   return students

####Add Student
@app.post("/addStudent")
def addStudent(student:Student):
   students.append(student)
   print(students)
   return students


#Get Specific Student by id
 
@app.get("/getStudent/{student_id}")
def get_specific_student(student_id: str):
    for student in students:
        if student["id"]== student_id:
            print("Student Found",student)
            return student
   
#Update Student through Put

@app.put("/getStudent/{student_id}")
def update_student(student_id:str,updated_student:Student):
   for student in students:
      if student["id"] == student_id:
         student["name"] = updated_student.name
         return {"message": f"Student with ID {student_id} updated successfully"}
      

#Delete  /students/{student_id}: Delete a student

@app.delete("/DelStudent/{student_id}")
def delete_student(student_id: str):
    global students
    index_to_Delete = None
    for i, student in enumerate(students):
        if student["id"] == student_id:
            index_to_Delete = i
            break
    # Check if a student with the given ID was found
    if index_to_Delete is not None:
        deleted_student = students.pop(index_to_Delete)
        return {"message": f"Student with ID {student_id} deleted successfully", "deleted_student": deleted_student}
   
   


def start():
  uvicorn.run("poetry_demo.main:app",host="127.0.0.1", port=5000, reload=True)
    

    
    