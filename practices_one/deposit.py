import math
def solution(deposit, rate, threshold):
    assert isinstance(deposit, object)
    r = (1+rate/100)
    t = (r-1)*deposit
    e = deposit*r**6
    log_e = math.ceil((math.log(threshold/deposit,r)/r)**r)
    return log_e
    return math.ceil(math.log(threshold/deposit, 1+rate/100))