import heapq

def solution(scoville, K):
    answer = 0
    heap = [];
    for i in scoville :
        heapq.heappush(heap, i)

    while heap[0] < K :
        if len(heap) < 2 :
            return -1;
        h1 = heapq.heappop(heap);
        h2 = heapq.heappop(heap);
        mix = h1 + (h2 * 2);
        heapq.heappush(heap, mix);
        answer+=1;
        
    
    return answer