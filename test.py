from TruthTable import Truths
import re


sentence="(~A ∧ B) → C ∧ D"

sp=re.compile('[a-zA-Z]')
variables=sp.findall(sentence)
result=Truths(variables, sentence).getResult()

