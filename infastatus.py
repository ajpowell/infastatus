'''
infastatus.py

Code to check and display Infa related processes

'''

import os

#     Ver    Author          Date       Comments
#     ===    =============== ========== =======================================
ver = 0.1  # Adrian Powell   2022-02-20 Initial code

appname = 'infastatus.py'

'''
Get the process details
'''
def getProcessDetails(name, user):
    processes=[]
    try:
        # iterating through each instance of the process
        for line in os.popen("ps aux | grep " + user + " | grep " + name + " | grep -v grep"):
            #print(lineno)
            fields = line.split()
             
            # extracting Process ID from the output
            # pid = fields[1]
            processes.append(fields)

            # print(fields) 
            # terminating process
            # os.kill(int(pid), signal.SIGKILL)

        # print("\nProcesses found: {}".format(len(processes)))
        return len(processes)
         
    except:
        print("Error Encountered while running script")
        return 0

'''
Return the formatted status display
'''
def displayStatus(displayname, name, user, position):
    if getProcessDetails(name, user):
        status_message = '[ OK ]'
    else:
        status_message = '[    ]'

    if len(displayname) > position:
        displayname = displayname[0:position-4] + '...'

    spaces = position - len(displayname)
    buffer = ''
    for n in range(spaces):
        buffer = buffer + ' '

    return displayname+ buffer + status_message



def main(): 
    print('\n{} v{}\n'.format(appname, ver))

    print(displayStatus('Tomcat Core', 'ISPTomcatBootstrap', 'informat', 25))
    print(displayStatus('Admin Console', '_AdminConsole', 'informat', 25))
    print(displayStatus('pmrepagent', 'pmrepagent', 'informat', 25))
    print(displayStatus('pmserver', 'pmserver', 'informat', 25))

    print('')


if __name__ == '__main__':
    main()
