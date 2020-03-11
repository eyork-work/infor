#This program reads a csv file of employee data in order to ouput the data as an employee hierarchy,
#and to output the total salary amount for the entire company.

#import csv module that holds employee data
import csv
class Employees:
    def __init__(self):
        #initialuze t
        self.theDB = []
    #method finds the employees of a specified manager within a list of dictionaries
    #level holds how far to indent
    def findEmployees(self,theList,theManager,Level):
        #list to hold the employees of the manager
        theEmployees=[]
        #just  dummy to hold a call we dont care about
        theDummy=[]
        #shift every thing over 5
        Level=Level+5
        #print out the employee were looking at
        print(' '.rjust(Level), theManager["Employee Name"])
        #flag set to see if they have reports
        started=False
        #loop the list and see if the manager has a manager id
        for theRow in theList:
            if theRow["Manager ID"] == theManager["ID"] :
                if started==False: 
                    started=True
                    print( ' '.rjust(Level), "Employees of:", theManager["Employee Name"])
                theEmployees.append(theRow["Employee Name"])
                #recusive call to find the list of employees under the current manager
                #and see if each employee is a manager
                theDummy=self.findEmployees(theList,theRow,Level)
        return theEmployees

    #load all the employees into a sorted DB(list of database)
    def loadEmployees(self,theFileLocation):
        self.reader = csv.DictReader(open(theFileLocation))
        self.sortedDB = sorted(self.reader, key=lambda x: x['Employee Name'])
        #make  list of the data 
        for row in self.sortedDB:
            self.theDB.append(row)

    #calculates the salary simple sum of the salary var for each user in DB
    def calcSalary(self,theList):
        salary=0
        for theRow in theList:
            salary+=int(theRow["salary"])
        return salary       

#Create the Employees object
theEmployees=Employees()
#load the object with data
theEmployees.loadEmployees('./employee_data.csv')

#look for the root employee (CEO no manager)
for theEmployee in theEmployees.theDB:
    if theEmployee["Manager ID"] =="" :
        theEmployeesOf=theEmployees.findEmployees(theEmployees.theDB,theEmployee,0)

#show the salary
print("$%s" % f"{theEmployees.calcSalary(theEmployees.theDB):,}")
