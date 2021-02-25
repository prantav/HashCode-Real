import numpy as np
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
car_list = [["r1","r2","r3"],["r2","r1"]]
inter_list = [["r2","r1"],["r3","r1"],["r2","r3"]]
    
     
    
output_dict = chooser(road_list_dict,car_list,inter_list)
output(output_dict,"test")  
        
        
    
    
        
    

    
    
        
    
