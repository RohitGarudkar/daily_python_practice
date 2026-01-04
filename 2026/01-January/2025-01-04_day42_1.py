#Problem: Task Scheduler (Greedy + Data Structures)

from heapq import *

tasks = [
    ("A", 4, 3),
    ("B", 3, 1),
    ("C", 5, 2),
    ("D", 6, 1),
    ("E", 7, 3),
]

# sort by deadline
tasks.sort(key=lambda x: x[1])

current_time = 0
max_heap = []  # store (-duration, task_name)

for name, deadline, duration in tasks:
    current_time += duration
    heappush(max_heap, (-duration, name))

    if current_time > deadline:
        longest = heappop(max_heap)
        current_time += longest[0]  # subtract duration

scheduled_tasks = [name for _, name in max_heap]

print("Tasks completed:", len(scheduled_tasks))
print("Scheduled tasks:", scheduled_tasks)


