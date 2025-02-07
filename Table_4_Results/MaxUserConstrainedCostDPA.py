'''
Algorithm : MaxUserConstrainedCostDPA

A dynamic programming based approach that finds minimum cost deployment O such 
that maximum no.of users are included in P for cost costraint cmax

Parameters:
   Network size = 200,250,300,350,400
   No. of ONUs  = 8
   cmax cost constraint : 75% of cost of O
   ONU deployment randomization : 100
   network area size: 200 x 200

Input : 
        Network size
        No. of ONU
        % of cost constraint for P (cmax value = 75% )

Output :
        Min deployment P with maximized no. of users for given cmax
'''

from  MaximizeUserDPA import MaximizeUserDPA

#Read data from network file 
def build_user_cost_lst(nw_file_path):
    min_dep_onu_cost_lst      = []
    onu_users_actl_count_lst  = []

    # Read cost of each onu
    with open(nw_file_path +"/min_dep_onu_cost.txt") as f:
        for line in f:
            onu_cost = line.split()
            min_dep_onu_cost_lst = list(map(int, onu_cost))

    #Read actual no. of users in each onu
    with open(nw_file_path +"/min_dep_onu_actl_users.txt") as f:
        for line in f:           
            onu_usr_cnt = line.split()
            onu_users_actl_count_lst = list(map(int, onu_usr_cnt))

    return onu_users_actl_count_lst, min_dep_onu_cost_lst
            

def save_results(no_of_users_P, sel_onu_P,cmax,cmax_val, onu_users_count_lst, normlzd_onu_cost_lst, m):
        f = open("Result_table4.txt","a")
        f.write("Number of ONU in O =" + str(m) + "\n")
        f.write("Number of users in O =" + str(sum(onu_users_count_lst)) + "\n") 
        f.write("Cost of O = "+ str(sum(normlzd_onu_cost_lst))+ "\n")
        f.write("Cost of each ONU in O= "+ str(normlzd_onu_cost_lst)+ "\n")
        f.write("Number of users in each onu in O =" + str(onu_users_count_lst) + "\n\n")       
        
        f.write("Cost constraint cmax for P = "+ str(cmax)+ "(" + str(cmax_val) + "% cost of O)\n")
        f.write("Selected ONU for P = "+ str(sel_onu_P)+ "\n")
        f.write("Number of users in P = "+ str(no_of_users_P)+ "\n")

        #cost of P
        cost_P = sum([normlzd_onu_cost_lst[i] for i in sel_onu_P]) 
        f.write("Cost of P = " + str(cost_P)+ "\n")

         # % user inclusion   
        percntg_incln =  (no_of_users_P * 100) / sum(onu_users_count_lst)
        f.write("Percentage user inclusion =" + str(percntg_incln)+ "\n")    
        f.write("---------------------------------------------\n")
   
#Start here
def MaxUserConstrainedCostDPA(nw_file,m,cmax_val):
        nw_file_path = "../data" + "/" + nw_file + "/" + str(m) 
        onu_users_actl_count_lst, min_dep_onu_cost_lst = build_user_cost_lst(nw_file_path)
        
        #Normalize the costs to fall within 100
        normlzd_onu_cost_lst = [int(float(i)/max(min_dep_onu_cost_lst)*100) for i in min_dep_onu_cost_lst]

        cmax = int(sum(normlzd_onu_cost_lst)*(cmax_val/100)) # Cost constraint

        #Create P with cmax constraint and  maximized users 
        no_of_users_P, sel_onu_P = MaximizeUserDPA(onu_users_actl_count_lst, normlzd_onu_cost_lst,int(cmax))
        save_results(no_of_users_P, sel_onu_P, cmax, cmax_val, onu_users_actl_count_lst, normlzd_onu_cost_lst, m)


# print("Nodes attached more than one ONU:")
# print([item for item, count in collections.Counter(all_nd_lst).items() if count > 1])







