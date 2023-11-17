print("PROGRAM KUADRAN TITIK \n")
#menentukan kuadran titik P(x,y) dibidang kartesian

#menginputkan nilai x dan y
Px = int(input("Masukkan titik P,x = "))
Py = int(input("Masukkan titik P,y = "))

if(Px > 0) and (Py > 0) :
    print("Kuadran I")
elif (Px < 0) and (Py > 0) :
    print("kuadran 2")
elif (Px < 0) and (Py < 0) :
    print("Kuadran 3")
elif (Px > 0) and (Py < 0) :
    print("Kuadran 4")
else :
    print("Tidak terletak di kuadran manapun")
