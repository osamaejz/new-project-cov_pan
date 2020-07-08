from DASS_calculation import survey_data, DASS_score
import numpy as np
######################## for awareness varaibles ############################
      
################## Social Awareness with symptom and transmission #############       
awareness = []
awareness = survey_data['Awareness']
per_75,per_100,per_50,per_25,per_0 = survey_data['Awareness'].value_counts()

per_75_DASS_score = np.zeros((per_75,6),dtype = np.double)
per_100_DASS_score = np.zeros((per_100,6),dtype = np.double)
per_50_DASS_score = np.zeros((per_50,6),dtype = np.double)
per_25_DASS_score = np.zeros((per_25,6),dtype = np.double)
per_0_DASS_score = np.zeros((per_0,6),dtype = np.double)

val_0 = 0
val_25 = 0
val_50 = 0
val_75 = 0
val_100 = 0

for aware_value in range (len(survey_data)):
    if awareness[aware_value] == '75%':
        for i in range(6):   
            per_75_DASS_score[val_75][i] = DASS_score[aware_value][i]
        val_75 += 1
    elif awareness[aware_value] == '100%':
        for j in range(6):       
            per_100_DASS_score[val_100][j] = DASS_score[aware_value][j]
        val_100 += 1
    elif awareness[aware_value] == '50%':
        for j in range(6):       
            per_50_DASS_score[val_50][j] = DASS_score[aware_value][j]
        val_50 += 1
    elif awareness[aware_value] == '25%':
        for j in range(6):       
            per_25_DASS_score[val_25][j] = DASS_score[aware_value][j]
        val_25 += 1
    elif awareness[aware_value] == 'unaware':
        for j in range(6):       
            per_0_DASS_score[val_0][j] = DASS_score[aware_value][j]
        val_0 += 1


########################### awareness anxiety count ###########

awareness_anxiety_count = np.zeros((10,5),dtype = np.double)


for l in range (2):
    normal_0 = 0
    mild_0 = 0
    moderate_0 = 0
    severe_0 = 0
    extreme_0 = 0
    
    normal_25 = 0
    mild_25 = 0
    moderate_25 = 0
    severe_25 = 0
    extreme_25 = 0
    
    normal_50 = 0
    mild_50 = 0
    moderate_50 = 0
    severe_50 = 0
    extreme_50 = 0
    
    normal_75 = 0
    mild_75 = 0
    moderate_75 = 0
    severe_75 = 0
    extreme_75 = 0
    
    normal_100 = 0
    mild_100 = 0
    moderate_100 = 0
    severe_100 = 0
    extreme_100 = 0
    
    
    for c in range(len(per_0_DASS_score)):
       
        ############## for unware anxiety ############# 

        if (per_0_DASS_score[c][l+2]>=0 and per_0_DASS_score[c][l+2]<8):
            normal_0 += 1
            
        elif (per_0_DASS_score[c][l+2]>=8 and per_0_DASS_score[c][l+2]<10):
            mild_0 += 1
            
        elif (per_0_DASS_score[c][l+2]>=10 and per_0_DASS_score[c][l+2]<15):
            moderate_0 += 1
            
        elif (per_0_DASS_score[c][l+2]>=15 and per_0_DASS_score[c][l+2]<20):
            severe_0 += 1
            
        else:
            extreme_0 += 1
        
        ############## for 25% anxiety ############# 
    for ys in range(len(per_25_DASS_score)):
    
        if (per_25_DASS_score[ys][l+2]>=0 and per_25_DASS_score[ys][l+2]<8):
            normal_25 += 1
            
        elif (per_25_DASS_score[ys][l+2]>=8 and per_25_DASS_score[ys][l+2]<10):
            mild_25 += 1
            
        elif (per_25_DASS_score[ys][l+2]>=10 and per_25_DASS_score[ys][l+2]<15):
            moderate_25 += 1
            
        elif (per_25_DASS_score[ys][l+2]>=15 and per_25_DASS_score[ys][l+2]<20):
            severe_25 += 1
            
        else:
            extreme_25 += 1
            
        ############## for 50% anxiety ############# 
    for y in range(len(per_50_DASS_score)):

        if (per_50_DASS_score[y][l+2]>=0 and per_50_DASS_score[y][l+2]<8):
            normal_50 += 1
            
        elif (per_50_DASS_score[y][l+2]>=8 and per_50_DASS_score[y][l+2]<10):
            mild_50 += 1
            
        elif (per_50_DASS_score[y][l+2]>=10 and per_50_DASS_score[y][l+2]<15):
            moderate_50 += 1
            
        elif (per_50_DASS_score[y][l+2]>=15 and per_50_DASS_score[y][l+2]<20):
            severe_50 += 1
            
        else:
            extreme_50 += 1
            
        ############## for 75% anxiety ############# 
    for ea in range(len(per_75_DASS_score)):

        if (per_75_DASS_score[ea][l+2]>=0 and per_75_DASS_score[ea][l+2]<8):
            normal_75 += 1
            
        elif (per_75_DASS_score[ea][l+2]>=8 and per_75_DASS_score[ea][l+2]<10):
            mild_75 += 1
            
        elif (per_75_DASS_score[ea][l+2]>=10 and per_75_DASS_score[ea][l+2]<15):
            moderate_75 += 1
            
        elif (per_75_DASS_score[ea][l+2]>=15 and per_75_DASS_score[ea][l+2]<20):
            severe_75 += 1
            
        else:
            extreme_75 += 1
            
        ############## for 100% anxiety ############# 
    for ma in range(len(per_100_DASS_score)):

        if (per_100_DASS_score[ma][l+2]>=0 and per_100_DASS_score[ma][l+2]<8):
            normal_100 += 1
            
        elif (per_100_DASS_score[ma][l+2]>=8 and per_100_DASS_score[ma][l+2]<10):
            mild_100 += 1
            
        elif (per_100_DASS_score[ma][l+2]>=10 and per_100_DASS_score[ma][l+2]<15):
            moderate_100 += 1
            
        elif (per_100_DASS_score[ma][l+2]>=15 and per_100_DASS_score[ma][l+2]<20):
            severe_100 += 1
            
        else:
            extreme_100 += 1
            
      
            
    temp_0 = [[normal_0, mild_0, moderate_0, severe_0, extreme_0],
            [normal_25, mild_25, moderate_25, severe_25, extreme_25],
            [normal_50, mild_50, moderate_50, severe_50, extreme_50],
            [normal_75, mild_75, moderate_75, severe_75, extreme_75],
            [normal_100, mild_100, moderate_100, severe_100, extreme_100]]        
            
    awareness_anxiety_count[l] = temp_0[0]  
    awareness_anxiety_count[l+2] = temp_0[1]  
    awareness_anxiety_count[l+4] = temp_0[2]     
    awareness_anxiety_count[l+6] = temp_0[3]        
    awareness_anxiety_count[l+8] = temp_0[4]        
     

################ Es filtration for awareness #######################


awareness_anxiety_count_es_filter = np.copy(awareness_anxiety_count)


for row in range (0,10,2):
    
    awareness_anxiety_count_es_filter[row][4] = abs(awareness_anxiety_count_es_filter[row][4] - awareness_anxiety_count_es_filter[row][4])
    awareness_anxiety_count_es_filter[row+1][4] = abs(awareness_anxiety_count_es_filter[row+1][4] - awareness_anxiety_count[row][4])

#####################################################################

  
################## Social Awareness from Connection with friends and family #############       
fnf_conn = []
fnf_conn = survey_data['Connection with friends and family']
Lessthanbefore,Morethanbefore,Nearlythesame = survey_data['Connection with friends and family'].value_counts()

less_DASS_score = np.zeros((Lessthanbefore,6),dtype = np.double)
more_DASS_score = np.zeros((Morethanbefore,6),dtype = np.double)
same_DASS_score = np.zeros((Nearlythesame,6),dtype = np.double)


val_l = 0
val_m = 0
val_s = 0


for conn_val in range (len(survey_data)):
    if fnf_conn[conn_val] == 'Lessthanbefore':
        for i in range(6):   
            less_DASS_score[val_l][i] = DASS_score[conn_val][i]
        val_l += 1
    elif fnf_conn[conn_val] == 'Morethanbefore':
        for j in range(6):       
            more_DASS_score[val_m][j] = DASS_score[conn_val][j]
        val_m += 1
    elif fnf_conn[conn_val] == 'Nearlythesame':
        for j in range(6):       
            same_DASS_score[val_s][j] = DASS_score[conn_val][j]
        val_s += 1
   
########################### fnf connection anxiety count ###########

fnf_conn_anxiety_count = np.zeros((6,5),dtype = np.double)


for l in range (2):
    normal_l = 0
    mild_l = 0
    moderate_l = 0
    severe_l = 0
    extreme_l = 0
    
    normal_m = 0
    mild_m = 0
    moderate_m = 0
    severe_m = 0
    extreme_m = 0
    
    normal_s = 0
    mild_s = 0
    moderate_s = 0
    severe_s = 0
    extreme_s = 0
 
    
    for c in range(len(less_DASS_score)):
       
        ############## for less than before anxiety ############# 

        if (less_DASS_score[c][l+2]>=0 and less_DASS_score[c][l+2]<8):
            normal_l += 1
            
        elif (less_DASS_score[c][l+2]>=8 and less_DASS_score[c][l+2]<10):
            mild_l += 1
            
        elif (less_DASS_score[c][l+2]>=10 and less_DASS_score[c][l+2]<15):
            moderate_l += 1
            
        elif (less_DASS_score[c][l+2]>=15 and less_DASS_score[c][l+2]<20):
            severe_l += 1
            
        else:
            extreme_l += 1
        
        ############## for more than before anxiety ############# 
    for ys in range(len(more_DASS_score)):
    
        if (more_DASS_score[ys][l+2]>=0 and more_DASS_score[ys][l+2]<8):
            normal_m += 1
            
        elif (more_DASS_score[ys][l+2]>=8 and more_DASS_score[ys][l+2]<10):
            mild_m += 1
            
        elif (more_DASS_score[ys][l+2]>=10 and more_DASS_score[ys][l+2]<15):
            moderate_m += 1
            
        elif (more_DASS_score[ys][l+2]>=15 and more_DASS_score[ys][l+2]<20):
            severe_m += 1
            
        else:
            extreme_m += 1
            
        ############## for nearly same anxiety ############# 
    for y in range(len(same_DASS_score)):

        if (same_DASS_score[y][l+2]>=0 and same_DASS_score[y][l+2]<8):
            normal_s += 1
            
        elif (same_DASS_score[y][l+2]>=8 and same_DASS_score[y][l+2]<10):
            mild_s += 1
            
        elif (same_DASS_score[y][l+2]>=10 and same_DASS_score[y][l+2]<15):
            moderate_s += 1
            
        elif (same_DASS_score[y][l+2]>=15 and same_DASS_score[y][l+2]<20):
            severe_s += 1
            
        else:
            extreme_s += 1
      
            
    temp_1 = [[normal_l, mild_l, moderate_l, severe_l, extreme_l],
            [normal_m, mild_m, moderate_m, severe_m, extreme_m],
            [normal_s, mild_s, moderate_s, severe_s, extreme_s]]        
            
    fnf_conn_anxiety_count[l] = temp_1[0]  
    fnf_conn_anxiety_count[l+2] = temp_1[1]  
    fnf_conn_anxiety_count[l+4] = temp_1[2]     
    

################ Es filtration for fnf connection #######################


fnf_conn_anxiety_count_es_filter = np.copy(fnf_conn_anxiety_count)


for row in range (0,6,2):
    
    fnf_conn_anxiety_count_es_filter[row][4] = abs(fnf_conn_anxiety_count_es_filter[row][4] - fnf_conn_anxiety_count_es_filter[row][4])
    fnf_conn_anxiety_count_es_filter[row+1][4] = abs(fnf_conn_anxiety_count_es_filter[row+1][4] - fnf_conn_anxiety_count[row][4])

#####################################################################


 
################## Social Awareness from you could infect #############       
you_infect = []
you_infect = survey_data['You spread virus']
Yes_you,Maybe_you,No_you = survey_data['You spread virus'].value_counts()

Yes_you_DASS_score = np.zeros((Yes_you,6),dtype = np.double)
Maybe_you_DASS_score = np.zeros((Maybe_you,6),dtype = np.double)
No_you_DASS_score = np.zeros((No_you,6),dtype = np.double)


val_yy = 0
val_my = 0
val_ny = 0


for you_val in range (len(survey_data)):
    if you_infect[you_val] == 'Yes':
        for i in range(6):   
            Yes_you_DASS_score[val_yy][i] = DASS_score[you_val][i]
        val_yy += 1
    elif you_infect[you_val] == 'Maybe':
        for j in range(6):       
            Maybe_you_DASS_score[val_my][j] = DASS_score[you_val][j]
        val_my += 1
    elif you_infect[you_val] == 'No':
        for j in range(6):       
            No_you_DASS_score[val_ny][j] = DASS_score[you_val][j]
        val_ny += 1
   
###################### you infect anxiety count ###########

you_infect_anxiety_count = np.zeros((6,5),dtype = np.double)


for l in range (2):
    normal_yy = 0
    mild_yy = 0
    moderate_yy = 0
    severe_yy = 0
    extreme_yy = 0
    
    normal_my = 0
    mild_my = 0
    moderate_my = 0
    severe_my = 0
    extreme_my = 0
    
    normal_ny = 0
    mild_ny = 0
    moderate_ny = 0
    severe_ny = 0
    extreme_ny = 0
 
    
    for c in range(len(Yes_you_DASS_score)):
       
        ############## for Yes anxiety ############# 

        if (Yes_you_DASS_score[c][l+2]>=0 and Yes_you_DASS_score[c][l+2]<8):
            normal_yy += 1
            
        elif (Yes_you_DASS_score[c][l+2]>=8 and Yes_you_DASS_score[c][l+2]<10):
            mild_yy += 1
            
        elif (Yes_you_DASS_score[c][l+2]>=10 and Yes_you_DASS_score[c][l+2]<15):
            moderate_yy += 1
            
        elif (Yes_you_DASS_score[c][l+2]>=15 and Yes_you_DASS_score[c][l+2]<20):
            severe_yy += 1
            
        else:
            extreme_yy += 1
        
        ############## for May be anxiety ############# 
    for ys in range(len(Maybe_you_DASS_score)):
    
        if (Maybe_you_DASS_score[ys][l+2]>=0 and Maybe_you_DASS_score[ys][l+2]<8):
            normal_my += 1
            
        elif (Maybe_you_DASS_score[ys][l+2]>=8 and Maybe_you_DASS_score[ys][l+2]<10):
            mild_my += 1
            
        elif (Maybe_you_DASS_score[ys][l+2]>=10 and Maybe_you_DASS_score[ys][l+2]<15):
            moderate_my += 1
            
        elif (Maybe_you_DASS_score[ys][l+2]>=15 and Maybe_you_DASS_score[ys][l+2]<20):
            severe_my += 1
            
        else:
            extreme_my += 1
            
        ############## for 'No' Depression ############# 
    for y in range(len(No_you_DASS_score)):

        if (No_you_DASS_score[y][l+2]>=0 and No_you_DASS_score[y][l+2]<8):
            normal_ny += 1
            
        elif (No_you_DASS_score[y][l+2]>=8 and No_you_DASS_score[y][l+2]<10):
            mild_ny += 1
            
        elif (No_you_DASS_score[y][l+2]>=10 and No_you_DASS_score[y][l+2]<15):
            moderate_ny += 1
            
        elif (No_you_DASS_score[y][l+2]>=15 and No_you_DASS_score[y][l+2]<20):
            severe_ny += 1
            
        else:
            extreme_ny += 1
      
            
    temp_2 = [[normal_yy, mild_yy, moderate_yy, severe_yy, extreme_yy],
            [normal_my, mild_my, moderate_my, severe_my, extreme_my],
            [normal_ny, mild_ny, moderate_ny, severe_ny, extreme_ny]]        
            
    you_infect_anxiety_count[l] = temp_2[0]  
    you_infect_anxiety_count[l+2] = temp_2[1]  
    you_infect_anxiety_count[l+4] = temp_2[2]     
    

################ Es filtration for you infect #######################


you_infect_anxiety_count_es_filter = np.copy(you_infect_anxiety_count)


for row in range (0,6,2):
    
    you_infect_anxiety_count_es_filter[row][4] = abs(you_infect_anxiety_count_es_filter[row][4] - you_infect_anxiety_count_es_filter[row][4])
    you_infect_anxiety_count_es_filter[row+1][4] = abs(you_infect_anxiety_count_es_filter[row+1][4] - you_infect_anxiety_count[row][4])

#####################################################################


 
################## Social Awareness from other could infect you #############       
other_infect = []
other_infect = survey_data['Others transfer virus']
Yes_other,Maybe_other,No_other = survey_data['Others transfer virus'].value_counts()

Yes_other_DASS_score = np.zeros((Yes_other,6),dtype = np.double)
Maybe_other_DASS_score = np.zeros((Maybe_other,6),dtype = np.double)
No_other_DASS_score = np.zeros((No_other,6),dtype = np.double)


val_yo = 0
val_mo = 0
val_no = 0


for other_val in range (len(survey_data)):
    if other_infect[other_val] == 'Yes':
        for i in range(6):   
            Yes_other_DASS_score[val_yo][i] = DASS_score[other_val][i]
        val_yo += 1
    elif other_infect[other_val] == 'Maybe':
        for j in range(6):       
            Maybe_other_DASS_score[val_mo][j] = DASS_score[other_val][j]
        val_mo += 1
    elif other_infect[other_val] == 'No':
        for j in range(6):       
            No_other_DASS_score[val_no][j] = DASS_score[other_val][j]
        val_no += 1
   
###################### other infect anxiety count ###########

other_infect_anxiety_count = np.zeros((6,5),dtype = np.double)


for l in range (2):
    normal_yo = 0
    mild_yo = 0
    moderate_yo = 0
    severe_yo = 0
    extreme_yo = 0
    
    normal_mo = 0
    mild_mo = 0
    moderate_mo = 0
    severe_mo = 0
    extreme_mo = 0
    
    normal_no = 0
    mild_no = 0
    moderate_no = 0
    severe_no = 0
    extreme_no = 0
 
    
    for c in range(len(Yes_other_DASS_score)):
       
        ############## for Yes anxiety ############# 

        if (Yes_other_DASS_score[c][l+2]>=0 and Yes_other_DASS_score[c][l+2]<8):
            normal_yo += 1
            
        elif (Yes_other_DASS_score[c][l+2]>=8 and Yes_other_DASS_score[c][l+2]<10):
            mild_yo += 1
            
        elif (Yes_other_DASS_score[c][l+2]>=10 and Yes_other_DASS_score[c][l+2]<15):
            moderate_yo += 1
            
        elif (Yes_other_DASS_score[c][l+2]>=15 and Yes_other_DASS_score[c][l+2]<20):
            severe_yo += 1
            
        else:
            extreme_yo += 1
        
        ############## for May be anxiety ############# 
    for ys in range(len(Maybe_other_DASS_score)):
    
        if (Maybe_other_DASS_score[ys][l+2]>=0 and Maybe_other_DASS_score[ys][l+2]<8):
            normal_mo += 1
            
        elif (Maybe_other_DASS_score[ys][l+2]>=8 and Maybe_other_DASS_score[ys][l+2]<10):
            mild_mo += 1
            
        elif (Maybe_other_DASS_score[ys][l+2]>=10 and Maybe_other_DASS_score[ys][l+2]<15):
            moderate_mo += 1
            
        elif (Maybe_other_DASS_score[ys][l+2]>=15 and Maybe_other_DASS_score[ys][l+2]<20):
            severe_mo += 1
            
        else:
            extreme_mo += 1
            
        ############## for 'No' Depression ############# 
    for y in range(len(No_other_DASS_score)):

        if (No_other_DASS_score[y][l+2]>=0 and No_other_DASS_score[y][l+2]<8):
            normal_no += 1
            
        elif (No_other_DASS_score[y][l+2]>=8 and No_other_DASS_score[y][l+2]<10):
            mild_no += 1
            
        elif (No_other_DASS_score[y][l+2]>=10 and No_other_DASS_score[y][l+2]<15):
            moderate_no += 1
            
        elif (No_other_DASS_score[y][l+2]>=15 and No_other_DASS_score[y][l+2]<20):
            severe_no += 1
            
        else:
            extreme_no += 1
      
            
    temp_3 = [[normal_yo, mild_yo, moderate_yo, severe_yo, extreme_yo],
            [normal_mo, mild_mo, moderate_mo, severe_mo, extreme_mo],
            [normal_no, mild_no, moderate_no, severe_no, extreme_no]]        
            
    other_infect_anxiety_count[l] = temp_3[0]  
    other_infect_anxiety_count[l+2] = temp_3[1]  
    other_infect_anxiety_count[l+4] = temp_3[2]     
    

################ Es filtration for other infect #######################


other_infect_anxiety_count_es_filter = np.copy(other_infect_anxiety_count)


for row in range (0,6,2):
    
    other_infect_anxiety_count_es_filter[row][4] = abs(other_infect_anxiety_count_es_filter[row][4] - other_infect_anxiety_count_es_filter[row][4])
    other_infect_anxiety_count_es_filter[row+1][4] = abs(other_infect_anxiety_count_es_filter[row+1][4] - other_infect_anxiety_count[row][4])

#####################################################################



import seaborn as sns
import matplotlib.pyplot as plt 


y_labels = ['Unaware','25%','50%','75%','100%','Less than before',
          'More than before','Nearly the same','Yes-you could infect',
          'Maybe-you could infect','No-you could infect','Yes-others could infect',
          'Maybe-others could infect','No-others could infect']
x_labels = ['Normal','Mild','Moderate','Severe','Extremely Severe']

################# for awareness BC data ###########################
awareness_var_anxiety_BC = np.zeros((14,5),dtype = np.double)

r = 0
for q in range (0,10,2):
    awareness_var_anxiety_BC[r] = awareness_anxiety_count[q] # for age group bc
    r += 1

for q in range (0,6,2):
    awareness_var_anxiety_BC[r] = fnf_conn_anxiety_count[q] # for age group bc
    r += 1

for q in range (0,6,2):
    awareness_var_anxiety_BC[r] = you_infect_anxiety_count[q] #for education bc
    r += 1

for q in range (0,6,2):
    awareness_var_anxiety_BC[r] = other_infect_anxiety_count[q]# for marital bc 
    r += 1


f, ax = plt.subplots(figsize=(10, 8))

sns.heatmap(awareness_var_anxiety_BC,vmin=0,vmax=820, xticklabels=x_labels, yticklabels = y_labels, mask=np.zeros_like(awareness_var_anxiety_BC, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, ax=ax)


#####################################################################


################# for awareness DC data ###########################
awareness_var_anxiety_DC = np.zeros((14,5),dtype = np.double)

r = 0
for q in range (1,10,2):
    awareness_var_anxiety_DC[r] = awareness_anxiety_count[q] # for age group bc
    r += 1

for q in range (1,6,2):
    awareness_var_anxiety_DC[r] = fnf_conn_anxiety_count[q] # for age group bc
    r += 1

for q in range (1,6,2):
    awareness_var_anxiety_DC[r] = you_infect_anxiety_count[q] #for education bc
    r += 1

for q in range (1,6,2):
    awareness_var_anxiety_DC[r] = other_infect_anxiety_count[q]# for marital bc 
    r += 1


f, ax = plt.subplots(figsize=(10, 8))

sns.heatmap(awareness_var_anxiety_DC,vmin=0,vmax=820, xticklabels=x_labels, yticklabels = y_labels, mask=np.zeros_like(awareness_var_anxiety_DC, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, ax=ax)


#####################################################################



################# for awareness BC data with es filter ###########################
awareness_var_anxiety_BC_es_filter = np.zeros((14,5),dtype = np.double)


r = 0
for q in range (0,10,2):
    awareness_var_anxiety_BC_es_filter[r] = awareness_anxiety_count_es_filter[q] # for age group bc
    r += 1

for q in range (0,6,2):
    awareness_var_anxiety_BC_es_filter[r] = fnf_conn_anxiety_count_es_filter[q] # for age group bc
    r += 1

for q in range (0,6,2):
    awareness_var_anxiety_BC_es_filter[r] = you_infect_anxiety_count_es_filter[q] #for education bc
    r += 1

for q in range (0,6,2):
    awareness_var_anxiety_BC_es_filter[r] = other_infect_anxiety_count_es_filter[q]# for marital bc 
    r += 1
 

f, ax = plt.subplots(figsize=(10, 8))

sns.heatmap(awareness_var_anxiety_BC_es_filter,vmin=0,vmax=820, xticklabels=x_labels, yticklabels = y_labels, mask=np.zeros_like(awareness_var_anxiety_BC_es_filter, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, ax=ax)


#####################################################################


################# for awareness DC data with es filter ###########################
awareness_var_anxiety_DC_es_filter = np.zeros((14,5),dtype = np.double)


r = 0
for q in range (1,10,2):
    awareness_var_anxiety_DC_es_filter[r] = awareness_anxiety_count_es_filter[q] # for age group bc
    r += 1

for q in range (1,6,2):
    awareness_var_anxiety_DC_es_filter[r] = fnf_conn_anxiety_count_es_filter[q] # for age group bc
    r += 1

for q in range (1,6,2):
    awareness_var_anxiety_DC_es_filter[r] = you_infect_anxiety_count_es_filter[q] #for education bc
    r += 1

for q in range (1,6,2):
    awareness_var_anxiety_DC_es_filter[r] = other_infect_anxiety_count_es_filter[q]# for marital bc 
    r += 1
 

f, ax = plt.subplots(figsize=(10, 8))

sns.heatmap(awareness_var_anxiety_DC_es_filter,vmin=0,vmax=820, xticklabels=x_labels, yticklabels = y_labels, mask=np.zeros_like(awareness_var_anxiety_DC_es_filter, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, ax=ax)

#####################################################################


############################## DC-BC ################################


############################ awareness ##############################

awareness_anxiety_count_diff = np.zeros((5,5),dtype = np.double)
per = [per_0, per_25, per_50, per_75, per_100]
a=1
for i in range(5):
    awareness_anxiety_count_diff[i] = (((awareness_anxiety_count[a])/per[i])*100) - (((awareness_anxiety_count[a-1])/per[i])*100)
    a += 2

#####################################################################

############################ fnf conn ##############################

fnf_conn_anxiety_count_diff = np.zeros((3,5),dtype = np.double)
fnf = [Lessthanbefore, Morethanbefore, Nearlythesame]
a=1
for i in range(3):
    fnf_conn_anxiety_count_diff[i] = (((fnf_conn_anxiety_count[a])/fnf[i])*100) - (((fnf_conn_anxiety_count[a-1])/fnf[i])*100)
    a += 2

#####################################################################

############################ you infect ##############################

you_infect_anxiety_count_diff = np.zeros((3,5),dtype = np.double)
you_option = [Yes_you, Maybe_you, No_you]

a=1
for i in range(3):
    you_infect_anxiety_count_diff[i] = (((you_infect_anxiety_count[a])/you_option[i])*100) - (((you_infect_anxiety_count[a-1])/you_option[i])*100)
    a += 2

#####################################################################


############################ other infect ##############################

other_infect_anxiety_count_diff = np.zeros((3,5),dtype = np.double)
other_option = [Yes_other, Maybe_other, No_other]

a=1
for i in range(3):
    other_infect_anxiety_count_diff[i] = (((other_infect_anxiety_count[a])/other_option[i])*100) - (((other_infect_anxiety_count[a-1])/other_option[i])*100)
    a += 2

#####################################################################


#####################################################################

awareness_var_anxiety_diff = np.zeros((14,5), dtype = np.double)


for i in range (5):
    awareness_var_anxiety_diff[i] = awareness_anxiety_count_diff[i]

for i in range (3):
    awareness_var_anxiety_diff[i+5] = fnf_conn_anxiety_count_diff[i]

for i in range (3):
    awareness_var_anxiety_diff[i+8] = you_infect_anxiety_count_diff[i]

for i in range (3):
    awareness_var_anxiety_diff[i+11] = other_infect_anxiety_count_diff[i]


f, ax = plt.subplots(figsize=(10, 8))

sns.heatmap(awareness_var_anxiety_diff,vmin = -50, vmax = 50, xticklabels=x_labels, yticklabels = y_labels, mask=np.zeros_like(awareness_var_anxiety_diff, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, ax=ax)


