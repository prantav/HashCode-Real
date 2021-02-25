import numpy as np

class Intersection_Info_Type:
  def __init__(self):
    self.Streets_in = []
    self.Streets_out = []

class Route_Info_Type:
  def __init__(self, Streets):
    self.Streets = Streets


def Read_input(file_name):
    Lines = open(file_name+".txt","r").readlines()
    
    # Common varibles
    [D_str, I_str, S_str, V_str, F_str] = Lines[0].split()
    D = int(D_str)
    I = int(I_str)
    S = int(S_str)
    V = int(V_str)
    F = int(F_str)
    
    Street_info = {}
    Intersection_info = []
    Route_Info = []
    
    
    for i in range(I):
        Intersection_info.append(Intersection_Info_Type())
    
    # Streets
    for i in range(1, S+1):
        [I_begin_str, I_end_str, Street_name, L_str] = Lines[i].split()
        Street_info[Street_name] = int(L_str)
        I_begin = int(I_begin_str)
        I_end = int(I_end_str)
        
        Intersection_info[I_begin].Streets_out.append(Street_name)
        Intersection_info[I_end].Streets_in.append(Street_name)
    
    
    # Vehicles
    for i in range(S+1, S+V+1):
       Route_Info.append(Route_Info_Type(Lines[i].split()[1:]))
    
    #for i in range(V):
    #   print (Route_Info[i].Streets)

    return Street_info, Intersection_info, Route_Info





def chooser(road_list_dict,car_list,inter_list):
    
    inter_road = {}
    for i in range(len(inter_list)):
        inter_road[i] = inter_list[i]
        
    
    road_list = road_list_dict.keys()
    road_dict = {}

    for road in road_list:
        road_dict[road] = 0

    for i in car_list:
        for road in i:
            road_dict[road] += 1
        

    output_dict = {}
        
        
    for intersection in inter_road.keys():
        intersection_dict = {}
        for road in inter_road[intersection]:
            intersection_dict[road] = round(road_dict[road]/10)*10+10
            
        intersection_dict_vals = []
        
        dict_vals_ratio = []
        
        for key in intersection_dict.keys():
            intersection_dict_vals.append(intersection_dict[key])
            
        gcf = np.gcd.reduce(intersection_dict_vals)
        
        gcf = float(gcf)
        
        for i in intersection_dict_vals:
            dict_vals_ratio.append(i/gcf)
        
        output_list = []
        
        for i in range(len(dict_vals_ratio)):
            output_list.append([inter_road[intersection][i],dict_vals_ratio[i]])
        
        output_dict[intersection] = output_list
        
    return output_dict
    
    
    
def output(output_dict,filename):
    f = open(filename+"submission.txt","w")
    f.write(str(len(output_dict.keys()))+"\n")
    
    for intersection in output_dict.keys():
        f.write(str(intersection)+"\n")
        f.write(str(len(output_dict[intersection]))+"\n")
        
        for i in output_dict[intersection]:
            f.write(str(i[0])+" "+str(int(i[1]))+"\n")
            


road_list_dict = {"r1":1,"r2":2,"r3":3}
car_list = []
inter_list = []

filename = "a"
    
road_list_dict,inter_list_class,car_list_class = Read_input(filename)

for item in inter_list_class:
  inter_list.append(item.Streets_in)

for item_car in car_list_class:
  car_list.append(item_car.Streets)

    
output_dict = chooser(road_list_dict,car_list,inter_list)
output(output_dict,"test")  
        
        
    
    
        
    

    
    
        
    
