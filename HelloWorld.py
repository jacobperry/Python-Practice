user = {"name":"Jake", "Experience": 100, "VIP": False}
class player:
    def __init__(self):
        pass
    def makeVIP(self):
        user["VIP"] = True
    def takeVIP(self):
        user["VIP"] = False
    def vipAlert(self):
        if (user["VIP"] == True):
            print('Congratulations, you are a VIP!')
        elif (user["VIP"] == False):
            print("You're not a VIP, visit the store to buy a VIP Pack Today!!!")
        else:
            print('Error. VIP status not found. Issue reported to console.')
class male(player):
    def __init__(self):
        pass
    def jobList(self):
        print("As a male, your available jobs are Plumber, Infantry, Construction and Police. Choose One!")
userType = male()

userType.makeVIP()
userType.jobList()
userType.vipAlert()
userType.takeVIP()
userType.vipAlert()