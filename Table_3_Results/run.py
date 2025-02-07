'''
This pyhon code generates Table 3 results. 


Input : Network size (200,250,300,350,400)
Output: Deployment with minimized cost and 100% user inclusion. 
'''

import MinCostAllUser
import os
from pathlib import Path

#Run this file to call MinCostAllUser
def main():

    my_file = Path("Result_table3.txt")
    if my_file.is_file():
            os.remove(my_file) 
    # m : ONU size
    m = 8
    nw_file_lst = ["network_size_200.txt","network_size_250.txt","network_size_300.txt","network_size_350.txt","network_size_400.txt"]

    for nw_file in nw_file_lst:
        nw_file = nw_file.split(".")[0]
        MinCostAllUser.MinCostAllUser(nw_file,m)

    print("Result_table3 is genrated")

if __name__ == '__main__':
    main()
