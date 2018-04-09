import numpy as np
import matplotlib.pyplot as plt

R = 6.8
mu = 4 * np.pi * 10**-7
x = [4, 6, 8, 10]
y = [1.23e17, 6.36e16, 5.9e16, 7.45e16]

def main():
    labNum = "08"
    num = "e/m vs x"
    a = 0.025
    b = -0.05

    y1 = []
    fit = np.polyfit(x, y, deg=1)

    for n in x:
        y1.append(fit[0] * n + fit[1])

    fig, ax = plt.subplots()
    ax.scatter(x, y, marker="o", linestyle="None", color="blue")
    ax.plot(x, y1, color="blue")

    fig.suptitle('PHYS220B Lab '+labNum+' '+num, fontsize=20)
    plt.xlabel('x (cm)', fontsize=18)
    plt.ylabel('e/m', fontsize=16)
    fig.savefig('lab08.jpg')
    fig.show()


def B(I, x):
    return mu * I * R**2 / (2 * (R**2 + x**2)**(3/2))

def em(V, B, r):
    return 2 * V / (B**2 * r**2)

def rad(x, y):
    return x**2 + y**2 / (2 * np.abs(y))

if __name__ == '__main__': main()