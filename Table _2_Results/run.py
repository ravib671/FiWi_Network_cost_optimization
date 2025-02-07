'''
This pyhon code generates Table 2 results. 


Input : ONU size (6-10)
Output: Deployment with minimized cost and  100% user inclusion. 
'''

import MinCostAllUser
import os
from pathlib import Path

# Run this file to call MinCostAllUser algorithm
def main():

    my_file = Path("Result_table2.txt") #Table 2 result
    if my_file.is_file():
            os.remove(my_file) 

    # m : ONU size from 6-10
    for m in range(6,11):
        MinCostAllUser.MinCostAllUser(m)

    print("Result_table2 is genrated")

if __name__ == '__main__':
    main()
