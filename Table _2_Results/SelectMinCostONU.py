#!/usr/bin/python

# Copyright (C) 2014 Zhiyang Su
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

import priorityqueue

MAXPRIORITY = 999999

def SelectMinCostONU(S, w):
    '''Selected ONU positions using Weighted set cover greedy algorithm:
  
    Input:
    udict - universe U, which contains the <elem, setlist>. (dict)
    S - a collection of sets. (list)
    w - corresponding weight to each set in S. (list)

    Output:
    selected: the selected set ids in order. (list)
    cost: the total cost of the selected sets.
    '''

    udict = {}
    selected = list()
    scopy = [] # During the process, S will be modified. Make a copy for S.
    for index, item in enumerate(S):
        scopy.append(set(item))
        for j in item:
            if j not in udict:
                udict[j] = set()
            udict[j].add(index)

    pq = priorityqueue.PriorityQueue()
    cost = 0
    coverednum = 0
    for index, item in enumerate(scopy): # add all sets to the priorityqueue
        if len(item) == 0:
            pq.addtask(index, MAXPRIORITY)
        else:
            pq.addtask(index, float(w[index]) / len(item))
    while coverednum < len(udict):
        a = pq.poptask() # get the most cost-effective set
        selected.append(a) # a: set id
        cost += w[a]
        coverednum += len(scopy[a])
        # Update the sets that contains the new covered elements
        for m in scopy[a]: # m: element
            for n in udict[m]:  # n: set id
                if n != a:
                    scopy[n].discard(m)
                    if len(scopy[n]) == 0:
                        pq.addtask(n, MAXPRIORITY)
                    else:
                        pq.addtask(n, float(w[n]) / len(scopy[n]))
        scopy[a].clear()
        pq.addtask(a, MAXPRIORITY)
                        
    return selected, cost


   

