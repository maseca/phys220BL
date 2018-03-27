import numpy as np
import matplotlib.pyplot as plt

labNum = "06"

def main():
    data = {
        'C1' : {
            'V': [10, 6.37, 3.68, 2.26, 1.33, 0.82, 0.5, 0.3, 0.18, 0.11],
            'color': "blue",
            'num': "C1"
        },
        'C2' : {
            'V': [10, 7.7, 5.73, 4.77, 3.68, 2.72, 2.23, 1.7, 1.33, 1.04, 0.81, 0.64, 0.5, 0.39, 0.3],
            'color': "red",
            'num': "C2"
        },
        'Cs' : {
            'V': [10, 8.47, 7.12, 6.08, 5.11, 4.3, 3.66, 3.06, 2.59, 2.18, 1.84, 1.56, 1.33, 1.12, 0.94],
            'color': "green",
            'num': "Cs"
        },
        'Cp' : {
            'V': [10, 4.74, 2.34, 1.12, 0.56, 0.26, 0.16],
            'color': "purple",
            'num': "Cp"
        }
    }

    plot(data, '')
    plot(data)

def plot(d, str='_Semi-Log'):
    fig, ax = plt.subplots()

    for C in d.values():
        x = range(0, len(C['V']))
        for i in x: i *= 10

        y = C['V']
        y1 = []

        fit = np.polyfit(x, y, deg=1)

        if str is not '':
            ax.set_yscale('log')
            ax.scatter(x, y, color=C['color'])
            ax.plot((x[0], x[-1]), (y[0], y[-1]), '-', color=C['color'])
            slope = (y[-1] - y[0])/(x[-1] - x[0])
            print('{}: {}, slope: {}'.format(C['num'], slope**-1 / -20e6, slope))
        else:
            for n in x:
                y1.append(fit[0] * n + fit[1])
            ax.scatter(x, y, color=C['color'])
            ax.plot(x, y, color=C['color'])


    plt.xlabel('Time (t)', fontsize=18)
    plt.ylabel('Voltage (V)', fontsize=16)

    fig.suptitle('PHYS220B Lab '+labNum+str, fontsize=20)
    fig.savefig('lab'+labNum+str+'.jpg')
    fig.show()

if __name__ == '__main__': main()