class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
       # Count the frequency of each task
        task_counts = Counter(tasks)
        
        # Use a max-heap to prioritize tasks with the highest frequency
        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)
        
        # Use a queue to manage tasks in cooldown
        cooldown_queue = deque()
        
        # Initialize the number of CPU cycles
        cycles = 0
        
        while max_heap or cooldown_queue:
            cycles += 1
            
            # If there are tasks in the max-heap, schedule the one with the highest frequency
            if max_heap:
                count = heapq.heappop(max_heap) + 1  # Reduce the count by 1
                if count < 0:
                    # If the task still has remaining occurrences, add it to the cooldown queue
                    cooldown_queue.append((count, cycles + n))
            
            # Check if any tasks in the cooldown queue are ready to be scheduled again
            if cooldown_queue and cooldown_queue[0][1] == cycles:
                heapq.heappush(max_heap, cooldown_queue.popleft()[0])
        
        return cycles 