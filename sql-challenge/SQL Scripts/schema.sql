-- DESTROY SCHEMAS
DROP TABLE IF EXISTS titles, employees, departments, dept_manager, dept_emp, salaries CASCADE;

-- Create All Schemas
-- Create Titles Schema
CREATE TABLE titles(title_id VARCHAR(255) NOT NULL PRIMARY KEY,
				    title VARCHAR(255));
					
-- Create Employees Schema
CREATE TABLE employees(emp_no INT PRIMARY KEY NOT NULL,
					   emp_title_id VARCHAR(255) NOT NULL,
					   birth_date DATE,
					   first_name VARCHAR(255),
					   last_name VARCHAR(255),
					   sex VARCHAR(255),
					   hire_date DATE,
					   FOREIGN KEY (emp_title_id) REFERENCES titles(title_id));

-- Create Departments Schema
CREATE TABLE departments(dept_no VARCHAR(255) NOT NULL PRIMARY KEY,
						 dept_name VARCHAR(255));

-- Create Dept_Manager Schema
CREATE TABLE dept_manager(dept_no VARCHAR(255) NOT NULL,
						   emp_no INT NOT NULL,
						  FOREIGN KEY (dept_no) REFERENCES departments(dept_no),
						  FOREIGN KEY (emp_no) REFERENCES employees(emp_no),
						  PRIMARY KEY (dept_no, emp_no));
						  
-- Create Dept_Emp Schema
CREATE TABLE dept_emp( emp_no INT NOT NULL,
					  dept_no VARCHAR(255),
					  FOREIGN KEY (emp_no) REFERENCES employees(emp_no),
					  FOREIGN KEY (dept_no) REFERENCES departments(dept_no),
					  PRIMARY KEY (emp_no, dept_no));

-- Create Salaries Schema
CREATE TABLE salaries(emp_no INT NOT NULL PRIMARY KEY,
					  salary INT,
					  FOREIGN KEY (emp_no) REFERENCES employees(emp_no));
					  			  
-- Copy Data from csvs into tables from tmp folder (avoids errors on MacOS)
-- ALSO I could have used pgAdmin's Import tool after creating the schemas.

-- COPY titles
COPY titles
FROM '/tmp/data/titles.csv'
DELIMITER ','
CSV HEADER;

-- COPY employees
COPY employees
FROM '/tmp/data/employees.csv'
DELIMITER ','
CSV HEADER;

-- COPY departments
COPY departments
FROM '/tmp/data/departments.csv'
DELIMITER ','
CSV HEADER;

-- COPY dept_manager
COPY dept_manager
FROM '/tmp/data/dept_manager.csv'
DELIMITER ','
CSV HEADER;

-- COPY dept_emp
COPY dept_emp
FROM '/tmp/data/dept_emp.csv'
DELIMITER ','
CSV HEADER;

-- COPY salaries
COPY salaries
FROM '/tmp/data/salaries.csv'
DELIMITER ','
CSV HEADER;

-- Select data to confirm import
SELECT * FROM titles;
SELECT * FROM employees;
SELECT * FROM departments;
SELECT * FROM dept_manager;
SELECT * FROM dept_emp;
SELECT * FROM salaries;