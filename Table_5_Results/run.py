'''
This pyhon code generates Table 5 results (Greedy Approach). 


Input : Network size (200,250,300,350,400) and cost constraint cmax = 75% of the original cost
Output: Deployment with minimized cost and maximized user inclusion. 
'''
import MaxUserConstrainedCostGA
import os
from pathlib import Path

def main():

    my_file = Path("Result_table5.txt")
    if my_file.is_file():
            os.remove(my_file) 
    # m : ONU size
    m = 8
    nw_file_lst = ["network_size_200.txt","network_size_250.txt","network_size_300.txt","network_size_350.txt","network_size_400.txt"]
    cmax_val = 75
    for nw_file in nw_file_lst:
        nw_file = nw_file.split(".")[0]
        MaxUserConstrainedCostGA.MaxUserConstrainedCostGA(nw_file,m,cmax_val)

    print("Result_table5 is generated")

if __name__ == '__main__':
    main()
