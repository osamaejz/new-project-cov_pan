from DASS_calculation import survey_data , DASS_score
import numpy as np
################# for Psychological effect variable ###################

##################### for dream sometime #####################

dream = []
dream = survey_data['Dream']
Yes_dream, No_dream = survey_data['Dream'].value_counts()

Yes_dream_DASS_score = np.zeros((Yes_dream,6),dtype = np.double)
No_dream_DASS_score = np.zeros((No_dream,6),dtype = np.double)


val_yd = 0
val_nd = 0


for dream_value in range (len(survey_data)):
    if dream[dream_value] == 'Yes':
        for i in range(6):   
            Yes_dream_DASS_score[val_yd][i] = DASS_score[dream_value][i]
        val_yd += 1
    elif dream[dream_value] == 'No':
        for j in range(6):       
            No_dream_DASS_score[val_nd][j] = DASS_score[dream_value][j]
        val_nd += 1



dream_depression_count = np.zeros((4,5),dtype = np.double)


for l in range (2):
    normal_yd = 0
    mild_yd = 0
    moderate_yd = 0
    severe_yd = 0
    extreme_yd = 0
    
    normal_nd = 0
    mild_nd = 0
    moderate_nd = 0
    severe_nd = 0
    extreme_nd = 0
  
    for c in range(len(Yes_dream_DASS_score)):
        ############## for yes depression ############# 

        if (Yes_dream_DASS_score[c][l]>=0 and Yes_dream_DASS_score[c][l]<10):
            normal_yd += 1
            
        elif (Yes_dream_DASS_score[c][l]>=10 and Yes_dream_DASS_score[c][l]<14):
            mild_yd += 1
            
        elif (Yes_dream_DASS_score[c][l]>=14 and Yes_dream_DASS_score[c][l]<21):
            moderate_yd += 1
            
        elif (Yes_dream_DASS_score[c][l]>=21 and Yes_dream_DASS_score[c][l]<28):
            severe_yd += 1
            
        else:
            extreme_yd += 1
    
  
        ############## for no depression ############# 
    for ys in range(len(No_dream_DASS_score)):
    
        if (No_dream_DASS_score[ys][l]>=0 and No_dream_DASS_score[ys][l]<10):
            normal_nd += 1
            
        elif (No_dream_DASS_score[ys][l]>=10 and No_dream_DASS_score[ys][l]<14):
            mild_nd += 1
            
        elif (No_dream_DASS_score[ys][l]>=14 and No_dream_DASS_score[ys][l]<21):
            moderate_nd += 1
            
        elif (No_dream_DASS_score[ys][l]>=21 and No_dream_DASS_score[ys][l]<28):
            severe_nd += 1
            
        else:
            extreme_nd += 1
        
   
    temp_0 = [[normal_yd, mild_yd, moderate_yd, severe_yd, extreme_yd],
            [normal_nd, mild_nd, moderate_nd, severe_nd, extreme_nd]]
            
       
    dream_depression_count[l] = temp_0[0]  
    dream_depression_count[l+2] = temp_0[1]  
    

################ Es filtration for dream #######################


dream_depression_count_es_filter = np.copy(dream_depression_count)


for row in range (0,4,2):
    
    dream_depression_count_es_filter[row][4] = abs(dream_depression_count_es_filter[row][4] - dream_depression_count_es_filter[row][4])
    dream_depression_count_es_filter[row+1][4] = abs(dream_depression_count_es_filter[row+1][4] - dream_depression_count[row][4])

#####################################################################



##################### for dream about COVID #####################

co_dream = []
co_dream = survey_data['Dream about COVID']
No_co_dream, Yes_co_dream = survey_data['Dream about COVID'].value_counts()

Yes_co_dream_DASS_score = np.zeros((Yes_co_dream,6),dtype = np.double)
No_co_dream_DASS_score = np.zeros((No_co_dream,6),dtype = np.double)


val_ycd = 0
val_ncd = 0


for co_dream_value in range (len(survey_data)):
    if co_dream[co_dream_value] == 'Yes':
        for i in range(6):   
            Yes_co_dream_DASS_score[val_ycd][i] = DASS_score[co_dream_value][i]
        val_ycd += 1
    elif co_dream[co_dream_value] == 'No':
        for j in range(6):       
            No_co_dream_DASS_score[val_ncd][j] = DASS_score[co_dream_value][j]
        val_ncd += 1



co_dream_depression_count = np.zeros((4,5),dtype = np.double)


for l in range (2):
    normal_ycd = 0
    mild_ycd = 0
    moderate_ycd = 0
    severe_ycd = 0
    extreme_ycd = 0
    
    normal_ncd = 0
    mild_ncd = 0
    moderate_ncd = 0
    severe_ncd = 0
    extreme_ncd = 0
  
    for c in range(len(Yes_co_dream_DASS_score)):
        ############## for yes depression ############# 

        if (Yes_co_dream_DASS_score[c][l]>=0 and Yes_co_dream_DASS_score[c][l]<10):
            normal_ycd += 1
            
        elif (Yes_co_dream_DASS_score[c][l]>=10 and Yes_co_dream_DASS_score[c][l]<14):
            mild_ycd += 1
            
        elif (Yes_co_dream_DASS_score[c][l]>=14 and Yes_co_dream_DASS_score[c][l]<21):
            moderate_ycd += 1
            
        elif (Yes_co_dream_DASS_score[c][l]>=21 and Yes_co_dream_DASS_score[c][l]<28):
            severe_ycd += 1
            
        else:
            extreme_ycd += 1
    
  
        ############## for no depression ############# 
    for ys in range(len(No_co_dream_DASS_score)):
    
        if (No_co_dream_DASS_score[ys][l]>=0 and No_co_dream_DASS_score[ys][l]<10):
            normal_ncd += 1
            
        elif (No_co_dream_DASS_score[ys][l]>=10 and No_co_dream_DASS_score[ys][l]<14):
            mild_ncd += 1
            
        elif (No_co_dream_DASS_score[ys][l]>=14 and No_co_dream_DASS_score[ys][l]<21):
            moderate_ncd += 1
            
        elif (No_co_dream_DASS_score[ys][l]>=21 and No_co_dream_DASS_score[ys][l]<28):
            severe_ncd += 1
            
        else:
            extreme_ncd += 1
        
   
    temp_1 = [[normal_ycd, mild_ycd, moderate_ycd, severe_ycd, extreme_ycd],
            [normal_ncd, mild_ncd, moderate_ncd, severe_ncd, extreme_ncd]]
            
       
    co_dream_depression_count[l] = temp_1[0]  
    co_dream_depression_count[l+2] = temp_1[1]  
    

################ Es filtration for dream #######################


co_dream_depression_count_es_filter = np.copy(co_dream_depression_count)


for row in range (0,4,2):
    
    co_dream_depression_count_es_filter[row][4] = abs(co_dream_depression_count_es_filter[row][4] - co_dream_depression_count_es_filter[row][4])
    co_dream_depression_count_es_filter[row+1][4] = abs(co_dream_depression_count_es_filter[row+1][4] - co_dream_depression_count[row][4])

#####################################################################


##################### for affect psychologically #####################

psycho = []
psycho = survey_data['Pandemic affect mentally']
Yes_psycho, No_psycho, Maybe_psycho = survey_data['Pandemic affect mentally'].value_counts()

Yes_psycho_DASS_score = np.zeros((Yes_psycho,6),dtype = np.double)
No_psycho_DASS_score = np.zeros((No_psycho,6),dtype = np.double)
Maybe_psycho_DASS_score = np.zeros((Maybe_psycho,6),dtype = np.double)


val_yp = 0
val_np = 0
val_mp = 0


for psycho_value in range (len(survey_data)):
    if psycho[psycho_value] == 'Yes':
        for i in range(6):   
            Yes_psycho_DASS_score[val_yp][i] = DASS_score[psycho_value][i]
        val_yp += 1
    elif psycho[psycho_value] == 'No':
        for j in range(6):       
            No_psycho_DASS_score[val_np][j] = DASS_score[psycho_value][j]
        val_np += 1
    elif psycho[psycho_value] == 'Maybe':
        for j in range(6):       
            Maybe_psycho_DASS_score[val_mp][j] = DASS_score[psycho_value][j]
        val_mp += 1


psycho_depression_count = np.zeros((6,5),dtype = np.double)


for l in range (2):
    normal_yp = 0
    mild_yp = 0
    moderate_yp = 0
    severe_yp = 0
    extreme_yp = 0
    
    normal_np = 0
    mild_np = 0
    moderate_np = 0
    severe_np = 0
    extreme_np = 0
    
    normal_mp = 0
    mild_mp = 0
    moderate_mp = 0
    severe_mp = 0
    extreme_mp = 0
  
    for c in range(len(Yes_psycho_DASS_score)):
        ############## for yes depression ############# 

        if (Yes_psycho_DASS_score[c][l]>=0 and Yes_psycho_DASS_score[c][l]<10):
            normal_yp += 1
            
        elif (Yes_psycho_DASS_score[c][l]>=10 and Yes_psycho_DASS_score[c][l]<14):
            mild_yp += 1
            
        elif (Yes_psycho_DASS_score[c][l]>=14 and Yes_psycho_DASS_score[c][l]<21):
            moderate_yp += 1
            
        elif (Yes_psycho_DASS_score[c][l]>=21 and Yes_psycho_DASS_score[c][l]<28):
            severe_yp += 1
            
        else:
            extreme_yp += 1
    
  
        ############## for no depression ############# 
    for ys in range(len(No_psycho_DASS_score)):
    
        if (No_psycho_DASS_score[ys][l]>=0 and No_psycho_DASS_score[ys][l]<10):
            normal_np += 1
            
        elif (No_psycho_DASS_score[ys][l]>=10 and No_psycho_DASS_score[ys][l]<14):
            mild_np += 1
            
        elif (No_psycho_DASS_score[ys][l]>=14 and No_psycho_DASS_score[ys][l]<21):
            moderate_np += 1
            
        elif (No_psycho_DASS_score[ys][l]>=21 and No_psycho_DASS_score[ys][l]<28):
            severe_np += 1
            
        else:
            extreme_np += 1
        
    for y in range(len(Maybe_psycho_DASS_score)):

        if (Maybe_psycho_DASS_score[y][l]>=0 and Maybe_psycho_DASS_score[y][l]<10):
            normal_mp += 1
            
        elif (Maybe_psycho_DASS_score[y][l]>=10 and Maybe_psycho_DASS_score[y][l]<14):
            mild_mp += 1
            
        elif (Maybe_psycho_DASS_score[y][l]>=14 and Maybe_psycho_DASS_score[y][l]<21):
            moderate_mp += 1
            
        elif (Maybe_psycho_DASS_score[y][l]>=21 and Maybe_psycho_DASS_score[y][l]<28):
            severe_mp += 1
            
        else:
            extreme_mp += 1
            
            
    temp_2 = [[normal_yp, mild_yp, moderate_yp, severe_yp, extreme_yp],
            [normal_np, mild_np, moderate_np, severe_np, extreme_np],
            [normal_mp, mild_mp, moderate_mp, severe_mp, extreme_mp]]
            
       
    psycho_depression_count[l] = temp_2[0]  
    psycho_depression_count[l+2] = temp_2[1] 
    psycho_depression_count[l+4] = temp_2[2]  
    

################ Es filtration for affect psycholodically #######################


psycho_depression_count_es_filter = np.copy(psycho_depression_count)


for row in range (0,6,2):
    
    psycho_depression_count_es_filter[row][4] = abs(psycho_depression_count_es_filter[row][4] - psycho_depression_count_es_filter[row][4])
    psycho_depression_count_es_filter[row+1][4] = abs(psycho_depression_count_es_filter[row+1][4] - psycho_depression_count[row][4])

#####################################################################
    
    
################## Psychological effect with health system #############       
health_sys = []
health_sys = survey_data['Confidence on health services']
h_per_50,h_per_25,h_per_0,h_per_75,h_per_100 = survey_data['Confidence on health services'].value_counts()

h_per_75_DASS_score = np.zeros((h_per_75,6),dtype = np.double)
h_per_100_DASS_score = np.zeros((h_per_100,6),dtype = np.double)
h_per_50_DASS_score = np.zeros((h_per_50,6),dtype = np.double)
h_per_25_DASS_score = np.zeros((h_per_25,6),dtype = np.double)
h_per_0_DASS_score = np.zeros((h_per_0,6),dtype = np.double)

val_0h_ = 0
val_25h_ = 0
val_50h_ = 0
val_75h_ = 0
val_100h_ = 0

for health_value in range (len(survey_data)):
    if health_sys[health_value] == 1:
        for i in range(6):   
            h_per_0_DASS_score[val_0h_][i] = DASS_score[health_value][i]
        val_0h_ += 1

    elif health_sys[health_value] == 2:
        for j in range(6):       
            h_per_25_DASS_score[val_25h_][j] = DASS_score[health_value][j]
        val_25h_ += 1

    elif health_sys[health_value] == 3:
        for j in range(6):       
            h_per_50_DASS_score[val_50h_][j] = DASS_score[health_value][j]
        val_50h_ += 1

    elif health_sys[health_value] == 4:
        for j in range(6):       
            h_per_75_DASS_score[val_75h_][j] = DASS_score[health_value][j]
        val_75h_ += 1

    elif health_sys[health_value] == 5:
        for j in range(6):       
            h_per_100_DASS_score[val_100h_][j] = DASS_score[health_value][j]
        val_100h_ += 1


########################### health system depression count ###########

health_sys_depression_count = np.zeros((10,5),dtype = np.double)


for l in range (2):
    normal_0h = 0
    mild_0h = 0
    moderate_0h = 0
    severe_0h = 0
    extreme_0h = 0
    
    normal_25h = 0
    mild_25h = 0
    moderate_25h = 0
    severe_25h = 0
    extreme_25h = 0
    
    normal_50h = 0
    mild_50h = 0
    moderate_50h = 0
    severe_50h = 0
    extreme_50h = 0
    
    normal_75h = 0
    mild_75h = 0
    moderate_75h = 0
    severe_75h = 0
    extreme_75h = 0
    
    normal_100h = 0
    mild_100h = 0
    moderate_100h = 0
    severe_100h = 0
    extreme_100h = 0
    
    
    for c in range(len(h_per_0_DASS_score)):
       
        ############## for 0% depression ############# 

        if (h_per_0_DASS_score[c][l]>=0 and h_per_0_DASS_score[c][l]<10):
            normal_0h += 1
            
        elif (h_per_0_DASS_score[c][l]>=10 and h_per_0_DASS_score[c][l]<14):
            mild_0h += 1
            
        elif (h_per_0_DASS_score[c][l]>=14 and h_per_0_DASS_score[c][l]<21):
            moderate_0h += 1
            
        elif (h_per_0_DASS_score[c][l]>=21 and h_per_0_DASS_score[c][l]<28):
            severe_0h += 1
            
        else:
            extreme_0h += 1
        
        ############## for 25% depression ############# 
    for ys in range(len(h_per_25_DASS_score)):
    
        if (h_per_25_DASS_score[ys][l]>=0 and h_per_25_DASS_score[ys][l]<10):
            normal_25h += 1
            
        elif (h_per_25_DASS_score[ys][l]>=10 and h_per_25_DASS_score[ys][l]<14):
            mild_25h += 1
            
        elif (h_per_25_DASS_score[ys][l]>=14 and h_per_25_DASS_score[ys][l]<21):
           moderate_25h += 1
            
        elif (h_per_25_DASS_score[ys][l]>=21 and h_per_25_DASS_score[ys][l]<28):
            severe_25h += 1
            
        else:
            extreme_25h += 1
            
        ############## for 50% depression ############# 
    for y in range(len(h_per_50_DASS_score)):

        if (h_per_50_DASS_score[y][l]>=0 and h_per_50_DASS_score[y][l]<10):
            normal_50h += 1
            
        elif (h_per_50_DASS_score[y][l]>=10 and h_per_50_DASS_score[y][l]<14):
            mild_50h += 1
            
        elif (h_per_50_DASS_score[y][l]>=14 and h_per_50_DASS_score[y][l]<21):
            moderate_50h += 1
            
        elif (h_per_50_DASS_score[y][l]>=21 and h_per_50_DASS_score[y][l]<28):
            severe_50h += 1
            
        else:
            extreme_50h += 1
            
        ############## for 75% depression ############# 
    for ea in range(len(h_per_75_DASS_score)):

        if (h_per_75_DASS_score[ea][l]>=0 and h_per_75_DASS_score[ea][l]<10):
            normal_75h += 1
            
        elif (h_per_75_DASS_score[ea][l]>=10 and h_per_75_DASS_score[ea][l]<14):
            mild_75h += 1
            
        elif (h_per_75_DASS_score[ea][l]>=14 and h_per_75_DASS_score[ea][l]<21):
            moderate_75h += 1
            
        elif (h_per_75_DASS_score[ea][l]>=21 and h_per_75_DASS_score[ea][l]<28):
            severe_75h += 1
            
        else:
            extreme_75h += 1
            
        ############## for 100% depression ############# 
    for ma in range(len(h_per_100_DASS_score)):

        if (h_per_100_DASS_score[ma][l]>=0 and h_per_100_DASS_score[ma][l]<10):
            normal_100h += 1
            
        elif (h_per_100_DASS_score[ma][l]>=10 and h_per_100_DASS_score[ma][l]<14):
            mild_100h += 1
            
        elif (h_per_100_DASS_score[ma][l]>=14 and h_per_100_DASS_score[ma][l]<21):
            moderate_100h += 1
            
        elif (h_per_100_DASS_score[ma][l]>=21 and h_per_100_DASS_score[ma][l]<28):
            severe_100h += 1
            
        else:
            extreme_100h += 1
            
      
            
    temp_3 = [[normal_0h, mild_0h, moderate_0h, severe_0h, extreme_0h],
            [normal_25h, mild_25h, moderate_25h, severe_25h, extreme_25h],
            [normal_50h, mild_50h, moderate_50h, severe_50h, extreme_50h],
            [normal_75h, mild_75h, moderate_75h, severe_75h, extreme_75h],
            [normal_100h, mild_100h, moderate_100h, severe_100h, extreme_100h]]        
            
    health_sys_depression_count[l] = temp_3[0]  
    health_sys_depression_count[l+2] = temp_3[1]  
    health_sys_depression_count[l+4] = temp_3[2]     
    health_sys_depression_count[l+6] = temp_3[3]        
    health_sys_depression_count[l+8] = temp_3[4]        
     

################ Es filtration for ahealth system #######################


health_sys_depression_count_es_filter = np.copy(health_sys_depression_count)


for row in range (0,10,2):
    
    health_sys_depression_count_es_filter[row][4] = abs(health_sys_depression_count_es_filter[row][4] - health_sys_depression_count_es_filter[row][4])
    health_sys_depression_count_es_filter[row+1][4] = abs(health_sys_depression_count_es_filter[row+1][4] - health_sys_depression_count[row][4])

#####################################################################




################### Psychological effect with cases and deaths ###############
cases_deaths = []
cases_deaths = survey_data['New cases and deaths']
cd_Worried,cd_Upset,cd_Depressed,cd_Fear,cd_Anxious,cd_None = survey_data['New cases and deaths'].value_counts()


cd_Worried_DASS_score = np.zeros((cd_Worried,6),dtype = np.double)
cd_Upset_DASS_score = np.zeros((cd_Upset,6),dtype = np.double)
cd_Depressed_DASS_score = np.zeros((cd_Depressed,6),dtype = np.double)
cd_Fear_DASS_score = np.zeros((cd_Fear,6),dtype = np.double)
cd_Anxious_DASS_score = np.zeros((cd_Anxious,6),dtype = np.double)
cd_None_DASS_score = np.zeros((cd_None,6),dtype = np.double)


val_cdw = 0
val_cdu = 0
val_cdd = 0
val_cdf = 0
val_cda = 0
val_cdn = 0
for cd_value in range (len(survey_data)):
    if cases_deaths[cd_value] == 'Worried':
        for i in range(6):   
            cd_Worried_DASS_score[val_cdw][i] = DASS_score[cd_value][i]
        val_cdw += 1
        
    elif cases_deaths[cd_value] == 'Upset':
        for j in range(6):       
            cd_Upset_DASS_score[val_cdu][j] = DASS_score[cd_value][j]
        val_cdu += 1
        
    elif cases_deaths[cd_value] == 'Depressed':
        for i in range(6):   
            cd_Depressed_DASS_score[val_cdd][i] = DASS_score[cd_value][i]
        val_cdd += 1
        
    elif cases_deaths[cd_value] == 'Fear':
        for i in range(6):   
            cd_Fear_DASS_score[val_cdf][i] = DASS_score[cd_value][i]
        val_cdf += 1
        
    elif cases_deaths[cd_value] == 'Anxious':
        for i in range(6):   
            cd_Anxious_DASS_score[val_cda][i] = DASS_score[cd_value][i]
        val_cda += 1
        
    elif cases_deaths[cd_value] == 'None':
        for i in range(6):   
            cd_None_DASS_score[val_cdn][i] = DASS_score[cd_value][i]
        val_cdn += 1


############# cases and deaths depression count ##############

cases_deaths_depression_count = np.zeros((12,5),dtype = np.double)


for l in range (2):
    normal_cdw = 0
    mild_cdw = 0
    moderate_cdw = 0
    severe_cdw = 0
    extreme_cdw = 0
    
    normal_cdu = 0
    mild_cdu = 0
    moderate_cdu = 0
    severe_cdu = 0
    extreme_cdu = 0
    
    normal_cdd = 0
    mild_cdd = 0
    moderate_cdd = 0
    severe_cdd = 0
    extreme_cdd = 0
    
    normal_cdf = 0
    mild_cdf = 0
    moderate_cdf = 0
    severe_cdf = 0
    extreme_cdf = 0
    
    normal_cda = 0
    mild_cda = 0
    moderate_cda = 0
    severe_cda = 0
    extreme_cda = 0
    
    normal_cdn = 0
    mild_cdn = 0
    moderate_cdn = 0
    severe_cdn = 0
    extreme_cdn = 0
    
    for c in range(len(cd_Worried_DASS_score)):
       
        ############## for less than 15 depression ############# 

        if (cd_Worried_DASS_score[c][l]>=0 and cd_Worried_DASS_score[c][l]<10):
            normal_cdw += 1
            
        elif (cd_Worried_DASS_score[c][l]>=10 and cd_Worried_DASS_score[c][l]<14):
            mild_cdw += 1
            
        elif (cd_Worried_DASS_score[c][l]>=14 and cd_Worried_DASS_score[c][l]<21):
            moderate_cdw += 1
            
        elif (cd_Worried_DASS_score[c][l]>=21 and cd_Worried_DASS_score[c][l]<28):
            severe_cdw += 1
            
        else:
            extreme_cdw += 1
        
        ############## for 15-18 depression ############# 
    for ys in range(len(cd_Upset_DASS_score)):
    
        if (cd_Upset_DASS_score[ys][l]>=0 and cd_Upset_DASS_score[ys][l]<10):
            normal_cdu += 1
            
        elif (cd_Upset_DASS_score[ys][l]>=10 and cd_Upset_DASS_score[ys][l]<14):
            mild_cdu += 1
            
        elif (cd_Upset_DASS_score[ys][l]>=14 and cd_Upset_DASS_score[ys][l]<21):
            moderate_cdu += 1
            
        elif (cd_Upset_DASS_score[ys][l]>=21 and cd_Upset_DASS_score[ys][l]<28):
            severe_cdu += 1
            
        else:
            extreme_cdu += 1
            
        ############## for 19-26 depression ############# 
    for y in range(len(cd_Depressed_DASS_score)):

        if (cd_Depressed_DASS_score[y][l]>=0 and cd_Depressed_DASS_score[y][l]<10):
            normal_cdd += 1
            
        elif (cd_Depressed_DASS_score[y][l]>=10 and cd_Depressed_DASS_score[y][l]<14):
            mild_cdd += 1
            
        elif (cd_Depressed_DASS_score[y][l]>=14 and cd_Depressed_DASS_score[y][l]<21):
            moderate_cdd += 1
            
        elif (cd_Depressed_DASS_score[y][l]>=21 and cd_Depressed_DASS_score[y][l]<28):
            severe_cdd += 1
            
        else:
            extreme_cdd += 1
            
        ############## for 27-40 depression ############# 
    for ea in range(len(cd_Fear_DASS_score)):

        if (cd_Fear_DASS_score[ea][l]>=0 and cd_Fear_DASS_score[ea][l]<10):
            normal_cdf += 1
            
        elif (cd_Fear_DASS_score[ea][l]>=10 and cd_Fear_DASS_score[ea][l]<14):
            mild_cdf += 1
            
        elif (cd_Fear_DASS_score[ea][l]>=14 and cd_Fear_DASS_score[ea][l]<21):
            moderate_cdf += 1
            
        elif (cd_Fear_DASS_score[ea][l]>=21 and cd_Fear_DASS_score[ea][l]<28):
            severe_cdf += 1
            
        else:
            extreme_cdf += 1
            
        ############## for 41-60 depression ############# 
    for ma in range(len(cd_Anxious_DASS_score)):

        if (cd_Anxious_DASS_score[ma][l]>=0 and cd_Anxious_DASS_score[ma][l]<10):
            normal_cda += 1
            
        elif (cd_Anxious_DASS_score[ma][l]>=10 and cd_Anxious_DASS_score[ma][l]<14):
            mild_cda += 1
            
        elif (cd_Anxious_DASS_score[ma][l]>=14 and cd_Anxious_DASS_score[ma][l]<21):
            moderate_cda += 1
            
        elif (cd_Anxious_DASS_score[ma][l]>=21 and cd_Anxious_DASS_score[ma][l]<28):
            severe_cda += 1
            
        else:
            extreme_cda += 1
            
            
        ############## for 60+ depression ############# 
    for o in range(len(cd_None_DASS_score)):

        if (cd_None_DASS_score[o][l]>=0 and cd_None_DASS_score[o][l]<10):
            normal_cdn += 1
            
        elif (cd_None_DASS_score[o][l]>=10 and cd_None_DASS_score[o][l]<14):
            mild_cdn += 1
            
        elif (cd_None_DASS_score[o][l]>=14 and cd_None_DASS_score[o][l]<21):
            moderate_cdn += 1
            
        elif (cd_None_DASS_score[o][l]>=21 and cd_None_DASS_score[o][l]<28):
            severe_cdn += 1
            
        else:
            extreme_cdn += 1
            
            
    temp_4 = [[normal_cdw, mild_cdw, moderate_cdw, severe_cdw, extreme_cdw],
            [normal_cdu, mild_cdu, moderate_cdu, severe_cdu, extreme_cdu],
            [normal_cdd, mild_cdd, moderate_cdd, severe_cdd, extreme_cdd],
            [normal_cdf, mild_cdf, moderate_cdf, severe_cdf, extreme_cdf],
            [normal_cda, mild_cda, moderate_cda, severe_cda, extreme_cda],
            [normal_cdn, mild_cdn, moderate_cdn, severe_cdn, extreme_cdn],]        
            
    cases_deaths_depression_count[l] = temp_4[0]  
    cases_deaths_depression_count[l+2] = temp_4[1]  
    cases_deaths_depression_count[l+4] = temp_4[2]     
    cases_deaths_depression_count[l+6] = temp_4[3]        
    cases_deaths_depression_count[l+8] = temp_4[4]        
    cases_deaths_depression_count[l+10] = temp_4[5]        

################ Es filtration for new cases and deaths #######################


cases_deaths_depression_count_es_filter = np.copy(cases_deaths_depression_count)


for row in range (0,12,2):
    
    cases_deaths_depression_count_es_filter[row][4] = abs(cases_deaths_depression_count_es_filter[row][4] - cases_deaths_depression_count_es_filter[row][4])
    cases_deaths_depression_count_es_filter[row+1][4] = abs(cases_deaths_depression_count_es_filter[row+1][4] - cases_deaths_depression_count[row][4])



#####################################################################

##################### Pychological effect with social media ####################
    

media = []
media = survey_data['Time on social media']
Lessthananhour,hours1_3,hours4_6,Morethan6hours= survey_data['Time on social media'].value_counts()



Lessthananhour_DASS_score = np.zeros((Lessthananhour,6),dtype = np.double)
hours1_3_DASS_score = np.zeros((hours1_3,6),dtype = np.double)
hours4_6_DASS_score = np.zeros((hours4_6,6),dtype = np.double)
Morethan6hours_DASS_score = np.zeros((Morethan6hours,6),dtype = np.double)



val_lt = 0
val_1 = 0
val_4 = 0
val_6p = 0

for media_value in range (len(survey_data)):
    if media[media_value] == 'Lessthananhour':
        for i in range(6):   
            Lessthananhour_DASS_score[val_lt][i] = DASS_score[media_value][i]
        val_lt += 1
        
    elif media[media_value] == '1hours3hours':
        for j in range(6):       
            hours1_3_DASS_score[val_1][j] = DASS_score[media_value][j]
        val_1 += 1
        
    elif media[media_value] == '4hours6hours':
        for i in range(6):   
            hours4_6_DASS_score[val_4][i] = DASS_score[media_value][i]
        val_4 += 1
        
    elif media[media_value] == 'Morethan6hours':
        for i in range(6):   
            Morethan6hours_DASS_score[val_6p][i] = DASS_score[media_value][i]
        val_6p += 1
   
################### for media depression count ########
media_depression_count = np.zeros((8,5),dtype = np.double)


for l in range (2):
    normal_lt = 0
    mild_lt = 0
    moderate_lt = 0
    severe_lt = 0
    extreme_lt = 0
    
    normal_1 = 0
    mild_1 = 0
    moderate_1 = 0
    severe_1 = 0
    extreme_1 = 0
    
    normal_4 = 0
    mild_4 = 0
    moderate_4 = 0
    severe_4 = 0
    extreme_4 = 0
    
    normal_6p = 0
    mild_6p = 0
    moderate_6p = 0
    severe_6p = 0
    extreme_6p = 0
    
    for c in range(len(Lessthananhour_DASS_score)):
       
        ############## for less than 1 hr depression ############# 

        if (Lessthananhour_DASS_score[c][l]>=0 and Lessthananhour_DASS_score[c][l]<10):
            normal_lt += 1
            
        elif (Lessthananhour_DASS_score[c][l]>=10 and Lessthananhour_DASS_score[c][l]<14):
            mild_lt += 1
            
        elif (Lessthananhour_DASS_score[c][l]>=14 and Lessthananhour_DASS_score[c][l]<21):
            moderate_lt += 1
            
        elif (Lessthananhour_DASS_score[c][l]>=21 and Lessthananhour_DASS_score[c][l]<28):
            severe_lt += 1
            
        else:
            extreme_lt += 1
        
        ############## for 1hrs - 3 hrs depression ############# 
    for ys in range(len(hours1_3_DASS_score)):
    
        if (hours1_3_DASS_score[ys][l]>=0 and hours1_3_DASS_score[ys][l]<10):
            normal_1 += 1
            
        elif (hours1_3_DASS_score[ys][l]>=10 and hours1_3_DASS_score[ys][l]<14):
            mild_1 += 1
            
        elif (hours1_3_DASS_score[ys][l]>=14 and hours1_3_DASS_score[ys][l]<21):
            moderate_1 += 1
            
        elif (hours1_3_DASS_score[ys][l]>=21 and hours1_3_DASS_score[ys][l]<28):
            severe_1 += 1
            
        else:
            extreme_1 += 1
            
        ############## for 4hrs - 6hrs depression ############# 
    for y in range(len(hours4_6_DASS_score)):

        if (hours4_6_DASS_score[y][l]>=0 and hours4_6_DASS_score[y][l]<10):
            normal_4 += 1
            
        elif (hours4_6_DASS_score[y][l]>=10 and hours4_6_DASS_score[y][l]<14):
            mild_4 += 1
            
        elif (hours4_6_DASS_score[y][l]>=14 and hours4_6_DASS_score[y][l]<21):
            moderate_4 += 1
            
        elif (hours4_6_DASS_score[y][l]>=21 and hours4_6_DASS_score[y][l]<28):
            severe_4 += 1
            
        else:
            extreme_4 += 1
            
        ############## for 6 hrs + depression ############# 
    for ea in range(len(Morethan6hours_DASS_score)):

        if (Morethan6hours_DASS_score[ea][l]>=0 and Morethan6hours_DASS_score[ea][l]<10):
            normal_6p += 1
            
        elif (Morethan6hours_DASS_score[ea][l]>=10 and Morethan6hours_DASS_score[ea][l]<14):
            mild_6p += 1
            
        elif (Morethan6hours_DASS_score[ea][l]>=14 and Morethan6hours_DASS_score[ea][l]<21):
            moderate_6p += 1
            
        elif (Morethan6hours_DASS_score[ea][l]>=21 and Morethan6hours_DASS_score[ea][l]<28):
            severe_6p += 1
            
        else:
            extreme_6p += 1
        
            
    temp_5 = [[normal_lt, mild_lt, moderate_lt, severe_lt, extreme_lt],
              [normal_1, mild_1, moderate_1, severe_1, extreme_1],
              [normal_4, mild_4, moderate_4, severe_4, extreme_4],
              [normal_6p, mild_6p, moderate_6p, severe_6p, extreme_6p]]        
            
    media_depression_count[l] = temp_5[0]  
    media_depression_count[l+2] = temp_5[1]  
    media_depression_count[l+4] = temp_5[2]     
    media_depression_count[l+6] = temp_5[3]        
  
#####################################################################

################ Es filtration for media  #######################


media_depression_count_es_filter = np.copy(media_depression_count)


for row in range (0,8,2):
    
    media_depression_count_es_filter[row][4] = abs(media_depression_count_es_filter[row][4] - media_depression_count_es_filter[row][4])
    media_depression_count_es_filter[row+1][4] = abs(media_depression_count_es_filter[row+1][4] - media_depression_count[row][4])

######################################################################    

##################### for indoor activities #####################

indoor = []
indoor = survey_data['Indoor activities']
Yes_ind, Sometimes_ind, No_ind= survey_data['Indoor activities'].value_counts()

Yes_ind_DASS_score = np.zeros((Yes_ind,6),dtype = np.double)
No_ind_DASS_score = np.zeros((No_ind,6),dtype = np.double)
Sometimes_ind_DASS_score = np.zeros((Sometimes_ind,6),dtype = np.double)


val_yi = 0
val_ni = 0
val_si = 0


for indoor_value in range (len(survey_data)):
    if indoor[indoor_value] == 'Yes':
        for i in range(6):   
            Yes_ind_DASS_score[val_yi][i] = DASS_score[indoor_value][i]
        val_yi += 1
    elif indoor[indoor_value] == 'No':
        for j in range(6):       
            No_ind_DASS_score[val_ni][j] = DASS_score[indoor_value][j]
        val_ni += 1
    elif indoor[indoor_value] == 'Sometimes':
        for j in range(6):       
            Sometimes_ind_DASS_score[val_si][j] = DASS_score[indoor_value][j]
        val_si += 1


indoor_depression_count = np.zeros((6,5),dtype = np.double)


for l in range (2):
    normal_yi = 0
    mild_yi = 0
    moderate_yi = 0
    severe_yi = 0
    extreme_yi = 0
    
    normal_ni = 0
    mild_ni = 0
    moderate_ni = 0
    severe_ni = 0
    extreme_ni = 0
    
    normal_si = 0
    mild_si = 0
    moderate_si = 0
    severe_si = 0
    extreme_si = 0
  
    for c in range(len(Yes_ind_DASS_score)):
        ############## for yes depression ############# 

        if (Yes_ind_DASS_score[c][l]>=0 and Yes_ind_DASS_score[c][l]<10):
            normal_yi += 1
            
        elif (Yes_ind_DASS_score[c][l]>=10 and Yes_ind_DASS_score[c][l]<14):
            mild_yi += 1
            
        elif (Yes_ind_DASS_score[c][l]>=14 and Yes_ind_DASS_score[c][l]<21):
            moderate_yi += 1
            
        elif (Yes_ind_DASS_score[c][l]>=21 and Yes_ind_DASS_score[c][l]<28):
            severe_yi += 1
            
        else:
            extreme_yi += 1
    
  
        ############## for no depression ############# 
    for ys in range(len(No_ind_DASS_score)):
    
        if (No_ind_DASS_score[ys][l]>=0 and No_ind_DASS_score[ys][l]<10):
            normal_ni += 1
            
        elif (No_ind_DASS_score[ys][l]>=10 and No_ind_DASS_score[ys][l]<14):
            mild_ni += 1
            
        elif (No_ind_DASS_score[ys][l]>=14 and No_ind_DASS_score[ys][l]<21):
            moderate_ni += 1
            
        elif (No_ind_DASS_score[ys][l]>=21 and No_ind_DASS_score[ys][l]<28):
            severe_ni += 1
            
        else:
            extreme_ni += 1
        ############## for sometimes depression ############# 
        
    for y in range(len(Sometimes_ind_DASS_score)):

        if (Sometimes_ind_DASS_score[y][l]>=0 and Sometimes_ind_DASS_score[y][l]<10):
            normal_si += 1
            
        elif (Sometimes_ind_DASS_score[y][l]>=10 and Sometimes_ind_DASS_score[y][l]<14):
            mild_si += 1
            
        elif (Sometimes_ind_DASS_score[y][l]>=14 and Sometimes_ind_DASS_score[y][l]<21):
            moderate_si += 1
            
        elif (Sometimes_ind_DASS_score[y][l]>=21 and Sometimes_ind_DASS_score[y][l]<28):
            severe_si += 1
            
        else:
            extreme_si += 1
            
            
    temp_6 = [[normal_yi, mild_yi, moderate_yi, severe_yi, extreme_yi],
            [normal_ni, mild_ni, moderate_ni, severe_ni, extreme_ni],
            [normal_si, mild_si, moderate_si, severe_si, extreme_si]]
            
       
    indoor_depression_count[l] = temp_6[0]  
    indoor_depression_count[l+2] = temp_6[1] 
    indoor_depression_count[l+4] = temp_6[2]  
    

################ Es filtration for indoor #######################


indoor_depression_count_es_filter = np.copy(indoor_depression_count)


for row in range (0,6,2):
    
    indoor_depression_count_es_filter[row][4] = abs(indoor_depression_count_es_filter[row][4] - indoor_depression_count_es_filter[row][4])
    indoor_depression_count_es_filter[row+1][4] = abs(indoor_depression_count_es_filter[row+1][4] - indoor_depression_count[row][4])

#####################################################################
 

##################### for survival chances #####################

survival = []
survival = survey_data['Survaival chances']
well_soon, not_sure, die = survey_data['Survaival chances'].value_counts()

well_soon_DASS_score = np.zeros((well_soon,6),dtype = np.double)
not_sure_DASS_score = np.zeros((not_sure,6),dtype = np.double)
die_DASS_score = np.zeros((die,6),dtype = np.double)


val_ws = 0
val_ns = 0
val_d = 0


for survival_value in range (len(survey_data)):
    if survival[survival_value] == 'Iwillgetwellsoon':
        for i in range(6):   
            well_soon_DASS_score[val_ws][i] = DASS_score[survival_value][i]
        val_ws += 1
    elif survival[survival_value] == 'Notsure':
        for j in range(6):       
            not_sure_DASS_score[val_ns][j] = DASS_score[survival_value][j]
        val_ns += 1
    elif survival[survival_value] == 'Iwillnotsurvive':
        for j in range(6):       
            die_DASS_score[val_d][j] = DASS_score[survival_value][j]
        val_d += 1


survival_depression_count = np.zeros((6,5),dtype = np.double)


for l in range (2):
    normal_ws = 0
    mild_ws = 0
    moderate_ws = 0
    severe_ws = 0
    extreme_ws = 0
    
    normal_ns = 0
    mild_ns = 0
    moderate_ns = 0
    severe_ns = 0
    extreme_ns = 0
    
    normal_d = 0
    mild_d = 0
    moderate_d = 0
    severe_d = 0
    extreme_d = 0
  
    for c in range(len(well_soon_DASS_score)):
        ############## for get well soon depression ############# 

        if (well_soon_DASS_score[c][l]>=0 and well_soon_DASS_score[c][l]<10):
            normal_ws += 1
            
        elif (well_soon_DASS_score[c][l]>=10 and well_soon_DASS_score[c][l]<14):
            mild_ws += 1
            
        elif (well_soon_DASS_score[c][l]>=14 and well_soon_DASS_score[c][l]<21):
            moderate_ws += 1
            
        elif (well_soon_DASS_score[c][l]>=21 and well_soon_DASS_score[c][l]<28):
            severe_ws += 1
            
        else:
            extreme_ws += 1
    
  
        ############## for not sure depression ############# 
    for ys in range(len(not_sure_DASS_score)):
    
        if (not_sure_DASS_score[ys][l]>=0 and not_sure_DASS_score[ys][l]<10):
            normal_ns += 1
            
        elif (not_sure_DASS_score[ys][l]>=10 and not_sure_DASS_score[ys][l]<14):
            mild_ns += 1
            
        elif (not_sure_DASS_score[ys][l]>=14 and not_sure_DASS_score[ys][l]<21):
            moderate_ns += 1
            
        elif (not_sure_DASS_score[ys][l]>=21 and not_sure_DASS_score[ys][l]<28):
            severe_ns += 1
            
        else:
            extreme_ns += 1
        ############## for die depression ############# 
        
    for y in range(len(die_DASS_score)):

        if (die_DASS_score[y][l]>=0 and die_DASS_score[y][l]<10):
            normal_d += 1
            
        elif (die_DASS_score[y][l]>=10 and die_DASS_score[y][l]<14):
            mild_d += 1
            
        elif (die_DASS_score[y][l]>=14 and die_DASS_score[y][l]<21):
            moderate_d += 1
            
        elif (die_DASS_score[y][l]>=21 and die_DASS_score[y][l]<28):
            severe_d += 1
            
        else:
            extreme_d += 1
            
            
    temp_7 = [[normal_ws, mild_ws, moderate_ws, severe_ws, extreme_ws],
            [normal_ns, mild_ns, moderate_ns, severe_ns, extreme_ns],
            [normal_d, mild_d, moderate_d, severe_d, extreme_d]]
            
       
    survival_depression_count[l] = temp_7[0]  
    survival_depression_count[l+2] = temp_7[1] 
    survival_depression_count[l+4] = temp_7[2]  
    

################ Es filtration for survival #######################


survival_depression_count_es_filter = np.copy(survival_depression_count)


for row in range (0,6,2):
    
    survival_depression_count_es_filter[row][4] = abs(survival_depression_count_es_filter[row][4] - survival_depression_count_es_filter[row][4])
    survival_depression_count_es_filter[row+1][4] = abs(survival_depression_count_es_filter[row+1][4] - survival_depression_count[row][4])

#####################################################################
    


################### Psychological effect with lockdown ###############
lockdown = []
lockdown = survey_data['Effect of lockdown']
ld_Depressed, ld_None, ld_Anxious, ld_Worried, ld_Upset, ld_Fear = survey_data['Effect of lockdown'].value_counts()


ld_Worried_DASS_score = np.zeros((ld_Worried,6),dtype = np.double)
ld_Upset_DASS_score = np.zeros((ld_Upset,6),dtype = np.double)
ld_Depressed_DASS_score = np.zeros((ld_Depressed,6),dtype = np.double)
ld_Fear_DASS_score = np.zeros((ld_Fear,6),dtype = np.double)
ld_Anxious_DASS_score = np.zeros((ld_Anxious,6),dtype = np.double)
ld_None_DASS_score = np.zeros((ld_None,6),dtype = np.double)


val_ldw = 0
val_ldu = 0
val_ldd = 0
val_ldf = 0
val_lda = 0
val_ldn = 0
for ld_value in range (len(survey_data)):
    if lockdown[ld_value] == 'Worried':
        for i in range(6):   
            ld_Worried_DASS_score[val_ldw][i] = DASS_score[ld_value][i]
        val_ldw += 1
        
    elif lockdown[ld_value] == 'Upset':
        for j in range(6):       
            ld_Upset_DASS_score[val_ldu][j] = DASS_score[ld_value][j]
        val_ldu += 1
        
    elif lockdown[ld_value] == 'Depressed':
        for i in range(6):   
            ld_Depressed_DASS_score[val_ldd][i] = DASS_score[ld_value][i]
        val_ldd += 1
        
    elif lockdown[ld_value] == 'Fear':
        for i in range(6):   
            ld_Fear_DASS_score[val_ldf][i] = DASS_score[ld_value][i]
        val_ldf += 1
        
    elif lockdown[ld_value] == 'Anxious':
        for i in range(6):   
            ld_Anxious_DASS_score[val_lda][i] = DASS_score[ld_value][i]
        val_lda += 1
        
    elif lockdown[ld_value] == 'Noeffect':
        for i in range(6):   
            ld_None_DASS_score[val_ldn][i] = DASS_score[ld_value][i]
        val_ldn += 1


############# lockdown depression count ##############

lockdown_depression_count = np.zeros((12,5),dtype = np.double)


for l in range (2):
    normal_ldw = 0
    mild_ldw = 0
    moderate_ldw = 0
    severe_ldw = 0
    extreme_ldw = 0
    
    normal_ldu = 0
    mild_ldu = 0
    moderate_ldu = 0
    severe_ldu = 0
    extreme_ldu = 0
    
    normal_ldd = 0
    mild_ldd = 0
    moderate_ldd = 0
    severe_ldd = 0
    extreme_ldd = 0
    
    normal_ldf = 0
    mild_ldf = 0
    moderate_ldf = 0
    severe_ldf = 0
    extreme_ldf = 0
    
    normal_lda = 0
    mild_lda = 0
    moderate_lda = 0
    severe_lda = 0
    extreme_lda = 0
    
    normal_ldn = 0
    mild_ldn = 0
    moderate_ldn = 0
    severe_ldn = 0
    extreme_ldn = 0
    
    for c in range(len(ld_Worried_DASS_score)):
       
        ############## for worried depression ############# 

        if (ld_Worried_DASS_score[c][l]>=0 and ld_Worried_DASS_score[c][l]<10):
            normal_ldw += 1
            
        elif (ld_Worried_DASS_score[c][l]>=10 and ld_Worried_DASS_score[c][l]<14):
            mild_ldw += 1
            
        elif (ld_Worried_DASS_score[c][l]>=14 and ld_Worried_DASS_score[c][l]<21):
            moderate_ldw += 1
            
        elif (ld_Worried_DASS_score[c][l]>=21 and ld_Worried_DASS_score[c][l]<28):
            severe_ldw += 1
            
        else:
            extreme_ldw += 1
        
        ############## for upset depression ############# 
    for ys in range(len(ld_Upset_DASS_score)):
    
        if (ld_Upset_DASS_score[ys][l]>=0 and ld_Upset_DASS_score[ys][l]<10):
            normal_ldu += 1
            
        elif (ld_Upset_DASS_score[ys][l]>=10 and ld_Upset_DASS_score[ys][l]<14):
            mild_ldu += 1
            
        elif (ld_Upset_DASS_score[ys][l]>=14 and ld_Upset_DASS_score[ys][l]<21):
            moderate_ldu += 1
            
        elif (ld_Upset_DASS_score[ys][l]>=21 and ld_Upset_DASS_score[ys][l]<28):
            severe_ldu += 1
            
        else:
            extreme_ldu += 1
            
        ############## for depressed depression ############# 
    for y in range(len(ld_Depressed_DASS_score)):

        if (ld_Depressed_DASS_score[y][l]>=0 and ld_Depressed_DASS_score[y][l]<10):
            normal_ldd += 1
            
        elif (ld_Depressed_DASS_score[y][l]>=10 and ld_Depressed_DASS_score[y][l]<14):
            mild_ldd += 1
            
        elif (ld_Depressed_DASS_score[y][l]>=14 and ld_Depressed_DASS_score[y][l]<21):
            moderate_ldd += 1
            
        elif (ld_Depressed_DASS_score[y][l]>=21 and ld_Depressed_DASS_score[y][l]<28):
            severe_ldd += 1
            
        else:
            extreme_ldd += 1
            
        ############## for fear depression ############# 
    for ea in range(len(ld_Fear_DASS_score)):

        if (ld_Fear_DASS_score[ea][l]>=0 and ld_Fear_DASS_score[ea][l]<10):
            normal_ldf += 1
            
        elif (ld_Fear_DASS_score[ea][l]>=10 and ld_Fear_DASS_score[ea][l]<14):
            mild_ldf += 1
            
        elif (ld_Fear_DASS_score[ea][l]>=14 and ld_Fear_DASS_score[ea][l]<21):
            moderate_ldf += 1
            
        elif (ld_Fear_DASS_score[ea][l]>=21 and ld_Fear_DASS_score[ea][l]<28):
            severe_ldf += 1
            
        else:
            extreme_ldf += 1
            
        ############## for anxious depression ############# 
    for ma in range(len(ld_Anxious_DASS_score)):

        if (ld_Anxious_DASS_score[ma][l]>=0 and ld_Anxious_DASS_score[ma][l]<10):
            normal_lda += 1
            
        elif (ld_Anxious_DASS_score[ma][l]>=10 and ld_Anxious_DASS_score[ma][l]<14):
            mild_lda += 1
            
        elif (ld_Anxious_DASS_score[ma][l]>=14 and ld_Anxious_DASS_score[ma][l]<21):
            moderate_lda += 1
            
        elif (ld_Anxious_DASS_score[ma][l]>=21 and ld_Anxious_DASS_score[ma][l]<28):
            severe_lda += 1
            
        else:
            extreme_lda += 1
            
            
        ############## for no effect depression ############# 
    for o in range(len(ld_None_DASS_score)):

        if (ld_None_DASS_score[o][l]>=0 and ld_None_DASS_score[o][l]<10):
            normal_ldn += 1
            
        elif (ld_None_DASS_score[o][l]>=10 and ld_None_DASS_score[o][l]<14):
            mild_ldn += 1
            
        elif (ld_None_DASS_score[o][l]>=14 and ld_None_DASS_score[o][l]<21):
            moderate_ldn += 1
            
        elif (ld_None_DASS_score[o][l]>=21 and ld_None_DASS_score[o][l]<28):
            severe_ldn += 1
            
        else:
            extreme_ldn += 1
            
            
    temp_8 = [[normal_ldw, mild_ldw, moderate_ldw, severe_ldw, extreme_ldw],
            [normal_ldu, mild_ldu, moderate_ldu, severe_ldu, extreme_ldu],
            [normal_ldd, mild_ldd, moderate_ldd, severe_ldd, extreme_ldd],
            [normal_ldf, mild_ldf, moderate_ldf, severe_ldf, extreme_ldf],
            [normal_lda, mild_lda, moderate_lda, severe_lda, extreme_lda],
            [normal_ldn, mild_ldn, moderate_ldn, severe_ldn, extreme_ldn],]        
            
    lockdown_depression_count[l] = temp_8[0]  
    lockdown_depression_count[l+2] = temp_8[1]  
    lockdown_depression_count[l+4] = temp_8[2]     
    lockdown_depression_count[l+6] = temp_8[3]        
    lockdown_depression_count[l+8] = temp_8[4]        
    lockdown_depression_count[l+10] = temp_8[5]        

################ Es filtration for lockdown #######################


lockdown_depression_count_es_filter = np.copy(lockdown_depression_count)


for row in range (0,12,2):
    
    lockdown_depression_count_es_filter[row][4] = abs(lockdown_depression_count_es_filter[row][4] - lockdown_depression_count_es_filter[row][4])
    lockdown_depression_count_es_filter[row+1][4] = abs(lockdown_depression_count_es_filter[row+1][4] - lockdown_depression_count[row][4])



#####################################################################


import seaborn as sns
import matplotlib.pyplot as plt 



y_labels = ['Yes-Dream','No-Dream', 'Yes-COVID dream','No-COVID dream',
            'Yes-affect mentally', 'No-affect mentally','Maybe-affect mentally',
            '0% confidence','25% confidence','50% confidence','75% confidence',
            '100% confidence','New cases and deaths-Worried','Upset','Depressed','Fear','Anxious',
            'None','Less than an hour','1-3 hours','4-6 hours','More than 6 hours',
            'Yes-indoor activities','No-indoor activities','sometimes-indoor activites',
            'Will get well soon','Not sure','Will not survive','Lockdown-Worried',
            'Upset','Depressed','Fear','Anxious','No effect']
x_labels = ['Normal','Mild','Moderate','Severe','Extremely Severe']

################# for Psychological BC data ###########################
psychology_var_depression_BC = np.zeros((34,5),dtype = np.double)

r = 0
for q in range (0,4,2):
    psychology_var_depression_BC[r] = dream_depression_count[q] # for age group bc
    r += 1

for q in range (0,4,2):
    psychology_var_depression_BC[r] = co_dream_depression_count[q] # for age group bc
    r += 1

for q in range (0,6,2):
    psychology_var_depression_BC[r] = psycho_depression_count[q] #for education bc
    r += 1

for q in range (0,10,2):
    psychology_var_depression_BC[r] = health_sys_depression_count[q]# for marital bc 
    r += 1
    
for q in range (0,12,2):
    psychology_var_depression_BC[r] = cases_deaths_depression_count[q]# for marital bc 
    r += 1
    
for q in range (0,8,2):
    psychology_var_depression_BC[r] = media_depression_count[q]# for marital bc 
    r += 1    

for q in range (0,6,2):
    psychology_var_depression_BC[r] = indoor_depression_count[q]# for marital bc 
    r += 1

for q in range (0,6,2):
    psychology_var_depression_BC[r] = survival_depression_count[q]# for marital bc 
    r += 1

for q in range (0,12,2):
    psychology_var_depression_BC[r] = lockdown_depression_count[q]# for marital bc 
    r += 1
    
f, ax = plt.subplots(figsize=(10, 8))

sns.heatmap(psychology_var_depression_BC, vmin = 0, vmax = 1300, xticklabels=x_labels, yticklabels = y_labels, mask=np.zeros_like(psychology_var_depression_BC, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, ax=ax)


#####################################################################


################# for Psychological DC data ###########################
psychology_var_depression_DC = np.zeros((34,5),dtype = np.double)

r = 0
for q in range (1,4,2):
    psychology_var_depression_DC[r] = dream_depression_count[q] # for age group bc
    r += 1

for q in range (1,4,2):
    psychology_var_depression_DC[r] = co_dream_depression_count[q] # for age group bc
    r += 1

for q in range (1,6,2):
    psychology_var_depression_DC[r] = psycho_depression_count[q] #for education bc
    r += 1

for q in range (1,10,2):
    psychology_var_depression_DC[r] = health_sys_depression_count[q]# for marital bc 
    r += 1
    
for q in range (1,12,2):
    psychology_var_depression_DC[r] = cases_deaths_depression_count[q]# for marital bc 
    r += 1
    
for q in range (1,8,2):
    psychology_var_depression_DC[r] = media_depression_count[q]# for marital bc 
    r += 1    

for q in range (1,6,2):
    psychology_var_depression_DC[r] = indoor_depression_count[q]# for marital bc 
    r += 1

for q in range (1,6,2):
    psychology_var_depression_DC[r] = survival_depression_count[q]# for marital bc 
    r += 1

for q in range (1,12,2):
    psychology_var_depression_DC[r] = lockdown_depression_count[q]# for marital bc 
    r += 1
    
f, ax = plt.subplots(figsize=(10, 8))

sns.heatmap(psychology_var_depression_DC, vmin = 0, vmax = 1300, xticklabels=x_labels, yticklabels = y_labels, mask=np.zeros_like(psychology_var_depression_DC, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, ax=ax)


#####################################################################


import seaborn as sns
import matplotlib.pyplot as plt 


################# for Psychological BC data ES filter ###########################
psychology_var_depression_BC_es_filter = np.zeros((34,5),dtype = np.double)

r = 0
for q in range (0,4,2):
    psychology_var_depression_BC_es_filter[r] = dream_depression_count_es_filter[q] # for age group bc
    r += 1

for q in range (0,4,2):
    psychology_var_depression_BC_es_filter[r] = co_dream_depression_count_es_filter[q] # for age group bc
    r += 1

for q in range (0,6,2):
    psychology_var_depression_BC_es_filter[r] = psycho_depression_count_es_filter[q] #for education bc
    r += 1

for q in range (0,10,2):
    psychology_var_depression_BC_es_filter[r] = health_sys_depression_count_es_filter[q]# for marital bc 
    r += 1
    
for q in range (0,12,2):
    psychology_var_depression_BC_es_filter[r] = cases_deaths_depression_count_es_filter[q]# for marital bc 
    r += 1
    
for q in range (0,8,2):
    psychology_var_depression_BC_es_filter[r] = media_depression_count_es_filter[q]# for marital bc 
    r += 1    

for q in range (0,6,2):
    psychology_var_depression_BC_es_filter[r] = indoor_depression_count_es_filter[q]# for marital bc 
    r += 1

for q in range (0,6,2):
    psychology_var_depression_BC_es_filter[r] = survival_depression_count_es_filter[q]# for marital bc 
    r += 1

for q in range (0,12,2):
    psychology_var_depression_BC_es_filter[r] = lockdown_depression_count_es_filter[q]# for marital bc 
    r += 1
    
f, ax = plt.subplots(figsize=(10, 8))

sns.heatmap(psychology_var_depression_BC_es_filter, vmin = 0, vmax = 1300, xticklabels=x_labels, yticklabels = y_labels, mask=np.zeros_like(psychology_var_depression_BC_es_filter, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, ax=ax)


#####################################################################


################# for Psychological DC data ES filter ###########################
psychology_var_depression_DC_es_filter = np.zeros((34,5),dtype = np.double)

r = 0
for q in range (1,4,2):
    psychology_var_depression_DC_es_filter[r] = dream_depression_count_es_filter[q] # for age group bc
    r += 1

for q in range (1,4,2):
    psychology_var_depression_DC_es_filter[r] = co_dream_depression_count_es_filter[q] # for age group bc
    r += 1

for q in range (1,6,2):
    psychology_var_depression_DC_es_filter[r] = psycho_depression_count_es_filter[q] #for education bc
    r += 1

for q in range (1,10,2):
    psychology_var_depression_DC_es_filter[r] = health_sys_depression_count_es_filter[q]# for marital bc 
    r += 1
    
for q in range (1,12,2):
    psychology_var_depression_DC_es_filter[r] = cases_deaths_depression_count_es_filter[q]# for marital bc 
    r += 1
    
for q in range (1,8,2):
    psychology_var_depression_DC_es_filter[r] = media_depression_count_es_filter[q]# for marital bc 
    r += 1    

for q in range (1,6,2):
    psychology_var_depression_DC_es_filter[r] = indoor_depression_count_es_filter[q]# for marital bc 
    r += 1

for q in range (1,6,2):
    psychology_var_depression_DC_es_filter[r] = survival_depression_count_es_filter[q]# for marital bc 
    r += 1

for q in range (1,12,2):
    psychology_var_depression_DC_es_filter[r] = lockdown_depression_count_es_filter[q]# for marital bc 
    r += 1
    
f, ax = plt.subplots(figsize=(10, 8))

sns.heatmap(psychology_var_depression_DC_es_filter, vmin = 0, vmax = 1300,  xticklabels=x_labels, yticklabels = y_labels, mask=np.zeros_like(psychology_var_depression_DC_es_filter, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, ax=ax)


#####################################################################


############################## DC-BC ################################


############################ Dream ##############################

dream_depression_count_diff = np.zeros((2,5),dtype = np.double)
dream_count = [Yes_dream, No_dream]
a=1
for i in range(2):
    dream_depression_count_diff[i] = (((dream_depression_count[a])/dream_count[i])*100) - (((dream_depression_count[a-1])/dream_count[i])*100)
    a += 2

#####################################################################
    
############################ COVID Dream ##############################

co_dream_depression_count_diff = np.zeros((2,5),dtype = np.double)
co_dream_count = [Yes_co_dream, No_co_dream]
a=1
for i in range(2):
    co_dream_depression_count_diff[i] = (((co_dream_depression_count[a])/co_dream_count[i])*100) - (((co_dream_depression_count[a-1])/co_dream_count[i])*100)
    a += 2

#####################################################################
    
############################ psycho ##############################

psycho_depression_count_diff = np.zeros((3,5),dtype = np.double)
psycho_count = [Yes_psycho, No_psycho, Maybe_psycho]
a=1
for i in range(3):
    psycho_depression_count_diff[i] = (((psycho_depression_count[a])/psycho_count[i])*100) - (((psycho_depression_count[a-1])/psycho_count[i])*100)
    a += 2

#####################################################################
    
############################ Health system ##############################

health_sys_depression_count_diff = np.zeros((5,5),dtype = np.double)
health_sys_count = [h_per_0,h_per_25,h_per_50,h_per_75,h_per_100]
a=1
for i in range(5):
    health_sys_depression_count_diff[i] = (((health_sys_depression_count[a])/health_sys_count[i])*100) - (((health_sys_depression_count[a-1])/health_sys_count[i])*100)
    a += 2

####################################################################
       
############################ cases and deaths ##############################

cases_deaths_depression_count_diff = np.zeros((6,5),dtype = np.double)
cases_deaths_count = [cd_Worried,cd_Upset,cd_Depressed,cd_Fear,cd_Anxious,cd_None]
a=1
for i in range(6):
    cases_deaths_depression_count_diff[i] = (((cases_deaths_depression_count[a])/cases_deaths_count[i])*100) - (((cases_deaths_depression_count[a-1])/cases_deaths_count[i])*100)
    a += 2

####################################################################
         
############################ media ##############################

media_depression_count_diff = np.zeros((4,5),dtype = np.double)
media_count = [Lessthananhour, hours1_3, hours4_6, Morethan6hours]
a=1
for i in range(4):
    media_depression_count_diff[i] = (((media_depression_count[a])/media_count[i])*100) - (((media_depression_count[a-1])/media_count[i])*100)
    a += 2

####################################################################
     
############################ Indoor ##############################

indoor_depression_count_diff = np.zeros((3,5),dtype = np.double)
indoor_count = [Yes_ind, No_ind, Sometimes_ind]
a=1
for i in range(3):
    indoor_depression_count_diff[i] = (((indoor_depression_count[a])/indoor_count[i])*100) - (((indoor_depression_count[a-1])/indoor_count[i])*100)
    a += 2

####################################################################
    
############################ Survival ##############################

survival_depression_count_diff = np.zeros((3,5),dtype = np.double)
survival_count = [well_soon, not_sure, die ]
a=1
for i in range(3):
    survival_depression_count_diff[i] = (((survival_depression_count[a])/survival_count[i])*100) - (((survival_depression_count[a-1])/survival_count[i])*100)
    a += 2

####################################################################

############################ lockdown ##############################

lockdown_depression_count_diff = np.zeros((6,5),dtype = np.double)
lockdown_count = [ld_Worried, ld_Upset, ld_Depressed, ld_Fear, ld_Anxious, ld_None]
a=1
for i in range(6):
    lockdown_depression_count_diff[i] = (((lockdown_depression_count[a])/lockdown_count[i])*100) - (((lockdown_depression_count[a-1])/lockdown_count[i])*100)
    a += 2

####################################################################

#####################################################################

psychology_var_depression_diff = np.zeros((34,5), dtype = np.double)


for i in range (2):
    psychology_var_depression_diff[i] = dream_depression_count_diff[i]

for i in range (2):
    psychology_var_depression_diff[i+2] = co_dream_depression_count_diff[i]

for i in range (3):
    psychology_var_depression_diff[i+4] = psycho_depression_count_diff[i]

for i in range (5):
    psychology_var_depression_diff[i+7] = health_sys_depression_count_diff[i]

for i in range (6):
    psychology_var_depression_diff[i+12] = cases_deaths_depression_count_diff[i]

for i in range (4):
    psychology_var_depression_diff[i+18] = media_depression_count_diff[i]

for i in range (3):
    psychology_var_depression_diff[i+22] = indoor_depression_count_diff[i]

for i in range (3):
    psychology_var_depression_diff[i+25] = survival_depression_count_diff[i]

for i in range (6):
    psychology_var_depression_diff[i+28] = lockdown_depression_count_diff[i]


f, ax = plt.subplots(figsize=(10, 8))

sns.heatmap(psychology_var_depression_diff, vmin=-50, vmax=50,  xticklabels=x_labels, yticklabels = y_labels, mask=np.zeros_like(psychology_var_depression_diff, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, ax=ax)
