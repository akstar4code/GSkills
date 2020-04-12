import heapq
heap_queue = [5, 7, 9, 1, 3,2,8,0,14]
heapq.heapify(heap_queue)
print(heap_queue)
print(heapq.heappop(heap_queue))
heapq.heappush(heap_queue,6)
print(heap_queue)
print(heapq.heappushpop(heap_queue,2))
print(heapq.heapreplace(heap_queue,2))
print(heapq.nlargest(3,heap_queue))
print(heapq.nsmallest(3,heap_queue))