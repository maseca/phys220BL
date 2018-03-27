import numpy as np
import matplotlib.pyplot as plt

labNum = "02"

def main():
    data = {
        'R1' : {
            'V': [0.814, 1.65, 3.28, 4.92, 5.68],
            'i': [31.7, 65.4, 127.6, 199.5, 238.7],
            'color': "blue",
            'num': "R1"
        },
        'R2' : {
            'V': [0.867, 1.677, 3.456, 5.15, 6],
            'i': [27.24, 52.3, 108, 160.8, 187.5],
            'color': "red",
            'num': "R2"
        },
        'Rs' : {
            'V': [0.913, 1.95, 3.68, 5.5, 6.41],
            'i': [16.22, 31.85, 65.1, 97.3, 113.7],
            'color': "green",
            'num': "Rs"
        },
        'Rp' : {
            'V': [0.701, 1.404, 2.865, 4.35, 5.01],
            'i': [50.7, 101.5, 207.5, 318.2, 367.5],
            'color': "purple",
            'num': "Rp"
        }
    }

    for R in data.values():
        plot(R)


def calcR(V, i):
    for n in range(0, len(V)):
        yield V[n] / (i[n] / 1000)

def plot(R):
    x = R['i']
    y = R['V']
    y1 = []
    fit = np.polyfit(x, y, deg=1)

    for n in x:
        y1.append(fit[0] * n + fit[1])

    fig, ax = plt.subplots()
    ax.scatter(x, y)
    ax.plot(x, y1, color='red')

    fig.suptitle('PHYS220B Lab '+labNum+' '+R['num'], fontsize=20)
    plt.xlabel('Current (mA)', fontsize=18)
    plt.ylabel('Voltage (V)', fontsize=16)
    fig.savefig('lab'+labNum+'_'+R['num']+'.jpg')
    fig.show()

    r = list(calcR(R['V'], R['i'])) #Ohm
    print("{}: {}".format(R['num'], np.mean(r)))
    print("Sigma {}: {}".format(R['num'], float(np.std(r))))

if __name__ == '__main__': main()