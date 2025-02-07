'''
Algorithm : MinCostAllUser

Given a random FiWi network deployment, this algorithm finds deployment with 
minimal cost such that all users in the original dpeloyment are included.

Parameters:
   network size = 200,250,300,350,400
   No. of ONUs  = 8
   ONU deployment randomization : 100
   network area size: 200 x 200

Input : n/w size and onu size
output : Min. deployment with all users

'''

from  SelectMinCostONU import SelectMinCostONU

#Read data from network file 
def build_node_cost_lst(nw_file_path):
    min_dep_onu_cost_lst = []
    min_dep_onu_node_lst = []

    #Read associated users in onu     
    with open(nw_file_path +"/min_dep_onu_assc_users.txt") as f:
        for line in f:
            node_lst = line.split()
            node_lst = list(map(int, node_lst))
            min_dep_onu_node_lst.append(node_lst)

    with open(nw_file_path +"/min_dep_onu_cost.txt") as f:
        for line in f:
            onu_cost = line.split()
            min_dep_onu_cost_lst = list(map(int, onu_cost))

    return min_dep_onu_node_lst, min_dep_onu_cost_lst
            

# Save results
def save_results(normlzd_onu_cost_lst, selected_ONU_pos, Pcost, m, nw_size):
        f = open("Result_table3.txt","a")

        f.write("Number of ONU in O=" + str(m) + "\n")
        f.write("Number of users in O =" + str(nw_size) + "\n")
        f.write("Cost of O = "+ str(sum(normlzd_onu_cost_lst))+ "\n")
        f.write("Cost of each ONU in O = "+ str(normlzd_onu_cost_lst)+ "\n")  

        f.write("Cost of P = "+ str(Pcost)+ "\n")
        f.write("Selected ONU for P = "+ str(selected_ONU_pos)+ "\n")
        f.write("Number of ONU in P = " + str(len(selected_ONU_pos))+ "\n")

        percntg_cost_decrease = (sum(normlzd_onu_cost_lst) - Pcost)/sum(normlzd_onu_cost_lst)*100 
        f.write("Percentage cost decrease =" + str(percntg_cost_decrease)+ "\n")    
        f.write("---------------------------------------------\n")
   
#Start here
def MinCostAllUser(nw_file, m):
        nw_file_path = "../data" + "/" + nw_file + "/" + str(m) 
        min_dep_onu_node_lst, min_dep_onu_cost_lst = build_node_cost_lst(nw_file_path)
        nw_size = nw_file[len(nw_file) - 3:]

        #Normalize the costs to fall within 100
        normlzd_onu_cost_lst = [int(float(i)/max(min_dep_onu_cost_lst)*100) for i in min_dep_onu_cost_lst] 

        # Create the deplployment  P
        # Note : SelectMinCostONU() uses the code provided by Zhiyang Su ( Copyright (C) 2014)
        # and distributed under GNU General Public License
        # the code has been modified as required by the implementation. 

        selected_ONU_pos, Pcost  = SelectMinCostONU(min_dep_onu_node_lst, normlzd_onu_cost_lst)        
        save_results(normlzd_onu_cost_lst, selected_ONU_pos, Pcost,m,nw_size)






# print("Nodes attached more than one ONU:")
# print([item for item, count in collections.Counter(all_nd_lst).items() if count > 1])







