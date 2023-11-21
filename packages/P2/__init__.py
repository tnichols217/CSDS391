import csv
import kMeans
import plotter
import random
import numpy as np
import neural

SEED = 42
DELTA = 0.02
K = range(2, 4)
DIMS = [2, 3]
CLASSFILTER = [1, 2]

classes = []
data = []
rawData = []

with open("./irisdata.csv") as f:
    reader = csv.reader(f)
    rawData = [i for i in reader][1:]
    random.seed(SEED)
    rawData = np.array(random.sample(rawData, k=len(rawData)))

    data = np.array([[float(j) for k, j in enumerate(i) if k != len(i)-1] for i in rawData])
    classes = np.array([i[-1] for i in rawData])

models = [kMeans.kMeans(data, k=k) for k in K]
[m.iterate(DELTA) for m in models]
ps = [plotter.Plotter.plotKmeans(model.hist, DIMS[0], DIMS[1]) for model in models]


i = np.array([
    [
        5.1,
        3.5,
        5,
        1.5
    ],
    [
        5.1,
        3.5,
        6,
        2.5
    ]
])

w = np.array([
    [
        0,
        0,
        8.12,
        7.15
    ]
])

b = np.array([
    -50
])

# print(neural.Neural.calculateLayer(i, w, b, neural.Neural.Activations.sigmoid))
# print(neural.Neural.makeLinspace(w, b, [0,0,0,0], [0,5], [0,5]))

# plotter.Plotter.plotWB(data, classes, lambda mean, xlim, ylim: neural.Neural.makeLinspace([w], [b], mean, xlim, ylim))

filteredClasses = np.array([np.unique(classes)[i] for i in CLASSFILTER])
filter = np.array([i in filteredClasses for i in classes])
filteredData = data[filter]
filteredRawData = rawData[filter]
filteredClassData = classes[filter]

# print(len(filteredData))

LT = plotter.Plotter.plotLinearTune(filteredData, filteredClassData, neural.Neural.makeLinspace, w, b, x=DIMS[0], y=DIMS[1])

result = neural.Neural.calculateOutput(filteredData, [w], [b], neural.Neural.Activations.sigmoid) > 0.5
# print(result)
result = np.where(result > 0.5, "virginica", "versicolor")
merged = np.array([[*i, *j] for i, j in zip(filteredRawData, result)])

print(merged)

print(np.sum(filteredRawData.transpose()[4]==result.transpose()))
print(len(result))


plotter.Plotter.show()
