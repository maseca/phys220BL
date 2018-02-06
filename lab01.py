import numpy as np
import matplotlib.pyplot as plt

def main():
    V1 = (0.97, 1.855, 2.787, 3.743, 4.66, 5.570) #V
    i1 = (12.05, 23.06, 34.64, 46.1, 57.4, 68.5) #mA
    R1 = list(calcR(V1, i1))

    V2 = (0.756, 0.873, 0.920, 0.946, 0.97)
    i2 = (46.5, 27.12, 19.04, 14.67, 12.05)
    L = (2, 4, 6, 8, 10)
    R2 = list(calcR(V2, i2)) #Ohm
    print("R: {}".format(np.mean(R1)))
    print("Sigma R: {}".format(float(np.std(R1))))

    A = list(calcA(V2, i2, L, 1.45 * 10 ** 6))
    D = list(calcD(A))

    print("A: {}".format(np.mean(A)))
    print("Sigma A: {}".format(np.std(A)))
    print("D: {}".format(np.mean(D)))
    print("Sigma D: {}".format(np.std(D)))

    fig = plt.figure()
    plt.plot(i1, V1, color="blue", linewidth=2.5, linestyle="-", marker=".")
    fig.suptitle('PHYS220B Lab 01', fontsize=20)
    plt.xlabel('Current (mA)', fontsize=18)
    plt.ylabel('Voltage (V)', fontsize=16)
    fig.savefig('lab01_01.jpg')
    plt.show()

    fig = plt.figure()
    plt.plot(R2, L, color="red", linewidth=2.5, linestyle="-", marker=".")
    fig.suptitle('PHYS220B Lab 01', fontsize=20)
    plt.xlabel('Resistance (\u03A9)', fontsize=18)
    plt.ylabel('Length (m)', fontsize=16)
    fig.savefig('lab01_02.jpg')
    plt.show()


def calcR(V, i):
    for n in range(0, len(V)):
        yield V[n] / (i[n] / 1000)


def calcA(V, i, L, sig):
    for n in range(0, len(V)):
        yield (i[n] / 1000) * L[n] / (sig * V[n])

def calcD(A):
    for n in range(0, len(A)):
        yield 2 * np.sqrt(A[n] / np.pi)

if __name__ == '__main__': main()