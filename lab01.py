import numpy as np
import matplotlib.pyplot as plt
def main():
    V1 = (0.97, 1.855, 2.787, 3.743, 4.66, 5.570) #V
    i1 = (12.05, 23.06, 34.64, 46.1, 57.4, 68.5) #mA
    m1 = np.polyfit(i1, V1, 1)
    R1 = m1[0] * 1000

    V2 = (0.756, 0.873, 0.920, 0.946, 0.97)
    i2 = (46.5, 27.12, 19.04, 14.67, 12.05)
    L = (2, 4, 6, 8, 10)
    R = list(calcR(V2, i2)) #Ohm
    m2 = np.polyfit(R, L, 1)

    fig = plt.figure()
    plt.plot(i1, V1, color="blue", linewidth=2.5, linestyle="-", marker=".", label="R' = {0:.2f}".format(R1))
    fig.suptitle('PHYS220B Lab 01', fontsize=20)
    plt.xlabel('Current (mA)', fontsize=18)
    plt.ylabel('Voltage (V)', fontsize=16)
    #fig.savefig('test.jpg')
    plt.legend()
    plt.show()

    fig = plt.figure()
    plt.plot(R, L, color="red", linewidth=2.5, linestyle="-", marker=".")
    fig.suptitle('PHYS220B Lab 01', fontsize=20)
    plt.xlabel('Resistance (\u03A9)', fontsize=18)
    plt.ylabel('Length (m)', fontsize=16)
    #fig.savefig('test.jpg')
    plt.legend()
    plt.show()


def calcR(V, i):
    for n in range(0, len(V)):
        yield V[n] / (i[n] / 1000)

if __name__ == '__main__': main()