from random import *

def CheapPaymentGateWay(data):
    return randint(0, 1)
def ExpensivePaymentGateWay(data):
    print("at expensive")
    return randint(0, 1)
def PremiumPaymentGateWay(data):
    print("at premium")
    rc = randint(0, 1) 
    print(rc)
    return rc