employee = session.query(Employee).filter(Employee.emp_num == 999).first()
employee.job_code = 510
session.commit()
