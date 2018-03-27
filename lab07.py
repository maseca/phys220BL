import numpy as np
import matplotlib.pyplot as plt

labNum = "07"

def main():
    data = {
        'R1' : {
            'a': 0.025,
            'b': -0.05,
            'x': [2, 2.8, 3.6, 4.2, 5, 5.8, 6.6, 7.2, 8, 8.8, 9, 9.6],
            'x2': [],
            'y_obs': [0.1, 0.15, 0.3, 0.4, 0.6, 0.85, 1.15, 1.4, 1.75, 2.1, 2.2, 2.6],
            'y_base': [],
            'y': [],
            'color': "blue",
            'num': "y vs x^2"
        },
    }

    for R in data.values():
        plot(R)


def plot(R):
    for n in range(len(R['y_obs'])):
        R['y_base'].append(R['a'] * R['x'][n] + R['b'])
        R['y'].append(R['y_obs'][n] - R['y_base'][n])
        R['x2'].append(R['x'][n]**2)

    x2 = R['x2']
    y = R['y']

    y1 = []
    fit = np.polyfit(x2, y, deg=1)

    for n in x2:
        y1.append(fit[0] * n + fit[1])

    fig, ax = plt.subplots()
    ax.scatter(x2, y, marker="o", linestyle="None", color="blue")
    ax.plot(x2, y1, color="blue")

    fig.suptitle('PHYS220B Lab '+labNum+' '+R['num'], fontsize=20)
    plt.xlabel('x^2 (cm^2)', fontsize=18)
    plt.ylabel('y (cm)', fontsize=16)
    plt.errorbar(x2, y, xerr=0.1**2, yerr=0.1, linestyle="None", color="blue")
    fig.savefig('lab'+labNum+'_'+R['num']+'.jpg')
    fig.show()

    print(R['y_base'])
    print(R['y'])
    print(fit[0])

    s = 5.6
    F = fit[0] * 4 * s
    print(F)

    rad = 6.8
    N = 320
    mu = 4 * np.pi * 10**-7
    V = [2, 2.5, 3, 3.5]
    B = []

    B.append(0.25 * 8 * mu * N / (rad * np.sqrt(125)))
    B.append(0.27 * 8 * mu * N / (rad * np.sqrt(125)))
    B.append(0.30 * 8 * mu * N / (rad * np.sqrt(125)))
    B.append(0.33 * 8 * mu * N / (rad * np.sqrt(125)))

    for n in range(len(V)):
        print(B[n])
        print(V[n] * F**2 / (2 * s**2 * B[n]**2))


if __name__ == '__main__': main()