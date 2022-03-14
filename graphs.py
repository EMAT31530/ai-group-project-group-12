import csv
import pandas as pd
import matplotlib.pyplot as plt

def winratesovertimegraph(csv):
    data = pd.read_csv(csv)
    Alice = data['Alice'].values
    Bob = data['Bob'].values
    Charlie = data['Charlie'].values
    x = data['Iteration'].values
    newA = []
    newB = []
    newC = []
    for i in range(len(x)):
        newA.append(Alice[i] / x[i] *100)
        newB.append(Bob[i] / x[i] *100)
        newC.append(Charlie[i] / x[i] *100)
    plt.plot(x, newA, label = 'Alice')
    plt.plot(x, newB, label = 'Bob')
    plt.plot(x, newC, label = 'Charlie')
    plt.xlabel('Iteration')
    plt.ylabel('Percentage Winrate')
    plt.legend()
    plt.grid()
    plt.title('Winrates of 3 Random Agents')
    plt.savefig('RandomWinrates.png', bbox_inches= 'tight')
    plt.show()


winratesovertimegraph('randomwinrates.csv')