import csv
import numpy as np
import kMeans

data = []

with open("./irisdata.csv") as f:
    reader = csv.reader(f)
    rawData = [i for i in reader]
    data = np.array([[float(j) for j in i[:-1]] for i in rawData[1:]])

model = kMeans.kMeans(data, k=2)
model.generateSubsets()
model.updateMeans()
print([i.shape for i in model.subsets])
print(model.getObjective())

for i in range(10):
    model.updateSubsets()
    model.updateMeans()
    print([i.shape for i in model.subsets])
    print(model.getObjective())
