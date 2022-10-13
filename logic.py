import sys
import xml.etree.ElementTree as et
from os import listdir #Python method listdir() returns a list containing the names of the entries in the directory given by path
from os.path import isfile, join #join - apvieno one or more path components isfile(Return True if path is an existing regular file.)
from openpyxl import Workbook
import matplotlib.pyplot as plt
import numpy as np
import pandas 
from termcolor import colored
from matplotlib.pyplot import annotate, figure
import seaborn as sb



def names_params(): #create link between human understandable vs config_file xml node.
    global hname, vname   #global make it usable outside function as global variable
    #hname  is column names understandable to human
    #vname - dictionary connecting (hyman name as key:node name as value)
    hname = ['offset X 1/1',
            'Gear ratio X 1',
            'offset Y 1/1',
            'Gear ratio Y 1',
            'offset Z 1/1',
            'Gear ratio Z 1',
            'Tool related to axis X 1/1',
            'Tool related to axis Y 1/1',
            'Tool related to axis Z 1/1',
            'Tool related to axis X 1/2',
            'Tool related to axis Y 1/2',
            'Tool related to axis Z 1/2',
            'offset X 2/1',
            'Gear ratio X 2',
            'offset Y 2/1',
            'Gear ratio Y 2',
            'offset Z 2/1',
            'Gear ratio Z 2',
            'Tool related to axis X 2/1',
            'Tool related to axis Y 2/1',
            'Tool related to axis Z 2/1',
            'Tool related to axis X 2/2',
            'Tool related to axis Y 2/2',
            'Tool related to axis Z 2/2',
            'offset X 3/1',
            'Gear ratio X 3',
            'offset Y 3/1',
            'Gear ratio Y 3',
            'offset Z 3/1',
            'Gear ratio Z 3',
            'Tool related to axis X 3/1',
            'Tool related to axis Y 3/1',
            'Tool related to axis Z 3/1',
            'Tool related to axis X 3/2',
            'Tool related to axis Y 3/2',
            'Tool related to axis Z 3/2']




    vname={ 'offset X 1/1' : 'Versaflow3xx.SELECTIV..gs_sttLm1_cSoll_VS.sttAchseX.sngNullpunktOffset',
            'Gear ratio X 1' :'Versaflow3xx.SELECTIV..gs_sttLm1_cSoll_VS.sttAchseX.sngUebersetzung',
            'offset Y 1/1' : 'Versaflow3xx.SELECTIV..gs_sttLm1_cSoll_VS.sttAchseY.sngNullpunktOffset',
            'Gear ratio Y 1' :'Versaflow3xx.SELECTIV..gs_sttLm1_cSoll_VS.sttAchseY.sngUebersetzung',
            'offset Z 1/1' :'Versaflow3xx.SELECTIV..gs_sttLm1_cSoll_VS.sttAchseZ.sngNullpunktOffset',
            'Gear ratio Z 1' :'Versaflow3xx.SELECTIV..gs_sttLm1_cSoll_VS.sttAchseZ.sngUebersetzung',
            'Tool related to axis X 1/1' :'Versaflow3xx.SELECTIV..gs_sttLm1_uSoll_VS.sttTi1.sngPositionX',
            'Tool related to axis Y 1/1' :'Versaflow3xx.SELECTIV..gs_sttLm1_uSoll_VS.sttTi1.sngPositionY',
            'Tool related to axis Z 1/1' :'Versaflow3xx.SELECTIV..gs_sttLm1_uSoll_VS.sttTi1.sngPositionZ',
            'Tool related to axis X 1/2' :'Versaflow3xx.SELECTIV..gs_sttLm1_uSoll_VS.sttTi2.sngPositionX',
            'Tool related to axis Y 1/2' :'Versaflow3xx.SELECTIV..gs_sttLm1_uSoll_VS.sttTi2.sngPositionY',
            'Tool related to axis Z 1/2' :'Versaflow3xx.SELECTIV..gs_sttLm1_uSoll_VS.sttTi2.sngPositionZ',
            'offset X 2/1' :'Versaflow3xx.SELECTIV..gs_sttLm2_cSoll_VS.sttAchseX.sngNullpunktOffset',
            'Gear ratio X 2' :'Versaflow3xx.SELECTIV..gs_sttLm2_cSoll_VS.sttAchseX.sngUebersetzung',
            'offset Y 2/1' :'Versaflow3xx.SELECTIV..gs_sttLm2_cSoll_VS.sttAchseY.sngNullpunktOffset',
            'Gear ratio Y 2' :'Versaflow3xx.SELECTIV..gs_sttLm2_cSoll_VS.sttAchseY.sngUebersetzung',
            'offset Z 2/1' :'Versaflow3xx.SELECTIV..gs_sttLm2_cSoll_VS.sttAchseZ.sngNullpunktOffset',
            'Gear ratio Z 2' :'Versaflow3xx.SELECTIV..gs_sttLm2_cSoll_VS.sttAchseZ.sngUebersetzung',
            'Tool related to axis X 2/1' :'Versaflow3xx.SELECTIV..gs_sttLm2_uSoll_VS.sttTi1.sngPositionX',
            'Tool related to axis Y 2/1' :'Versaflow3xx.SELECTIV..gs_sttLm2_uSoll_VS.sttTi1.sngPositionY',
            'Tool related to axis Z 2/1' :'Versaflow3xx.SELECTIV..gs_sttLm2_uSoll_VS.sttTi1.sngPositionZ',
            'Tool related to axis X 2/2' :'Versaflow3xx.SELECTIV..gs_sttLm2_uSoll_VS.sttTi2.sngPositionX',
            'Tool related to axis Y 2/2' :'Versaflow3xx.SELECTIV..gs_sttLm2_uSoll_VS.sttTi2.sngPositionY',
            'Tool related to axis Z 2/2' :'Versaflow3xx.SELECTIV..gs_sttLm2_uSoll_VS.sttTi2.sngPositionZ',
            'offset X 3/1' :'Versaflow3xx.SELECTIV..gs_sttLm3_cSoll_VS.sttAchseX.sngNullpunktOffset',
            'Gear ratio X 3' :'Versaflow3xx.SELECTIV..gs_sttLm3_cSoll_VS.sttAchseX.sngUebersetzung',
            'offset Y 3/1' :'Versaflow3xx.SELECTIV..gs_sttLm3_cSoll_VS.sttAchseY.sngNullpunktOffset',
            'Gear ratio Y 3' :'Versaflow3xx.SELECTIV..gs_sttLm3_cSoll_VS.sttAchseY.sngUebersetzung',
            'offset Z 3/1' :'Versaflow3xx.SELECTIV..gs_sttLm3_cSoll_VS.sttAchseZ.sngNullpunktOffset',
            'Gear ratio Z 3' :'Versaflow3xx.SELECTIV..gs_sttLm3_cSoll_VS.sttAchseZ.sngUebersetzung',
            'Tool related to axis X 3/1' :'Versaflow3xx.SELECTIV..gs_sttLm3_uSoll_VS.sttTi1.sngPositionX',
            'Tool related to axis Y 3/1' :'Versaflow3xx.SELECTIV..gs_sttLm3_uSoll_VS.sttTi1.sngPositionY',
            'Tool related to axis Z 3/1' :'Versaflow3xx.SELECTIV..gs_sttLm3_uSoll_VS.sttTi1.sngPositionZ',
            'Tool related to axis X 3/2' :'Versaflow3xx.SELECTIV..gs_sttLm3_uSoll_VS.sttTi2.sngPositionX',
            'Tool related to axis Y 3/2' :'Versaflow3xx.SELECTIV..gs_sttLm3_uSoll_VS.sttTi2.sngPositionY',
            'Tool related to axis Z 3/2' :'Versaflow3xx.SELECTIV..gs_sttLm3_uSoll_VS.sttTi2.sngPositionZ'}




def get_all_files(list_of_files, list_of_params): #retreeving required parameters for config check
    global data_list
    data_list = [[] for i in range(len(list_of_params))]
    ind = 0
    for f in list_of_files:
        tree = et.parse(f)
        root = tree.getroot()
        for i in range(len(root)):
            for n in list_of_params:
                if root[i].attrib['Name'] == vname[n]:
                    x = float(root[i].attrib['Wert'])
                    print("Human name: ", n, "\t", "Conf name: ", vname[n], "Value: ", x)
                    data_list[ind].append(x)
                    ind += 1
        ind = 0
    return(data_list)



def save_data_to_txt(list_of_params):
    with open('output.txt','w') as of:
        for i in range(len(list_of_params)):
            line = list_of_params[i] + ': \t' + str(data_list[i]) + '\n'
            of.write(line)




'''
def graphs_drawing(list_of_params):
    for i in range(len(data_list)):
        stand_dev = np.std(data_list[i])
        videjais = np.mean(data_list[i])               
        plus_viena_std = videjais + stand_dev
        plus_divas_std = 2 * stand_dev + videjais
        plus_tris_std = 3 * stand_dev + videjais
        minus_viena_std = videjais - stand_dev
        minus_divas_std = videjais - 2 * stand_dev
        minus_tris_std = videjais - 3 * stand_dev
        videjais_grafikam = [] 
        plus_viena = []
        minus_viena = []
        plus_divas = []
        minus_divas = []
        plus_tris = []
        minus_tris = []              
        for simb in range(len(data_list[0])): #vairojam konstantas values lai ievietot grafika
            videjais_grafikam.append(videjais)
            plus_viena.append(plus_viena_std)
            minus_viena.append(minus_viena_std)
            plus_divas.append(plus_divas_std)
            minus_divas.append(minus_divas_std)
            plus_tris.append(plus_tris_std)
            minus_tris.append(minus_tris_std)
            if minus_tris > data_list[i] and data_list[i] >plus_tris:
                print(i)
        #print(stand_dev)
        #print(videjais)
        #print(list_of_params)
        figure(figsize=(15,6), dpi =600)
        plt.plot(data_list[i], 'o-k')
        plt.plot(videjais_grafikam, '-.b')
        plt.plot(plus_viena, '--g')
        plt.plot(minus_viena, '--g')
        plt.plot(plus_divas, '--r')
        plt.plot(minus_divas, '--r')
        plt.plot(plus_tris, '-r')
        plt.plot(minus_tris, '-r')
        plt.ylabel("mm")
        plt.title(f' Graph: {list_of_params[i]}')
        #plt.legend()
        name_of_fig = 'output_figs/' + str(i) + '.png'
        plt.savefig(name_of_fig)
        plt.close()        
'''


def graphs_drawing(list_of_params):
    #aray1 = [75.6, 75.6, 75.7, 75.5, 75.9, 75.0, 76.1, 76.0, 78.5, 78.3, 78.9, 75.9, 75.8, 74.7, 74.6, 74.5, 74.4, 75.0, 74.2, 75.0, 75.0, 75.6, 75.8, 75.7, 75.6, 75.6, 75.9, 75.3, 75.9, 75.4, 76.0, 75.6, 76.2, 75.9, 75.6, 75.6, 75.8, 75.8, 75.8, 75.6, 75.9, 75.6, 75.3, 75.6, 75.3, 75.6, 75.8, 75.9, 75.9, 75.3, 75.8, 75.6, 75.6, 75.9, 75.9, 75.9, 75.8, 75.6, 75.9, 75.6, 75.6, 76.3, 75.6, 75.8, 75.7, 75.3, 75.8, 75.6, 75.6, 75.6, 75.8, 75.7, 75.6, 75.7, 76.2, 75.6, 75.8, 75.8, 75.8, 75.0, 76.0, 75.9, 75.9, 75.6, 75.6, 75.7, 75.9, 75.3, 75.3, 75.6, 75.9, 75.6, 75.6, 75.9, 75.6, 75.6, 75.8, 75.6, 75.6, 75.6, 75.9, 75.6, 75.6, 75.3, 75.3, 75.6, 75.6, 75.8, 75.6, 75.6, 75.8, 75.4, 75.9, 75.6, 75.3, 75.9, 75.9, 75.9, 75.3, 75.9, 76.5, 75.6, 74.0, 74.0, 76.5, 75.6, 75.8, 75.8, 75.6, 75.6, 76.0, 75.4, 76.2, 75.3, 75.6, 75.9, 75.6, 75.7, 75.7, 76.1, 75.7, 75.5, 75.5, 75.6, 75.7, 75.7, 75.6, 75.6, 75.6, 75.8, 75.8, 75.8, 75.8, 75.8, 75.8, 75.8, 75.8, 76.2]
    #print(aray1)
    aray1 = []
    for i in range(len(data_list)):
        aray1 = data_list[i]
        vid = np.mean(aray1)
        #vid = 75.55
        stan_div = np.std(aray1)
        print(vid)
        print(stan_div)
        #zone definition:
        zone_c_up_lim = vid + stan_div
        zone_c_down_lim = vid - stan_div
        zone_b_up_lim = zone_c_up_lim + stan_div
        zone_b_down_lim = zone_c_down_lim - stan_div
        zone_a_up_lim = zone_b_up_lim + stan_div
        zone_a_down_lim = zone_b_down_lim - stan_div


        #Rule NR1 - point outside the A/B/C zone
        rule1 = []
        place_marker = []
        aray1_iks = []
        videjais_grafikam = []
        plus_viena = []
        minus_viena = []
        plus_divas = []
        minus_divas = []
        plus_tris = []
        minus_tris = [] 
        labelius = [['Var change'],['Average'],['zone C'],['zone C'],['Zone B'],['Zone B'],['Zone A'],['Zone A'], ['Rule NR 1'],['Rule NR 2'],['Rule NR3']]
        checker = []
        point_checker_x = []
        temp_value = vid
        che = []
        po_checker_x = []
        p_checker_x = []
        ch = []
        checker_negative = []
        point_checker_x_negative = []

        pirmais_value = aray1[0]
        rule3_hujna = []
        rule3_hujna_down = []

        point_nr_3 = []
        point_nr_3_down = []

        rule_3 = []
        rule_3_point = []
        rule_3_final = []
        points_rule_3_final = []

        rule_5_up = []
        rule_5_down = []
        rule_5_pointer_up = []
        rule_5_pointer_down = []
        rule_5_final = []
        rule_5_pointer_final = []

        rule_6_up = []
        rule_6_down = []
        rule_6_pointer_up = []
        rule_6_pointer_down = []
        rule_6_final = []
        rule_6_pointer_final = []

        rule_7_up = []
        rule_7_down = []
        rule_7_pointer_up = []
        rule_7_pointer_down = []
        rule_7_final = []
        rule_7_pointer_final = []

        helper_array = []
        rule_4_val = []
        rule_4_point = []

        rule_8_val = []
        rule_8_point = []
        rule_8_val_fin = []
        rule_8_point_fin = []

        for var in range(len(aray1)):

            aray1_iks.append(var)
            videjais_grafikam.append(vid)
            plus_viena.append(zone_c_up_lim)
            minus_viena.append(zone_c_down_lim)
            plus_divas.append(zone_b_up_lim)
            minus_divas.append(zone_b_down_lim)
            plus_tris.append(zone_a_up_lim)
            minus_tris.append(zone_a_down_lim)
            #Rule NR1: 1 point beyond zone A or outside the 3sigma limits
            if aray1[var] > zone_a_up_lim or aray1[var] < zone_a_down_lim:
                rule1.append(aray1[var])
                place_marker.append(var)

            
            #Rule NR2: 9 points on the side of the center line, regardless of zone
            if aray1[var] > vid: 
                checker_negative.clear()
                point_checker_x_negative.clear()
                checker.append(aray1[var])
                point_checker_x.append(var)
                first_chek = point_checker_x[0]
                po_checker_x = []
                che = []

                for point in range(len(point_checker_x)):
                    if point_checker_x[point] == first_chek+1:
                        po_checker_x.append(point_checker_x[point])
                        che.append(checker[point])
                        first_chek = point_checker_x[point]
                    else:
                        po_checker_x.clear()
                        che.clear()
                        po_checker_x.append(point_checker_x[point])
                        che.append(checker[point])
                        first_check = point_checker_x[point]

                    if len(po_checker_x) >= 9:
                        p_checker_x.append(po_checker_x)
                        ch.append(che)
            
            else:
                checker.clear()
                point_checker_x.clear()
                checker_negative.append(aray1[var])
                point_checker_x_negative.append(var)

                first_chek = point_checker_x_negative[0]
                po_checker_x = []
                che = []
                p_checker_x_negative=[]
                ch_negative = []
                for point in range(len(point_checker_x_negative)):
                    if point_checker_x_negative[point] == first_chek+1:
                        po_checker_x.append(point_checker_x_negative[point])
                        che.append(checker_negative[point])
                        first_chek = point_checker_x_negative[point]
                    else:
                        po_checker_x.clear()
                        che.clear()
                        po_checker_x.append(point_checker_x_negative[point])
                        che.append(checker_negative[point])
                        first_check = point_checker_x_negative[point]
                    if len(po_checker_x) >= 9:
                        p_checker_x.append(po_checker_x)
                        ch.append(che)

            #Rule NR3: 6 points stedily increasing or decreasing
            
            if pirmais_value < aray1[var]:
                rule3_hujna_down.append(pirmais_value)
                point_nr_3_down.append(var-1)        
                rule3_hujna.append(pirmais_value)
                point_nr_3.append(var-1)
                pirmais_value = aray1[var]
                
                if len(point_nr_3_down) >= 6:
                    rule_3 = rule3_hujna_down.copy()
                    rule_3_point = point_nr_3_down.copy()

                rule3_hujna_down.clear()
                point_nr_3_down.clear()
                
            elif pirmais_value > aray1[var]:
                rule3_hujna.append(pirmais_value)
                point_nr_3.append(var-1)    
                rule3_hujna_down.append(pirmais_value)
                point_nr_3_down.append(var-1)
                pirmais_value = aray1[var]

                if len(point_nr_3) >= 6:
                    rule_3= rule3_hujna.copy()
                    rule_3_point = point_nr_3.copy()

                
                rule3_hujna.clear()
                point_nr_3.clear()

            
            else: 
                pirmais_value = aray1[var]
                rule3_hujna.clear()
                point_nr_3.clear()
                rule3_hujna_down.clear()
                point_nr_3_down.clear()
                


            #Rule NR4: 14 points alternating up and down every other time
            #Creating additional array that follow rule:
            #if value bigger than previous write in 1
            #if value smaller than previous write in -1
            #if value is the sam write in 2
            #ater check the summ inside if summ == 0 then we have a change, if we have 14 "0" in a row need to print dots to the grapg with rule 4 mark
            
            if aray1[var] > aray1[var - 1]:
                helper_array.append(1)
            elif aray1[var] < aray1[var - 1]:
                helper_array.append(-1)
            else:
                helper_array.append(2)
            
            rule_4_val_cop = []
            rule_4_point_cop = []
            for dot in range(len(helper_array)):
                if helper_array[dot] + helper_array[dot-1] == 0:
                    rule_4_val.append(aray1[dot])
                    rule_4_point.append(dot)
                    if len(rule_4_val) > 14:
                        rule_4_val_cop = rule_4_val.copy()
                        rule_4_point_cop = rule_4_point.copy()
                else:
                    rule_4_val.clear()
                    rule_4_point.clear()

            

            #Rule NR5: 2 or 3 points in the same zone A or beyond
            if aray1[var] > zone_b_up_lim:
                rule_5_down.clear()
                rule_5_pointer_down.clear()
                
                rule_5_up.append(aray1[var])
                rule_5_pointer_up.append(var)
                
                if len(rule_5_up) >= 2:
                    rule_5_final.append(rule_5_up.copy())
                    rule_5_pointer_final.append(rule_5_pointer_up.copy())


            
            elif aray1[var] < zone_b_down_lim:
                rule_5_up.clear()
                rule_5_pointer_up.clear()
                
                rule_5_down.append(aray1[var])
                rule_5_pointer_down.append(var)
                
                if len(rule_5_down) >= 2:
                    rule_5_final.append(rule_5_down.copy())
                    rule_5_pointer_final.append(rule_5_pointer_down.copy())
            else:
                rule_5_down.clear()
                rule_5_pointer_down.clear()
                rule_5_up.clear()
                rule_5_pointer_up.clear()


            #Rule NR6: 4 or 5 points in the same zone B or beyond

            if aray1[var] > zone_c_up_lim:
                rule_6_down.clear()
                rule_6_pointer_down.clear()
                
                rule_6_up.append(aray1[var])
                rule_6_pointer_up.append(var)
                
                if len(rule_6_up) >= 4:
                    
                    rule_6_final=rule_6_up.copy()
                    rule_6_pointer_final=rule_6_pointer_up.copy()
        
            
            elif aray1[var] < zone_c_down_lim:
                rule_6_up.clear()
                rule_6_pointer_up.clear()
                
                rule_6_down.append(aray1[var])
                rule_6_pointer_down.append(var)
                
                if len(rule_6_down) >= 4:
                    
                    rule_6_final=rule_6_down.copy()
                    rule_6_pointer_final=rule_6_pointer_down.copy()  
            else:
                rule_6_up.clear()
                rule_6_pointer_up.clear()                
                rule_6_down.clear()
                rule_6_pointer_down.clear()

            #Rule NR7: 15 points in either zone C with very tight distribution      

            if aray1[var] < zone_c_up_lim and aray1[var] > zone_c_down_lim:

                
                rule_7_up.append(aray1[var])
                rule_7_pointer_up.append(var)
                
                if len(rule_7_up) >= 15:
                    
                    rule_7_final.append(rule_7_up.copy())
                    rule_7_pointer_final.append(rule_7_pointer_up.copy())
            
            else:
                rule_7_up.clear()
                rule_7_pointer_up.clear()
            

            
            #Rule NR8: 8 points with none in zone C on both sides of the center line

            if (aray1[var] > zone_c_up_lim) ^ (aray1[var] < zone_c_down_lim):
                rule_8_val.append(aray1[var])
                rule_8_point.append(var)
                if len(rule_8_val) >= 8:
                    rule_8_val_fin = rule_8_val.copy()
                    rule_8_point_fin = rule_8_point.copy()
            else:
                rule_8_point.clear()
                rule_8_val.clear()
            #print(rule_8_val_fin)
                        
            #print()
            #print(colored("evolution of rule and points for graph", 'magenta'))
            
            #print(colored(rule_3, 'magenta'))
            #print(colored(rule_3_point, 'magenta'))   
            rule_3_final.append(rule_3)
            points_rule_3_final.append(rule_3_point)
            #print(colored(rule_3_final, 'magenta'))
            #print(colored(points_rule_3_final, 'magenta')) 
            
        #histogramm to check distribution
        num_bins = 70
        fig, ax = plt.subplots()
        n, bins, patches = ax.hist(aray1, num_bins, density=True)

        # add a 'best fit' line
        y = ((1 / (np.sqrt(2 * np.pi) * stan_div)) * np.exp(-0.5 * (1 / stan_div * (bins - np.mean(aray1)))**2))
        ax.plot(bins, y, '--')

        ax.set_xlabel('Values')
        ax.set_ylabel('Probability density')
        a= ('Histogram mean:', round(np.mean(aray1),4), 'sigma=' , round(stan_div,3))
        ax.set_title(a)


        fig.tight_layout()

        #print("Y=", y )
        #plt.plot(50,y, '--')
        #ax.bar_label( padding=3)
        #ax.set(xlim=(min(aray1), max(aray1)), xticks=np.arange(min(aray1), max(aray1)),
        #       ylim=(0, 20), yticks=np.linspace(0, max(aray1), 20))
        #ax.autoscale(enable=None, axis="y", tight=True)
        plt.show()

        plt.plot(aray1_iks, aray1, '-' , label = 'Var cahange')

        plt.plot(videjais_grafikam, '-.b' , label = 'Average')
        plt.plot(plus_viena, '--g' )
        plt.plot(minus_viena, '--g' )
        plt.plot(plus_divas, '--r'  )
        plt.plot(minus_divas, '--r' )
        plt.plot(plus_tris, '-r' )
        plt.plot(minus_tris, '-r' )

        #print(rule1)
        #print(place_marker)
        for rule_1_y in range(len(rule1)):
            plt.plot(place_marker[rule_1_y], rule1[rule_1_y], color='none', linestyle='none', marker = '.', markerfacecolor='blue', markersize=15)
            #offset for nr marker
            rule1[rule_1_y] = rule1[rule_1_y] - (stan_div/1.5)
            plt.plot(place_marker[rule_1_y], rule1[rule_1_y], color='none', linestyle='none', marker = '$1$', markerfacecolor='blue', markersize=7)




        for array_rule_3 in range (len(rule_3_final)):
            if len(rule_3_final[array_rule_3])>=6:    
                plt.plot(points_rule_3_final[array_rule_3], rule_3_final[array_rule_3],color='none', linestyle='none', marker = '.', markerfacecolor='green', markersize=15)
                rule_3_final[array_rule_3] = rule_3_final[array_rule_3] - (stan_div/2)
                plt.plot(points_rule_3_final[array_rule_3], rule_3_final[array_rule_3],color='none', linestyle='none', marker = '$3$', markerfacecolor='blue', markersize=7)

        plt.plot(rule_4_point_cop,rule_4_val_cop,color='none', linestyle='none', marker = '.', markerfacecolor='blue', markersize=15)
        rule_4_val_cop = rule_4_val_cop + (stan_div/2)
        plt.plot(rule_4_point_cop,rule_4_val_cop,color='none', linestyle='none', marker = '$4$', markerfacecolor='blue', markersize=7)

        for rule_5_y in range (len(rule_5_final)):
            plt.plot(rule_5_pointer_final[rule_5_y], rule_5_final[rule_5_y], color='none', linestyle='none', marker = '.', markerfacecolor='red', markersize=15) 
            #offset for nr marker
            rule_5_final[rule_5_y] = rule_5_final[rule_5_y] - (stan_div/3)
            plt.plot(rule_5_pointer_final[rule_5_y], rule_5_final[rule_5_y], color='none', linestyle='none', marker = '$5$', markerfacecolor='black', markersize=7)

        for rule_6_y in range (len(rule_6_final)):
            plt.plot(rule_6_pointer_final[rule_6_y], rule_6_final[rule_6_y], color='none', linestyle='none', marker = '.', markerfacecolor='blue', markersize=15) 
            #offset for nr marker
            rule_6_final[rule_6_y] = rule_6_final[rule_6_y] + (stan_div/3)
            plt.plot(rule_6_pointer_final[rule_6_y], rule_6_final[rule_6_y], color='none', linestyle='none', marker = '$6$', markerfacecolor='black', markersize=7)    
            
        for rule_7_y in range (len(rule_7_final)):
            plt.plot(rule_7_pointer_final[rule_7_y], (rule_7_final[rule_7_y]), color='none', linestyle='none', marker = '.', markerfacecolor='red', markersize=15)
            #offset for nr marker
            rule_7_final[rule_7_y] = rule_7_final[rule_7_y] + (stan_div/3)
            plt.plot(rule_7_pointer_final[rule_7_y], (rule_7_final[rule_7_y]), color='none', linestyle='none', marker = '$7$', markerfacecolor='black', markersize=7)
            
            #plt.annotate('7', xy=(rule_7_pointer_final[rule_7_y], rule_7_final[rule_7_y]))
        plt.plot(rule_8_point_fin,rule_8_val_fin, color='none', linestyle='none', marker = '.', markerfacecolor='yellow', markersize=15)
        rule_8_val_fin = rule_8_val_fin + (stan_div/2)
        plt.plot(rule_8_point_fin,rule_8_val_fin, color='none', linestyle='none', marker = '$8$', markerfacecolor='black', markersize=7)
        for array in range (len(ch)):
            #p_checker_x[array] = p_checker_x[array] - (stan_div/3)
            plt.plot(p_checker_x[array],ch[array], color='none', linestyle='none', marker = '$2$', markerfacecolor='blue', markersize=7)
        
        plt.title(f' Graph: {list_of_params[i]}')
        plt.show()







