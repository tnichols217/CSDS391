import csv
import kMeans
import plotter
import random

SEED = 42
DELTA = 0.02
K = range(2, 6)
DIMS = [2, 3]

data = []

with open("./irisdata.csv") as f:
    reader = csv.reader(f)
    rawData = [i for i in reader]
    data = [[float(j) for j in i[:-1]] for i in rawData[1:]]
    random.seed(SEED)
    data = random.sample(data, k=len(data))

models = [kMeans.kMeans(data, k=k) for k in K]
[m.iterate(DELTA) for m in models]
ps = [plotter.Plotter.plot(model.hist, DIMS[0], DIMS[1]) for model in models]

plotter.show()
