
import random
import math
import numpy as np

n = 20
k = 5


def partitions(n, k, min_p1=1):
    if k == 0:
        return [[]] if n == 0 else []
    else:
        ret = []
        for p1 in range(min_p1, n + 1):
            for ps in partitions(n - p1, k - 1, p1):
                ret.append([p1] + ps)

        return ret


def check_s(n, k):
    if (Sigma_n(n) % k != 0):
        print("s is not in not a natural number,can't continue...")
        return -1

    s = Sigma_n(n) / k
    return s


def get_s():
    return (Sigma_n(n) / k)


def Sigma_n(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i;
    return sum;


def check_Sigma_Pj(P, n, k):
    Pj = np.zeros(k)
    for i in range(0, k):
        for j in range(0, i + 1):
            Pj[i] += P[j]

    for j in range(0, k):

        if (Pj[j] * n - (Pj[j] * (Pj[j] - 1)) / 2 < ((j + 1) * n * (n + 1)) / (2 * k)):
            return False

    return True


def getPartitions(n, k):
    List = partitions(n, k)

    legal = []
    for list in List:
        if (check_Sigma_Pj(list, n, k) == True):
            legal.append(list)
    print("Your (n,k) = (" + str(n) + "," + str(k) + ")")
    print("Your s(n,k) = " + str(get_s()))
    print("The number of Partitions is " + str(len(legal)))
    print("The legal Partitions is:")
    print(legal)
    print()
    print("Please wait....")
    return legal





def allPartitons_1_to_n():
    allPartitons_1_to_n = []
    for partition in Legal_Partitions:
        list1_n = []
        i = n
        a = []
        for j in partition:
            for index in range(0, j):
                a.append(i)
                i -= 1
            list1_n.append(a)
            a = []

        allPartitons_1_to_n.append(list1_n)

    return allPartitons_1_to_n


def allPartitons_1_to_n_2():
    allPartitons_1_to_n = []
    for partition in Legal_Partitions:
        list1_n = []
        i = n
        a = []
        for j in partition:
            for index in range(0, j):
                a.append(0)

            list1_n.append(a)
            a = []

        while (i > 0):
            for p in list1_n:
                if (0 in p):
                    p.remove(0)
                    p.append(i)
                    i -= 1

        allPartitons_1_to_n.append(list1_n)

    return allPartitons_1_to_n




def Diff(list):
    return ((sum(list) - get_s()) ** 2)


def getDiff(List):
    diff = 0
    for list in List:
        diff += Diff(list)
    return int(diff)


def switch(A, B, a, b):
    A.append(b)
    A.remove(a)
    B.append(a)
    B.remove(b)


def SumPN(list, s):
    Sum = sum(list)
    if (Sum > s):
        return 1
    elif(Sum < s):
        return -1

    else:return 0




def Find(List, list, d):
    new_diff = 0
    current_diff = getDiff(List)
    for list2 in List:
        if (list2 != list and SumPN(list2, get_s()) == -1):
            for a in list:
                for b in list2:
                    new_diff -= (sum(list) - get_s()) ** 2
                    new_diff -= (sum(list2) - get_s()) ** 2
                    new_diff += (sum(list) - a + b - get_s()) ** 2
                    new_diff += (sum(list2) - b + a - get_s()) ** 2

                    if (a - b == d and new_diff <= current_diff):
                        switch(list, list2, a, b)
                        current_diff=getDiff(List)




def f(All):
    NoSolution=[]
    q = 0
    for List in All:
        q += 1

        if (n >= 0):
            r = random.randint(0, 3)
            if (r == 0):
                print("Loading... ", math.floor(100 * q / len(Legal_Partitions)), "%")
            if (r == 1):
                print("Loading..  ", math.floor(100 * q / len(Legal_Partitions)), "%")
            if (r == 2):
                print("Loading.   ", math.floor(100 * q / len(Legal_Partitions)), "%")

        d = 0
        Z = []

        while (getDiff(List) != 0):
            d += 1
            if (d > n-1):


                for i in range(0,2*k):

                    if (h2(List, np.inf, []) == True):
                        break

                    else:
                        if (K_Moves(List) == True):
                            break


                if(getDiff(List)!=0):
                    NoSolution.append([q,Legal_Partitions[q-1]])
                    List=[[get_s()]]


            if(d <= n-1):

                for list in List:
                    if (SumPN(list, get_s()) == 1):
                            if (OneMove(List, list, Z) == True):
                                d = d
                            else:
                                Find(List, list, d)

    print("Done")
    print("Here is the solution:")
    print()
    i = 0


    for List in All:
        if(getDiff(List)==0):
         print("Partition", i + 1, "is", Legal_Partitions[i])
         print(List)
         print()
        i+=1

    j=0
    if(len(NoSolution)==0):
     for List in All:
         for list in List:
             if (j == 0):
                 print(
                     "Great ,now if there is a problem I will print it here")
                 j = 1
             if (sum(list) != get_s()):
                 i += 1
                 print("False:" + str(i))
                 print("s=" + str(get_s()))
                 print("list sum=" + str(sum(list)))
                 print(list)
                 print()
                 print(List)
                 print()
                 print()




    if(len(NoSolution)>0):
        print("There is ", len(NoSolution), "partitions without solution")
        print("The partitions with no solution is :")
        print("<Index,Partition>")
        for l in NoSolution:
            print(l)

        return -1

    return 1


def IsInZ(Z, V):
    for v in Z:
        if (v == V):
            return True
    return False


def OneMove(List, list, Z):
    for list2 in List:
        if (list2 != list and SumPN(list2, get_s()) != 0):
            for a in list:
                for b in list2:

                    if (a - b == sum(list) - get_s()):
                        V = []
                        V.append(a)
                        V.append(b)
                        V.sort()
                        if (IsInZ(Z, V) == False):
                            Z.append(V)
                            switch(list, list2, a, b)
                            return True

    return False


def h2(List, old_diff, S):
    D = []
    diff = 0


    for list in List:

        for a in list:
            for list2 in List:
                if (list2 != list):
                    for b in list2:

                        diff = getDiff(List)
                        diff -= (sum(list) - get_s()) ** 2
                        diff -= (sum(list2) - get_s()) ** 2
                        diff += (sum(list) - a + b - get_s()) ** 2
                        diff += (sum(list2) - b + a - get_s()) ** 2

                        y = [a, b, diff]

                        if (a != b and y not in S):

                            if (diff <= old_diff):
                                D.append([list, list2, a, b, diff])
                                old_diff = diff

                            if (diff == 0):
                                switch(list, list2, a, b)
                                return True



    if (len(D) == 0):
        return False

    min = D[len(D) - 1][4]

    C = D[len(D) - 1]
    if (C[4] == min):

        for list in List:
            if (list == C[0]):
                for list2 in List:
                    if (list2 == C[1]):
                        for a in list:
                            if (a == C[2]):
                                for b in list2:
                                    if (b == C[3]):
                                        S.append([a,b,min])
                                        switch(list, list2, a, b)
                                        break


    return h2(List, old_diff, S)


def K_Moves(List):
    K = k
    for list in List:
        for list2 in List:
            if (list != list2):
                i = random.randint(0, len(list) - 1)
                j = random.randint(0, len(list2) - 1)

                switch(list, list2, list[i], list2[j])
                K-=1

                if(K==0):
                    if getDiff(List)==0:
                        return True
                    return False
                if (getDiff(List) == 0):
                    return True




if(check_s(n, k) == -1):
    print("for (n,k) = ("+str(n)+","+str(k)+"), s(n,k) is",get_s())


else:
    Legal_Partitions=getPartitions(n,k)
    All_Partitons=allPartitons_1_to_n()
    f(All_Partitons)


