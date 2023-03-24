-- DESTROY VIEWS IF EXISTS FOR REPRODUCIBILITY
DROP VIEW IF EXISTS employee_base_info, employees_1986, manager_info, employees_dpt_info, 
					"Hercules_B", sales_dept, sales_and_development, last_name_freq;

-- Create Queries for Employee Analysis

-- Query #1
-- List the employee number, last name, first name, sex, and salary of each employee.
CREATE VIEW employee_base_info AS
SELECT e.emp_no, e.last_name, e.first_name, e.sex, s.salary
  FROM employees AS e
  LEFT JOIN salaries AS s
    ON s.emp_no = e.emp_no;
	
-- Query #2
-- List the first name, last name, and hire date for the employees who were hired in 1986.
CREATE VIEW employees_1986 AS
SELECT first_name, last_name, hire_date
  FROM employees
 WHERE hire_date >=  '1986-01-01' AND hire_date < '1986-12-31';
 
-- Query #3
-- List the manager of each department along with their department number, department name, employee number, last name, and first name.
CREATE VIEW manager_info AS
SELECT e.emp_no, e.last_name, e.first_name, d.dept_no, d.dept_name
  FROM employees AS e
 INNER JOIN dept_manager as dm
    ON dm.emp_no = e.emp_no
 INNER JOIN departments as d
    ON d.dept_no = dm.dept_no;
	
	
	
-- Query #4
-- List the department number for each employee along with that employee’s employee number, last name, first name, and department name.
CREATE VIEW employees_dpt_info AS
SELECT e.emp_no, e.last_name, e.first_name, d.dept_no, d.dept_name
  FROM employees AS e
 INNER JOIN dept_emp as de
    ON de.emp_no = e.emp_no
 INNER JOIN departments as d
    ON d.dept_no = de.dept_no;


-- Query #5
--List first name, last name, and sex of each employee whose first name is Hercules and whose last name begins with the letter B.
CREATE VIEW "Hercules_B" AS
SELECT first_name, last_name, sex
  FROM employees
 WHERE first_name = 'Hercules' AND last_name LIKE 'B%';
 
 
-- Query #6
-- List each employee in the Sales department, including their employee number, last name, and first name.
CREATE VIEW sales_dept AS
SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
  FROM employees AS e 
 INNER JOIN dept_emp AS de
    ON de.emp_no = e.emp_no
 INNER JOIN departments AS d
    ON d.dept_no = de.dept_no
  WHERE d.dept_name = 'Sales';
  
-- Query #7
-- List each employee in the Sales and Development departments, including their employee number, last name, first name, and department name.
CREATE VIEW sales_and_development AS
SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
  FROM employees AS e 
 INNER JOIN dept_emp AS de
    ON de.emp_no = e.emp_no
 INNER JOIN departments AS d
    ON d.dept_no = de.dept_no
  WHERE d.dept_name IN ('Sales', 'Development')
  ORDER BY d.dept_name DESC, e.emp_no;

-- Query #8
-- List the frequency counts, in descending order, of all the employee last names (that is, how many employees share each last name).
CREATE VIEW last_name_freq AS
SELECT last_name, COUNT(last_name)
FROM employees
GROUP BY last_name
ORDER BY COUNT(last_name) DESC;

-- SELECT ALL FROM EACH VIEW TO VALIDATE VIEWS
SELECT * FROM employee_base_info;
SELECT * FROM employees_1986;
SELECT * FROM manager_info;
SELECT * FROM employees_dpt_info;
SELECT * FROM "Hercules_B";
SELECT * FROM sales_dept;
SELECT * FROM sales_and_development;
SELECT * FROM last_name_freq;
