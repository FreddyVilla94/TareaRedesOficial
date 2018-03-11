import socket

def getHostName():
    hostName = socket.gethostname()
    return hostName

def getHostIp():
    hostName = socket.gethostname()
    ipAddress = socket.gethostbyname(hostName)
    return ipAddress
'''
def getDateTimeZ(zone):
    utc = pytz.utc
    utc.zone
    amsterdam = timezone('Europe/Amsterdam')
    fmt = '%Y-%m-%d %H:%M:%S %Z%z'
    loc_dt = amsterdam.localize(datetime(2002, 10, 27, 6, 0, 0))
    print(loc_dt.strftime(fmt))
'''
def mainMenu():
    print(".::Welcome to CHATEC::.")
    while True:
        option = int(input(" 1. Get server name   \n"
                              " 2. Get server IP     \n"
                              " 3. Get quantity of running processes    \n"
                              " 4. Get time from another country        \n"
                              " 5. Send message client - server         \n"
                              " 6. Exit     \n"
                              "     Option: "))
        if option == 1:
            print("Server Name: ",getHostName())
        elif option ==2:
            print("Server IP: ", getHostIp())
        elif option == 3:
            print("")
        elif option == 4:
            getDateTimeZ("")
            print("")
        elif option == 5:
            print("")
        elif option == 6:
            break
