# error handling
def errHandle(fnc):
    print("                                                                     **********Please choose from the following options**********")
    fnc()


def comErrHandle(fnc, flavor, target):
    print("                                                                     **********Please choose from the following options**********")
    fnc(*flavor, *target)