def toMachineNumber(n,b):
    n = str(n)
    splitting = n.split(".")
    n = "".join(splitting)
    mag = [len(splitting[0]),len(splitting[1])]
    ans = []
    for k,d in enumerate(n):
        # d = int(d)
        a = f"{d}*{b}^{mag[0]-1-k}"
        ans.append(a)
    return " + ".join(ans)
def toFloat(n,b):
    uncode = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = str(n)
    s=0
    total = 0
    for k,d in enumerate(str(n)):
        if k==0:
            s=pow(-1,int(d))
            print(s)
        else:
            val = uncode.find(d)
            print(val)
            real_val = val*pow(b,(len(n)-1-k))
            print(val, real_val, pow(b,(len(n)-1-k)))
            total+=real_val
    return(total)
def toBase(num,base,new_base):
    pass
def findError(n,b):
    pass
    
if __name__ == '__main__':
    print(toMachineNumber(125.33,10))
    print(toFloat("01FF",50))