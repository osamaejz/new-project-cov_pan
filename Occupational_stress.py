from DASS_calculation import survey_data , DASS_score
import numpy as np

################# for Occupational variable ###################

##################### for fronline #####################
frontline = []
frontline = survey_data['Frontline']
No_frontline,Yes_frontline = survey_data['Frontline'].value_counts()

no_frontline_DASS_score = np.zeros((No_frontline,6),dtype = np.double)
yes_frontline_DASS_score = np.zeros((Yes_frontline,6),dtype = np.double)


val_nf = 0
val_yf = 0

for frontline_value in range (len(survey_data)):
    if frontline[frontline_value] == 'No':
        for i in range(6):   
            no_frontline_DASS_score[val_nf][i] = DASS_score[frontline_value][i]
        val_nf += 1
    elif frontline[frontline_value] == 'Yes':
        for i in range(6):   
            yes_frontline_DASS_score[val_yf][i] = DASS_score[frontline_value][i]
        val_yf += 1



        
frontline_stress_count = np.zeros((4,5),dtype = np.double)

for l in range (2):
    normal_nf = 0
    mild_nf = 0
    moderate_nf = 0
    severe_nf = 0
    extreme_nf = 0
    
    normal_yf = 0
    mild_yf = 0
    moderate_yf = 0
    severe_yf = 0
    extreme_yf = 0
    
    for k in range(len(no_frontline_DASS_score)):
       
        if (no_frontline_DASS_score[k][l+4]>=0 and no_frontline_DASS_score[k][l+4]<15):
            normal_nf += 1
            
        elif (no_frontline_DASS_score[k][l+4]>=15 and no_frontline_DASS_score[k][l+4]<19):
            mild_nf += 1
            
        elif (no_frontline_DASS_score[k][l+4]>=19 and no_frontline_DASS_score[k][l+4]<26):
            moderate_nf += 1
            
        elif (no_frontline_DASS_score[k][l+4]>=26 and no_frontline_DASS_score[k][l+4]<34):
            severe_nf += 1
            
        else:
            extreme_nf += 1



    for k in range(len(yes_frontline_DASS_score)):
       
        if (yes_frontline_DASS_score[k][l+4]>=0 and yes_frontline_DASS_score[k][l+4]<15):
            normal_yf += 1
            
        elif (yes_frontline_DASS_score[k][l+4]>=15 and yes_frontline_DASS_score[k][l+4]<19):
            mild_yf += 1
            
        elif (yes_frontline_DASS_score[k][l+4]>=19 and yes_frontline_DASS_score[k][l+4]<26):
            moderate_yf += 1
            
        elif (yes_frontline_DASS_score[k][l+4]>=26 and yes_frontline_DASS_score[k][l+4]<34):
            severe_yf += 1
            
        else:
            extreme_yf += 1


    temp_0 = [[normal_yf, mild_yf, moderate_yf, severe_yf, extreme_yf],
            [normal_nf, mild_nf, moderate_nf, severe_nf, extreme_nf]]
            
       
    frontline_stress_count[l] = temp_0[0]  
    frontline_stress_count[l+2] = temp_0[1]



################ Es filtration for frontline #######################


frontline_stress_count_es_filter = np.copy(frontline_stress_count)


for row in range (0,4,2):
    
    frontline_stress_count_es_filter[row][4] = abs(frontline_stress_count_es_filter[row][4] - frontline_stress_count_es_filter[row][4])
    frontline_stress_count_es_filter[row+1][4] = abs(frontline_stress_count_es_filter[row+1][4] - frontline_stress_count[row][4])

#####################################################################

##################### for income #####################

income = []
income = survey_data['Income']
income = income.replace(np.nan,'na')
# income_update = income.replace(np.nan,0)
fourtyk_plus, hundredk_plus, na, plus_tenk, less_tenk = income.value_counts()


fourtyk_plus_DASS_score = np.zeros((fourtyk_plus,6),dtype = np.double)
hundredk_plus_DASS_score = np.zeros((hundredk_plus,6),dtype = np.double)
na_DASS_score = np.zeros((na,6),dtype = np.double)
plus_tenk_DASS_score = np.zeros((plus_tenk,6),dtype = np.double)
less_tenk_DASS_score = np.zeros((less_tenk,6),dtype = np.double)



val_40 = 0
val_100 = 0
val_na = 0
val_10p = 0
val_10l = 0

for income_value in range (len(survey_data)):
    if income[income_value] == 'Lessthan10000Rs':
        for i in range(6):   
            less_tenk_DASS_score[val_10l][i] = DASS_score[income_value][i]
        val_10l += 1
        
    elif income[income_value] == '10000Rs40000Rs':
        for j in range(6):       
            plus_tenk_DASS_score[val_10p][j] = DASS_score[income_value][j]
        val_10p += 1
        
    elif income[income_value] == '40001Rs100000Rs':
        for i in range(6):   
            fourtyk_plus_DASS_score[val_40][i] = DASS_score[income_value][i]
        val_40 += 1
        
    elif income[income_value] == 'Morethan100000Rs':
        for i in range(6):   
            hundredk_plus_DASS_score[val_100][i] = DASS_score[income_value][i]
        val_100 += 1
        
    elif income[income_value] == 'na':
        for i in range(6):   
            na_DASS_score[val_na][i] = DASS_score[income_value][i]
        val_na += 1
        
   
    
#################### income DASS count #################



income_stress_count = np.zeros((10,5),dtype = np.double)


for l in range (2):
    normal_10l = 0
    mild_10l = 0
    moderate_10l = 0
    severe_10l = 0
    extreme_10l = 0
    
    normal_10p = 0
    mild_10p = 0
    moderate_10p = 0
    severe_10p = 0
    extreme_10p = 0
    
    normal_40 = 0
    mild_40 = 0
    moderate_40 = 0
    severe_40 = 0
    extreme_40 = 0
    
    normal_100 = 0
    mild_100 = 0
    moderate_100 = 0
    severe_100 = 0
    extreme_100 = 0
    
    normal_na = 0
    mild_na = 0
    moderate_na = 0
    severe_na = 0
    extreme_na = 0
 
    
    for c in range(len(less_tenk_DASS_score)):
       
        ############## for <10,000 stress ############# 

        if (less_tenk_DASS_score[c][l+4]>=0 and less_tenk_DASS_score[c][l+4]<15):
            normal_10l += 1
            
        elif (less_tenk_DASS_score[c][l+4]>=15 and less_tenk_DASS_score[c][l+4]<19):
            mild_10l += 1
            
        elif (less_tenk_DASS_score[c][l+4]>=19 and less_tenk_DASS_score[c][l+4]<26):
            moderate_10l += 1
            
        elif (less_tenk_DASS_score[c][l+4]>=26 and less_tenk_DASS_score[c][l+4]<34):
            severe_10l += 1
            
        else:
            extreme_10l += 1
        
        ############## for 10,000 - 40,000 stress ############# 
    for ys in range(len(plus_tenk_DASS_score)):
    
        if (plus_tenk_DASS_score[ys][l+4]>=0 and plus_tenk_DASS_score[ys][l+4]<15):
            normal_10p += 1
            
        elif (plus_tenk_DASS_score[ys][l+4]>=15 and plus_tenk_DASS_score[ys][l+4]<19):
            mild_10p += 1
            
        elif (plus_tenk_DASS_score[ys][l+4]>=19 and plus_tenk_DASS_score[ys][l+4]<26):
            moderate_10p += 1
            
        elif (plus_tenk_DASS_score[ys][l+4]>=26 and plus_tenk_DASS_score[ys][l+4]<34):
            severe_10p += 1
            
        else:
            extreme_10p += 1
            
        ############## for 40,000 - 100,000 stress ############# 
    for y in range(len(fourtyk_plus_DASS_score)):

        if (fourtyk_plus_DASS_score[y][l+4]>=0 and fourtyk_plus_DASS_score[y][l+4]<15):
            normal_40 += 1
            
        elif (fourtyk_plus_DASS_score[y][l+4]>=15 and fourtyk_plus_DASS_score[y][l+4]<19):
            mild_40 += 1
            
        elif (fourtyk_plus_DASS_score[y][l+4]>=19 and fourtyk_plus_DASS_score[y][l+4]<26):
            moderate_40 += 1
            
        elif (fourtyk_plus_DASS_score[y][l+4]>=26 and fourtyk_plus_DASS_score[y][l+4]<34):
            severe_40 += 1
            
        else:
            extreme_40 += 1
            
        ############## for >100,000 ############# 
    for ea in range(len(hundredk_plus_DASS_score)):

        if (hundredk_plus_DASS_score[ea][l+4]>=0 and hundredk_plus_DASS_score[ea][l+4]<15):
            normal_100 += 1
            
        elif (hundredk_plus_DASS_score[ea][l+4]>=15 and hundredk_plus_DASS_score[ea][l+4]<19):
            mild_100 += 1
            
        elif (hundredk_plus_DASS_score[ea][l+4]>=19 and hundredk_plus_DASS_score[ea][l+4]<26):
            moderate_100 += 1
            
        elif (hundredk_plus_DASS_score[ea][l+4]>=26 and hundredk_plus_DASS_score[ea][l+4]<34):
            severe_100 += 1
            
        else:
            extreme_100 += 1
            
        ############## for N/A stress ############# 
    for ma in range(len(na_DASS_score)):

        if (na_DASS_score[ma][l+4]>=0 and na_DASS_score[ma][l+4]<15):
            normal_na += 1
            
        elif (na_DASS_score[ma][l+4]>=15 and na_DASS_score[ma][l+4]<19):
            mild_na += 1
            
        elif (na_DASS_score[ma][l+4]>=19 and na_DASS_score[ma][l+4]<26):
            moderate_na += 1
            
        elif (na_DASS_score[ma][l+4]>=26 and na_DASS_score[ma][l+4]<34):
            severe_na += 1
            
        else:
            extreme_na += 1
            
    
            
    temp_1 = [[normal_10l, mild_10l, moderate_10l, severe_10l, extreme_10l],
              [normal_10p, mild_10p, moderate_10p, severe_10p, extreme_10p],
              [normal_40, mild_40, moderate_40, severe_40, extreme_40],
              [normal_100, mild_100, moderate_100, severe_100, extreme_100],
              [normal_na, mild_na, moderate_na, severe_na, extreme_na]]        
            
    income_stress_count[l] = temp_1[0]  
    income_stress_count[l+2] = temp_1[1]  
    income_stress_count[l+4] = temp_1[2]     
    income_stress_count[l+6] = temp_1[3]        
    income_stress_count[l+8] = temp_1[4]        
         

#####################################################################

################ Es filtration for income #######################


income_stress_count_es_filter = np.copy(income_stress_count)


for row in range (0,10,2):
    
    income_stress_count_es_filter[row][4] = abs(income_stress_count_es_filter[row][4] - income_stress_count_es_filter[row][4])
    income_stress_count_es_filter[row+1][4] = abs(income_stress_count_es_filter[row+1][4] - income_stress_count[row][4])

 
#####################################################################


####################### for earning comparison #########################
earning = []
earning = survey_data['Earning comparision']
earning = earning.replace(np.nan,'na')
no_change, decr, na_earn, lost_job, incr = earning.value_counts()



no_change_DASS_score = np.zeros((no_change,6),dtype = np.double)
decr_DASS_score = np.zeros((decr,6),dtype = np.double)
na_earn_DASS_score = np.zeros((na_earn,6),dtype = np.double)
lost_job_DASS_score = np.zeros((lost_job,6),dtype = np.double)
incr_DASS_score = np.zeros((incr,6),dtype = np.double)



val_nc = 0
val_inc = 0
val_dec = 0
val_lj = 0
val_nae = 0



for earning_value in range (len(survey_data)):
    if earning[earning_value] == 'Nochange':
        for i in range(6):   
            no_change_DASS_score[val_nc][i] = DASS_score[earning_value][i]
        val_nc += 1
        
    elif earning[earning_value] == 'Increased':
        for j in range(6):       
            incr_DASS_score[val_inc][j] = DASS_score[earning_value][j]
        val_inc += 1
        
    elif earning[earning_value] == 'Decreased':
        for i in range(6):   
            decr_DASS_score[val_dec][i] = DASS_score[earning_value][i]
        val_dec += 1
        
    elif earning[earning_value] == 'NoearningLostmyjob':
        for i in range(6):   
            lost_job_DASS_score[val_lj][i] = DASS_score[earning_value][i]
        val_lj += 1
        
    elif earning[earning_value] == 'na':
        for i in range(6):   
            na_earn_DASS_score[val_nae][i] = DASS_score[earning_value][i]
        val_nae += 1
        
   
    
#################### Earning stress count #################



earning_stress_count = np.zeros((10,5),dtype = np.double)


for l in range (2):
    normal_nc = 0
    mild_nc = 0
    moderate_nc = 0
    severe_nc = 0
    extreme_nc = 0
    
    normal_inc = 0
    mild_inc = 0
    moderate_inc = 0
    severe_inc = 0
    extreme_inc = 0
    
    normal_dec = 0
    mild_dec = 0
    moderate_dec = 0
    severe_dec = 0
    extreme_dec = 0
    
    normal_lj = 0
    mild_lj = 0
    moderate_lj = 0
    severe_lj = 0
    extreme_lj = 0
    
    normal_nae = 0
    mild_nae = 0
    moderate_nae = 0
    severe_nae = 0
    extreme_nae = 0
 
    
    for c in range(len(no_change_DASS_score)):
       
        ############## for no change stress ############# 

        if (no_change_DASS_score[c][l+4]>=0 and no_change_DASS_score[c][l+4]<15):
            normal_nc += 1
            
        elif (no_change_DASS_score[c][l+4]>=15 and no_change_DASS_score[c][l+4]<19):
            mild_nc += 1
            
        elif (no_change_DASS_score[c][l+4]>=19 and no_change_DASS_score[c][l+4]<26):
            moderate_nc += 1
            
        elif (no_change_DASS_score[c][l+4]>=26 and no_change_DASS_score[c][l+4]<34):
            severe_nc += 1
            
        else:
            extreme_nc += 1
        
        ############## for increased stress ############# 
    for ys in range(len(incr_DASS_score)):
    
        if (incr_DASS_score[ys][l+4]>=0 and incr_DASS_score[ys][l+4]<15):
            normal_inc += 1
            
        elif (incr_DASS_score[ys][l+4]>=15 and incr_DASS_score[ys][l+4]<19):
            mild_inc += 1
            
        elif (incr_DASS_score[ys][l+4]>=19 and incr_DASS_score[ys][l+4]<26):
            moderate_inc += 1
            
        elif (incr_DASS_score[ys][l+4]>=26 and incr_DASS_score[ys][l+4]<34):
            severe_inc += 1
            
        else:
            extreme_inc += 1
            
        ############## for decreased stress ############# 
    for y in range(len(decr_DASS_score)):

        if (decr_DASS_score[y][l+4]>=0 and decr_DASS_score[y][l+4]<15):
            normal_dec += 1
            
        elif (decr_DASS_score[y][l+4]>=15 and decr_DASS_score[y][l+4]<19):
            mild_dec += 1
            
        elif (decr_DASS_score[y][l+4]>=19 and decr_DASS_score[y][l+4]<26):
            moderate_dec += 1
            
        elif (decr_DASS_score[y][l+4]>=26 and decr_DASS_score[y][l+4]<34):
            severe_dec += 1
            
        else:
            extreme_dec += 1
            
        ############## for lost job stress ############# 
    for ea in range(len(lost_job_DASS_score)):

        if (lost_job_DASS_score[ea][l+4]>=0 and lost_job_DASS_score[ea][l+4]<15):
            normal_lj += 1
            
        elif (lost_job_DASS_score[ea][l+4]>=15 and lost_job_DASS_score[ea][l+4]<19):
            mild_lj += 1
            
        elif (lost_job_DASS_score[ea][l+4]>=19 and lost_job_DASS_score[ea][l+4]<26):
            moderate_lj += 1
            
        elif (lost_job_DASS_score[ea][l+4]>=26 and lost_job_DASS_score[ea][l+4]<34):
            severe_lj += 1
            
        else:
            extreme_lj += 1
            
        ############## for N/A stress ############# 
    for ma in range(len(na_earn_DASS_score)):

        if (na_earn_DASS_score[ma][l+4]>=0 and na_earn_DASS_score[ma][l+4]<15):
            normal_nae += 1
            
        elif (na_earn_DASS_score[ma][l+4]>=15 and na_earn_DASS_score[ma][l+4]<19):
            mild_nae += 1
            
        elif (na_earn_DASS_score[ma][l+4]>=19 and na_earn_DASS_score[ma][l+4]<26):
            moderate_nae += 1
            
        elif (na_earn_DASS_score[ma][l+4]>=26 and na_earn_DASS_score[ma][l+4]<34):
            severe_nae += 1
            
        else:
            extreme_nae += 1
            
    
            
    temp_2 = [[normal_nc, mild_nc, moderate_nc, severe_nc, extreme_nc],
              [normal_inc, mild_inc, moderate_inc, severe_inc, extreme_inc],
              [normal_dec, mild_dec, moderate_dec, severe_dec, extreme_dec],
              [normal_lj, mild_lj, moderate_lj, severe_lj, extreme_lj],
              [normal_nae, mild_nae, moderate_nae, severe_nae, extreme_nae]]        
            
    earning_stress_count[l] = temp_2[0]  
    earning_stress_count[l+2] = temp_2[1]  
    earning_stress_count[l+4] = temp_2[2]     
    earning_stress_count[l+6] = temp_2[3]        
    earning_stress_count[l+8] = temp_2[4]        
         

#####################################################################

################ Es filtration for earning #######################


earning_stress_count_es_filter = np.copy(earning_stress_count)


for row in range (0,10,2):
    
    earning_stress_count_es_filter[row][4] = abs(earning_stress_count_es_filter[row][4] - earning_stress_count_es_filter[row][4])
    earning_stress_count_es_filter[row+1][4] = abs(earning_stress_count_es_filter[row+1][4] - earning_stress_count[row][4])

 
#####################################################################

#########################Time to profession online#########################
    

online = []
online = survey_data['Time to profession online']
online = online.replace(np.nan,'na')
not_online, na_online, more_online, less_online, same_online = online.value_counts()
      

not_online_DASS_score = np.zeros((not_online,6),dtype = np.double)
na_online_DASS_score = np.zeros((na_online,6),dtype = np.double)
more_online_DASS_score = np.zeros((more_online,6),dtype = np.double)
less_online_DASS_score = np.zeros((less_online,6),dtype = np.double)
same_online_DASS_score = np.zeros((same_online,6),dtype = np.double)



val_so = 0
val_mo = 0
val_lo = 0
val_no = 0
val_nao = 0



for online_value in range (len(survey_data)):
    if online[online_value] == 'Sameasonsitetime':
        for i in range(6):   
            same_online_DASS_score[val_so][i] = DASS_score[online_value][i]
        val_so += 1
        
    elif online[online_value] == 'Morethanonsitetime':
        for j in range(6):       
            more_online_DASS_score[val_mo][j] = DASS_score[online_value][j]
        val_mo += 1
        
    elif online[online_value] == 'Lessthanonsitetime':
        for i in range(6):   
            less_online_DASS_score[val_lo][i] = DASS_score[online_value][i]
        val_lo += 1
        
    elif online[online_value] == 'Iamnotworkingremotelyonline':
        for i in range(6):   
            not_online_DASS_score[val_no][i] = DASS_score[online_value][i]
        val_no += 1
        
    elif online[online_value] == 'na':
        for i in range(6):   
            na_online_DASS_score[val_nao][i] = DASS_score[online_value][i]
        val_nao += 1
        
   
    
#################### online stress count #################



online_stress_count = np.zeros((10,5),dtype = np.double)


for l in range (2):
    normal_so = 0
    mild_so = 0
    moderate_so = 0
    severe_so = 0
    extreme_so = 0
    
    normal_mo = 0
    mild_mo = 0
    moderate_mo = 0
    severe_mo = 0
    extreme_mo = 0
    
    normal_lo = 0
    mild_lo = 0
    moderate_lo = 0
    severe_lo = 0
    extreme_lo = 0
    
    normal_no = 0
    mild_no = 0
    moderate_no = 0
    severe_no = 0
    extreme_no = 0
    
    normal_nao = 0
    mild_nao = 0
    moderate_nao = 0
    severe_nao = 0
    extreme_nao = 0
 
    
    for c in range(len(same_online_DASS_score)):
       
        ############## for smae as onsite stress ############# 

        if (same_online_DASS_score[c][l+4]>=0 and same_online_DASS_score[c][l+4]<15):
            normal_so += 1
            
        elif (same_online_DASS_score[c][l+4]>=15 and same_online_DASS_score[c][l+4]<19):
            mild_so += 1
            
        elif (same_online_DASS_score[c][l+4]>=19 and same_online_DASS_score[c][l+4]<26):
            moderate_so += 1
            
        elif (same_online_DASS_score[c][l+4]>=26 and same_online_DASS_score[c][l+4]<34):
            severe_so += 1
            
        else:
            extreme_so += 1
        
        ############## for more than onsite stress ############# 
    for ys in range(len(more_online_DASS_score)):
    
        if (more_online_DASS_score[ys][l+4]>=0 and more_online_DASS_score[ys][l+4]<15):
            normal_mo += 1
            
        elif (more_online_DASS_score[ys][l+4]>=15 and more_online_DASS_score[ys][l+4]<19):
            mild_mo += 1
            
        elif (more_online_DASS_score[ys][l+4]>=19 and more_online_DASS_score[ys][l+4]<26):
            moderate_mo += 1
            
        elif (more_online_DASS_score[ys][l+4]>=26 and more_online_DASS_score[ys][l+4]<34):
            severe_mo += 1
            
        else:
            extreme_mo += 1
            
        ############## for less than onsite stress ############# 
    for y in range(len(less_online_DASS_score)):

        if (less_online_DASS_score[y][l+4]>=0 and less_online_DASS_score[y][l+4]<15):
            normal_lo += 1
            
        elif (less_online_DASS_score[y][l+4]>=15 and less_online_DASS_score[y][l+4]<19):
            mild_lo += 1
            
        elif (less_online_DASS_score[y][l+4]>=19 and less_online_DASS_score[y][l+4]<26):
            moderate_lo += 1
            
        elif (less_online_DASS_score[y][l+4]>=26 and less_online_DASS_score[y][l+4]<34):
            severe_lo += 1
            
        else:
            extreme_lo += 1
            
        ############## for no online work stress ############# 
    for ea in range(len(not_online_DASS_score)):

        if (not_online_DASS_score[ea][l+4]>=0 and not_online_DASS_score[ea][l+4]<15):
            normal_no += 1
            
        elif (not_online_DASS_score[ea][l+4]>=15 and not_online_DASS_score[ea][l+4]<19):
            mild_no += 1
            
        elif (not_online_DASS_score[ea][l+4]>=19 and not_online_DASS_score[ea][l+4]<26):
            moderate_no += 1
            
        elif (not_online_DASS_score[ea][l+4]>=26 and not_online_DASS_score[ea][l+4]<34):
            severe_no += 1
            
        else:
            extreme_no += 1
            
        ############## for N/A stress ############# 
    for ma in range(len(na_online_DASS_score)):

        if (na_online_DASS_score[ma][l+4]>=0 and na_online_DASS_score[ma][l+4]<15):
            normal_nao += 1
            
        elif (na_online_DASS_score[ma][l+4]>=15 and na_online_DASS_score[ma][l+4]<19):
            mild_nao += 1
            
        elif (na_online_DASS_score[ma][l+4]>=19 and na_online_DASS_score[ma][l+4]<26):
            moderate_nao += 1
            
        elif (na_online_DASS_score[ma][l+4]>=26 and na_online_DASS_score[ma][l+4]<34):
            severe_nao += 1
            
        else:
            extreme_nao += 1
            
    
            
    temp_3 = [[normal_so, mild_so, moderate_so, severe_so, extreme_so],
              [normal_mo, mild_mo, moderate_mo, severe_mo, extreme_mo],
              [normal_lo, mild_lo, moderate_lo, severe_lo, extreme_lo],
              [normal_no, mild_no, moderate_no, severe_no, extreme_no],
              [normal_nao, mild_nao, moderate_nao, severe_nao, extreme_nao]]        
            
    online_stress_count[l] = temp_3[0]  
    online_stress_count[l+2] = temp_3[1]  
    online_stress_count[l+4] = temp_3[2]     
    online_stress_count[l+6] = temp_3[3]        
    online_stress_count[l+8] = temp_3[4]        
         

#####################################################################

################ Es filtration for online #######################


online_stress_count_es_filter = np.copy(online_stress_count)


for row in range (0,10,2):
    
    online_stress_count_es_filter[row][4] = abs(online_stress_count_es_filter[row][4] - online_stress_count_es_filter[row][4])
    online_stress_count_es_filter[row+1][4] = abs(online_stress_count_es_filter[row+1][4] - online_stress_count[row][4])

 
#####################################################################

###########################For dependents#############################   


dependents = []
dependents = survey_data['Dependents']
lfour, lseven, lten, mten = survey_data['Dependents'].value_counts()
 

lfour_DASS_score = np.zeros((lfour,6),dtype = np.double)
lseven_DASS_score = np.zeros((lseven,6),dtype = np.double)
lten_DASS_score = np.zeros((lten,6),dtype = np.double)
mten_DASS_score = np.zeros((mten,6),dtype = np.double)



val_fl = 0
val_sl = 0
val_tl = 0
val_tm = 0




for dependents_value in range (len(survey_data)):
    if dependents[dependents_value] == '0_4':
        for i in range(6):   
            lfour_DASS_score[val_fl][i] = DASS_score[dependents_value][i]
        val_fl += 1
        
    elif dependents[dependents_value] == '5_7':
        for j in range(6):       
            lseven_DASS_score[val_sl][j] = DASS_score[dependents_value][j]
        val_sl += 1
        
    elif dependents[dependents_value] == '8_10':
        for i in range(6):   
            lten_DASS_score[val_tl][i] = DASS_score[dependents_value][i]
        val_tl += 1
        
    elif dependents[dependents_value] == 'Morethan10':
        for i in range(6):   
            mten_DASS_score[val_tm][i] = DASS_score[dependents_value][i]
        val_tm += 1
    
   
    
#################### dependents stress count #################



dependents_stress_count = np.zeros((8,5),dtype = np.double)


for l in range (2):
    normal_fl = 0
    mild_fl = 0
    moderate_fl = 0
    severe_fl = 0
    extreme_fl = 0
    
    normal_sl = 0
    mild_sl = 0
    moderate_sl = 0
    severe_sl = 0
    extreme_sl = 0
    
    normal_tl = 0
    mild_tl = 0
    moderate_tl = 0
    severe_tl = 0
    extreme_tl = 0
    
    normal_tm = 0
    mild_tm = 0
    moderate_tm = 0
    severe_tm = 0
    extreme_tm = 0
   
 
    ############## for 0-4 stress ############# 
 
    for c in range(len(lfour_DASS_score)):
       
        ############## for illiterate stress ############# 

        if (lfour_DASS_score[c][l+4]>=0 and lfour_DASS_score[c][l+4]<15):
            normal_fl += 1
            
        elif (lfour_DASS_score[c][l+4]>=15 and lfour_DASS_score[c][l+4]<19):
            mild_fl += 1
            
        elif (lfour_DASS_score[c][l+4]>=19 and lfour_DASS_score[c][l+4]<26):
            moderate_fl += 1
            
        elif (lfour_DASS_score[c][l+4]>=26 and lfour_DASS_score[c][l+4]<34):
            severe_fl += 1
            
        else:
            extreme_fl += 1
        
        ############## for 5-7 stress ############# 
    for ys in range(len(lseven_DASS_score)):
    
        if (lseven_DASS_score[ys][l+4]>=0 and lseven_DASS_score[ys][l+4]<15):
            normal_sl += 1
            
        elif (lseven_DASS_score[ys][l+4]>=15 and lseven_DASS_score[ys][l+4]<19):
            mild_sl += 1
            
        elif (lseven_DASS_score[ys][l+4]>=19 and lseven_DASS_score[ys][l+4]<26):
            moderate_sl += 1
            
        elif (lseven_DASS_score[ys][l+4]>=26 and lseven_DASS_score[ys][l+4]<34):
            severe_sl += 1
            
        else:
            extreme_sl += 1
            
        ############## for 8-10 stress ############# 
    for y in range(len(lten_DASS_score)):

        if (lten_DASS_score[y][l+4]>=0 and lten_DASS_score[y][l+4]<15):
            normal_tl += 1
            
        elif (lten_DASS_score[y][l+4]>=15 and lten_DASS_score[y][l+4]<19):
            mild_tl += 1
            
        elif (lten_DASS_score[y][l+4]>=19 and lten_DASS_score[y][l+4]<26):
            moderate_tl += 1
            
        elif (lten_DASS_score[y][l+4]>=26 and lten_DASS_score[y][l+4]<34):
            severe_tl += 1
            
        else:
            extreme_tl += 1
            
        ############## for 10+ stress ############# 
    for ea in range(len(mten_DASS_score)):

        if (mten_DASS_score[ea][l+4]>=0 and mten_DASS_score[ea][l+4]<15):
            normal_tm += 1
            
        elif (mten_DASS_score[ea][l+4]>=15 and mten_DASS_score[ea][l+4]<19):
            mild_tm += 1
            
        elif (mten_DASS_score[ea][l+4]>=19 and mten_DASS_score[ea][l+4]<26):
            moderate_tm += 1
            
        elif (mten_DASS_score[ea][l+4]>=26 and mten_DASS_score[ea][l+4]<34):
            severe_tm += 1
            
        else:
            extreme_tm += 1
     
            
    temp_4 = [[normal_fl, mild_fl, moderate_fl, severe_fl, extreme_fl],
              [normal_sl, mild_sl, moderate_sl, severe_sl, extreme_sl],
              [normal_tl, mild_tl, moderate_tl, severe_tl, extreme_tl],
              [normal_tm, mild_tm, moderate_tm, severe_tm, extreme_tm]]        
            
    dependents_stress_count[l] = temp_4[0]  
    dependents_stress_count[l+2] = temp_4[1]  
    dependents_stress_count[l+4] = temp_4[2]     
    dependents_stress_count[l+6] = temp_4[3]        
        
         

#####################################################################

################ Es filtration for dependents #######################


dependents_stress_count_es_filter = np.copy(dependents_stress_count)


for row in range (0,8,2):
    
    dependents_stress_count_es_filter[row][4] = abs(dependents_stress_count_es_filter[row][4] - dependents_stress_count_es_filter[row][4])
    dependents_stress_count_es_filter[row+1][4] = abs(dependents_stress_count_es_filter[row+1][4] - dependents_stress_count[row][4])

 
#####################################################################

###########################For profession#############################  
    

profession = []
profession = survey_data['Profession']
student, private, gov, hwife, selfemployed, unemployed, retired, corp_buisness, small_buisness, labour = survey_data['Profession'].value_counts()
    

gov_DASS_score =  np.zeros((gov,6),dtype = np.double)
private_DASS_score =  np.zeros((private,6),dtype = np.double)
selfemployed_DASS_score =  np.zeros((selfemployed,6),dtype = np.double)
small_buisness_DASS_score =  np.zeros((small_buisness,6),dtype = np.double)
hwife_DASS_score =  np.zeros((hwife,6),dtype = np.double)
corp_buisness_DASS_score =  np.zeros((corp_buisness,6),dtype = np.double)
student_DASS_score =  np.zeros((student,6),dtype = np.double)
retired_DASS_score =  np.zeros((retired,6),dtype = np.double)
labour_DASS_score =  np.zeros((labour,6),dtype = np.double)
unemployed_DASS_score =  np.zeros((unemployed,6),dtype = np.double)


val_g = 0
val_p = 0
val_se = 0
val_sb = 0
val_hw = 0
val_cb = 0
val_st = 0
val_r = 0
val_l = 0
val_ue = 0



for profession_value in range (len(survey_data)):
    if profession[profession_value] == 'Governmentemployee':
        for i in range(6):   
            gov_DASS_score[val_g][i] = DASS_score[profession_value][i]
        val_g += 1
        
    elif profession[profession_value] == 'Privatesectoremployee':
        for j in range(6):       
            private_DASS_score[val_p][j] = DASS_score[profession_value][j]
        val_p += 1
        
    elif profession[profession_value] == 'SelfemployedFreelancer':
        for i in range(6):   
            selfemployed_DASS_score[val_se][i] = DASS_score[profession_value][i]
        val_se += 1
        
    elif profession[profession_value] == 'SmallscalebusinessownerShopkeeper':
        for i in range(6):   
            small_buisness_DASS_score[val_sb][i] = DASS_score[profession_value][i]
        val_sb += 1
        
    elif profession[profession_value] == 'Housewife':
        for j in range(6):       
            hwife_DASS_score[val_hw][j] = DASS_score[profession_value][j]
        val_hw += 1
        
    elif profession[profession_value] == 'Corporatebusinessmanbusinesswoman':
        for i in range(6):   
            corp_buisness_DASS_score[val_cb][i] = DASS_score[profession_value][i]
        val_cb += 1
        
    elif profession[profession_value] == 'Student':
        for i in range(6):   
            student_DASS_score[val_st][i] = DASS_score[profession_value][i]
        val_st += 1
        
    elif profession[profession_value] == 'Retiredpensioner':
        for j in range(6):       
            retired_DASS_score[val_r][j] = DASS_score[profession_value][j]
        val_r += 1
        
    elif profession[profession_value] == 'LabourDailywager':
        for i in range(6):   
            labour_DASS_score[val_l][i] = DASS_score[profession_value][i]
        val_l += 1
        
    elif profession[profession_value] == 'Unemployed':
        for i in range(6):   
            unemployed_DASS_score[val_ue][i] = DASS_score[profession_value][i]
        val_ue += 1
    

############# profession stress count ##############

profession_stress_count = np.zeros((20,5),dtype = np.double)


for l in range (2):
    normal_g = 0
    mild_g = 0
    moderate_g = 0
    severe_g = 0
    extreme_g = 0
    
    normal_p = 0
    mild_p = 0
    moderate_p = 0
    severe_p = 0
    extreme_p = 0
    
    normal_se = 0
    mild_se = 0
    moderate_se = 0
    severe_se = 0
    extreme_se = 0
    
    normal_sb = 0
    mild_sb = 0
    moderate_sb = 0
    severe_sb = 0
    extreme_sb = 0
    
    normal_hw = 0
    mild_hw = 0
    moderate_hw = 0
    severe_hw = 0
    extreme_hw = 0
    
    normal_cb = 0
    mild_cb = 0
    moderate_cb = 0
    severe_cb = 0
    extreme_cb = 0
    
    normal_st = 0
    mild_st = 0
    moderate_st = 0
    severe_st = 0
    extreme_st = 0
    
    normal_r = 0
    mild_r = 0
    moderate_r = 0
    severe_r = 0
    extreme_r = 0
    
    normal_l = 0
    mild_l = 0
    moderate_l = 0
    severe_l = 0
    extreme_l = 0
    
    normal_ue = 0
    mild_ue = 0
    moderate_ue = 0
    severe_ue = 0
    extreme_ue = 0
    
    for c in range(len(gov_DASS_score)):
       
        ############## for government stress ############# 

        if (gov_DASS_score[c][l+4]>=0 and gov_DASS_score[c][l+4]<15):
            normal_g += 1
            
        elif (gov_DASS_score[c][l+4]>=15 and gov_DASS_score[c][l+4]<19):
            mild_g += 1
            
        elif (gov_DASS_score[c][l+4]>=19 and gov_DASS_score[c][l+4]<26):
            moderate_g += 1
            
        elif (gov_DASS_score[c][l+4]>=26 and gov_DASS_score[c][l+4]<34):
            severe_g += 1
            
        else:
            extreme_g += 1
        
        ############## for private stress ############# 
    for ys in range(len(private_DASS_score)):
    
        if (private_DASS_score[ys][l+4]>=0 and private_DASS_score[ys][l+4]<15):
            normal_p += 1
            
        elif (private_DASS_score[ys][l+4]>=15 and private_DASS_score[ys][l+4]<19):
            mild_p += 1
            
        elif (private_DASS_score[ys][l+4]>=19 and private_DASS_score[ys][l+4]<26):
            moderate_p += 1
            
        elif (private_DASS_score[ys][l+4]>=26 and private_DASS_score[ys][l+4]<34):
            severe_p += 1
            
        else:
            extreme_p += 1
            
        ############## for self employed stress ############# 
    for y in range(len(selfemployed_DASS_score)):

        if (selfemployed_DASS_score[y][l+4]>=0 and selfemployed_DASS_score[y][l+4]<15):
            normal_se += 1
            
        elif (selfemployed_DASS_score[y][l+4]>=15 and selfemployed_DASS_score[y][l+4]<19):
            mild_se += 1
            
        elif (selfemployed_DASS_score[y][l+4]>=19 and selfemployed_DASS_score[y][l+4]<26):
            moderate_se += 1
            
        elif (selfemployed_DASS_score[y][l+4]>=26 and selfemployed_DASS_score[y][l+4]<34):
            severe_se += 1
            
        else:
            extreme_se += 1
            
        ############## for small business stress ############# 
    for ea in range(len(small_buisness_DASS_score)):

        if (small_buisness_DASS_score[ea][l+4]>=0 and small_buisness_DASS_score[ea][l+4]<15):
            normal_sb += 1
            
        elif (small_buisness_DASS_score[ea][l+4]>=15 and small_buisness_DASS_score[ea][l+4]<19):
            mild_sb += 1
            
        elif (small_buisness_DASS_score[ea][l+4]>=19 and small_buisness_DASS_score[ea][l+4]<26):
            moderate_sb += 1
            
        elif (small_buisness_DASS_score[ea][l+4]>=26 and small_buisness_DASS_score[ea][l+4]<34):
            severe_sb += 1
            
        else:
            extreme_sb += 1
            
        ############## for housewife stress ############# 
    for ma in range(len(hwife_DASS_score)):

        if (hwife_DASS_score[ma][l+4]>=0 and hwife_DASS_score[ma][l+4]<15):
            normal_hw += 1
            
        elif (hwife_DASS_score[ma][l+4]>=15 and hwife_DASS_score[ma][l+4]<19):
            mild_hw += 1
            
        elif (hwife_DASS_score[ma][l+4]>=19 and hwife_DASS_score[ma][l+4]<26):
            moderate_hw += 1
            
        elif (hwife_DASS_score[ma][l+4]>=26 and hwife_DASS_score[ma][l+4]<34):
            severe_hw += 1
            
        else:
            extreme_hw += 1
            
            
        ############## for no corp business stress ############# 
    for o in range(len(corp_buisness_DASS_score)):

        if (corp_buisness_DASS_score[o][l+4]>=0 and corp_buisness_DASS_score[o][l+4]<15):
            normal_cb += 1
            
        elif (corp_buisness_DASS_score[o][l+4]>=15 and corp_buisness_DASS_score[o][l+4]<19):
            mild_cb += 1
            
        elif (corp_buisness_DASS_score[o][l+4]>=19 and corp_buisness_DASS_score[o][l+4]<26):
            moderate_cb += 1
            
        elif (corp_buisness_DASS_score[o][l+4]>=26 and corp_buisness_DASS_score[o][l+4]<34):
            severe_cb += 1
            
        else:
            extreme_cb += 1
            
  ############## for student stress ############# 
    for ea in range(len(student_DASS_score)):

        if (student_DASS_score[ea][l+4]>=0 and student_DASS_score[ea][l+4]<15):
            normal_st += 1
            
        elif (student_DASS_score[ea][l+4]>=15 and student_DASS_score[ea][l+4]<19):
            mild_st += 1
            
        elif (student_DASS_score[ea][l+4]>=19 and student_DASS_score[ea][l+4]<26):
            moderate_st += 1
            
        elif (student_DASS_score[ea][l+4]>=26 and student_DASS_score[ea][l+4]<34):
            severe_st += 1
            
        else:
            extreme_st += 1
            
        ############## for retired stress ############# 
    for ma in range(len(retired_DASS_score)):

        if (retired_DASS_score[ma][l+4]>=0 and retired_DASS_score[ma][l+4]<15):
            normal_r += 1
            
        elif (retired_DASS_score[ma][l+4]>=15 and retired_DASS_score[ma][l+4]<19):
            mild_r += 1
            
        elif (retired_DASS_score[ma][l+4]>=19 and retired_DASS_score[ma][l+4]<26):
            moderate_r += 1
            
        elif (retired_DASS_score[ma][l+4]>=26 and retired_DASS_score[ma][l+4]<34):
            severe_r += 1
            
        else:
            extreme_r += 1
            
            
        ############## for no labour stress ############# 
    for o in range(len(labour_DASS_score)):

        if (labour_DASS_score[o][l+4]>=0 and labour_DASS_score[o][l+4]<15):
            normal_l += 1
            
        elif (labour_DASS_score[o][l+4]>=15 and labour_DASS_score[o][l+4]<19):
            mild_l += 1
            
        elif (labour_DASS_score[o][l+4]>=19 and labour_DASS_score[o][l+4]<26):
            moderate_l += 1
            
        elif (labour_DASS_score[o][l+4]>=26 and labour_DASS_score[o][l+4]<34):
            severe_l += 1
            
        else:
            extreme_l += 1
     
          ############## for unemployed stress ############# 
    for o in range(len(unemployed_DASS_score)):

        if (unemployed_DASS_score[o][l+4]>=0 and unemployed_DASS_score[o][l+4]<15):
            normal_ue += 1
            
        elif (unemployed_DASS_score[o][l+4]>=15 and unemployed_DASS_score[o][l+4]<19):
            mild_ue += 1
            
        elif (unemployed_DASS_score[o][l+4]>=19 and unemployed_DASS_score[o][l+4]<26):
            moderate_ue += 1
            
        elif (unemployed_DASS_score[o][l+4]>=26 and unemployed_DASS_score[o][l+4]<34):
            severe_ue += 1
            
        else:
            extreme_ue += 1
           

            
    temp_5 = [[normal_g, mild_g, moderate_g, severe_g, extreme_g],
            [normal_p, mild_p, moderate_p, severe_p, extreme_p],
            [normal_se, mild_se, moderate_se, severe_se, extreme_se],
            [normal_sb, mild_sb, moderate_sb, severe_sb, extreme_sb],
            [normal_hw, mild_hw, moderate_hw, severe_hw, extreme_hw],
            [normal_cb, mild_cb, moderate_cb, severe_cb, extreme_cb],
            [normal_st, mild_st, moderate_st, severe_st, extreme_st],
            [normal_r, mild_r, moderate_r, severe_r, extreme_r],
            [normal_l, mild_l, moderate_l, severe_l, extreme_l],
            [normal_ue, mild_ue, moderate_ue, severe_ue, extreme_ue]]        
            
    profession_stress_count[l] = temp_5[0]  
    profession_stress_count[l+2] = temp_5[1]  
    profession_stress_count[l+4] = temp_5[2]     
    profession_stress_count[l+6] = temp_5[3]        
    profession_stress_count[l+8] = temp_5[4]        
    profession_stress_count[l+10] = temp_5[5]  
    profession_stress_count[l+12] = temp_5[6]     
    profession_stress_count[l+14] = temp_5[7]        
    profession_stress_count[l+16] = temp_5[8]        
    profession_stress_count[l+18] = temp_5[9]       

################ Es filtration for profession #######################


profession_stress_count_es_filter = np.copy(profession_stress_count)


for row in range (0,20,2):
    
    profession_stress_count_es_filter[row][4] = abs(profession_stress_count_es_filter[row][4] - profession_stress_count_es_filter[row][4])
    profession_stress_count_es_filter[row+1][4] = abs(profession_stress_count_es_filter[row+1][4] - profession_stress_count[row][4])


#####################################################################



import seaborn as sns
import matplotlib.pyplot as plt 



y_labels = ['Yes-Frontline','No-Frontline', 'Less than 10,000Rs',
            '10,000Rs-40,000Rs','40,000Rs-100,000Rs','More than 100,000 Rs',
            'N/A','No change','Increased','Descreased','Lost job/No earning',
            'N/A','Same as onsite','More than onsite','Less than onsite',
            'Not working online','N/A','0-4','5-7','8-10','More than 10',
            'Government employee','Private sector employee','Self-employed',
            'Small business/Shopkeeper','Housewife','Corporate Businessman',
            'Student','Retired/Pensioner','Labour/Daily wager','Unemployed']
x_labels = ['Normal','Mild','Moderate','Severe','Extremely Severe']

################# for occupational BC data ###########################
occupation_var_stress_BC = np.zeros((31,5),dtype = np.double)

r = 0
for q in range (0,4,2):
    occupation_var_stress_BC[r] = frontline_stress_count[q] # for age group bc
    r += 1

for q in range (0,10,2):
    occupation_var_stress_BC[r] = income_stress_count[q] # for age group bc
    r += 1

for q in range (0,10,2):
    occupation_var_stress_BC[r] = earning_stress_count[q] #for education bc
    r += 1

for q in range (0,10,2):
    occupation_var_stress_BC[r] = online_stress_count[q]# for marital bc 
    r += 1
    
for q in range (0,8,2):
    occupation_var_stress_BC[r] = dependents_stress_count[q]# for marital bc 
    r += 1
    
for q in range (0,20,2):
    occupation_var_stress_BC[r] = profession_stress_count[q]# for marital bc 
    r += 1    


f, ax = plt.subplots(figsize=(10, 8))

sns.heatmap(occupation_var_stress_BC, vmin = 0, vmax = 1300, xticklabels=x_labels, yticklabels = y_labels, mask=np.zeros_like(occupation_var_stress_BC, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, ax=ax)


#####################################################################


################# for occupational DC data ###########################
occupation_var_stress_DC = np.zeros((31,5),dtype = np.double)

r = 0
for q in range (1,4,2):
    occupation_var_stress_DC[r] = frontline_stress_count[q] # for age group bc
    r += 1

for q in range (1,10,2):
    occupation_var_stress_DC[r] = income_stress_count[q] # for age group bc
    r += 1

for q in range (1,10,2):
    occupation_var_stress_DC[r] = earning_stress_count[q] #for education bc
    r += 1

for q in range (1,10,2):
    occupation_var_stress_DC[r] = online_stress_count[q]# for marital bc 
    r += 1
    
for q in range (1,8,2):
    occupation_var_stress_DC[r] = dependents_stress_count[q]# for marital bc 
    r += 1
    
for q in range (1,20,2):
    occupation_var_stress_DC[r] = profession_stress_count[q]# for marital bc 
    r += 1    


f, ax = plt.subplots(figsize=(10, 8))

sns.heatmap(occupation_var_stress_DC, vmin = 0, vmax = 1300, xticklabels=x_labels, yticklabels = y_labels, mask=np.zeros_like(occupation_var_stress_DC, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, ax=ax)


#####################################################################


################# for occupational BC data with ES filter ###########################
occupation_var_stress_BC_es_filter = np.zeros((31,5),dtype = np.double)

r = 0
for q in range (0,4,2):
    occupation_var_stress_BC_es_filter[r] = frontline_stress_count_es_filter[q] # for age group bc
    r += 1

for q in range (0,10,2):
    occupation_var_stress_BC_es_filter[r] = income_stress_count_es_filter[q] # for age group bc
    r += 1

for q in range (0,10,2):
    occupation_var_stress_BC_es_filter[r] = earning_stress_count_es_filter[q] #for education bc
    r += 1

for q in range (0,10,2):
    occupation_var_stress_BC_es_filter[r] = online_stress_count_es_filter[q]# for marital bc 
    r += 1
    
for q in range (0,8,2):
    occupation_var_stress_BC_es_filter[r] = dependents_stress_count_es_filter[q]# for marital bc 
    r += 1
    
for q in range (0,20,2):
    occupation_var_stress_BC_es_filter[r] = profession_stress_count_es_filter[q]# for marital bc 
    r += 1    


f, ax = plt.subplots(figsize=(10, 8))

sns.heatmap(occupation_var_stress_BC_es_filter, vmin = 0, vmax = 1300, xticklabels=x_labels, yticklabels = y_labels, mask=np.zeros_like(occupation_var_stress_BC_es_filter, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, ax=ax)


#####################################################################


################# for occupational DC data with ES filter ###########################
occupation_var_stress_DC_es_filter = np.zeros((31,5),dtype = np.double)

r = 0
for q in range (1,4,2):
    occupation_var_stress_DC_es_filter[r] = frontline_stress_count_es_filter[q] # for age group bc
    r += 1

for q in range (1,10,2):
    occupation_var_stress_DC_es_filter[r] = income_stress_count_es_filter[q] # for age group bc
    r += 1

for q in range (1,10,2):
    occupation_var_stress_DC_es_filter[r] = earning_stress_count_es_filter[q] #for education bc
    r += 1

for q in range (1,10,2):
    occupation_var_stress_DC_es_filter[r] = online_stress_count_es_filter[q]# for marital bc 
    r += 1
    
for q in range (1,8,2):
    occupation_var_stress_DC_es_filter[r] = dependents_stress_count_es_filter[q]# for marital bc 
    r += 1
    
for q in range (1,20,2):
    occupation_var_stress_DC_es_filter[r] = profession_stress_count_es_filter[q]# for marital bc 
    r += 1    


f, ax = plt.subplots(figsize=(10, 8))

sns.heatmap(occupation_var_stress_DC_es_filter, vmin = 0, vmax = 1300, xticklabels=x_labels, yticklabels = y_labels, mask=np.zeros_like(occupation_var_stress_DC_es_filter, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, ax=ax)


#####################################################################

############################## DC-BC ################################


############################ frontline ##############################

frontline_stress_count_diff = np.zeros((2,5),dtype = np.double)
frontline_count = [Yes_frontline, No_frontline]
a=1
for i in range(2):
    frontline_stress_count_diff[i] = (((frontline_stress_count[a])/frontline_count[i])*100) - (((frontline_stress_count[a-1])/frontline_count[i])*100)
    a += 2

#####################################################################
    
############################ income ##############################

income_stress_count_diff = np.zeros((5,5),dtype = np.double)
income_count = [less_tenk, plus_tenk, fourtyk_plus, hundredk_plus, na]
a=1
for i in range(5):
    income_stress_count_diff[i] = (((income_stress_count[a])/income_count[i])*100) - (((income_stress_count[a-1])/income_count[i])*100)
    a += 2

#####################################################################
    
############################ earning ##############################

earning_stress_count_diff = np.zeros((5,5),dtype = np.double)
earning_count = [no_change, incr, decr, lost_job, na_earn]
a=1
for i in range(5):
    earning_stress_count_diff[i] = (((earning_stress_count[a])/earning_count[i])*100) - (((earning_stress_count[a-1])/earning_count[i])*100)
    a += 2

#####################################################################
    
############################ online ##############################

online_stress_count_diff = np.zeros((5,5),dtype = np.double)
online_count = [same_online, more_online, less_online, not_online, na_online]
a=1
for i in range(5):
    online_stress_count_diff[i] = (((online_stress_count[a])/online_count[i])*100) - (((online_stress_count[a-1])/online_count[i])*100)
    a += 2

####################################################################
       
############################ dependents ##############################

dependents_stress_count_diff = np.zeros((4,5),dtype = np.double)
dependents_count = [lfour, lseven, lten, mten]
a=1
for i in range(4):
    dependents_stress_count_diff[i] = (((dependents_stress_count[a])/dependents_count[i])*100) - (((dependents_stress_count[a-1])/dependents_count[i])*100)
    a += 2

####################################################################
         
############################ profession ##############################

profession_stress_count_diff = np.zeros((10,5),dtype = np.double)
professtion_count = [gov, private, selfemployed, small_buisness, hwife, corp_buisness, student, retired, labour, unemployed]
a=1
for i in range(10):
    profession_stress_count_diff[i] = (((profession_stress_count[a])/professtion_count[i])*100) - (((profession_stress_count[a-1])/professtion_count[i])*100)
    a += 2

####################################################################
     
    
#####################################################################

occupation_var_stress_diff = np.zeros((31,5), dtype = np.double)


for i in range (2):
    occupation_var_stress_diff[i] = frontline_stress_count_diff[i]

for i in range (5):
    occupation_var_stress_diff[i+2] = income_stress_count_diff[i]

for i in range (5):
    occupation_var_stress_diff[i+7] = earning_stress_count_diff[i]

for i in range (5):
    occupation_var_stress_diff[i+12] = online_stress_count_diff[i]

for i in range (4):
    occupation_var_stress_diff[i+17] = dependents_stress_count_diff[i]

for i in range (10):
    occupation_var_stress_diff[i+21] = profession_stress_count_diff[i]


f, ax = plt.subplots(figsize=(10, 8))

sns.heatmap(occupation_var_stress_diff, vmin=-50, vmax=50, xticklabels=x_labels, yticklabels = y_labels, mask=np.zeros_like(occupation_var_stress_diff, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, ax=ax)

