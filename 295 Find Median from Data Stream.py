import heapq


class MedianFinder(object):

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num):
        heapq.heappush(self.small, -1 * num)

        if (self.small and self.large and ((-1*self.small[0]) > self.large[0])):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.small) > (len(self.large)+1):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > (len(self.small)+1):
            val = -1 * heapq.heappop(self.large)
            heapq.heappush(self.small, val)


    def findMedian(self):
        if len(self.small) == len(self.large):
            val = ((-1 * self.small[0]) + self.large[0])/2
            return val

        elif len(self.small) > len(self.large):
            return self.small[0]

        elif len(self.large) > len(self.small):
            return self.large[0]


medfin = MedianFinder()
medfin.addNum(1)
medfin.addNum(2)
medfin.addNum(3)
print(medfin.findMedian())