import random
import math
import sys

# Wouldnt it be nice for graders to see your explaination of what craziness you are doing???
def satoshi(q,z):
    # Computes initial terms needed for formula
    p = 1 - q
    λ = (z * q) / p
    sum_series = 0
    
    # This computes the series formula listed in the assignment write up
    for k in range(0, z + 1):
      sum_series += ((math.pow(λ, k) * math.exp(-λ))/math.factorial(k)) * (1 - math.pow(q / p, z - k))
    # Returns final probability
    return 1 - sum_series

# Remember to comment the what, why and high-level how
# Dont explain basic python language features.  Expect that your reader knows python.  Explain what you are trying to do and how the python code
# gets there!
MAX_LEAD = 35
def monteCarlo(q,z, numTrials=50000):
    # Runs simulation 50000 times and calculates attacker success
    attacker_success = 0
    for i in range (0, numTrials):
      if monte_helper(q, z):
         attacker_success += 1
    return attacker_success/numTrials
       
def monte_helper(q, z):
   q_len = 0 # Attacker length
   p_len = 0 # Honest length
   winner = False # By default honest is winnner
  
   # Keep running while honest chain is less than z and less than 35 blocks than
   # attacker chain
   while(p_len < z or p_len < q_len + MAX_LEAD):
      
      # Checking for attacker win, has to be longer than honest chain and honest has to have z or less confirmations
      if(q_len >= p_len and q_len >= z + 1):
         winner = True
         break
      # Simulate attacker or honest mining
      if random.random() < q:
        q_len += 1
      else:
        p_len += 1

   return winner
 

# Testing your work by repeated submission is a giant waste of your time.  Always optimize your time when coding!!!
# Instead, write your own tests!
def Test():
  # Your algorithm might go deep, so you may need to change the recursion limit.
  # At the same time, this might make an infinite recursion hard to find
  sys.setrecursionlimit(5000)
  q=0.1

  for z in range(0,11):
    s = satoshi(q,z)
    mc = monteCarlo(q,z, 50000)
    print("q:", q, " z:", z, " satoshi: %3.3f" % (s*100), " monte carlo: %3.3f" % (mc*100))

Test()