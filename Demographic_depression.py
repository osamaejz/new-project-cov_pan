from DASS_calculation import survey_data , DASS_score
import numpy as np
################ Demographic_Gender ################
gender = []
gender = survey_data['Gender']
male_count,female_count = survey_data['Gender'].value_counts()

male_DASS_score = np.zeros((male_count,6),dtype = np.double)
female_DASS_score = np.zeros((female_count,6),dtype = np.double)
m_val = 0
f_val = 0
for gender_value in range (len(survey_data)):
    if gender[gender_value] == 'Male':
        for i in range(6):   
            male_DASS_score[m_val][i] = DASS_score[gender_value][i]
        m_val += 1
    elif gender[gender_value] == 'Female':
        for j in range(6):       
            female_DASS_score[f_val][j] = DASS_score[gender_value][j]
        f_val += 1
        
####################################################
        
        
################# Male DASS count ####################

male_DASS_count = np.zeros((6,5),dtype = np.double)


for l in range (2):
    d_normal = 0
    d_mild = 0
    d_moderate = 0
    d_severe = 0
    d_extreme = 0
    
    a_normal = 0
    a_mild = 0
    a_moderate = 0
    a_severe = 0
    a_extreme = 0
    
    s_normal = 0
    s_mild = 0
    s_moderate = 0
    s_severe = 0
    s_extreme = 0
    for k in range(len(male_DASS_score)):
       
        ############## for depression ############# 

        if (male_DASS_score[k][l]>=0 and male_DASS_score[k][l]<10):
            d_normal += 1
            
        elif (male_DASS_score[k][l]>=10 and male_DASS_score[k][l]<14):
            d_mild += 1
            
        elif (male_DASS_score[k][l]>=14 and male_DASS_score[k][l]<21):
            d_moderate += 1
            
        elif (male_DASS_score[k][l]>=21 and male_DASS_score[k][l]<28):
            d_severe += 1
            
        else:
            d_extreme += 1
            
       ############## for anxiety ############# 
        if (male_DASS_score[k][l+2]>=0 and male_DASS_score[k][l+2]<8):
            a_normal += 1
            
        elif (male_DASS_score[k][l+2]>=8 and male_DASS_score[k][l+2]<10):
            a_mild += 1
            
        elif (male_DASS_score[k][l+2]>=10 and male_DASS_score[k][l+2]<15):
            a_moderate += 1
            
        elif (male_DASS_score[k][l+2]>=15 and male_DASS_score[k][l+2]<20):
            a_severe += 1
            
        else:
            a_extreme += 1
            
        ############## for stress ############# 
        if (male_DASS_score[k][l+4]>=0 and male_DASS_score[k][l+4]<15):
            s_normal += 1
            
        elif (male_DASS_score[k][l+4]>=15 and male_DASS_score[k][l+4]<19):
            s_mild += 1
            
        elif (male_DASS_score[k][l+4]>=19 and male_DASS_score[k][l+4]<26):
            s_moderate += 1
            
        elif (male_DASS_score[k][l+4]>=26 and male_DASS_score[k][l+4]<34):
            s_severe += 1
            
        else:
            s_extreme += 1
            
             
    temp_2 = [[d_normal, d_mild, d_moderate, d_severe, d_extreme],
            [a_normal, a_mild, a_moderate, a_severe, a_extreme],
            [s_normal, s_mild, s_moderate, s_severe, s_extreme]]        
            
    male_DASS_count[l] = temp_2[0]  
    male_DASS_count[l+2] = temp_2[1]  
    male_DASS_count[l+4] = temp_2[2]
    

#################################################################


################# Female DASS count ####################

female_DASS_count = np.zeros((6,5),dtype = np.double)


for l in range (2):
    d_normal = 0
    d_mild = 0
    d_moderate = 0
    d_severe = 0
    d_extreme = 0
    
    a_normal = 0
    a_mild = 0
    a_moderate = 0
    a_severe = 0
    a_extreme = 0
    
    s_normal = 0
    s_mild = 0
    s_moderate = 0
    s_severe = 0
    s_extreme = 0
    for k in range(len(female_DASS_score)):
       
        ############## for depression ############# 

        if (female_DASS_score[k][l]>=0 and female_DASS_score[k][l]<10):
            d_normal += 1
            
        elif (female_DASS_score[k][l]>=10 and female_DASS_score[k][l]<14):
            d_mild += 1
            
        elif (female_DASS_score[k][l]>=14 and female_DASS_score[k][l]<21):
            d_moderate += 1
            
        elif (female_DASS_score[k][l]>=21 and female_DASS_score[k][l]<28):
            d_severe += 1
            
        else:
            d_extreme += 1
            
       ############## for anxiety ############# 
        if (female_DASS_score[k][l+2]>=0 and female_DASS_score[k][l+2]<8):
            a_normal += 1
            
        elif (female_DASS_score[k][l+2]>=8 and female_DASS_score[k][l+2]<10):
            a_mild += 1
            
        elif (female_DASS_score[k][l+2]>=10 and female_DASS_score[k][l+2]<15):
            a_moderate += 1
            
        elif (female_DASS_score[k][l+2]>=15 and female_DASS_score[k][l+2]<20):
            a_severe += 1
            
        else:
            a_extreme += 1
            
        ############## for stress ############# 
        if (female_DASS_score[k][l+4]>=0 and female_DASS_score[k][l+4]<15):
            s_normal += 1
            
        elif (female_DASS_score[k][l+4]>=15 and female_DASS_score[k][l+4]<19):
            s_mild += 1
            
        elif (female_DASS_score[k][l+4]>=19 and female_DASS_score[k][l+4]<26):
            s_moderate += 1
            
        elif (female_DASS_score[k][l+4]>=26 and female_DASS_score[k][l+4]<34):
            s_severe += 1
            
        else:
            s_extreme += 1
            
    temp_3 = [[d_normal, d_mild, d_moderate, d_severe, d_extreme],
            [a_normal, a_mild, a_moderate, a_severe, a_extreme],
            [s_normal, s_mild, s_moderate, s_severe, s_extreme]]        
            
    female_DASS_count[l] = temp_3[0]  
    female_DASS_count[l+2] = temp_3[1]  
    female_DASS_count[l+4] = temp_3[2]        
#####################################################################

################ BC extremely severe subtraction ####################  

male_DASS_count_es_filter = np.copy(male_DASS_count)
female_DASS_count_es_filter = np.copy(female_DASS_count)


for row in range (0,6,2):
    
    male_DASS_count_es_filter[row][4] = abs(male_DASS_count_es_filter[row][4] - male_DASS_count_es_filter[row][4])
    male_DASS_count_es_filter[row+1][4] = abs(male_DASS_count_es_filter[row+1][4] - male_DASS_count[row][4])

    female_DASS_count_es_filter[row][4] = abs(female_DASS_count_es_filter[row][4] - female_DASS_count_es_filter[row][4])
    female_DASS_count_es_filter[row+1][4] = abs(female_DASS_count_es_filter[row+1][4] - female_DASS_count[row][4])





######################## Demographic_Age ###############
age_group = []
age_group = survey_data['Age']
young,early_adulthood,middle_adulthood,youngest,old_age,children = survey_data['Age'].value_counts()


young_DASS_score = np.zeros((young,6),dtype = np.double)
early_adulthood_DASS_score = np.zeros((early_adulthood,6),dtype = np.double)
middle_adulthood_DASS_score = np.zeros((middle_adulthood,6),dtype = np.double)
youngest_DASS_score = np.zeros((youngest,6),dtype = np.double)
old_age_DASS_score = np.zeros((old_age,6),dtype = np.double)
children_DASS_score = np.zeros((children,6),dtype = np.double)


val_22 = 0
val_33 = 0
val_50 = 0
val_17 = 0
val_70 = 0
val_10 = 0
for age_value in range (len(survey_data)):
    if age_group[age_value] == '19years26years':
        for i in range(6):   
            young_DASS_score[val_22][i] = DASS_score[age_value][i]
        val_22 += 1
        
    elif age_group[age_value] == '27years40years':
        for j in range(6):       
            early_adulthood_DASS_score[val_33][j] = DASS_score[age_value][j]
        val_33 += 1
        
    elif age_group[age_value] == '41years60years':
        for i in range(6):   
            middle_adulthood_DASS_score[val_50][i] = DASS_score[age_value][i]
        val_50 += 1
        
    elif age_group[age_value] == '15years18years':
        for i in range(6):   
            youngest_DASS_score[val_17][i] = DASS_score[age_value][i]
        val_17 += 1
        
    elif age_group[age_value] == 'Greaterthan60years':
        for i in range(6):   
            old_age_DASS_score[val_70][i] = DASS_score[age_value][i]
        val_70 += 1
        
    elif age_group[age_value] == 'Lessthan15years':
        for i in range(6):   
            children_DASS_score[val_10][i] = DASS_score[age_value][i]
        val_10 += 1


############# Age depression count ##############

age_depression_count = np.zeros((12,5),dtype = np.double)


for l in range (2):
    normal_10 = 0
    mild_10 = 0
    moderate_10 = 0
    severe_10 = 0
    extreme_10 = 0
    
    normal_17 = 0
    mild_17 = 0
    moderate_17 = 0
    severe_17 = 0
    extreme_17 = 0
    
    normal_22 = 0
    mild_22 = 0
    moderate_22 = 0
    severe_22 = 0
    extreme_22 = 0
    
    normal_33 = 0
    mild_33 = 0
    moderate_33 = 0
    severe_33 = 0
    extreme_33 = 0
    
    normal_50 = 0
    mild_50 = 0
    moderate_50 = 0
    severe_50 = 0
    extreme_50 = 0
    
    normal_70 = 0
    mild_70 = 0
    moderate_70 = 0
    severe_70 = 0
    extreme_70 = 0
    
    for c in range(len(children_DASS_score)):
       
        ############## for less than 15 depression ############# 

        if (children_DASS_score[c][l]>=0 and children_DASS_score[c][l]<10):
            normal_10 += 1
            
        elif (children_DASS_score[c][l]>=10 and children_DASS_score[c][l]<14):
            mild_10 += 1
            
        elif (children_DASS_score[c][l]>=14 and children_DASS_score[c][l]<21):
            moderate_10 += 1
            
        elif (children_DASS_score[c][l]>=21 and children_DASS_score[c][l]<28):
            severe_10 += 1
            
        else:
            extreme_10 += 1
        
        ############## for 15-18 depression ############# 
    for ys in range(len(youngest_DASS_score)):
    
        if (youngest_DASS_score[ys][l]>=0 and youngest_DASS_score[ys][l]<10):
            normal_17 += 1
            
        elif (youngest_DASS_score[ys][l]>=10 and youngest_DASS_score[ys][l]<14):
            mild_17 += 1
            
        elif (youngest_DASS_score[ys][l]>=14 and youngest_DASS_score[ys][l]<21):
            moderate_17 += 1
            
        elif (youngest_DASS_score[ys][l]>=21 and youngest_DASS_score[ys][l]<28):
            severe_17 += 1
            
        else:
            extreme_17 += 1
            
        ############## for 19-26 depression ############# 
    for y in range(len(young_DASS_score)):

        if (young_DASS_score[y][l]>=0 and young_DASS_score[y][l]<10):
            normal_22 += 1
            
        elif (young_DASS_score[y][l]>=10 and young_DASS_score[y][l]<14):
            mild_22 += 1
            
        elif (young_DASS_score[y][l]>=14 and young_DASS_score[y][l]<21):
            moderate_22 += 1
            
        elif (young_DASS_score[y][l]>=21 and young_DASS_score[y][l]<28):
            severe_22 += 1
            
        else:
            extreme_22 += 1
            
        ############## for 27-40 depression ############# 
    for ea in range(len(early_adulthood_DASS_score)):

        if (early_adulthood_DASS_score[ea][l]>=0 and early_adulthood_DASS_score[ea][l]<10):
            normal_33 += 1
            
        elif (early_adulthood_DASS_score[ea][l]>=10 and early_adulthood_DASS_score[ea][l]<14):
            mild_33 += 1
            
        elif (early_adulthood_DASS_score[ea][l]>=14 and early_adulthood_DASS_score[ea][l]<21):
            moderate_33 += 1
            
        elif (early_adulthood_DASS_score[ea][l]>=21 and early_adulthood_DASS_score[ea][l]<28):
            severe_33 += 1
            
        else:
            extreme_33 += 1
            
        ############## for 41-60 depression ############# 
    for ma in range(len(middle_adulthood_DASS_score)):

        if (middle_adulthood_DASS_score[ma][l]>=0 and middle_adulthood_DASS_score[ma][l]<10):
            normal_50 += 1
            
        elif (middle_adulthood_DASS_score[ma][l]>=10 and middle_adulthood_DASS_score[ma][l]<14):
            mild_50 += 1
            
        elif (middle_adulthood_DASS_score[ma][l]>=14 and middle_adulthood_DASS_score[ma][l]<21):
            moderate_50 += 1
            
        elif (middle_adulthood_DASS_score[ma][l]>=21 and middle_adulthood_DASS_score[ma][l]<28):
            severe_50 += 1
            
        else:
            extreme_50 += 1
            
            
        ############## for 60+ depression ############# 
    for o in range(len(old_age_DASS_score)):

        if (old_age_DASS_score[o][l]>=0 and old_age_DASS_score[o][l]<10):
            normal_70 += 1
            
        elif (old_age_DASS_score[o][l]>=10 and old_age_DASS_score[o][l]<14):
            mild_70 += 1
            
        elif (old_age_DASS_score[o][l]>=14 and old_age_DASS_score[o][l]<21):
            moderate_70 += 1
            
        elif (old_age_DASS_score[o][l]>=21 and old_age_DASS_score[o][l]<28):
            severe_70 += 1
            
        else:
            extreme_70 += 1
            
            
    temp_4 = [[normal_10, mild_10, moderate_10, severe_10, extreme_10],
            [normal_17, mild_17, moderate_17, severe_17, extreme_17],
            [normal_22, mild_22, moderate_22, severe_22, extreme_22],
            [normal_33, mild_33, moderate_33, severe_33, extreme_33],
            [normal_50, mild_50, moderate_50, severe_50, extreme_50],
            [normal_70, mild_70, moderate_70, severe_70, extreme_70],]        
            
    age_depression_count[l] = temp_4[0]  
    age_depression_count[l+2] = temp_4[1]  
    age_depression_count[l+4] = temp_4[2]     
    age_depression_count[l+6] = temp_4[3]        
    age_depression_count[l+8] = temp_4[4]        
    age_depression_count[l+10] = temp_4[5]        

################ Es filtration for age group #######################


age_depression_count_es_filter = np.copy(age_depression_count)


for row in range (0,12,2):
    
    age_depression_count_es_filter[row][4] = abs(age_depression_count_es_filter[row][4] - age_depression_count_es_filter[row][4])
    age_depression_count_es_filter[row+1][4] = abs(age_depression_count_es_filter[row+1][4] - age_depression_count[row][4])

 



#####################################################################

################### Demographic_Education ###########################
    
education = []
education = survey_data['Education']
BachelorDiploma,Master,FScIntermediate,PhD,Matric,Schoolstudent,Illiterate = survey_data['Education'].value_counts()



bachelor_DASS_score = np.zeros((BachelorDiploma,6),dtype = np.double)
master_DASS_score = np.zeros((Master,6),dtype = np.double)
inter_DASS_score = np.zeros((FScIntermediate,6),dtype = np.double)
phd_DASS_score = np.zeros((PhD,6),dtype = np.double)
matric_DASS_score = np.zeros((Matric,6),dtype = np.double)
illiterate_DASS_score = np.zeros((Illiterate,6),dtype = np.double)
school_student_DASS_score = np.zeros((Schoolstudent,6),dtype = np.double)



val_b = 0
val_m = 0
val_i = 0
val_p = 0
val_mat = 0
val_ill = 0
val_sch = 0
for edu_value in range (len(survey_data)):
    if education[edu_value] == 'BachelorDiploma':
        for i in range(6):   
            bachelor_DASS_score[val_b][i] = DASS_score[edu_value][i]
        val_b += 1
        
    elif education[edu_value] == 'Master':
        for j in range(6):       
            master_DASS_score[val_m][j] = DASS_score[edu_value][j]
        val_m += 1
        
    elif education[edu_value] == 'FScIntermediate':
        for i in range(6):   
            inter_DASS_score[val_i][i] = DASS_score[edu_value][i]
        val_i += 1
        
    elif education[edu_value] == 'PhD':
        for i in range(6):   
            phd_DASS_score[val_p][i] = DASS_score[edu_value][i]
        val_p += 1
        
    elif education[edu_value] == 'Matric':
        for i in range(6):   
            matric_DASS_score[val_mat][i] = DASS_score[edu_value][i]
        val_mat += 1
        
    elif education[edu_value] == 'Illiterate':
        for i in range(6):   
            illiterate_DASS_score[val_ill][i] = DASS_score[edu_value][i]
        val_ill += 1

    elif education[edu_value] == 'Schoolstudent':
        for i in range(6):   
            school_student_DASS_score[val_sch][i] = DASS_score[edu_value][i]
        val_sch += 1
    
#################### Education DASS count #################



education_depression_count = np.zeros((14,5),dtype = np.double)


for l in range (2):
    normal_b = 0
    mild_b = 0
    moderate_b = 0
    severe_b = 0
    extreme_b = 0
    
    normal_m = 0
    mild_m = 0
    moderate_m = 0
    severe_m = 0
    extreme_m = 0
    
    normal_i = 0
    mild_i = 0
    moderate_i = 0
    severe_i = 0
    extreme_i = 0
    
    normal_p = 0
    mild_p = 0
    moderate_p = 0
    severe_p = 0
    extreme_p = 0
    
    normal_mat = 0
    mild_mat = 0
    moderate_mat = 0
    severe_mat = 0
    extreme_mat = 0
    
    normal_ill = 0
    mild_ill = 0
    moderate_ill = 0
    severe_ill = 0
    extreme_ill = 0
    
    normal_sch = 0
    mild_sch = 0
    moderate_sch = 0
    severe_sch = 0
    extreme_sch = 0
    
    for c in range(len(illiterate_DASS_score)):
       
        ############## for illiterate depression ############# 

        if (illiterate_DASS_score[c][l]>=0 and illiterate_DASS_score[c][l]<10):
            normal_ill += 1
            
        elif (illiterate_DASS_score[c][l]>=10 and illiterate_DASS_score[c][l]<14):
            mild_ill += 1
            
        elif (illiterate_DASS_score[c][l]>=14 and illiterate_DASS_score[c][l]<21):
            moderate_ill += 1
            
        elif (illiterate_DASS_score[c][l]>=21 and illiterate_DASS_score[c][l]<28):
            severe_ill += 1
            
        else:
            extreme_ill += 1
        
        ############## for school student depression ############# 
    for ys in range(len(school_student_DASS_score)):
    
        if (school_student_DASS_score[ys][l]>=0 and school_student_DASS_score[ys][l]<10):
            normal_sch += 1
            
        elif (school_student_DASS_score[ys][l]>=10 and school_student_DASS_score[ys][l]<14):
            mild_sch += 1
            
        elif (school_student_DASS_score[ys][l]>=14 and school_student_DASS_score[ys][l]<21):
            moderate_sch += 1
            
        elif (school_student_DASS_score[ys][l]>=21 and school_student_DASS_score[ys][l]<28):
            severe_sch += 1
            
        else:
            extreme_sch += 1
            
        ############## for matric depression ############# 
    for y in range(len(matric_DASS_score)):

        if (matric_DASS_score[y][l]>=0 and matric_DASS_score[y][l]<10):
            normal_mat += 1
            
        elif (matric_DASS_score[y][l]>=10 and matric_DASS_score[y][l]<14):
            mild_mat += 1
            
        elif (matric_DASS_score[y][l]>=14 and matric_DASS_score[y][l]<21):
            moderate_mat += 1
            
        elif (matric_DASS_score[y][l]>=21 and matric_DASS_score[y][l]<28):
            severe_mat += 1
            
        else:
            extreme_mat += 1
            
        ############## for inter depression ############# 
    for ea in range(len(inter_DASS_score)):

        if (inter_DASS_score[ea][l]>=0 and inter_DASS_score[ea][l]<10):
            normal_i += 1
            
        elif (inter_DASS_score[ea][l]>=10 and inter_DASS_score[ea][l]<14):
            mild_i += 1
            
        elif (inter_DASS_score[ea][l]>=14 and inter_DASS_score[ea][l]<21):
            moderate_i += 1
            
        elif (inter_DASS_score[ea][l]>=21 and inter_DASS_score[ea][l]<28):
            severe_i += 1
            
        else:
            extreme_i += 1
            
        ############## for bachelor depression ############# 
    for ma in range(len(bachelor_DASS_score)):

        if (bachelor_DASS_score[ma][l]>=0 and bachelor_DASS_score[ma][l]<10):
            normal_b += 1
            
        elif (bachelor_DASS_score[ma][l]>=10 and bachelor_DASS_score[ma][l]<14):
            mild_b += 1
            
        elif (bachelor_DASS_score[ma][l]>=14 and bachelor_DASS_score[ma][l]<21):
            moderate_b += 1
            
        elif (bachelor_DASS_score[ma][l]>=21 and bachelor_DASS_score[ma][l]<28):
            severe_b += 1
            
        else:
            extreme_b += 1
            
            
        ############## for master depression ############# 
    for o in range(len(master_DASS_score)):

        if (master_DASS_score[o][l]>=0 and master_DASS_score[o][l]<10):
            normal_m += 1
            
        elif (master_DASS_score[o][l]>=10 and master_DASS_score[o][l]<14):
            mild_m += 1
            
        elif (master_DASS_score[o][l]>=14 and master_DASS_score[o][l]<21):
            moderate_m += 1
            
        elif (master_DASS_score[o][l]>=21 and master_DASS_score[o][l]<28):
            severe_m += 1
            
        else:
            extreme_m += 1
 
        ############## for phd depression ############# 
           
    for o in range(len(phd_DASS_score)):

        if (phd_DASS_score[o][l]>=0 and phd_DASS_score[o][l]<10):
            normal_p += 1
            
        elif (phd_DASS_score[o][l]>=10 and phd_DASS_score[o][l]<14):
            mild_p += 1
            
        elif (phd_DASS_score[o][l]>=14 and phd_DASS_score[o][l]<21):
            moderate_p += 1
            
        elif (phd_DASS_score[o][l]>=21 and phd_DASS_score[o][l]<28):
            severe_p += 1
            
        else:
            extreme_p += 1
            
            
    temp_5 = [[normal_ill, mild_ill, moderate_ill, severe_ill, extreme_ill],
              [normal_sch, mild_sch, moderate_sch, severe_sch, extreme_sch],
              [normal_mat, mild_mat, moderate_mat, severe_mat, extreme_mat],
              [normal_i, mild_i, moderate_i, severe_i, extreme_i],
              [normal_b, mild_b, moderate_b, severe_b, extreme_b],
              [normal_m, mild_m, moderate_m, severe_m, extreme_m],
              [normal_p, mild_p, moderate_p, severe_p, extreme_p]]        
            
    education_depression_count[l] = temp_5[0]  
    education_depression_count[l+2] = temp_5[1]  
    education_depression_count[l+4] = temp_5[2]     
    education_depression_count[l+6] = temp_5[3]        
    education_depression_count[l+8] = temp_5[4]        
    education_depression_count[l+10] = temp_5[5]    
    education_depression_count[l+12] = temp_5[6]       

#####################################################################

################ Es filtration for education #######################


education_depression_count_es_filter = np.copy(education_depression_count)


for row in range (0,14,2):
    
    education_depression_count_es_filter[row][4] = abs(education_depression_count_es_filter[row][4] - education_depression_count_es_filter[row][4])
    education_depression_count_es_filter[row+1][4] = abs(education_depression_count_es_filter[row+1][4] - education_depression_count[row][4])

 



#####################################################################

##################### Demographic Marital status ####################
    

marital = []
marital = survey_data['Marital Status']
Single,Married,Divorced,WidowWidower= survey_data['Marital Status'].value_counts()



single_DASS_score = np.zeros((Single,6),dtype = np.double)
married_DASS_score = np.zeros((Married,6),dtype = np.double)
widow_DASS_score = np.zeros((WidowWidower,6),dtype = np.double)
divorced_DASS_score = np.zeros((Divorced,6),dtype = np.double)



val_sin = 0
val_mar = 0
val_wid = 0
val_div = 0

for marital_value in range (len(survey_data)):
    if marital[marital_value] == 'Single':
        for i in range(6):   
            single_DASS_score[val_sin][i] = DASS_score[marital_value][i]
        val_sin += 1
        
    elif marital[marital_value] == 'Married':
        for j in range(6):       
            married_DASS_score[val_mar][j] = DASS_score[marital_value][j]
        val_mar += 1
        
    elif marital[marital_value] == 'WidowWidower':
        for i in range(6):   
            widow_DASS_score[val_wid][i] = DASS_score[marital_value][i]
        val_wid += 1
        
    elif marital[marital_value] == 'Divorced':
        for i in range(6):   
            divorced_DASS_score[val_div][i] = DASS_score[marital_value][i]
        val_div += 1
   
################### for marital depression count ########
marital_depression_count = np.zeros((8,5),dtype = np.double)


for l in range (2):
    normal_sin = 0
    mild_sin = 0
    moderate_sin = 0
    severe_sin = 0
    extreme_sin = 0
    
    normal_mar = 0
    mild_mar = 0
    moderate_mar = 0
    severe_mar = 0
    extreme_mar = 0
    
    normal_wid = 0
    mild_wid = 0
    moderate_wid = 0
    severe_wid = 0
    extreme_wid = 0
    
    normal_div = 0
    mild_div = 0
    moderate_div = 0
    severe_div = 0
    extreme_div = 0
    
    for c in range(len(single_DASS_score)):
       
        ############## for less than 15 depression ############# 

        if (single_DASS_score[c][l]>=0 and single_DASS_score[c][l]<10):
            normal_sin += 1
            
        elif (single_DASS_score[c][l]>=10 and single_DASS_score[c][l]<14):
            mild_sin += 1
            
        elif (single_DASS_score[c][l]>=14 and single_DASS_score[c][l]<21):
            moderate_sin += 1
            
        elif (single_DASS_score[c][l]>=21 and single_DASS_score[c][l]<28):
            severe_sin += 1
            
        else:
            extreme_sin += 1
        
        ############## for 15-18 depression ############# 
    for ys in range(len(married_DASS_score)):
    
        if (married_DASS_score[ys][l]>=0 and married_DASS_score[ys][l]<10):
            normal_mar += 1
            
        elif (married_DASS_score[ys][l]>=10 and married_DASS_score[ys][l]<14):
            mild_mar += 1
            
        elif (married_DASS_score[ys][l]>=14 and married_DASS_score[ys][l]<21):
            moderate_mar += 1
            
        elif (married_DASS_score[ys][l]>=21 and married_DASS_score[ys][l]<28):
            severe_mar += 1
            
        else:
            extreme_mar += 1
            
        ############## for 19-26 depression ############# 
    for y in range(len(widow_DASS_score)):

        if (widow_DASS_score[y][l]>=0 and widow_DASS_score[y][l]<10):
            normal_wid += 1
            
        elif (widow_DASS_score[y][l]>=10 and widow_DASS_score[y][l]<14):
            mild_wid += 1
            
        elif (widow_DASS_score[y][l]>=14 and widow_DASS_score[y][l]<21):
            moderate_wid += 1
            
        elif (widow_DASS_score[y][l]>=21 and widow_DASS_score[y][l]<28):
            severe_wid += 1
            
        else:
            extreme_wid += 1
            
        ############## for 27-40 depression ############# 
    for ea in range(len(divorced_DASS_score)):

        if (divorced_DASS_score[ea][l]>=0 and divorced_DASS_score[ea][l]<10):
            normal_div += 1
            
        elif (divorced_DASS_score[ea][l]>=10 and divorced_DASS_score[ea][l]<14):
            mild_div += 1
            
        elif (divorced_DASS_score[ea][l]>=14 and divorced_DASS_score[ea][l]<21):
            moderate_div += 1
            
        elif (divorced_DASS_score[ea][l]>=21 and divorced_DASS_score[ea][l]<28):
            severe_div += 1
            
        else:
            extreme_div += 1
        
            
    temp_6 = [[normal_sin, mild_sin, moderate_sin, severe_sin, extreme_sin],
              [normal_mar, mild_mar, moderate_mar, severe_mar, extreme_mar],
              [normal_wid, mild_wid, moderate_wid, severe_wid, extreme_wid],
              [normal_div, mild_div, moderate_div, severe_div, extreme_div]]        
            
    marital_depression_count[l] = temp_6[0]  
    marital_depression_count[l+2] = temp_6[1]  
    marital_depression_count[l+4] = temp_6[2]     
    marital_depression_count[l+6] = temp_6[3]        
  
#####################################################################

################ Es filtration for marital  #######################


marital_depression_count_es_filter = np.copy(marital_depression_count)


for row in range (0,8,2):
    
    marital_depression_count_es_filter[row][4] = abs(marital_depression_count_es_filter[row][4] - marital_depression_count_es_filter[row][4])
    marital_depression_count_es_filter[row+1][4] = abs(marital_depression_count_es_filter[row+1][4] - marital_depression_count[row][4])

 


################ demographic family member 60+ #######################
    
    
plus60 = []
plus60 = survey_data['Family member 60+']
yes_60,no_60= survey_data['Family member 60+'].value_counts()



yes_60_DASS_score = np.zeros((yes_60,6),dtype = np.double)
no_60_DASS_score = np.zeros((no_60,6),dtype = np.double)

val_yes_60 = 0
val_no_60 = 0

for value_plus_60 in range (len(survey_data)):
    if plus60[value_plus_60] == 'Yes':
        for i in range(6):   
            yes_60_DASS_score[val_yes_60][i] = DASS_score[value_plus_60][i]
        val_yes_60 += 1
        
    elif plus60[value_plus_60] == 'No':
        for j in range(6):       
            no_60_DASS_score[val_no_60][j] = DASS_score[value_plus_60][j]
        val_no_60 += 1

################### 60 + depression count ##################

plus_60_depression_count = np.zeros((4,5),dtype = np.double)


for l in range (2):
    normal_y60 = 0
    mild_y60= 0
    moderate_y60 = 0
    severe_y60 = 0
    extreme_y60 = 0
    
    normal_n60 = 0
    mild_n60 = 0
    moderate_n60 = 0
    severe_n60 = 0
    extreme_n60 = 0
    
    for y in range(len(yes_60_DASS_score)):

        if (yes_60_DASS_score[y][l]>=0 and yes_60_DASS_score[y][l]<10):
            normal_y60 += 1
            
        elif (yes_60_DASS_score[y][l]>=10 and yes_60_DASS_score[y][l]<14):
            mild_y60 += 1
            
        elif (yes_60_DASS_score[y][l]>=14 and yes_60_DASS_score[y][l]<21):
            moderate_y60 += 1
            
        elif (yes_60_DASS_score[y][l]>=21 and yes_60_DASS_score[y][l]<28):
            severe_y60 += 1
            
        else:
            extreme_y60 += 1
            
        ############## for 27-40 depression ############# 
    for ea in range(len(no_60_DASS_score)):

        if (no_60_DASS_score[ea][l]>=0 and no_60_DASS_score[ea][l]<10):
            normal_n60 += 1
            
        elif (no_60_DASS_score[ea][l]>=10 and no_60_DASS_score[ea][l]<14):
            mild_n60 += 1
            
        elif (no_60_DASS_score[ea][l]>=14 and no_60_DASS_score[ea][l]<21):
            moderate_n60 += 1
            
        elif (no_60_DASS_score[ea][l]>=21 and no_60_DASS_score[ea][l]<28):
            severe_n60 += 1
            
        else:
            extreme_n60 += 1
        
            
    temp_7 = [[normal_y60, mild_y60, moderate_y60, severe_y60, extreme_y60],
              [normal_n60, mild_n60, moderate_n60, severe_n60, extreme_n60]]        
            
    plus_60_depression_count[l] = temp_7[0]  
    plus_60_depression_count[l+2] = temp_7[1]  
     
  
#####################################################################

################ Es filtration for 60+  #########################


plus_60_depression_count_es_filter = np.copy(plus_60_depression_count)


for row in range (0,4,2):
    
    plus_60_depression_count_es_filter[row][4] = abs(plus_60_depression_count_es_filter[row][4] - plus_60_depression_count_es_filter[row][4])
    plus_60_depression_count_es_filter[row+1][4] = abs(plus_60_depression_count_es_filter[row+1][4] - plus_60_depression_count[row][4])

 

####################################################################

import seaborn as sns
import matplotlib.pyplot as plt 

y_labels = ['Male','Female','Less than 15 years','15-18 years','19-26 years',
          '27-40 years','41-60 years','More than 60 years','Illiterate',
          'School student','Matric','FSc/Intermediate','Bachelor/Diploma',
          'Masters','PhD','Single','Married','Widow','Divorced',
          'Yes-60+ family member','No-60+ family member']
x_labels = ['Normal','Mild','Moderate','Severe','Extremely Severe']

################# for demographic BC data ###########################
demographic_depression_BC = np.zeros((21,5),dtype = np.double)

demographic_depression_BC[0] = male_DASS_count[0] # for male_gender bc
demographic_depression_BC[1] = female_DASS_count[0] # for female gender bc
r = 2
for q in range (0,11,2):
    demographic_depression_BC[r] = age_depression_count[q] # for age group bc
    r += 1
r = 8
for q in range (0,13,2):
    demographic_depression_BC[r] = education_depression_count[q] #for education bc
    r += 1
r = 15
for q in range (0,7,2):
    demographic_depression_BC[r] = marital_depression_count[q]# for marital bc 
    r += 1
demographic_depression_BC[19] = plus_60_depression_count[0]# for yes 60+ bc 
demographic_depression_BC[20] = plus_60_depression_count[2]# for no 60+ bc


f, ax = plt.subplots(figsize=(10, 8))

sns.heatmap(demographic_depression_BC, vmin=0, vmax=900, xticklabels=x_labels, yticklabels = y_labels, mask=np.zeros_like(demographic_depression_BC, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, ax=ax)


#####################################################################


################# for demographic DC data ###########################
demographic_depression_DC = np.zeros((21,5),dtype = np.double)

demographic_depression_DC[0] = male_DASS_count[1] # for male_gender bc
demographic_depression_DC[1] = female_DASS_count[1] # for female gender bc

r = 2
for q in range (1,12,2):
    demographic_depression_DC[r] = age_depression_count[q] # for age group bc
    r += 1

r = 8
for q in range (1,14,2):
    demographic_depression_DC[r] = education_depression_count[q] #for education bc
    r += 1
    
r = 15
for q in range (1,8,2):
    demographic_depression_DC[r] = marital_depression_count[q]# for marital bc 
    r += 1
    
demographic_depression_DC[19] = plus_60_depression_count[0]# for yes 60+ bc 
demographic_depression_DC[20] = plus_60_depression_count[2]# for no 60+ bc
 

f, ax = plt.subplots(figsize=(10, 8))

sns.heatmap(demographic_depression_DC, vmin=0, vmax=900, xticklabels=x_labels, yticklabels = y_labels,  mask=np.zeros_like(demographic_depression_DC, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, ax=ax)


#####################################################################



################# for demographic BC data with es filter ###########################
demographic_depression_BC_es_filter = np.zeros((21,5),dtype = np.double)

demographic_depression_BC_es_filter[0] = male_DASS_count_es_filter[0] # for male_gender bc
demographic_depression_BC_es_filter[1] = female_DASS_count_es_filter[0] # for female gender bc
r = 2
for q in range (0,11,2):
    demographic_depression_BC_es_filter[r] = age_depression_count_es_filter[q] # for age group bc
    r += 1
r = 8
for q in range (0,13,2):
    demographic_depression_BC_es_filter[r] = education_depression_count_es_filter[q] #for education bc
    r += 1
r = 15
for q in range (0,7,2):
    demographic_depression_BC_es_filter[r] = marital_depression_count_es_filter[q]# for marital bc 
    r += 1
demographic_depression_BC_es_filter[19] = plus_60_depression_count_es_filter[0]# for yes 60+ bc 
demographic_depression_BC_es_filter[20] = plus_60_depression_count_es_filter[2]# for no 60+ bc
 

f, ax = plt.subplots(figsize=(10, 8))

sns.heatmap(demographic_depression_BC_es_filter, vmin=0, vmax=900, xticklabels=x_labels, yticklabels = y_labels,  mask=np.zeros_like(demographic_depression_BC_es_filter, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, ax=ax)


#####################################################################


################# for demographic DC data with es filter ###########################
demographic_depression_DC_es_filter = np.zeros((21,5),dtype = np.double)

demographic_depression_DC_es_filter[0] = male_DASS_count_es_filter[1] # for male_gender bc
demographic_depression_DC_es_filter[1] = female_DASS_count_es_filter[1] # for female gender bc

r = 2
for q in range (1,12,2):
    demographic_depression_DC_es_filter[r] = age_depression_count_es_filter[q] # for age group bc
    r += 1

r = 8
for q in range (1,14,2):
    demographic_depression_DC_es_filter[r] = education_depression_count_es_filter[q] #for education bc
    r += 1
    
r = 15
for q in range (1,8,2):
    demographic_depression_DC_es_filter[r] = marital_depression_count_es_filter[q]# for marital bc 
    r += 1
    
demographic_depression_DC_es_filter[19] = plus_60_depression_count_es_filter[0]# for yes 60+ bc 
demographic_depression_DC_es_filter[20] = plus_60_depression_count_es_filter[2]# for no 60+ bc
 

f, ax = plt.subplots(figsize=(10, 8))

sns.heatmap(demographic_depression_DC_es_filter, vmin=0, vmax=900, xticklabels=x_labels, yticklabels = y_labels,  mask=np.zeros_like(demographic_depression_DC_es_filter, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, ax=ax)

#####################################################################

############################## DC-BC ################################


############################# Gender ################################
male_DASS_count_diff = np.zeros((3,5),dtype = np.double)
female_DASS_count_diff = np.zeros((3,5),dtype = np.double)

a=1
for i in range(3):
    male_DASS_count_diff[i] = (((male_DASS_count[a])/male_count)*100) - (((male_DASS_count[a-1])/male_count)*100)
    female_DASS_count_diff[i] = (((female_DASS_count[a])/female_count)*100) - (((female_DASS_count[a-1])/female_count)*100)
    a += 2

#####################################################################

############################ Age group ##############################

age_depression_count_diff = np.zeros((6,5),dtype = np.double)
ages = [children,youngest,young,early_adulthood,middle_adulthood,old_age]
a=1
for i in range(6):
    age_depression_count_diff[i] = (((age_depression_count[a])/ages[i])*100) - (((age_depression_count[a-1])/ages[i])*100)
    a += 2

#####################################################################

############################ Education ##############################

education_depression_count_diff = np.zeros((7,5),dtype = np.double)
edu = [Illiterate,Schoolstudent,Matric,FScIntermediate,BachelorDiploma,Master,PhD]
a=1
for i in range(7):
    education_depression_count_diff[i] = (((education_depression_count[a])/edu[i])*100) - (((education_depression_count[a-1])/edu[i])*100)
    a += 2

#####################################################################

############################ Marital ##############################

marital_depression_count_diff = np.zeros((4,5),dtype = np.double)
marit = [Single,Married,WidowWidower,Divorced]

a=1
for i in range(4):
    marital_depression_count_diff[i] = (((marital_depression_count[a])/marit[i])*100) - (((marital_depression_count[a-1])/marit[i])*100)
    a += 2

#####################################################################

############################ 60 plus ##############################

plus_60_depression_count_diff = np.zeros((2,5),dtype = np.double)
sixty_plus = [yes_60,no_60]
a=1
for i in range(2):
    plus_60_depression_count_diff[i] = (((plus_60_depression_count[a])/sixty_plus[i])*100) - (((plus_60_depression_count[a-1])/sixty_plus[i])*100)
    a += 2

#####################################################################

demographic_depression_diff = np.zeros((21,5), dtype = np.double)

demographic_depression_diff[0] = male_DASS_count_diff[0]
demographic_depression_diff[1] = female_DASS_count_diff[0]
for i in range (6):
    demographic_depression_diff[i+2] = age_depression_count_diff[i]

for i in range (7):
    demographic_depression_diff[i+8] = education_depression_count_diff[i]

for i in range (4):
    demographic_depression_diff[i+15] = marital_depression_count_diff[i]

for i in range (2):
    demographic_depression_diff[i+19] = plus_60_depression_count_diff[i]


f, ax = plt.subplots(figsize=(10, 8))

sns.heatmap(demographic_depression_diff,vmin = -50, vmax = 50, xticklabels=x_labels, yticklabels = y_labels, mask=np.zeros_like(demographic_depression_diff, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, ax=ax)

