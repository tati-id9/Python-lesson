# Постройте график функции 𝑓(𝑥)=5𝑥^2+10𝑥−30
# По графику определите, при каких значения x значение функции отрицательно.

from sympy import *

x = symbols('x')
f = 5*x*x+10*x-30
p1 = plot(f)