'''
Algorithm : Generating  Minimum cost deployements among 100 random deployement
these generated deployments are used in the experiments 

Parameters:
   network size = 200,250,300,350,400
   No. of ONUs  = 6-10 for each network size   
   ONU deployment randomization : 100
   network area size: 200 x 200

'''
import numpy as np
import random
import os


#-----------------
#Golbal variables 
#---------------
#Stores x,y cordinates of users 
ux = []
uy = []
#Stores x,y cordinates of ONUs 
ox = []
oy = []

dist = [] # Stores distance to the nearest ONUs for given user
dep_cost_lst = [] # list of deployments
dep_node_lst = [] # All users in a deployment
cost_lst =[] # List of costs for different deployments
dep_onu_lst = []

#Read the network
def read_network(nw_file_name):
    ux.clear()
    uy.clear() 
    f = open(nw_file_name, "r")
    for l in f:
        row = l.split()
        ux.append(int(row[0]))
        uy.append(int(row[1]))

#Generate m ONUs
def gen_onu(m):
    ox.clear()
    oy.clear()
    ox.extend(random.sample(range(1, 200), m))
    oy.extend(random.sample(range(1, 200), m))


#Find the distance to the nearest ONU from x1,x2
def find_nearest_distTo_ONU(x1,x2):
    point1 = np.array((x1,x2))        
    #for the Euclidean distance from the given node to each ONU
    for o1,o2 in zip(ox,oy):
        point2 = np.array((o1,o2))
        dist.append(int(np.linalg.norm(point1 - point2)))
    return min(dist)


# Save min deployment details to files
def saveTo_file_sel_deployment(min_cost_pos,nw_file,m):
    file_name = (nw_file.split(".")[0])
    dirname = "../data" + "/" + file_name + "/" + str(m)

    if not os.path.exists(dirname):
        os.makedirs(dirname)

    f = open(dirname + "/min_dep_onu_assc_users.txt","w") #min deplyoment with users associated with each onu 
    sel_min_cost_dep_node = dep_node_lst[min_cost_pos]

    #Store users associated with each onu     
    for onu in sel_min_cost_dep_node:
        for i in sel_min_cost_dep_node[onu]:
            f.write(str(i) + " ")
        f.write("\n")
    f.close()


    #Store actual number of users associated with each onu
    f = open(dirname + "/min_dep_onu_assc_users.txt")
    onu_actual_users_cnt = [] 
    user_set = set()   
    for l in f:
        lst_usr = l.split()     
        if not onu_actual_users_cnt:
            onu_actual_users_cnt.append(len(lst_usr))
            user_set.update(lst_usr)
        else:
            temp_set = set(lst_usr).difference(user_set)
            onu_actual_users_cnt.append(len(temp_set))
            user_set.update(lst_usr)

    f = open(dirname + "/min_dep_onu_actl_users.txt", "w")
    for usr_cnt in onu_actual_users_cnt:
        f.write(str(usr_cnt) + " ")
    f.close()

    #Store ONU costs of the selected deployment in a file
    f = open(dirname + "/min_dep_onu_cost.txt","w")
    min_dep = dep_cost_lst[min_cost_pos]
    for onu in min_dep:
        f.write(str(sum(min_dep[onu])) + " ")
    f.close()


#start here
print("Generating data...")
nw_file_lst = ["network_size_200.txt","network_size_250.txt","network_size_300.txt","network_size_350.txt","network_size_400.txt"]
for nw_file in nw_file_lst:
    read_network(nw_file)
    for m in range(6,11):
        for r in range(0,50):
            gen_onu(m) #create random ONUs 
            onu_cost_lst = {} #ONUs with costs
            onu_node_lst = {} #ONUs with nodes/users
            nd_index = 0 #node index
            cost = 0 #deployment cost  
            for x1,x2 in zip(ux,uy):
                nd_index += 1
                dist.clear()
                min_dist_value = find_nearest_distTo_ONU(x1,x2)

                #Associate the node with all ONUs which are within distance of 50 meters from
                # the node
                dist_pos_lst = [i for i, d in enumerate(dist) if d - min_dist_value <= 50]
                dist_lst = [d for i, d in enumerate(dist) if d - min_dist_value <= 50]
                cost = cost +  sum(dist_lst)

                #Store this node index and distances for selected ONU 
                for i in dist_pos_lst:
                    if i in onu_cost_lst:
                        onu_cost_lst[i].append(dist[i])
                        onu_node_lst[i].append(nd_index)
                    else:
                        onu_cost_lst.update({i:[dist[i]]})
                        onu_node_lst.update({i:[nd_index]})
                
            #Store the deployement along with costs and  nodes
            dep_cost_lst.append(onu_cost_lst) # deployment with nodes
            dep_node_lst.append(onu_node_lst) # deployment with nodes 
            cost_lst.append(cost/m)  # Total cost of the deployment
   

        min_cost_pos = cost_lst.index(min(cost_lst))

        #Store all costs and nodes of min deployment in files 
        saveTo_file_sel_deployment(min_cost_pos,nw_file,m)
        dep_cost_lst.clear()
        dep_node_lst.clear()
        cost_lst.clear()

print("Data creation completed")




    



