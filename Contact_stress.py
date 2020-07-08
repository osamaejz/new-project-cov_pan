from DASS_calculation import survey_data , DASS_score
import numpy as np
######################## for Contact varaibles ############################
 
################## Contact with Recent consultancy #############       
consultancy = []
consultancy = survey_data['Recent consultancy']
No_recent, Yes_recent = survey_data['Recent consultancy'].value_counts()

No_recent_DASS_score = np.zeros((No_recent,6),dtype = np.double)
Yes_recent_DASS_score = np.zeros((Yes_recent,6),dtype = np.double)


val_nr = 0
val_yr = 0


for consult_value in range (len(survey_data)):
    if consultancy[consult_value] == 'No':
        for i in range(6):   
            No_recent_DASS_score[val_nr][i] = DASS_score[consult_value][i]
        val_nr += 1
    elif consultancy[consult_value] == 'Yes':
        for j in range(6):       
            Yes_recent_DASS_score[val_yr][j] = DASS_score[consult_value][j]
        val_yr += 1


consultancy_stress_count = np.zeros((4,5),dtype = np.double)


for l in range (2):
    normal_nr = 0
    mild_nr = 0
    moderate_nr = 0
    severe_nr = 0
    extreme_nr = 0
    
    normal_yr = 0
    mild_yr = 0
    moderate_yr = 0
    severe_yr = 0
    extreme_yr = 0
  
 
    for c in range(len(No_recent_DASS_score)):
       
        ############## for unware stress ############# 

        if (No_recent_DASS_score[c][l+4]>=0 and No_recent_DASS_score[c][l+4]<15):
            normal_nr += 1
            
        elif (No_recent_DASS_score[c][l+4]>=15 and No_recent_DASS_score[c][l+4]<19):
            mild_nr += 1
            
        elif (No_recent_DASS_score[c][l+4]>=19 and No_recent_DASS_score[c][l+4]<26):
            moderate_nr += 1
            
        elif (No_recent_DASS_score[c][l+4]>=26 and No_recent_DASS_score[c][l+4]<34):
            severe_nr += 1
            
        else:
            extreme_nr += 1
        
        ############## for 25% stress ############# 
    for ys in range(len(Yes_recent_DASS_score)):
    
        if (Yes_recent_DASS_score[ys][l+4]>=0 and Yes_recent_DASS_score[ys][l+4]<15):
            normal_yr += 1
            
        elif (Yes_recent_DASS_score[ys][l+4]>=15 and Yes_recent_DASS_score[ys][l+4]<19):
            mild_yr += 1
            
        elif (Yes_recent_DASS_score[ys][l+4]>=19 and Yes_recent_DASS_score[ys][l+4]<26):
            moderate_yr += 1
            
        elif (Yes_recent_DASS_score[ys][l+4]>=26 and Yes_recent_DASS_score[ys][l+4]<34):
            severe_yr += 1
            
        else:
            extreme_yr += 1
      
       
    temp_0 = [[normal_nr, mild_nr, moderate_nr, severe_nr, extreme_nr],
            [normal_yr, mild_yr, moderate_yr, severe_yr, extreme_yr]]
            
            
    consultancy_stress_count[l] = temp_0[0]  
    consultancy_stress_count[l+2] = temp_0[1]  
    

################ Es filtration for recent consultancy #######################


consultancy_stress_count_es_filter = np.copy(consultancy_stress_count)


for row in range (0,4,2):
    
    consultancy_stress_count_es_filter[row][4] = abs(consultancy_stress_count_es_filter[row][4] - consultancy_stress_count_es_filter[row][4])
    consultancy_stress_count_es_filter[row+1][4] = abs(consultancy_stress_count_es_filter[row+1][4] - consultancy_stress_count[row][4])

#####################################################################

 
################## Contact with you been infected #############       
you_infected = []
you_infected = survey_data['You infected']
No_you_inf, Yes_you_inf = survey_data['You infected'].value_counts()

No_you_inf_DASS_score = np.zeros((No_you_inf,6),dtype = np.double)
Yes_you_inf_DASS_score = np.zeros((Yes_you_inf,6),dtype = np.double)


val_nyi = 0
val_yyi = 0


for you_inf_value in range (len(survey_data)):
    if you_infected[you_inf_value] == 'No':
        for i in range(6):   
            No_you_inf_DASS_score[val_nyi][i] = DASS_score[you_inf_value][i]
        val_nyi += 1
    elif you_infected[you_inf_value] == 'Yes':
        for j in range(6):       
            Yes_you_inf_DASS_score[val_yyi][j] = DASS_score[you_inf_value][j]
        val_yyi += 1


you_inf_stress_count = np.zeros((4,5),dtype = np.double)


for l in range (2):
    normal_nyi = 0
    mild_nyi = 0
    moderate_nyi = 0
    severe_nyi = 0
    extreme_nyi = 0
    
    normal_yyi = 0
    mild_yyi = 0
    moderate_yyi = 0
    severe_yyi = 0
    extreme_yyi = 0
  
 
    for c in range(len(No_you_inf_DASS_score)):
       
        ############## for no stress ############# 

        if (No_you_inf_DASS_score[c][l+4]>=0 and No_you_inf_DASS_score[c][l+4]<15):
            normal_nyi += 1
            
        elif (No_you_inf_DASS_score[c][l+4]>=15 and No_you_inf_DASS_score[c][l+4]<19):
            mild_nyi += 1
            
        elif (No_you_inf_DASS_score[c][l+4]>=19 and No_you_inf_DASS_score[c][l+4]<26):
            moderate_nyi += 1
            
        elif (No_you_inf_DASS_score[c][l+4]>=26 and No_you_inf_DASS_score[c][l+4]<34):
            severe_nyi += 1
            
        else:
            extreme_nyi += 1
        
        ############## for yes stress ############# 
    for ys in range(len(Yes_you_inf_DASS_score)):
    
        if (Yes_you_inf_DASS_score[ys][l+4]>=0 and Yes_you_inf_DASS_score[ys][l+4]<15):
            normal_yyi += 1
            
        elif (Yes_you_inf_DASS_score[ys][l+4]>=15 and Yes_you_inf_DASS_score[ys][l+4]<19):
            mild_yyi += 1
            
        elif (Yes_you_inf_DASS_score[ys][l+4]>=19 and Yes_you_inf_DASS_score[ys][l+4]<26):
            moderate_yyi += 1
            
        elif (Yes_you_inf_DASS_score[ys][l+4]>=26 and Yes_you_inf_DASS_score[ys][l+4]<34):
            severe_yyi += 1
            
        else:
            extreme_yyi += 1
      
       
    temp_1 = [[normal_nyi, mild_nyi, moderate_nyi, severe_nyi, extreme_nyi],
            [normal_yyi, mild_yyi, moderate_yyi, severe_yyi, extreme_yyi]]
            
            
    you_inf_stress_count[l] = temp_1[0]  
    you_inf_stress_count[l+2] = temp_1[1]  
    

################ Es filtration for you infected #######################


you_inf_stress_count_es_filter = np.copy(you_inf_stress_count)


for row in range (0,4,2):
    
    you_inf_stress_count_es_filter[row][4] = abs(you_inf_stress_count_es_filter[row][4] - you_inf_stress_count_es_filter[row][4])
    you_inf_stress_count_es_filter[row+1][4] = abs(you_inf_stress_count_es_filter[row+1][4] - you_inf_stress_count[row][4])

#####################################################################
 

 
################## Contact with someone in your home infected #############       
home_infected = []
home_infected = survey_data['Family member infected']
No_home_inf, Yes_home_inf = survey_data['Family member infected'].value_counts()

No_home_inf_DASS_score = np.zeros((No_home_inf,6),dtype = np.double)
Yes_home_inf_DASS_score = np.zeros((Yes_home_inf,6),dtype = np.double)


val_nhi = 0
val_yhi = 0


for home_inf_value in range (len(survey_data)):
    if home_infected[home_inf_value] == 'No':
        for i in range(6):   
            No_home_inf_DASS_score[val_nhi][i] = DASS_score[home_inf_value][i]
        val_nhi += 1
    elif home_infected[home_inf_value] == 'Yes':
        for j in range(6):       
            Yes_home_inf_DASS_score[val_yhi][j] = DASS_score[home_inf_value][j]
        val_yhi += 1


home_inf_stress_count = np.zeros((4,5),dtype = np.double)


for l in range (2):
    normal_nhi = 0
    mild_nhi = 0
    moderate_nhi = 0
    severe_nhi = 0
    extreme_nhi = 0
    
    normal_yhi = 0
    mild_yhi = 0
    moderate_yhi = 0
    severe_yhi = 0
    extreme_yhi = 0
  
 
    for c in range(len(No_home_inf_DASS_score)):
       
        ############## for no stress ############# 

        if (No_home_inf_DASS_score[c][l+4]>=0 and No_home_inf_DASS_score[c][l+4]<15):
            normal_nhi += 1
            
        elif (No_home_inf_DASS_score[c][l+4]>=15 and No_home_inf_DASS_score[c][l+4]<19):
            mild_nhi += 1
            
        elif (No_home_inf_DASS_score[c][l+4]>=19 and No_home_inf_DASS_score[c][l+4]<26):
            moderate_nhi += 1
            
        elif (No_home_inf_DASS_score[c][l+4]>=26 and No_home_inf_DASS_score[c][l+4]<34):
            severe_nhi += 1
            
        else:
            extreme_nhi += 1
        
        ############## for yes stress ############# 
    for ys in range(len(Yes_home_inf_DASS_score)):
    
        if (Yes_home_inf_DASS_score[ys][l+4]>=0 and Yes_home_inf_DASS_score[ys][l+4]<15):
            normal_yhi += 1
            
        elif (Yes_home_inf_DASS_score[ys][l+4]>=15 and Yes_home_inf_DASS_score[ys][l+4]<19):
            mild_yhi += 1
            
        elif (Yes_home_inf_DASS_score[ys][l+4]>=19 and Yes_home_inf_DASS_score[ys][l+4]<26):
            moderate_yhi += 1
            
        elif (Yes_home_inf_DASS_score[ys][l+4]>=26 and Yes_home_inf_DASS_score[ys][l+4]<34):
            severe_yhi += 1
            
        else:
            extreme_yhi += 1
      
       
    temp_2 = [[normal_nhi, mild_nhi, moderate_nhi, severe_nhi, extreme_nhi],
            [normal_yhi, mild_yhi, moderate_yhi, severe_yhi, extreme_yhi]]
            
            
    home_inf_stress_count[l] = temp_2[0]  
    home_inf_stress_count[l+2] = temp_2[1]  
    

################ Es filtration for home infected #######################


home_inf_stress_count_es_filter = np.copy(home_inf_stress_count)


for row in range (0,4,2):
    
    home_inf_stress_count_es_filter[row][4] = abs(home_inf_stress_count_es_filter[row][4] - home_inf_stress_count_es_filter[row][4])
    home_inf_stress_count_es_filter[row+1][4] = abs(home_inf_stress_count_es_filter[row+1][4] - home_inf_stress_count[row][4])

#####################################################################
 

 
################## Contact with someone in your fnr infected #############       
fnr_infected = []
fnr_infected = survey_data['Friend and relative infected']
Yes_fnr_inf, No_fnr_inf  = survey_data['Friend and relative infected'].value_counts()

No_fnr_inf_DASS_score = np.zeros((No_fnr_inf,6),dtype = np.double)
Yes_fnr_inf_DASS_score = np.zeros((Yes_fnr_inf,6),dtype = np.double)


val_nfi = 0
val_yfi = 0


for fnr_inf_value in range (len(survey_data)):
    if fnr_infected[fnr_inf_value] == 'No':
        for i in range(6):   
            No_fnr_inf_DASS_score[val_nfi][i] = DASS_score[fnr_inf_value][i]
        val_nfi += 1
    elif fnr_infected[fnr_inf_value] == 'Yes':
        for j in range(6):       
            Yes_fnr_inf_DASS_score[val_yfi][j] = DASS_score[fnr_inf_value][j]
        val_yfi += 1


fnr_inf_stress_count = np.zeros((4,5),dtype = np.double)


for l in range (2):
    normal_nfi = 0
    mild_nfi = 0
    moderate_nfi = 0
    severe_nfi = 0
    extreme_nfi = 0
    
    normal_yfi = 0
    mild_yfi = 0
    moderate_yfi = 0
    severe_yfi = 0
    extreme_yfi = 0
  
 
    for c in range(len(No_fnr_inf_DASS_score)):
       
        ############## for no stress ############# 

        if (No_fnr_inf_DASS_score[c][l+4]>=0 and No_fnr_inf_DASS_score[c][l+4]<15):
            normal_nfi += 1
            
        elif (No_fnr_inf_DASS_score[c][l+4]>=15 and No_fnr_inf_DASS_score[c][l+4]<19):
            mild_nfi += 1
            
        elif (No_fnr_inf_DASS_score[c][l+4]>=19 and No_fnr_inf_DASS_score[c][l+4]<26):
            moderate_nfi += 1
            
        elif (No_fnr_inf_DASS_score[c][l+4]>=26 and No_fnr_inf_DASS_score[c][l+4]<34):
            severe_nfi += 1
            
        else:
            extreme_nfi += 1
        
        ############## for yes stress ############# 
    for ys in range(len(Yes_fnr_inf_DASS_score)):
    
        if (Yes_fnr_inf_DASS_score[ys][l+4]>=0 and Yes_fnr_inf_DASS_score[ys][l+4]<15):
            normal_yfi += 1
            
        elif (Yes_fnr_inf_DASS_score[ys][l+4]>=15 and Yes_fnr_inf_DASS_score[ys][l+4]<19):
            mild_yfi += 1
            
        elif (Yes_fnr_inf_DASS_score[ys][l+4]>=19 and Yes_fnr_inf_DASS_score[ys][l+4]<26):
            moderate_yfi += 1
            
        elif (Yes_fnr_inf_DASS_score[ys][l+4]>=26 and Yes_fnr_inf_DASS_score[ys][l+4]<34):
            severe_yfi += 1
            
        else:
            extreme_yfi += 1
      
       
    temp_3 = [[normal_nfi, mild_nfi, moderate_nfi, severe_nfi, extreme_nfi],
            [normal_yfi, mild_yfi, moderate_yfi, severe_yfi, extreme_yfi]]
            
            
    fnr_inf_stress_count[l] = temp_3[0]  
    fnr_inf_stress_count[l+2] = temp_3[1]  
    

################ Es filtration for fnr infected#######################


fnr_inf_stress_count_es_filter = np.copy(fnr_inf_stress_count)


for row in range (0,4,2):
    
    fnr_inf_stress_count_es_filter[row][4] = abs(fnr_inf_stress_count_es_filter[row][4] - fnr_inf_stress_count_es_filter[row][4])
    fnr_inf_stress_count_es_filter[row+1][4] = abs(fnr_inf_stress_count_es_filter[row+1][4] - fnr_inf_stress_count[row][4])

#####################################################################
 
         
#####################################################################


import seaborn as sns
import matplotlib.pyplot as plt 


y_labels = ['No-recent consultancy', 'Yes-recent consultancy', 'No-You infected',
          'Yes-you infected', 'No-family member infected', 'Yes-family member infected',
          'No-friends & relative infected','Yes-friends & relative infected']
x_labels = ['Normal','Mild','Moderate','Severe','Extremely Severe']

################# for Contact BC data ###########################
contact_var_stress_BC = np.zeros((8,5),dtype = np.double)

r = 0
for q in range (0,4,2):
    contact_var_stress_BC[r] = consultancy_stress_count[q] # for age group bc
    r += 1

for q in range (0,4,2):
    contact_var_stress_BC[r] = you_inf_stress_count[q] # for age group bc
    r += 1

for q in range (0,4,2):
    contact_var_stress_BC[r] = home_inf_stress_count[q] #for education bc
    r += 1

for q in range (0,4,2):
    contact_var_stress_BC[r] = fnr_inf_stress_count[q]# for marital bc 
    r += 1


f, ax = plt.subplots(figsize=(10, 8))

sns.heatmap(contact_var_stress_BC, vmin=0, vmax=1350, xticklabels=x_labels, yticklabels = y_labels,   mask=np.zeros_like(contact_var_stress_BC, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, ax=ax)


#####################################################################


################# for Contact DC data ###########################
contact_var_stress_DC = np.zeros((8,5),dtype = np.double)

r = 0
for q in range (1,4,2):
    contact_var_stress_DC[r] = consultancy_stress_count[q] # for age group bc
    r += 1

for q in range (1,4,2):
    contact_var_stress_DC[r] = you_inf_stress_count[q] # for age group bc
    r += 1

for q in range (1,4,2):
    contact_var_stress_DC[r] = home_inf_stress_count[q] #for education bc
    r += 1

for q in range (1,4,2):
    contact_var_stress_DC[r] = fnr_inf_stress_count[q]# for marital bc 
    r += 1


f, ax = plt.subplots(figsize=(10, 8))

sns.heatmap(contact_var_stress_DC, vmin=0, vmax=1350, xticklabels=x_labels, yticklabels = y_labels,   mask=np.zeros_like(contact_var_stress_DC, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, ax=ax)


#####################################################################


################# for Contact BC data with ES filter ###########################
contact_var_stress_BC_es_filter = np.zeros((8,5),dtype = np.double)

r = 0
for q in range (0,4,2):
    contact_var_stress_BC_es_filter[r] = consultancy_stress_count_es_filter[q] # for age group bc
    r += 1

for q in range (0,4,2):
    contact_var_stress_BC_es_filter[r] = you_inf_stress_count_es_filter[q] # for age group bc
    r += 1

for q in range (0,4,2):
    contact_var_stress_BC_es_filter[r] = home_inf_stress_count_es_filter[q] #for education bc
    r += 1

for q in range (0,4,2):
    contact_var_stress_BC_es_filter[r] = fnr_inf_stress_count_es_filter[q]# for marital bc 
    r += 1


f, ax = plt.subplots(figsize=(10, 8))

sns.heatmap(contact_var_stress_BC_es_filter, vmin=0, vmax=1350, xticklabels=x_labels, yticklabels = y_labels,   mask=np.zeros_like(contact_var_stress_BC_es_filter, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, ax=ax)


#####################################################################


################# for Contact DC data with ES filter ###########################
contact_var_stress_DC_es_filter = np.zeros((8,5),dtype = np.double)

r = 0
for q in range (1,4,2):
    contact_var_stress_DC_es_filter[r] = consultancy_stress_count_es_filter[q] # for age group bc
    r += 1

for q in range (1,4,2):
    contact_var_stress_DC_es_filter[r] = you_inf_stress_count_es_filter[q] # for age group bc
    r += 1

for q in range (1,4,2):
    contact_var_stress_DC_es_filter[r] = home_inf_stress_count_es_filter[q] #for education bc
    r += 1

for q in range (1,4,2):
    contact_var_stress_DC_es_filter[r] = fnr_inf_stress_count_es_filter[q]# for marital bc 
    r += 1


f, ax = plt.subplots(figsize=(10, 8))

sns.heatmap(contact_var_stress_DC_es_filter, vmin=0, vmax=1350, xticklabels=x_labels, yticklabels = y_labels,   mask=np.zeros_like(contact_var_stress_DC_es_filter, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, ax=ax)


#####################################################################

############################## DC-BC ################################


############################ Recent consultancy ##############################

consultancy_stress_count_diff = np.zeros((2,5),dtype = np.double)
cons = [No_recent, Yes_recent]
a=1
for i in range(2):
    consultancy_stress_count_diff[i] = (((consultancy_stress_count[a])/cons[i])*100) - (((consultancy_stress_count[a-1])/cons[i])*100)
    a += 2

#####################################################################

############################ you infected ##############################

you_inf_stress_count_diff = np.zeros((2,5),dtype = np.double)
y_inf = [No_you_inf, Yes_you_inf]
a=1
for i in range(2):
    you_inf_stress_count_diff[i] = (((you_inf_stress_count[a])/y_inf[i])*100) - (((you_inf_stress_count[a-1])/y_inf[i])*100)
    a += 2

#####################################################################


############################ home infected  ##############################

home_inf_stress_count_diff = np.zeros((2,5),dtype = np.double)
h_inf = [No_home_inf, Yes_home_inf]
a=1
for i in range(2):
    home_inf_stress_count_diff[i] = (((home_inf_stress_count[a])/h_inf[i])*100) - (((home_inf_stress_count[a-1])/h_inf[i])*100)
    a += 2

#####################################################################



############################ FNR infected  ##############################

fnr_inf_stress_count_diff = np.zeros((2,5),dtype = np.double)
f_inf = [No_fnr_inf, Yes_fnr_inf]
a=1
for i in range(2):
    fnr_inf_stress_count_diff[i] = (((fnr_inf_stress_count[a])/f_inf[i])*100) - (((fnr_inf_stress_count[a-1])/f_inf[i])*100)
    a += 2

#####################################################################

#####################################################################

contact_var_stress_diff = np.zeros((8,5), dtype = np.double)


for i in range (2):
    contact_var_stress_diff[i] = consultancy_stress_count_diff[i]

for i in range (2):
    contact_var_stress_diff[i+2] = you_inf_stress_count_diff[i]

for i in range (2):
    contact_var_stress_diff[i+4] = home_inf_stress_count_diff[i]

for i in range (2):
    contact_var_stress_diff[i+6] = fnr_inf_stress_count_diff[i]


f, ax = plt.subplots(figsize=(10, 8))

sns.heatmap(contact_var_stress_diff, vmin=-50, vmax=50, xticklabels=x_labels, yticklabels = y_labels,   mask=np.zeros_like(contact_var_stress_diff, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, ax=ax)




