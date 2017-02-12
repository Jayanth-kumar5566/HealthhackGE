 ============ How to Predict disease================
    
We provide a tar file named "GE_HealthHack.tar" 
which contains R and Python scripts that will assist the clinician 
in diagnosing a patient.

The model here is trained on Parkinson's dataset

The R script classifies a subject into is PD,healthy or inconclusive.
This model then follows the progression of a PD patient from the first visit 
in terms of personalised score. This progression marker along with the 
personalised score is used to decide the drug or treatment that is to be 
administerd to the patient.

=======================Features=============================
1)Training uses 70 % of the data) and testing uses the remaining data on each
 run. The results of testing are printed out in a confusion matrix.

2)Feature importance plots are saved into the directory on each
  run as "Rplots.pdf".
======================Installation===========================

1)Download and install R from "http://lib.stat.cmu.edu/R/CRAN/" for 
your appropriate distribution.
 
2)Install following R packages from CRAN repository
    a) xgboost
    b) data.table
    c) Ckmeans.1d.dp

3)Download and install following Python packages(Assuming Python 2.7)
	a)Python-Pandas
	b)Scipy
	c)SkLearn
	d)Matplotlib

======================How to use============================
 
 1)Untar "GE_HealthHack.tar", on Linux based 
 system navigate to the directory containing "PPMI.tar" and type the 
 following command in the terminal:
 
			"tar -xvf GE_HealthHack.tar"
			
This will create a folder named "Hackathon Ge_healthcare" in the directory 
from which the command was executed.


2)Navigate to the directory "Hackathon_Ge_healthcare". The user has to enter the test results for tests mentioned in the 
"stage1_input.csv" of the patient in the "stage1_input.csv" and save the file. 
If there are any tests for which the results is not known, leave that entry blank.
The other two csv files ("data.csv","label.csv") are the ones used
for the training and testing of the algorithm.

3) Getback to the previous directory

4) Run the shell script using

        "chmod +x run.sh"
        "./run.sh"

=====================Interpretation===========================
StageI output: 

This should print out an integer between 0 and 4 for each patient
 filled in the "stage1_input.csv" which is to be interpreted as follows:
         
           	1 -----------> PD Patient
         	2 -----------> Healthy Control
         	3 -----------> Swedd
         	4 -----------> Prodormal

Predicting/Classifying the Subjects:
          
          The algorithm will classify each class into 3 classes
          			
          			a) Give Levadopa Drug
          			b) Needs Imaging Analysis
          			c) Healthy
  The file of the results can be found in "./HealthhackGE/Hackathon_Ge_heathcare/PartII/treatments1.csv" 
  
==========================Note=================================
   If the code asks for
         "Do you wish to change the prediction?"
   If the user feels that the code is predicting wrong
   he/she should type in "yes", followed by 
   answering the posed questions
  
   This will retrain the model based on this
   new correction and make the model better
   
   Or you could type in "no" to continue further
===============================================================   
If the code asks "Which visit is it?"
Do type in the visit number as "Visit1" or "Visit2"


Predicting the Drug of the patient:
             
            1 -----------> Try a new drug
         	2 -----------> Reduce the Dosage of Levadopa
         	3 -----------> Keep the same medications
         	4 -----------> Increase the Dosage
             

   


