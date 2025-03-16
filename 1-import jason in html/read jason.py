import json
from html import escape

with open("2-import jason in html/students.json") as input_file:
    students = json.load(input_file)

with open('2-import jason in html/students.html','w') as output_file:
    output_file.write("""<!DOCTYPE html>
    <html>
    <head>
        <meta charset='UTF-8'>
        <title>Student Information</title>          
    </head>
    <body>
        <h1>Student Information</h1>
        <table border='1'>
            <tr>
                <th>id</th>
                <th>name</th>
                <th>year_of_birth</th>
                <th>study_program</th>
                <th>Hometown</th>
            </tr>
     
    """)
    for student in students:
        student_id=escape(str(student['id']))
        student_name=escape(student['name'])
        year_of_birth=escape(str(student['year_of_birth']))
        study_program=escape(student['study_program'])
        hometown=escape(student['hometown'])

        output_file.write(f"""
            <tr>
                <td>{student_id}</td>
                <td>{student_name}</td>
                <td>{year_of_birth}</td>
                <td>{study_program}</td>
                <td>{hometown}</td>
            </tr>
        """)

    output_file.write("""
            </table>
        </body>
        </html>
    """)