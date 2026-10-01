class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        

    def addNum(self, num: int) -> None:
        #insert to the minheap
        if len(self.minHeap) <= len(self.maxHeap):
            if not self.minHeap or num >= self.maxHeap[0]: 
                heapq.heappush(self.minHeap,num)
            else:
                tmp = heapq.heappushpop_max(self.maxHeap,num)
                heapq.heappush(self.minHeap,tmp)
        else:
            #inset to max heap
            if num  <= self.minHeap[0]:
                heapq.heappush_max(self.maxHeap,num)
            else:
                tmp = heapq.heappushpop(self.minHeap,num) 
                heapq.heappush_max(self.maxHeap,tmp)

    def findMedian(self) -> float:
        #even
        if (len(self.minHeap) + len(self.maxHeap)) % 2 == 0:
            return (self.minHeap[0] + self.maxHeap[0]) / 2 
        else:
            return self.minHeap[0]
        