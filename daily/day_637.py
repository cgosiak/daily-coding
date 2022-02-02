"""
Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].
"""

def merge_intervals(intervals):
    merged_intervals = []
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    lower_bound = sorted_intervals[0][0]
    upper_bound = sorted_intervals[0][1]
    for i in range(1, len(sorted_intervals)):
        local_lower_bound = sorted_intervals[i][0]
        local_upper_bound = sorted_intervals[i][1]
        if local_upper_bound > upper_bound:
            merged_intervals.append((lower_bound, upper_bound))
            lower_bound = local_lower_bound
            upper_bound = local_upper_bound
    merged_intervals.append((lower_bound, upper_bound))    
    return merged_intervals

print("Merged Intervals:", merge_intervals([(1, 3), (5, 8), (4, 10), (20, 25)]))