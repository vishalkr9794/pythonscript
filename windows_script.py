import platform
import wmi
import logging

# System Informations

my_system = platform.uname()
print(f"System: {my_system.system}")
print(f"Node Name: {my_system.node}")
print(f"Release: {my_system.release}")
print(f"Version: {my_system.version}")
print(f"Machine: {my_system.machine}")
print(f"Processor: {my_system.processor}")

c = wmi.WMI()   
my_system = c.Win32_ComputerSystem()[0]

print(f"Manufacturer: {my_system.Manufacturer}")
print(f"Model: {my_system. Model}")
print(f"Name: {my_system.Name}")
print(f"NumberOfProcessors: {my_system.NumberOfProcessors}")
print(f"SystemType: {my_system.SystemType}")
print(f"SystemFamily: {my_system.SystemFamily}")

# System Processes

# Initializing the wmi constructor
f = wmi.WMI()
 
# Printing the header for the later columns
print("pid   Process name")
 
# Iterating through all the running processes
for process in f.Win32_Process():
     
    # Displaying the P_ID and P_Name of the process
    print(f"{process.ProcessId:<10} {process.Name}")


# Logging Store

#now we will Create and configure logger 
logging.basicConfig(filename="logs_windows.log", 
					format='%(asctime)s %(message)s %(date)s', 
					filemode='w') 

#Let us Create an object 
logger=logging.getLogger() 

#Now we are going to Set the threshold of logger to DEBUG 
logger.setLevel(logging.DEBUG)

#some messages to test
logger.debug("Debug message")
logging.warning('Feature is deprecated')
