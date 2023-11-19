from datetime import datetime
from Model import Employee, Job, Assignment, Project
from db import session, engine
from sqlalchemy import text


'''
Query all employee records from the employee table
And query employee with condition, emp_num > 101
'''
# employees = session.query(Employee).first()

# print(employees.emp_fname)


# employees = session.query(Employee).all()
# employees = session.query(Employee).filter(Employee.emp_num > 101).all()
# for employee in employees:
#     print(employee.emp_num, employee.emp_lname, employee.emp_fname, employee.emp_hiredate)


'''
Join employee with job
'''
# employees = session.query(Employee, Job).filter(
#     Employee.job_code == Job.job_code).filter(Employee.emp_num > 101).all()
# for employee in employees:
#     print(employee.Employee.emp_num, employee.Employee.emp_lname, employee.Employee.emp_fname, employee.Job.job_description)

'''
Insert new employee record
'''
# employee = Employee(emp_num=999, emp_lname="Doe", emp_fname="John", emp_initial="D", emp_hiredate="2020-01-01")
# session.add(employee)
# session.commit()

'''
Update employee record

'''
# employee = session.query(Employee).filter(Employee.emp_num == 999).first()
# employee.job_code = 510
# session.commit()

'''
Delete employee record
'''
# employee = session.query(Employee).filter(Employee.emp_num == 999).first()
# session.delete(employee)
# session.commit()

'''
Query assigment where assign_date is larger than 2010-01-01
'''

# date = datetime.strptime('2010-01-01', '%Y-%m-%d')

# assignments = session.query(Assignment).filter(Assignment.assign_date > date).all()
# for assignment in assignments:
#     print(assignment.assign_num , assignment.proj_num, assignment.assign_date)

# connection = engine.connect()
# query = "SELECT * FROM employee WHERE emp_num > :value"
# sql_expression = text(query)
# param = {'value': 101}
# result = connection.execute(sql_expression, param)

# for row in result:
#     print(row[0])

# connection.close()

'''
1. add new employee record to employee table with id = 168, firstname = 'John', lastname = 'Doe', initials = 'JD', job = 'Programmer', hire_date = today's date.
'''
# employees = session.query(Employee).first()
# employees = employee(emp_num=168, emp_lname="Doe", emp_fname="John", emp_initial="JD", emp_job= "Programmer", emp_hiredate=datetime.today())
# session.add(employees)
# session.commit()
'''
2. query the new created employee (id=168) from employee table, with information of employee id, firstname, lastname, initials, job description (join with job), charge per hour (join with job) and hire_date.
'''
# employees = session.query(Employee).first()
# employees = session.query(Employee.emp_num, Employee.emp_fname, Employee.emp_lname, Employee.emp_initial, Job.job_description, Job.job_chg_hour, Employee.emp_hiredate).\
#     join(Job, Employee.job_code == Job.job_code).filter(Employee.emp_num == 168).first()

# print(employees)

'''
3. update the new created employee (id=168) job, from 'Programmer' to 'Database Designer'.
'''
# employee = session.query(Employee).filter(Employee.emp_num == 168).first()
# employee.emp_job = "Database Designer"
# session.commit()
'''
4. query all project that has "Programmer" assigned to, with information of project id, project name and program manager (join with employee).
'''
# projects = session.query(Project.proj_num, Project.proj_name, Employee.emp_fname, Employee.emp_lname).\
#     join(Assignment, Project.proj_num == Assignment.proj_num).\
#     join(Employee, Assignment.emp_num == Employee.emp_num).\
#     filter(Employee.emp_job == "Programmer").all()

# for project in projects:
#     print(project.proj_num, project.proj_name, project.emp_fname, project.emp_lname)
    
'''
5. delete the new created employee (id=168) from employee table.
'''
# employee = session.query(Employee).filter(Employee.emp_num == 168).first()
# session.delete(employee)
# session.commit()