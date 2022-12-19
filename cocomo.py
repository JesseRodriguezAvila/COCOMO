# Function to calculate parameters of Basic COCOMO
import sys

def printResults(effort, time, staff, model, table, size):
    print("\n-- Effort = {} Person-Month".format(round(effort)))
    print("     E = a * (KLOC^b) = {} * {}^({}) = {}".format(table[model][0], size, table[model][1], effort))

    print("\n-- Development Time = {} Months".format(round(time)))
    print("     time = c * (effort)^d = {} * ({})^{} = {}".format(table[model][2], effort, table[model][3], time) )
    
    print("\n-- Average Staff Required = {} Persons".format(round(staff)))
    print("     AvgStaffReq = effort / time = {} / {} = {}\n".format(effort, time, staff))

def calcuateSoftwareProjectMode(kloc):
    if (kloc >= 2 and kloc <= 50):
        # Organic
        return 0
    elif (kloc > 50 and kloc <= 300):
        # Semi-detached
        return 1
    elif (kloc > 300):
        # Embedded
        return 2
    else:
        sys.exit( "KLoC must be atleast 2 or greater " )

def cocomo(table, kloc):
    # depending on kloc, organic, semi-detached or embedded will be used
    software_project_mode = ["Organic","Semi-Detached","Embedded"]

    # calculate which Software Project mode based on KLoC is going to be used
    whichMode = calcuateSoftwareProjectMode(kloc)
     
    # select row/mode based on kloc (whichMode)
    # index 0 = a, 1 = b, 2 = c, 3 = d
    a, b, c, d = table[whichMode] 


    print("The Software project mode being used: ", software_project_mode[whichMode])

    # Calculate Effort = a * (KLoC)^b
    effort = a * pow(kloc, b)
     
    # Calculate Time = c * (effort)^d
    time = c * pow(effort, d)
     
    # Calculate staff Required, personsRequired = effort / time
    staff_required = effort / time;
     
    # Output Results
    printResults(effort, time, staff_required, whichMode, table, kloc)


software_project_table = [
    [2.4, 1.05, 2.5, 0.38],
    [3.0, 1.12, 2.5, 0.35],
    [3.6, 1.20, 2.5, 0.32]
]

kloc = 9;

cocomo(software_project_table, kloc)