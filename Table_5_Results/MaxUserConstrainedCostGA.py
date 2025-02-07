'''
Algorithm : MaxUserConstrainedCostGA

This greedy algorithm maximizes the user inclusion in the deployment P for a given
deployment and its cost constraint cmax. It allows either full or a part of a ONU
to be included  in P thereby maximizing  user including compared to the dynamic approach  


Parameters:
   network size = 200,250,300,350,400
   No. of ONUs  = 8
   ONU deployment randomization : 100
   network area size: 200 x 200

Input :
        Network size
        No. of ONUs
        %of cost constraint(75% of cost of O)
Output:
        Deployment P whose cost is within cmax and that includes maximum user

'''

from  MaximizeUserGA import MaximizeUserGA

#Read data from network file 
def build_user_cost_lst(nw_file_path):
    min_dep_onu_cost_lst = []
    onu_users_actl_count_lst = []

    with open(nw_file_path +"/min_dep_onu_cost.txt") as f:
        for line in f:
            onu_cost = line.split()
            min_dep_onu_cost_lst = list(map(int, onu_cost))

    with open(nw_file_path +"/min_dep_onu_actl_users.txt") as f:
        for line in f:
            onu_usr_cnt = line.split()
            onu_users_actl_count_lst = list(map(int, onu_usr_cnt))


    return onu_users_actl_count_lst, min_dep_onu_cost_lst

def find_cost_usr_cnt_P(sel_onu_P,normlzd_onu_cost_lst):
    #cost of P
    indx = 0
    cost_P = 0
    no_of_onu_P = 0
    for i in sel_onu_P:
        if i != 0:
            cost_P +=  normlzd_onu_cost_lst[indx] * i 
            no_of_onu_P += 1      
        indx += 1

    return cost_P, no_of_onu_P

            

def save_results(no_of_users_P, sel_onu_P,cmax, cmax_val, onu_users_actl_count_lst, normlzd_onu_cost_lst, m):
        f = open("Result_table5.txt","a")
        f.write("Number of ONU in O =" + str(m) + "\n")
        f.write("Number of users in O =" + str(sum(onu_users_actl_count_lst)) + "\n") 
        f.write("Number of users in each onu in O =" + str(onu_users_actl_count_lst) + "\n")       
        f.write("Cost of O = "+ str(sum(normlzd_onu_cost_lst))+ "\n")
        f.write("Cost of each ONU in O= "+ str(normlzd_onu_cost_lst)+ "\n\n")

        f.write("Cost constraint cmax for P = "+ str(cmax)+ "(" + str(cmax_val) + "% of cost of O)\n")
        f.write("Selected ONU for P(0-not selected) = "+ str(sel_onu_P)+ "\n")
        f.write("Number of users in P = "+ str(round(no_of_users_P,0))+ "\n")

        #find cost of P and no. of onu in P
        cost_P,no_of_onu_P = find_cost_usr_cnt_P(sel_onu_P,normlzd_onu_cost_lst)

        f.write("Cost of P = " + str(int(cost_P)) + "\n")
        f.write("Number of onu in P = " + str(no_of_onu_P) + "\n")
        # % user inclusion   
        percntg_incln =  round((no_of_users_P * 100) / sum(onu_users_actl_count_lst),0)
        f.write("Percentage user inclusion =" + str(percntg_incln)+ "%\n")    
        f.write("---------------------------------------------\n")
   
#Start here
def MaxUserConstrainedCostGA(nw_file, m, cmax_val):
        nw_file_path = "../data" + "/" + nw_file + "/" + str(m) 
        onu_users_actl_count_lst, min_dep_onu_cost_lst = build_user_cost_lst(nw_file_path)

        
        #Normalize the costs to fall within 100
        normlzd_onu_cost_lst = [int(float(i)/max(min_dep_onu_cost_lst)*100) for i in min_dep_onu_cost_lst]
        cmax = int(sum(normlzd_onu_cost_lst)*(cmax_val/100)) # Cost contstraint

        #Create P with maximized users 
        no_of_users_P, sel_onu_P = MaximizeUserGA(onu_users_actl_count_lst, normlzd_onu_cost_lst,int(cmax))
        sel_onu_P = [round(i,2) for i in sel_onu_P]
        save_results(no_of_users_P, sel_onu_P,cmax, cmax_val, onu_users_actl_count_lst, normlzd_onu_cost_lst, m)


# print("Nodes attached more than one ONU:")
# print([item for item, count in collections.Counter(all_nd_lst).items() if count > 1])







