
import random
import math    # cos() for Rastrigin
import copy    # array-copying convenience
import sys     # max float
from pdb import pm
import time 
import csv;
import numpy as np


#Structures et fonctions liées à la problématiques

class Node:
    def __init__(self,sol,item,nbr_item,pmax):
        self.sol=sol
        self.item=item
        self.nbr_item=nbr_item
        self.pmax=pmax

class so:
    def __init__(self,item,nbr_item,):
        self.item=item
        self.nbr_item=nbr_item
        
def sortie_sol(solution,items_ord):
    res=[]
    
    for i in range(len(solution)):
        if (solution[i] != 0):
            s=so(i+1,solution[i])
            res.append(s)
    return res
        
def fitness_(position,items_ord, s):
      value=0
      for t in range(int(s)):
          value+=position[t]*items_ord[t][0]
      return value
 
#Fonction Générer nbr_exmp
def rand_nbr_exp(item,items_ord, s,cap):
        nbr_exp=0
        nbr_exp_max= cap // items_ord[item][1]
        
        nbr_exp= random.randint(0,int(nbr_exp_max/20))
        return nbr_exp 

#Fonction Ajuster Solution
def Ajust_sol(solution,items_ord, s,cap_sac):
        tab_pourc=[0.0 for i in range(int(s))]
        som=abs(np.sum(solution))
        
        sol=[0 for i in range(int(s))]
        k=0
        
        while (k < int(s)):
            p=abs(solution[k])/som
            tab_pourc[k]=p
            k+=1
        
        tab_ind=[-1 for i in range(int(s))]
        tab_coche=[0 for i in range(int(s))]
        
        ind=0
        j=0
        while (j < int(s)):
           max_p=0
           for i in range(int(s)):
               if ((tab_pourc[i]>=max_p) and (tab_coche[i]!= -1)):
                   max_p=tab_pourc[i]
                   ind=i
           tab_ind[j]=ind
           tab_coche[ind]=-1
           j+=1
         
        k=0
        #print("Voici tab ind",tab_ind)
        
        while (k < int(s)):
            indice=tab_ind[k]
            cap= Capacity(sol, items_ord, s, cap_sac)
            nbr_exp_max= cap // items_ord[indice][1]
            nbr_exp= random.randint(nbr_exp_max-2,nbr_exp_max)
            if (nbr_exp<0):
                nbr_exp=0
            sol[indice]= nbr_exp
            k+=1    
         
        t=0
        while (t < int(s)):
            indice=tab_ind[t]
            cap=Capacity(sol, items_ord, s, cap_sac)
            if (cap >= items_ord[indice][1]):
                sol[indice]+=cap//items_ord[indice][1]
    
            t+=1
       
        return sol
    
# wolf class
class wolf:
  def __init__(self,s, items_ord, cap_sac):
    
    self.position = [0 for i in range(int(s))]

    for i in range(int(s)):
        cap=Capacity(self.position, items_ord, s,cap_sac) 
        x=rand_nbr_exp(i,items_ord, s,cap)
        
        if (cap >= items_ord[i][1]):
             
             self.position[i] = x
             
 
    self.fitness = fitness_(self.position,items_ord, s) # curr fitness
    
 


def Eval(items_ord,Q1,s):
    
    e=0
    for t in range(int(s)):
        e+=Q1.sol[t]*items_ord[t][0]
    e=float(e)
    if (Q1.item != (int(s)-1)):
        e=e+((Q1.pmax /(items_ord[Q1.item+1][1]))*items_ord[Q1.item+1][0])
    return e

def Objfun(solution, items_ord, s):
       value=0
       for t in range(int(s)):
          value+=solution[t]*items_ord[t][0]
       return value
   
def Capacity(solution, items_ord, s,cap_sac):
        full=0
        capacity=cap_sac
        for t in range(int(s)):
           full+=solution[t]*items_ord[t][1]
        capacity=cap_sac-full
        return capacity

def Voisin( solution,k, i ,j , cap_sac,items_ord,s):
        solu=[solution[k] for k in range(int(s))]


        
        nb=0
       
        while (k>=items_ord[j][1]):
            
            nb+=1
            solu[j]= nb
            k-=items_ord[j][1]
            
        #print("voici solu apres nb",solu)
        return solu


def nouv_voisinage(solution,i,items_ord,cap_sac,s):
        solu=[solution[o] for o in range(int(s))]
        if (solution[i]!=0):
          solu[i] = solution[i]-1
        else:
          solu[i]=0
        return solu

def min_poids(items_ord,cap_sac,s):
    min=cap_sac
    for i in range (int(s)):
        if (items_ord[i][1]<min):
            min=items_ord[i][1]
    return min


#Fonction Générer nbr_exmp
def rand_nbr_exp_ag(item,items_ord, s,cap):
        nbr_exp=0
        nbr_exp_max= cap // items_ord[item][1]
        nbr_exp= random.randint(0,nbr_exp_max)
        return nbr_exp 
    
#creer sol aléatoire
def rand_sol_ag(production,w_max,dim):
    sol=[0 for i in range(dim)]
    for i in range(dim):
        cap=Capacity(sol, production, dim,w_max) 
        x=rand_nbr_exp_ag(i,production, dim,cap)
        if (cap >= production[i][1]):
            sol[i] = x
    return sol

def Ajust_sol_ag(solution,production,w_max,dim):
       
        sol=[solution[i] for i in range(dim)]
        t=0
        while (t < dim):
            cap=Capacity(solution, production, dim, w_max)
            if (cap >= production[t][1]):
                sol[t]+=cap//production[t][1]
    
            t+=1
       
        return sol







def f(g,w_max,production,dim):
    weight = sum([production[j][1] * g[j] for j in range(dim)])
    if weight <= w_max:
        return sum([production[j][0] * g[j] for j in range(dim)]), weight
    else:
        return 1, weight
    
    
    
def select(score):
    total = sum(score)
    threshold = random.random() * total
    sum_s = 0
    for i, s in enumerate(score):
        sum_s += s
        if sum_s > threshold:
            return i
        
def find_elite(score, weight=None):
    if not weight is None and len(list(set(score))) == 1:
        min_weight = 1e+6
        min_index = None
        for i, w in enumerate(weight):
            if min_weight > w:
                min_weight = w
                min_index = i
        return min_index
    else:
        max_score = -1
        max_index = None
        for i, val in enumerate(score):
            if max_score < val:
                max_score = val
                max_index = i
        return max_index


def cross(parent1, parent2):
    length = len(parent1)
    r1 = int(math.floor(random.random() * length))
    r2 = r1 + int(math.floor(random.random() * (length - r1)))

    child = copy.deepcopy(parent1)
    child[r1:r2] = parent2[r1:r2]

    return child

def mutate(geen,n,cross_rate,dim):
    for i in range(n):
        for l in range(dim):
            if random.random() > cross_rate:
                geen[i][l] = 1 - geen[i][l]
                if geen [i][l] < 0 :
                    geen [i][l] = 0

    return geen











def import_csv(URL):
  URL+=".csv"
  f=open(URL)
  myReader=csv.reader(f)
  array= np.loadtxt(f,delimiter=";")
  
  return array



def GWO(cap_sac, array , n, nb_it ):

    rnd = random.Random(0)
    items_ord = []
    items=[]
    s=len(array)
    for i in range(int(s)):
        items.insert(i, (int(array[i][0]),int(array[i][1]),i))
     
    
    items_ord=sorted(items,key=lambda item1: (item1 [0]/item1[1]) )  
    items_ord.reverse()

    
    # create n random wolves
    
    population = [ wolf(s,items_ord,cap_sac) for i in range(n)]
 
    # On the basis of fitness values of wolves
    # sort the population in asc order
    population = sorted(population, key = lambda temp: temp.fitness)
    population.reverse()
 
    # best 3 solutions will be called as
    # alpha, beta and gaama
    alpha_wolf, beta_wolf, gamma_wolf = copy.copy(population[: 3])
    #print("alpha_wolf.position=", alpha_wolf.position)
    
    if (nb_it > 2 ) and (nb_it <=5):
        nb_it=nb_it-1
    if (nb_it >5):
        nb_it=nb_it//5
    max_iter=nb_it
    # main loop of gwo
    Iter = 0
    tps1=time.time()
    while Iter < max_iter:
 
        # after every 10 iterations
        # print iteration number and best fitness value so far
       # if Iter % 10 == 0 and Iter > 1:
           # print("Iter = " + str(Iter) + " best fitness = " , alpha_wolf.fitness,"best sol=" ,alpha_wolf.position)
 
        # linearly decreased from 2 to 0
        a = 2*(1 - Iter/max_iter)
 
        # updating each population member with the help of best three members
        for i in range(n):
            
            A1, A2, A3 = a * (2 * random.randint(1,2)-1 ), a * (
              2 * random.randint(1,2) - 1), a * (2 * random.randint(1,2) - 1)
            C1, C2, C3 = 2 * random.randint(1,2), 2*random.randint(1,2), 2*random.randint(1,2)
            #print("A1, A2, A3 =", A1, A2, A3 )
 
            X1 = [0 for i in range(int(s))]
            X2 = [0 for i in range(int(s))]
            X3 = [0 for i in range(int(s))]
            Xnew = [0 for i in range(int(s))]
            for j in range(int(s)):
                X1[j] = abs(alpha_wolf.position[j] - A1 * abs(
                  C1 * alpha_wolf.position[j] - population[i].position[j]))
                X2[j] = abs( beta_wolf.position[j] - A2 * abs(
                  C2 *  beta_wolf.position[j] - population[i].position[j]))
                X3[j] = abs(gamma_wolf.position[j] - A3 * abs(
                  C3 * gamma_wolf.position[j] - population[i].position[j]))
                Xnew[j]+= X1[j] + X2[j] + X3[j]
                Xnew[j]=Xnew[j]//3
             
            #for j in range(int(s)):
               # Xnew[j]=Xnew[j]//3
                
            
            Xnew=Ajust_sol(Xnew,items_ord, s,cap_sac)
            #print("Xnew=", Xnew)
            # fitness calculation of new solution
            fnew = fitness_(Xnew,items_ord, s)
 
            # greedy selection
            if fnew > population[i].fitness:
                population[i].position = Xnew
                population[i].fitness = fnew
                 
        # On the basis of fitness values of wolves
        # sort the population in asc order
        population = sorted(population, key = lambda temp: temp.fitness)
        population.reverse()
        
        # best 3 solutions will be called as
        # alpha, beta and gaama
        alpha_wolf, beta_wolf, gamma_wolf = copy.copy(population[: 3])
         
        Iter+= 1
    tps2=time.time()
    tps=(tps2-tps1)/2
    # end-while
 
    # returning the best solution
    capacite_prise=cap_sac-Capacity(alpha_wolf.position, items_ord, s, cap_sac)
    resultat=sortie_sol(alpha_wolf.position,items_ord)
    return tps, alpha_wolf.fitness,capacite_prise, resultat
