import time
from Counter import Counter

#   create new counter before the loop or loops you wanna count
#   goal may be result of multiplying more iterations, e.g.:
#   
#      num1=10
#      num2=40
#      num3=500
#      tripleLoopCounter = Counter.Counter(num1*num2*num3[,**kvargs])
#      for a in xrange(num1):
#          <your stuff>
#          for b in xrange(num2):
#              for c in xrange(num3):
#                  <your stuff>
#                  tripleLoopCounter.count() <-- creates visualisation of progres in console
#    !!!Remember to place <object>.count() in the last loop/loops you wanna track!!!
    
numbers = [1000,7,31,555,189,99]

for number in numbers:
    counter = Counter(number, bar=20) #start tracking in here
    for x in xrange(number):
        #CODE
        time.sleep(0.01)
        counter.count() #count every time #code is executed
