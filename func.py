import re
from TruthTable import Truths


def getVariables(expression):
    """
    regex the variables (only alphabets supported)
    also have to set and sort them
    """
    sp = re.compile('[a-zA-Z0-9]')
    variables = sp.findall(expression)
    return sorted(list(set(variables)))

def getTruths(variables,expression):
    """ return Truths (with lists and tables)"""
    result = Truths(variables, expression)
    return result

def GenCNF(variables,t):
    """ generate CNF list """
    res = []
    for row in t:
        if row[-1] == True:
            continue
        res.append('∨'.join(map(lambda iv: ('' if iv[0] else '￢') + variables[iv[0]], enumerate(row[:-1]))))
    return res

def GenDNF(variables,t):
    """ generate DNF list """
    res = []
    for row in t:
        if row[-1] == False:
            continue
        res.append('∧'.join(map(lambda iv: ('' if iv[1] else '￢') + variables[iv[0]], enumerate(row[:-1]))))
    return res


def PrintCNF(variables,table):
    """ print CNF """
    cnfs = GenCNF(variables,table)
    return 'CNF: ' + ' ∧ '.join(cnf.join('()') for cnf in cnfs)

def PrintDNF(variables,table):
    """ print DNF """
    dnfs = GenDNF(variables,table)
    return 'DNF: ' + ' ∨ '.join(dnf.join('()') for dnf in dnfs)

def deduce(variables,results):
    """ pick out the False column and return dict with variables as key"""
    for result in results:
        if not result[-1]:
            return dict(zip(sorted(variables),result))
    return 'Failed'


