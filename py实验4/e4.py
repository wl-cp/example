def powerValue(num):
    GOOD = (num+1) ** 365
    BAD = (1-num) ** 365
    dis = GOOD/BAD
    print("N=1%, GOOD={:.2f}, BAD={:.2f}, dis={:.2f}".format(GOOD, BAD, dis))
powerValue(0.01)