"""
You are given a histogram consisting of rectangles of different heights. These heights are represented 
in an input list, such that [1, 3, 2, 5] corresponds to the following diagram:

      x
      x  
  x   x
  x x x
x x x x
Determine the area of the largest rectangle that can be formed only from the bars of the histogram. 
For the diagram above, for example, this would be six, representing the 2 x 3 area at the bottom right.
"""
def get_max_area(histogram) -> int:
    max_area = 0
    for i in range(len(histogram)):
        chunk_size = histogram[i]
        local_area = 0
        for k in range(i, len(histogram)):
            if histogram[k] >= chunk_size:
                local_area += chunk_size
        if local_area > max_area:
            max_area = local_area
    return max_area

print("Histogram Area:", get_max_area([1, 3, 2, 5]))