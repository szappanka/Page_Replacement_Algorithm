class Lap:
    def __init__(self, x = None, y = 0):
        self.szam = x   # a lap értéke, ami 1-99-ig tart
        self.zar = y    # tárba fagyasztás értéke

def LapToString(x):
    return ("Érték: " + str(x.szam) + ", fagyasztás: " + str(x.zar))

def csokken(A,B,C):
    if A.zar>0:
        A.zar=A.zar-1
    if B.zar>0:
        B.zar=B.zar-1
    if C.zar>0:
        C.zar=C.zar-1

def main():
    #beolvasás

    fifo = []
    memo = []
    osszes = []
    A = Lap()
    B = Lap()
    C = Lap()
    megoldas=[]

    for x in range(0, 1):
        try:
            memo = input()
            memo = memo.split(",")
            
        except EOFError:
            break

    for n in range(0,len(memo)):
        memo[n] = int(memo[n])

    # rendezés

    for m in range(0, len(memo)):
        csokken(A,B,C)
        if not fifo:  # 1. szám
            if memo[m]<0:
                A = Lap(abs(memo[m]))
            else:    
                A = Lap(memo[m],4)

            fifo.append("A")
            megoldas.append("A")
            
        elif len(fifo)==1: #2. szám
            if A.szam == memo[m]: # ha ugyanaz a szám jön be 2.nak
                megoldas.append("-")
            elif (-1)*A.szam == memo[m]: # ha dirty jelzéssel jön be ugyanaz
                A = Lap(abs(memo[m]))
                ind = fifo.index("A")
                del fifo[ind]
                fifo.append("A")
                megoldas.append("-")
            else: # ha nem ugyanaz a szám jön be
                if memo[m]<0:
                    B = Lap(abs(memo[m]))
                else:
                    B = Lap(abs(memo[m]),4)
                fifo.append("B")
                megoldas.append("B")
            

        elif len(fifo)==2: #3. szám
            if A.szam == memo[m] or B.szam == memo[m]:
                megoldas.append("-")
            elif (-1)*A.szam == memo[m]: # ha dirty jelzéssel jön be ugyanaz, mint A
                A = Lap(abs(memo[m]))
                ind = fifo.index("A")
                del fifo[ind]
                fifo.append("A")
                megoldas.append("-")
            elif (-1)*B.szam == memo[m]: # ha dirty jelzéssel jön be ugyanaz, mint B
                B = Lap(abs(memo[m]))
                ind = fifo.index("B")
                del fifo[ind]
                fifo.append("B")
                megoldas.append("-")
            else: # ha nem ugyanaz a szám jön be
                if memo[m]<0:
                    C = Lap(abs(memo[m]))
                else:
                    C = Lap(abs(memo[m]),4)
                fifo.append("C")
                megoldas.append("C")

        else: # tele a fifo :c
            #print(memo[m])
            if A.szam == memo[m] or B.szam == memo[m] or C.szam == memo[m]:
                megoldas.append("-")
                if A.szam == memo[m]:
                    ind = fifo.index("A")
                    del fifo[ind]
                    fifo.append("A")
                elif B.szam == memo[m]:
                    ind = fifo.index("B")
                    del fifo[ind]
                    fifo.append("B")
                elif C.szam == memo[m]:
                    ind = fifo.index("C")
                    del fifo[ind]
                    fifo.append("C")
            elif (-1)*A.szam == memo[m]: # ha dirty jelzéssel jön be ugyanaz, mint A
                A = Lap(abs(memo[m]))
                ind = fifo.index("A")
                del fifo[ind]
                fifo.append("A")
                megoldas.append("-")
            elif (-1)*B.szam == memo[m]: # ha dirty jelzéssel jön be ugyanaz, mint B
                B = Lap(abs(memo[m]))
                ind = fifo.index("B")
                del fifo[ind]
                fifo.append("B")
                megoldas.append("-")
            elif (-1)*C.szam == memo[m]: # ha dirty jelzéssel jön be ugyanaz, mint C
                C = Lap(abs(memo[m]))
                ind = fifo.index("C")
                del fifo[ind]
                fifo.append("C")
                megoldas.append("-")

            else: # új szám jön
                
                if A.zar > 0 and B.zar > 0 and C.zar > 0:
                    megoldas.append("*")
                    
                elif A.zar == 0 and B.zar > 0 and C.zar > 0:
                    if memo[m]<0:
                        A = Lap(abs(memo[m]))
                    else:    
                        A = Lap(memo[m],4)
                    ind = fifo.index("A")
                    del fifo[ind]
                    fifo.append("A")
                    megoldas.append("A")
                elif A.zar > 0 and B.zar == 0 and C.zar > 0:
                    if memo[m]<0:
                        B = Lap(abs(memo[m]))
                    else:    
                        B = Lap(memo[m],4)
                    ind = fifo.index("B")
                    del fifo[ind]
                    fifo.append("B")
                    megoldas.append("B")
                elif A.zar > 0 and B.zar > 0 and C.zar == 0:
                    if memo[m]<0:
                        C = Lap(abs(memo[m]))
                    else:    
                        C = Lap(memo[m],4)
                    ind = fifo.index("C")
                    del fifo[ind]
                    fifo.append("C")
                    megoldas.append("C")
                else: # több közül választhat és legalább 2be tud rakni
                    #megoldas.append("X")
                    for f in fifo:
                        if f == "A" and A.zar==0:
                            A = Lap(memo[m],4)
                            ind = fifo.index("A")
                            del fifo[ind]
                            fifo.append("A")
                            megoldas.append("A")
                            break
                        elif f == "B" and B.zar==0:
                            B = Lap(memo[m],4)
                            ind = fifo.index("B")
                            del fifo[ind]
                            fifo.append("B")
                            megoldas.append("B")
                            break
                        elif f == "C" and C.zar==0:
                            C = Lap(memo[m],4)
                            ind = fifo.index("C")
                            del fifo[ind]
                            fifo.append("C")
                            megoldas.append("C")
                            break
        
        X = Lap(A.szam, A.zar)
        Y = Lap(B.szam, B.zar)
        Z = Lap(C.szam, C.zar)
        o = [X, Y, Z]
        osszes.append(o)


    #for m in osszes:
    #    print(LapToString(m[0])+" "+LapToString(m[1])+" "+LapToString(m[2]))

    y=0

    for r in megoldas:
        if r != "-":
            y += 1

    print("".join(megoldas))
    print(y)
    
main()
