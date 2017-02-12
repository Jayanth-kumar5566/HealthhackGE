#!/bin/bash
echo "Please do read the Readme.txt"
echo
echo
cd Hackathon_Ge_heathcare
echo "Hey Doc !! open stage1_input.csv and add the attributes of the subject(if there are any missing values leave them blank)"
echo
echo
echo"Running XgBoost(Boosted Decision tree on the entered values)"
Rscript 4wayclassifiation.R
cd PartII
echo
echo
echo "Predicting/Classifying the Subjects"
python read_score.py
echo "Change Directory into PartII open the file treatments1.csv to know more about the predictions of the model"
cd Total_score_Metric
cd Personal_scoring
echo 
echo
echo "Creating a Personal Score for each patient based on his Symptoms datasets"
python personal_scoring.py
Rscript merging.R
echo
echo
echo "Note: If there are any missing values in the stage1_input.csv, then use the Imputer with mean.ipynb to impute the values"
cd ..
cd Drug_prediction
echo
echo
echo "Using Ordinary Least Square Regression to quantify the patient progression and prediction of drug"
python regression.py
Rscript merge_dynam.R
Rscript drug_classifier.R
echo
echo
python dynamicity_drug.py
echo 
echo
echo "Thank you, #Clinicians&code"
