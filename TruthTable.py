import itertools
from prettytable import PrettyTable
from util import *

class Truths(object):
    def __init__(self, base=None, phrases=None, ints=True):
        if not base:
            raise Exception('Base items are required')
        self.base = base
        self.phrases = phrases or []
        self.ints = ints
        self.results=[]
        # generate the sets of booleans for the bases
        self.base_conditions = list(itertools.product([False, True],repeat=len(base)))

        # regex to match whole words defined in self.bases
        # used to add object context to variables in self.phrases
        self.p = re.compile(r'(?<!\w)(' + '|'.join(self.base) + ')(?!\w)')


    def calculate(self, *args):
        # convert tuple args  to dict, then evaluate it.
        evaluate_phrases=(evaluate(parse(self.phrases,),dict(zip(self.base,list(args)))))
        row=list(args) + [evaluate_phrases]
        self.results.append(row)
        if self.ints:
            return [int(item) for item in row]
        else:
            return row

    def getResult(self):
        self.getTruthTable()
        return self.results

    def getTruthTable(self):
        t = PrettyTable(self.base + [self.phrases])
        t.format=True
        for conditions_set in self.base_conditions:
            t.add_row(self.calculate(*conditions_set))
        """only for self debugging"""
        """return str(t)"""
        return t.get_html_string()

