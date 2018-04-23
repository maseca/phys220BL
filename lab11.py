import matplotlib.pyplot as plt


def main():
    labNum = "09"
    HP = [
        {"f": 100, "Vin": 5.03, "Vout": 0.259},
        {"f": 200, "Vin": 5.02, "Vout": 0.370},
        {"f": 500, "Vin": 5.01, "Vout": 0.945},
        {"f": 1000, "Vin": 5.00, "Vout": 1.755},
        {"f": 5000, "Vin": 4.80, "Vout": 2.987},
        {"f": 10000, "Vin": 4.53, "Vout": 1.996}
    ]

    LP = [
        {"f": 100, "Vin": 5.06, "Vout": 4.67},
        {"f": 200, "Vin": 5.05, "Vout": 4.66},
        {"f": 500, "Vin": 5.05, "Vout": 4.63},
        {"f": 1000, "Vin": 5.04, "Vout": 4.53},
        {"f": 5000, "Vin": 4.97, "Vout": 2.76},
        {"f": 10000, "Vin": 4.73, "Vout": 1.02}
    ]

    BP = [
        {"f": 1000, "Vin": 5.03, "Vout": 2.26, "Vc": 4.93, "Vl": 0.65, "Vlc": 4.27},
        {"f": 1500, "Vin": 5.00, "Vout": 3.23, "Vc": 4.86, "Vl": 1.36, "Vlc": 3.48},
        {"f": 2000, "Vin": 4.97, "Vout": 3.68, "Vc": 4.76, "Vl": 1.80, "Vlc": 2.92},
        {"f": 2500, "Vin": 4.95, "Vout": 4.26, "Vc": 4.38, "Vl": 2.66, "Vlc": 1.72},
        {"f": 3000, "Vin": 4.91, "Vout": 4.51, "Vc": 3.80, "Vl": 3.54, "Vlc": 0.38},
        {"f": 3500, "Vin": 4.89, "Vout": 4.38, "Vc": 3.06, "Vl": 4.20, "Vlc": 1.05},
        {"f": 4000, "Vin": 4.89, "Vout": 4.11, "Vc": 2.53, "Vl": 4.50, "Vlc": 1.87},
        {"f": 4500, "Vin": 4.88, "Vout": 3.75, "Vc": 2.03, "Vl": 4.69, "Vlc": 2.54},
        {"f": 5000, "Vin": 4.87, "Vout": 3.36, "Vc": 1.63, "Vl": 4.79, "Vlc": 3.04},
    ]

    plot(HP, LP, BP, labNum, "RC (blue) & RL (red) & RLC (green)")
    plot2(BP, labNum, "V_L / V_R vs f")
    plot3(BP, labNum, "V_C / V_R vs 1 / f")


def plot(data1, data2, data3, labNum, num):
    x, y = [], []
    x2, y2 = [], []
    x3, y3 = [], []

    for datum in data1:
        x.append(datum.get('f'))
        y.append(datum.get('Vout') / datum.get('Vin'))

    fig, ax = plt.subplots()
    ax.plot(x, y, marker="o", color="blue")

    for datum in data2:
        x2.append(datum.get('f'))
        y2.append(datum.get('Vout') / datum.get('Vin'))

    ax.plot(x2, y2, marker="o", color="red")

    for datum in data3:
        x3.append(datum.get('f'))
        y3.append(datum.get('Vout') / datum.get('Vin'))

    ax.plot(x3, y3, marker="o", color="green")

    fig.suptitle('PHYS220B Lab '+labNum+' '+num, fontsize=20)
    fig.savefig('lab'+labNum+'01.jpg')
    fig.show()


def plot2(data, labNum, num):
    x, y = [], []

    for datum in data:
        x.append(datum.get('f'))
        y.append(datum.get('Vl') / datum.get('Vout'))

    fig, ax = plt.subplots()
    ax.plot(x, y, marker="o", color="blue")

    fig.suptitle('PHYS220B Lab '+labNum+' '+num, fontsize=20)
    fig.savefig('lab'+labNum+'02.jpg')
    fig.show()


def plot3(data, labNum, num):
    x, y = [], []

    for datum in data:
        x.append(1 / datum.get('f'))
        y.append(datum.get('Vc') / datum.get('Vout'))

    fig, ax = plt.subplots()
    ax.plot(x, y, marker="o", color="blue")

    fig.suptitle('PHYS220B Lab '+labNum+' '+num, fontsize=20)
    fig.savefig('lab'+labNum+'03.jpg')
    fig.show()


if __name__ == '__main__': main()