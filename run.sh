#!/bin/bash
echo "Please do read the Readme.txt"
cd Hackathon_Ge_heathcare
echo "Hey Doc !! open stage1_input.csv and add the attributes of the subject(if there are any missing values leave them blank)"
RScript 4wayclassification.R
cd PartII
python read_score.py
echo "Change Directory into PartII open the file treatments1.csv to know the predictions of the model"
cd Total_score_Metric
cd Personal_scoring
python personal_scoring.py
echo "Note: If there are any missing values in the stage1_input.csv, then use the Imputer with mean.ipynb to impute the values"
cd ..
cd Drug_prediction
python regression.py
RScript drug_classifier.R
echo "To do:If you get 15 Visits of a single patient then copy paste the patient from drug_input.csv to data.csv"
echo "Thank you for using me #Clinicians&code"
