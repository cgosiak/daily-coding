from queue import PriorityQueue

backpack: PriorityQueue = PriorityQueue()
backpack.put((5, "Knife"))
backpack.put((2, "Matches"))
backpack.put((4, "Tent"))
backpack.put((1, "Playing Cards"))

while backpack.qsize() > 0:
    print(backpack.get())