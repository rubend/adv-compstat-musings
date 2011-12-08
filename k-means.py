#K-means clustering simple python implementation
#educational purposes
import random
from point import *

class Clusterer():
    'Clusterer class that implements the K-means clustering algorithm and helper functions'
    'Next step is implementing it as an EM algorithm'
    
    def cluster(self,means,points):
        'Given an initial set of k means, we alternate between 2 steps.'
        'the classification of the points is given by a map of: keys the points number'
        'and values the cluster number.'
        'k = the number of clusters = len(means)'
        'points = the data points we have'
        'means = the k starting means'
        
        k = len(means)
        print k
        old = means
        classification = self.assignmentStep(means,points)
        means = self.updateStep(classification,points,k)
        stepsdone = 0
        while self.significantDiff(old,means):
            old = means
            classification = self.assignmentStep(means,points)
            means = self.updateStep(classification,points,k)
            stepsdone += 1
            
        print "Stepsdone = " + str(stepsdone)

        return classification
    
    def significantDiff(self,old,new):
        'tests if any elements of old are significantly different'
        'numerically from the corresponding in new'
        for i in range(len(old)):
            if new[i].distanceTo(old[i]) > 0:
                return True
        return False
    
    def assignmentStep(self,means,points):
        'assignment step of the K-means algorithm'
        classification = [0]*len(points)
        for p in points:
            min = p.distanceTo(means[0])
            for m in means:
                if p.distanceTo(m) < min:
                    min = p.distanceTo(m)
                    classification[points.index(p)] = means.index(m)
        return classification

    def updateStep(self,classification,points,k):
        'update step: the new means are being calculated'
        means = self.zeros(k)
        clustersizes = [0]*k
        
        for p in points:
            cluster = classification[points.index(p)]
            clustersizes[cluster] += 1
            means[cluster].x += p.x
            means[cluster].y += p.y

        for c in range(k):
            if clustersizes[c] > 0:
                means[c].x /= float(clustersizes[c])
                means[c].y /= float(clustersizes[c])
            
        return means

    def genPoints(self,k,max,seed):
        'Generates k random points in a list'
        points = []
        random.seed(seed);
        for i in range(k):
            tmp = Point(max*random.random(),max*random.random())
            points.append(tmp)
        return points
    
    def zeros (self,k):
        'Generates k points 0,0'
        points = []
        for i in range(k):
            points.append(Point(0,0))
        return points
    
    def w_cDistances(self,classification,points,k):
        'Within cluster distances, a quality measure for the clustering.'
        'It\'s what we want to optimize.'
        'You automatically optimize the betwen cluster differences see theory.'
        #clusterList is needed, otherwise would make sense to work with it all
        #the way through the algorithm. Think about it.
        clusterList = self.createListOfClusters(classification,points,k)
        w_c = 0
        for c in clusterList:
            for p in range(len(c)):
                for p2 in range(len(c)):
                    if p != p2:
                        w_c += points[p].distanceTo(points[p2])
        return w_c
    
    def createListOfClusters(self,classification,points,k):
        'creates a list of lists that contain all the points'
        'belonging to one particular cluster.'
        list = []*k
        for i in range(k):
            list.append([])
        for p in range(len(points)):
            c = classification[p]
            list[c].append(points[p])
        return list

        
d = Clusterer()
k = [3,5,10,20]
k = 5
n = 1000
#not working perfectly yet
def runsimul(k):
    wc=[]
    mean=[]
    for n in range(5):
        means=d.genPoints(k,50,random.random())
        mean.append(mean)
        points = d.genPoints(n,50,random.random())
        classif = d.cluster(means,points)
        wc.append(d.w_cDistances(classif,points,k))
    return mean[wc.index(min(wc))]

print runsimul(10)

