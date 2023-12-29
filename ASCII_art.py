"""Ce code permet d'afficher les chaines de caractères saisis avec des caractères # (tous en majuscules)"""
from random import randint
import time

 ##
#  #
####
#  #
#  #

A = [" ## ","#  #","####","#  #","#  #"]

##
# #
###
#  #
###

B = ["##  ","# # ","### ","#  #","### "]

 ##
#  #
#
#  #
 ##

C = [" ## ","#  #","#   ","#  #"," ## "]


###
#  #
#  #
#  #
###

D = ["### ","#  #","#  #","#  #","### "]

####
#
###
#
####

E = ["####","#   ","### ","#   ","####"]

####
#
###
#
#

F = ["####","#   ","### ","#   ","#   "]

 ## 
#  
# ##
#  #
 ##

G = [" ## ","#   ","# ##","#  #"," ## "]

#  #
#  #
####
#  #
#  #

H = ["#  #","#  #","####","#  #","#  #"]

###
 #
 #
 #
###

I = ["### "," #  "," #  "," #  ","### "]

 ###
  #
  #
# #
 # 

J = [" ###","  # ","  # ","# # "," #  "]

#  #
# #
##
# #
#  #

K = ["#  #","# # ","##  ","# # ","#  #"]

#
#
#
#
####

L = ["#   ","#   ","#   ","#   ","####"]

#   #
## ##
# # #
#   #
#   #

M = ["#   #","## ##","# # #","#   #","#   #"]

#   #
##  #
# # #
#  ##
#   #

N = ["#  #","## #","# ##","#  #","#  #"]

 ## 
#  #
#  #
#  #
 ## 
 
O = [" ## ","#  #","#  #","#  #"," ## "]

###
#  #
###
#
#

P = ["### ","#  #","### ","#   ","#   "]

 ## 
#  #
#  #
# ##
 # #

Q = [" ## ","#  #","#  #","# ##"," # #"]

###
#  #
###
# #
#  #

R = ["### ","#  #","### ","# # ","#  #"]

 ##
#  
 ##
   #
 ##

S = [" ## ","#   "," ## ","   #"," ## "]

####
 ##
 ##
 ##
 ##

T = ["####"," ## "," ## "," ## "," ## "]

#  #
#  #
#  #
#  #
####

U = ["#  #","#  #","#  #","#  #","####"]

 #   # 
 #   #
 #   #
  # #
   #
 
V = ["#   #","#   #","#   #"," # # ","  #  "]

#     #
#  #  #
# # # #
##   ##
#     #

W = ["#     #","#  #  #","# # # #","##   ##","#     #"]

##   ##
  # #  
   #   
  # #  
##   ##

X = ["##   ##","  # #  ","   #   ","  # #  ","##   ##"]

##   ##
  # #  
   #   
   #
  ###  

Y = ["##   ##","  # #  ","   #   ","   #   ","  ###  "]

#####
   # 
  #
 #
#####

Z = ["#####","   # ","  #  "," #   ","#####"]


INCONNU = ["????","????","????","????","????"]
## ==== Programme principale :
print('\n')   
l = input("Veuillez saisir la chaine de caracteres a convertir en ASCII_art : ")
print("\n")

i = l.lower() # Mettre toutes les lettres en miniscules
chaine_split = i.split("\n")
for p in chaine_split: # i est un mot 
    for k in range(5): # Parcourir les lignes
        for j in range(len(p)): # Parcourir les colones
            if   p[j] == "a": print(A[k],end=" ")
            elif p[j] == "b": print(B[k],end=" ")
            elif p[j] == "c": print(C[k],end=" ")
            elif p[j] == "d": print(D[k],end=" ")
            elif p[j] == "e": print(E[k],end=" ")
            elif p[j] == "f": print(F[k],end=" ")
            elif p[j] == "g": print(G[k],end=" ")
            elif p[j] == "h": print(H[k],end=" ")
            elif p[j] == "i": print(I[k],end=" ")
            elif p[j] == "j": print(J[k],end=" ")
            elif p[j] == "k": print(K[k],end=" ")
            elif p[j] == "l": print(L[k],end=" ")
            elif p[j] == "m": print(M[k],end=" ")
            elif p[j] == "n": print(N[k],end=" ")
            elif p[j] == "o": print(O[k],end=" ")
            elif p[j] == "p": print(P[k],end=" ")
            elif p[j] == "q": print(Q[k],end=" ")
            elif p[j] == "r": print(R[k],end=" ")
            elif p[j] == "s": print(S[k],end=" ")
            elif p[j] == "t": print(T[k],end=" ")
            elif p[j] == "u": print(U[k],end=" ")
            elif p[j] == "v": print(V[k],end=" ")
            elif p[j] == "w": print(W[k],end=" ")
            elif p[j] == "x": print(X[k],end=" ")
            elif p[j] == "y": print(Y[k],end=" ")
            elif p[j] == "z": print(Z[k],end=" ")
            elif p[j] == " ": print("  ",end=" ")
            else: print(INCONNU[k],end=" ")
        print("")
    print("")


