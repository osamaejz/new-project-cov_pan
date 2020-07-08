import pandas as pd
import numpy as np

column_names = ['Timestamp','PleaseAccept','City','Area','Gender','Age','Education',
              'Marital Status','Family member 60+','Frontline','Recent consultancy',          
              'You infected','Family member infected','Friend and relative infected',
              'Survaival chances','You spread virus','Others transfer virus','Dream',
              'Dream about COVID','Pandemic affect mentally','Indoor activities','Profession',
              'Income','Earning comparision','Dependents','Time to profession online',
              'Awareness','Confidence on health services','New cases and deaths',
              'Connection with friends and family','Time on social media',
              'Effect of lockdown','Positive feeling BC','Positive feeling DC',
              'Work initiative BC','Work initiative DC','Nothing to look forward BC',
              'Nothing to look forward DC','Down hearted BC','Down hearted DC',
              'Enthusiast BC','Enthusiast DC','Worthless BC','Worthless DC',
              'Meaningless BC','Meaningless DC','Mouth dryness BC','Mouth dryness DC',
              'Breathing difficulty BC','Breathing difficulty DC','Trembling BC',
              'Trembling DC','Fool BC','Fool DC','Close to panic BC',
              'Close to panic DC','Heart beat BC','Heart beat DC','Scared BC',
              'Scared DC','Wind down BC','Wind down DC','Overreact BC','Overreact DC',
              'Nervous energy BC','Nervous energy DC','Agitated BC','Agitated DC',
              'Relax BC','Relax DC','Intolerant BC','Intolerant DC','Touchy BC', 
              'Touchy DC','Contact']

survey_data = pd.read_csv("COVID-19 Survey .csv",names = column_names, 
                          index_col= False)



depression_variable  = survey_data.iloc[:,32:46].values

anxiety_variable  = survey_data.iloc[:,46:60].values

stress_variable  = survey_data.iloc[:,60:-1].values



###### Calaculating DASS total score (sum of 7 questions score)
DASS_score = np.zeros((len(survey_data),6), dtype = np.double)

for row_value in range (len(survey_data)):
    ############ for BC ###################
    depression_score_BC = 0
    anxiety_score_BC = 0
    stress_score_BC = 0

    for i in range (0,14,2):
        depression_score_BC += depression_variable[row_value][i]
        anxiety_score_BC += anxiety_variable[row_value][i]
        stress_score_BC += stress_variable[row_value][i]

    DASS_score[row_value][0] = depression_score_BC * 2 # Due to multiplying factor for DASS-21
    DASS_score[row_value][2] = anxiety_score_BC * 2
    DASS_score[row_value][4] = stress_score_BC * 2

   
    ########### for DC ####################
    depression_score_DC = 0
    anxiety_score_DC = 0
    stress_score_DC = 0

    for j in range (1,14,2):
        depression_score_DC += depression_variable[row_value][j]
        anxiety_score_DC += anxiety_variable[row_value][j]
        stress_score_DC += stress_variable[row_value][j]

    DASS_score[row_value][1] = depression_score_DC * 2 # Due to multiplying factor for DASS-21
    DASS_score[row_value][3] = anxiety_score_DC * 2
    DASS_score[row_value][5] = stress_score_DC * 2
#############################################
    

 
# for mean and std of DASS-21 (BC & DC)
    
DASS_mean_std = np.zeros((4,3), dtype = np.double) 
############  for mean and std of depression score at 00,10,20,30###################
col = 1
for i in range (3): 
    DASS_mean_std[0][i] = np.mean(np.transpose(DASS_score)[i*2])   
    DASS_mean_std[1][i] = np.std(np.transpose(DASS_score)[i*2])
    DASS_mean_std[2][i] = np.mean(np.transpose(DASS_score)[i+col])
    DASS_mean_std[3][i] = np.std(np.transpose(DASS_score)[i+col])
    col += 1

############ Total count of subscales of DASS
    
DASS_count = np.zeros((6,5),dtype = np.double)
row_value = 0
for l in range (6):
    d_normal = 0
    d_mild = 0
    d_moderate = 0
    d_severe = 0
    d_extreme = 0
    
    a_normal = 0
    a_mild = 0
    a_moderate = 1
    a_severe = 0
    a_extreme = 1
    
    s_normal = 2
    s_mild = 0
    s_moderate = 2
    s_severe = 0
    s_extreme = 0
    
    for k in range(len(survey_data)):
        if (l<2):
            if (DASS_score[k][l]>=0 and DASS_score[k][l]<10):
                d_normal += 1
            
            elif (DASS_score[k][l]>=10 and DASS_score[k][l]<14):
                d_mild += 1
            
            elif (DASS_score[k][l]>=14 and DASS_score[k][l]<21):
                d_moderate += 1
            
            elif (DASS_score[k][l]>=21 and DASS_score[k][l]<28):
                d_severe += 1
            
            else:
                d_extreme += 1
                
        elif (l>=2 and l<4):
            if (DASS_score[k][l]>=0 and DASS_score[k][l]<8):
                a_normal += 1
            
            elif (DASS_score[k][l]>=8 and DASS_score[k][l]<10):
                a_mild += 1
            
            elif (DASS_score[k][l]>=10 and DASS_score[k][l]<15):
                a_moderate += 1
            
            elif (DASS_score[k][l]>=15 and DASS_score[k][l]<20):
                a_severe += 1
            
            else:
                a_extreme += 1
        
        elif (l>=4):
            if (DASS_score[k][l]>=0 and DASS_score[k][l]<15):
                s_normal += 1
            
            elif (DASS_score[k][l]>=15 and DASS_score[k][l]<19):
                s_mild += 1
            
            elif (DASS_score[k][l]>=19 and DASS_score[k][l]<26):
                s_moderate += 1
            
            elif (DASS_score[k][l]>=26 and DASS_score[k][l]<34):
                s_severe += 1
            
            else:
                s_extreme += 1
            
    temp = [[d_normal, d_mild, d_moderate, d_severe, d_extreme],
            [a_normal, a_mild, a_moderate, a_severe, a_extreme],
            [s_normal, s_mild, s_moderate, s_severe, s_extreme]]        
    
    if(l<2):
        DASS_count[l] = temp[0]
    
    elif(l>=2 and l<4):
        DASS_count[l] = temp[1]
    
    elif(l>=4):
        DASS_count[l] = temp[2]

##############################################################

