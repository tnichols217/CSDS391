import math
import numpy as np

class kMeans:
    def __init__(self, data, k=2):
        self.k = k
        self.data = np.array(data)
        self.dimentions = self.data.shape[1]
        self.means = []

    def generateSubsets(self):
        self.samples = self.data.shape[0]
        self.subsets = [
            np.array(self.data[math.floor(i * self.samples/self.k):math.floor((i+1) * self.samples/self.k)])
            for i
            in range(self.k)
        ]

    def closestMean(self, point):
        distances = np.array([np.linalg.norm(np.array(point) - i) for i in self.means])
        o = distances.argmin()
        return (o, distances[o])
    
    def updateSubsets(self):
        means = np.array([self.closestMean(i)[0] for i in self.data])
        self.subsets = [
            self.data[means == i]
            for i
            in range(self.k)
        ]

    def updateMeans(self):
        self.means = [np.mean(i, axis=0) for i in self.subsets]

    def getObjective(self):
        return np.sum([self.closestMean(i)[1] ** 2 for i in self.data])
