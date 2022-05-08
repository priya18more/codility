S = 'CAGCCTA'
P = [2,5,0]
Q = [4,5,6]
'''
impact factor : A:1, C:2, G:3 and T:4
'''
def impactFactor(S,P,Q):
   R = []
   N = len(S)
   A = [0]*N
   C = [0]*N
   G = [0]*N
   T = [0]*N

   a=c=g=t=0

   for i in range(N):
       if S[i] == 'A':
           a+=1
           print('a: ',a)
       elif S[i] == 'C':
           c+=1
           print('c :', c)
       elif S[i] == 'G':
           g+=1
           print('g: ',g)
       elif S[i] == 'T':
           t+=1
           print('t :',t)
       A[i] = a
       print(A)
       C[i] = c
       print(C)
       G[i] = g
       print(G)
       T[i] = t
       print(T)

   for i in range(len(P)):
       if P[i] == Q[i]:
           if S[P[i]] == 'A':
               R.append(1)
           elif S[P[i]] == 'C':
               R.append(2)
           elif S[P[i]] == 'G':
               R.append(3)
           elif S[P[i]] == 'T':
               R.append(4)
       elif A[P[i]] < A[Q[i]] or S[P[i]] == 'A':
           print(A[P[i]])
           print(A[Q[i]])
           R.append(1)
       elif C[P[i]] < C[Q[i]] or S[P[i]] == 'C':
           print(C[P[i]])
           print(C[Q[i]])
           R.append(2)
       elif G[P[i]] < G[Q[i]] or S[P[i]] == 'G':
           R.append(3)
       elif T[P[i]] < T[Q[i]] or S[P[i]] == 'T':
           R.append(4)
   return R

print(impactFactor(S,P,Q))