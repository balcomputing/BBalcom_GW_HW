CREATE TABLE departments (
	dep_no		VARCHAR(10)	NOT NULL,
	dept_name	VARCHAR(20)	NOT NULL,
	PRIMARY KEY (dep_no)
);

CREATE TABLE employees (
   emp_no      INT             NOT NULL,
   birth_date  DATE            NOT NULL,
   first_name  VARCHAR(14)     NOT NULL,
   last_name   VARCHAR(16)     NOT NULL,
   gender      VARCHAR(1)      NOT NULL,
   hire_date   DATE            NOT NULL,
   PRIMARY KEY (emp_no)
);

CREATE TABLE dept_emp (
	emp_no		INT		NOT NULL,
	dept_no		VARCHAR(10)	NOT NULL,
	from_date	DATE		NOT NULL,
	to_date		DATE		NOT NULL,
	FOREIGN KEY (emp_no) REFERENCES employees(emp_no),
	FOREIGN KEY (dept_no) REFERENCES departments(dep_no)
);

CREATE TABLE dept_manager (
	dept_no		VARCHAR(10)	NOT NULL,
	emp_no		INT		NOT NULL,
	from_date	DATE		NOT NULL,
	to_date		DATE		NOT NULL,
	FOREIGN KEY (emp_no) REFERENCES employees(emp_no),
	FOREIGN KEY (dept_no) REFERENCES departments(dep_no)
);

CREATE TABLE salaries (
	emp_no		INT		NOT NULL,
	salary		INT		NOT NULL,
	from_date	DATE		NOT NULL,
	to_date		DATE		NOT NULL,
	FOREIGN KEY (emp_no) REFERENCES employees(emp_no)
);

CREATE TABLE titles (
	emp_no		INT		NOT NULL,
	title		VARCHAR(20)	NOT NULL,
	from_date	DATE		NOT NULL,
	to_date		DATE		NOT NULL,
	FOREIGN KEY (emp_no) REFERENCES employees(emp_no)
);

-- List the following details of each employee: employee number, last name, first name, gender, and salary.

SELECT employees.emp_no, employees.first_name, employees.last_name, employees.gender, salaries.salary
FROM salaries
INNER JOIN employees ON
employees.emp_no=salaries.emp_no;


-- List employees who were hired in 1986.

SELECT *
FROM employees
WHERE employees.hire_date BETWEEN '$1986-01-01' AND '$1986-12-31'


-- List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name, and start and end employment dates.

SELECT employees.first_name, employees.last_name, departments.dept_name, dept_manager.dept_no, dept_manager.emp_no, dept_manager.from_date, dept_manager.to_date
FROM employees
INNER JOIN dept_manager ON employees.emp_no = dept_manager.emp_no
INNER JOIN departments ON dept_manager.dept_no = departments.dep_no 


-- List the department of each employee with the following information: employee number, last name, first name, and department name.

SELECT employees.first_name, employees.last_name, departments.dept_name, dept_emp.emp_no
FROM employees
INNER JOIN dept_emp ON employees.emp_no = dept_emp.emp_no
INNER JOIN departments ON dept_emp.dept_no = departments.dep_no 

-- List all employees whose first name is "Hercules" and last names begin with "B."

SELECT *
FROM employees
WHERE employees.first_name = 'Hercules' AND employees.last_name LIKE 'B%'


-- List all employees in the Sales department, including their employee number, last name, first name, and department name.

SELECT employees.first_name, employees.last_name, departments.dept_name, dept_emp.emp_no
FROM employees
INNER JOIN dept_emp ON employees.emp_no = dept_emp.emp_no
INNER JOIN departments ON dept_emp.dept_no = departments.dep_no 
WHERE departments.dept_name = 'Sales'

-- List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.

SELECT employees.first_name, employees.last_name, departments.dept_name, dept_emp.emp_no
FROM employees
INNER JOIN dept_emp ON employees.emp_no = dept_emp.emp_no
INNER JOIN departments ON dept_emp.dept_no = departments.dep_no 
WHERE departments.dept_name = 'Sales' OR departments.dept_name = 'Development'

-- In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.

SELECT employees.last_name, COUNT(employees.last_name) 
FROM employees
GROUP BY employees.last_name
ORDER BY COUNT(employees.last_name) DESC