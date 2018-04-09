import numpy as np
import matplotlib.pyplot as plt

def main():
    labNum = "09"
    num = "1/2*pi*f_exp vs tan(Phi_av)"
    x, y, y1 = [], [], []

    data = [
        {"fs": 1000, "deltaT": 1.25e-4, "T": 7.5e-4, "Vbc": 0.75, "Vac": 2},
        {"fs": 2000, "deltaT": 6.00e-5, "T": 4.6e-3, "Vbc": 1.10, "Vac": 2},
        {"fs": 3000, "deltaT": 3.10e-4, "T": 0.3e-4, "Vbc": 1.30, "Vac": 2},
        {"fs": 4000, "deltaT": 0.20e-4, "T": 2.4e-4, "Vbc": 1.50, "Vac": 2},
        {"fs": 5000, "deltaT": 0.10e-4, "T": 1.9e-4, "Vbc": 1.50, "Vac": 2}
    ]

    for datum in data:
        datum['f_exp'] = 1 / datum.get('T')
        datum['Phi1'] = np.arccos(datum.get('Vbc') / datum.get('Vac'))
        datum['Phi2'] = 2 * np.pi * datum.get('deltaT') / datum.get('T')
        datum['Phi_avg'] = (datum.get('Phi1') + datum.get('Phi2')) / 2
        datum['tan_Phi'] = np.tan(datum.get('Phi_avg'))

        x.append(datum.get('tan_Phi'))
        y.append(np.pi * datum.get('f_exp') / 2)

        """
        for k, v in datum.items():
            print(k, v)
            
        print()
        """

    fit = np.polyfit(x, y, deg=1)
    print(fit[0])

    for n in x:
        y1.append(fit[0] * n + fit[1])

    fig, ax = plt.subplots()
    ax.scatter(x, y, marker="o", linestyle="None", color="blue")
    ax.plot(x, y1, color="blue")

    fig.suptitle('PHYS220B Lab '+labNum+' '+num, fontsize=20)
    plt.xlabel('x (cm)', fontsize=18)
    plt.ylabel('e/m', fontsize=16)
    fig.savefig('lab'+labNum+'.jpg')
    fig.show()


if __name__ == '__main__': main()