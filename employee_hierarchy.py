#This program reads a csv file of employee data in order to ouput the data as an employee hierarchy,
#and to output the total salary amount for the entire company.

#import csv module
import csv

#This function recursively finds employees under a manager within the company.
def findEmployees(theList,theManager,Level):
    Level=Level+5
   
    print(' '.rjust(Level), theManager["Employee Name"])
    #This is a flag to determine if the employee is a manager.  If started is True, then
    #the employee is a manager, and don't reprint Employees of:
    started=False
    #Loop through list of employees, and determine if they are an employee of the requested manager(theManager)
    for theRow in theList:
        if theRow["Manager ID"] == theManager["ID"] :
            if started==False: 
                started=True
                print(' '.rjust(Level), "Employees of:", theManager["Employee Name"])
            #Recursive call of findEmployees to determine if the employee is a manager and which
            #employees are under this manager
            findEmployees(theList,theRow,Level)

#Initializes the list of employees
employee_list = []

#Opens the csv file and sets up the reader to read from the given csv file
#reader = csv.DictReader(open('/Users/libbyyork/Documents/Job_applications/infor/employee_data.csv'))
reader = csv.DictReader(open('./employee_data.csv'))

#This for loop creates a list of dictionaries of all employees from the csv file.
for row in reader:
    employee_list.append(row)

sortedDB = sorted(employee_list, key=lambda x: x['Employee Name'])
#This for loop finds the CEO of the company, which is a manager without a manager
for theEmployee in sortedDB:
    if theEmployee["Manager ID"] =="" :
        findEmployees(sortedDB,theEmployee,0)

#Initialize total salary count        
salary_count=0

#This loop sum the salary for each employee into a total and prints out the total
for theEmployee in sortedDB:
    salary_count += int(theEmployee['salary'])
print("Total salary: $%i" % salary_count)
