class Solution:
    def kthLargest(nums,k):
        import heapq
        heap=[]
        for i in range(len(nums)):
            heapq.heappush(heap,nums[i])
            while len(heap)>k:
                heapq.heappop(heap)
        return heap[0]