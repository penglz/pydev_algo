from __future__ import division
from copy import deepcopy


def weight(pair): return pair[0]
def length(pair): return pair[1]

def differnce(item):
    return weight(item) - length(item)

def ratio(item):
    return weight(item) / length(item)
    
def compare_1(item1, item2):
    a = differnce(item2) - differnce(item1)
    if a == 0:
        return weight(item2) - weight(item1)
    else:
        return a

def compare_2(item1, item2):
    return cmp(ratio(item2),ratio(item1))
   
    
def sched(job_list, compare_method):
    sorted_job_list = deepcopy(job_list)
    return sorted(sorted_job_list, cmp=compare_method)

def weighted_completion_time(sorted_job_list):
    sum_time = 0
    time = 0
    for job in sorted_job_list:
        time = time + length(job)
        sum_time = sum_time + weight(job)*time
    return sum_time

def main():

    job_list = []

    with open('./jobs.txt', 'r') as f:
        lines = f.readlines()
        for line in lines[1:]:
            job_list.append(map(int, line.split()))
          
          
    print weighted_completion_time(sched(job_list, compare_1))
    print weighted_completion_time(sched(job_list, compare_2))
    
    #iarray = [1, 2, 3, 4, 5, 6, 7, 8]




if __name__ == "__main__":
    main()