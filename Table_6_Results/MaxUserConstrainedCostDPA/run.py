'''
This pyhon code generates Table 6 results  


Input : Network size (200,250,300,350,400) and for each network cmax value = 60 - 100%
Output: Deployment with minimized cost and maximized user inclusion. 
'''

import MaxUserConstrainedCostDPA
import os
from pathlib import Path


def main():

    my_file = Path("Result_table6.txt")
    if my_file.is_file():
            os.remove(my_file) 
    # m : ONU size
    m = 8
    nw_file_lst = ["network_size_200.txt","network_size_250.txt","network_size_300.txt","network_size_350.txt","network_size_400.txt"]
    for nw_file in nw_file_lst:
        for cmax_val in range(60,101):
            nw_file = nw_file.split(".")[0]
            if MaxUserConstrainedCostDPA.MaxUserConstrainedCostDPA(nw_file,m,cmax_val) == True:
                    break

    print("Result_table6 is generated")

if __name__ == '__main__':
    main()
