student={
    "name":"amy",
    "age":28,
    "grade":"8th"

}
print("original:",student)
student["city"]="new york"
print("after adding city:",student)
student["age"]=18
print("after adding age:",student)
del student["grade"]
print("after deleting grade:",student)