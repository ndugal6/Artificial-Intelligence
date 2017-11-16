from utils import *
from logic import *
import argparse
import random


# Nicholas Dugal
# Artificial Intelligence: A Modern Approach
# 11/15/2017
#-----------------------
# Randomly determines the sign of a given symbol using the given probability
#-----------------------
def nORp(value,q):  #Desperately needs hacking. Ugly but works.
    #Here we create an array with a proportional amount Trues and False as the specified probability
    pNeg = int(100*q)
    pPos = 100-pNeg
    pArrayLol = [True*pNeg] + [False*pPos]
    #We select a random value and either add a negation symbol or return the symbol w/o modifications
    prefix = random.choice(pArrayLol)
    if prefix:
        return '~' + value
    return value

#-----------------------
# Randomly returns a valid operator for literal construction
#-----------------------
def randomOp():
    allOperators = [' & ', ' | ', ' ^ ', ' ==> ', ' <== ', ' <=> ']
    pleasePizza =  random.choice(allOperators)
    return pleasePizza

#-----------------------
# Randomly returns a symbol from a subset of size n of all possible symbols,
#-----------------------
def getSymb(n,q):
    # Since I know the max number of max symbols you can specify I manually made an array and slice off only what I need
    allSymbols = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q']
    distinctSymbols = allSymbols[:n]
    # Randomly add negation to the symbols
    hopeFullyRandom = nORp(random.choice(distinctSymbols),q)
    return hopeFullyRandom

#-----------------------
# This beast implements the walksat algorithm as defined in Artificial Intelligence: A Modern Approach
#-----------------------
def walkSat(n, m, k, q):
    myClauses = []
    # Loop until we have aquired the proper amount of clauses
    while (len(myClauses) < m):
        # Expression is a string we will be working with in building the clauses
        expressions = ""
        litCount = 0 # How Lit we are
        #Loop until we have constructed a proper expression -- contains either k or k-1 literals
        while (litCount) < (k - 1):
            #--Do I want a compound or single literal construction this go round
            decisionsDecisions = random.choice([0, 1])
           # Single literal constructor
            if decisionsDecisions == 0:
                val1 = getSymb(n,q)
                theOP = randomOp()
                ugh = str(theOP + val1)
                expressions += ugh
                litCount += 1
            else:
                val1 = getSymb(n,q)
                val2 = getSymb(n,q)
                paren = random.choice([True,False])
                theOP = randomOp()
                theOP2 = randomOp()
                newExpression = val1 + theOP + val2
                #Let's randomly surround coumpound literals with parenthesis
                if paren:
                    newExpression = "( "+newExpression+" )"
                #Unless this is the first literal, we will need an operator on the left hand side
                if litCount > 0:
                    newExpression = theOP2 + newExpression
                expressions += newExpression
                litCount += 2

        try:
            tellExpr = expr(expressions)
            print(tellExpr)
            myClauses.append(tellExpr)
        except:
            continue
    print(WalkSAT(myClauses, 0.5, max_flips=100))


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('-n', action='store', dest='n', required=True, nargs='+',
                        help=' ex: "-n 10\nA positive integer representing the number of distinct propositional symbols in a random set of clauses.')

    parser.add_argument('-m', action='store', dest='m', required=True,
                        help=' ex: "-m 15\nA positive integer representing the number of clauses in S.')

    parser.add_argument('-k\n', action='store', dest='k', required=True,
                        help=' ex: "-k 4\nthe maximum number of literals in a clause in the random set of clauses.')

    parser.add_argument('-q', action='store', dest='q', required=True,
                        help='ex: "-q 0.5\n0.40 ≤ q ≤ 0.60, rounded to the hundredths,  q is the probability that a literal in a clause is a negative literal. \n'
                             'The purpose of this parameter is to assure that the random clauses generated each would \n'
                             'typically have both positive and negative literals - if all clauses have only positive literals, \n'
                             'we know for sure the set S is satisfiable')
    # ---------------------------
    # Argument Parsing
    # ---------------------------
    args = parser.parse_args()
    n = args.n
    m = args.m
    k = args.k
    q = args.q


    # -----------------------------------------
    # Print the information recd.
    # -----------------------------------------
    print("Parameters passed")
    print("=" * 15)
    print("Distinct Symbols    : %s" % str(n))
    print("Number of clauses : %s" % str(m))
    print("Max Amount of Literals   : %s" % str(k))
    print("Negative Literal Probability : %s" % str(q))
    # walkSat(n, m, k, q)
    try:
        walkSat(n,m,k,q)
    except:
        print("Uhhh-Ohhhh")





if __name__ == "__main__": main()