from utils import *
from logic import *
import argparse
import random
parser = argparse.ArgumentParser()
parser.add_argument("Something")

def nORp(value):
    prefix = random.choice([True,False])
    if prefix:
        return '~' + value
    else:
        return value

def randomOp():
    allOperators = [' & ', ' | ', ' ^ ', ' ==> ', ' <== ', ' <=> ']
    pleasePizza =  random.choice(allOperators)
    return pleasePizza

def getSymb():
    allSymbols = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q']
    distinctSymbols = allSymbols[:8]
    hopeFullyRandom = nORp(random.choice(distinctSymbols))
    return hopeFullyRandom


def walkSat(nSym, mClause, maxLit, valueProb):
    kb = PropKB()
    allSymbols = list(symbols('A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q'))
    distinctSymbols = allSymbols[:8]

    # where 0 is a partial expression, and 1 is a full expression
    litNum = 0
    myClauses = []
    while (litNum < mClause):
        expressions = ""
        exCount = 0
        while (exCount) < (maxLit - 1):
            pORf = random.choice([0, 1])
            # print(type(nORp(random.choice(allSymbols))))
            # print(nORp(random.choice(allSymbols)))
            # exit(0)
            if pORf == 0:
                val1 = getSymb()
                # ugh = Expr(randomOp,val1,val2)
                theOP = randomOp()
                ugh = str(theOP + val1)
                expressions += ugh
                litNum += 1
                exCount += 1
            else:
                val1 = getSymb()
                val2 = getSymb()
                paren = random.choice([True,False])
                theOP = randomOp()
                theOP2 = randomOp()
                # if paren:
                #     bitchPlease = str(" ( " + val1 + theOP + val2 + " ) ")
                # else:
                #
                if exCount > 0:
                    bitchPlease = theOP2 + val1 + theOP + val2
                else:
                    bitchPlease = val1 + theOP + val2
                # if exCount > 0:
                #     slow = randomOp()
                #     pleaseWork = slow.join(bitchPlease)
                #     bitchPlease = pleaseWork
                # bitchPlease = Expr(randomOp(),val1,val2)
                expressions += bitchPlease
                exCount += 1
                litNum += 2
        # tellKB = ''.join(map(str, expressions))
        tellExpr = expr(expressions)
        print(tellExpr)
        exit(0)
        myClauses.append(tellExpr)
    print(WalkSAT(myClauses, 0.5, max_flips=10000))


def main():
    # getSymb()
    # exit(0)
    try:
        walkSat(5,0.1,5,1)
    except:
        print("")





if __name__ == "__main__": main()