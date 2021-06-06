import csv

maxFactor = float(input("max. crashpoint: "))
currentCrashPoint = 0
allChecked = 0
winFactor = 1


def testFactor(factorToTest):

    with open("crash_game_roobet.csv") as file:
        reader = csv.reader(file, delimiter= ";")

        underFactor = 0
        overFactor = 0
        allChecked = 0
        counter = 0

        for row in reader:
            if counter > 0:  
                if float(row[2]) >= factorToTest:
                    overFactor += 1
                else:
                    underFactor += 1
            counter += 1

        allChecked = overFactor + underFactor
        winFactor = (overFactor * factorToTest) / allChecked
        print(factorToTest, winFactor)


procedures = int((maxFactor - 1) * 10) + 1

for i in range(1, procedures):
    factor = 1 + (i / 10)
    testFactor(factor)