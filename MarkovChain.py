import sys

CUTOFF = 1.0/1e60

def markovChainSum(q,z):
    # Starts the cache outside the helper so that it saves correctly
    cache = {}

    return markovHelper(0, 0, q, z, cache, 1.0)


def markovHelper(q_len, p_len, q, z, cache, prob):

   # Makes sure the honest has reached z confirmations and is greater than the attacker
   # Also checks for probability cutoff
   if prob < CUTOFF or (p_len >= z and q_len < z and p_len - q_len >= 35):
      return 0.0

   # Makes sure the attacker has z or more confirmations and that they caught up to the honest chain
   if q_len >= p_len and q_len >= z:
      return 1.0

   # Keeps track of honest and attacker length
   lengths = (q_len, p_len)

   # Returns probability already calculated for specific state
   if lengths in cache:
      return cache[lengths]
   p = 1 - q 

   # Recursive formula described in README
   prob = q * markovHelper(q_len + 1, p_len, q, z, cache, prob * q) + p * markovHelper(q_len, p_len + 1, q, z, cache, prob * p)

   # Saves state with probability calculated
   cache[lengths] = prob

   return prob


# Testing your work by repeated submission is a giant waste of your time.  Always optimize your time when coding!!!

# Instead, write your own tests!

def Test():

  # Your algorithm might go deep, so you may need to change the recursion limit.
  # At the same time, this might make an infinite recursion hard to find

  sys.setrecursionlimit(10000)

  q=0.3

  for z in range(1,11):
    #s = satoshi(q,z)
    #mc = monteCarlo(q,z, 10000)
    ms = markovChainSum(q,z)
    #print("q:", q, " z:", z, " satoshi: %3.3f" % (s*100), " monte carlo: %3.3f" % (mc*100), " markov sum: %3.3f" % (ms*100))
    print(ms)
Test()