import random
import pandas
import sys

thetha = 0.5

def learning():
    #STEP1:ASSIGNING WEIGHTS Randomly
    weight1 = round(random.uniform(-0.5, 0.5), 2)
    weight2 = round(random.uniform(-0.5, 0.5), 2)
    print(weight1)
    print(weight2)
    
    alpha = 0.1
    flage = True     # flage will be false when convergence reaches
    output = 1
    test = pandas.read_csv("learn.csv")
    inputData = test.values.tolist()
    while(flage == True):
        flage = False
        #Step2:Learning
        for data in inputData:
            value = (data[0]*weight1)+(data[1]*weight2)
            if(value >= thetha):  # if perceptoron excited
                output = 1
            else:
                output = 0
            if(output != data[2]):
                #step3:Updating weights
                weight1 = round(weight1+(alpha*(data[2]-output)*data[0]), 2)
                weight2 = round(weight2+(alpha*(data[2]-output)*data[1]), 2)
                print(weight1)
                print(weight2)
                flage = True
    weightsFile = open('weights.txt', 'w')
    weightsFile.write('{0}\n'.format(weight1))
    weightsFile.write('{0}\n'.format(weight2))

    weightsFile.close()

#Testing
def testing():
    test = pandas.read_csv("test.csv")
    listt = test.values.tolist()

    weights = []
    weightsFile = open('weights.txt', 'r')
    for w in weightsFile.readlines():
        weights.append(float(w))

    weight1 = weights[0]
    weight2 = weights[1]

    columns = ['x', 'y', 'actual', 'predicted']#list 
    out = pandas.DataFrame(columns=columns)
    for i in range(0, len(listt)):#copy test data in result data
        values = []
        for j in range(0, len(test.columns)):
            values.append(test.iloc[i, j])

        desired = weight1*listt[i][0] + weight2*listt[i][1]
        if desired < thetha:
            desired = 0
        else:
            desired = 1
        values.append(desired)#list of values 
        out.loc[len(out)] = values #data frame  

    out.to_csv("results.csv", index=False)


if __name__ == '__main__':
    if '--learning' in sys.argv:
        learning()
    if '--testing' in sys.argv:
        testing()
