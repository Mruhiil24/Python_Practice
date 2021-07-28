import queue
# inbuilt queue
q = queue.Queue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)

while not q.empty():
     print(q.get())

# inbuilt stack

q1=queue.LifoQueue()
q1.put(1)
q1.put(2)
q1.put(3)
q1.put(4)

while not q1.empty():
     print(q1.get())