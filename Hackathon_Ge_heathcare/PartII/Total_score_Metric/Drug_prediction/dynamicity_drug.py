a=raw_input("Do you wish to change the prediction? ")
if a=="yes":
    import pandas
    indf=pandas.read_csv("prog_data_pred.csv")
    outdf=pandas.read_csv("prog_data.csv")
    try:
    	del outdf["Unnamed: 0"]
    except:
    	pass
    old_label=open("labels.csv",'a')
    pat=raw_input("Please enter the patient number? ")
    diag=raw_input("Please input the correct drug number that is to be administered? ")
    indf=indf.set_index("PATNO")
    indf=indf.loc[int(pat)]
    new_df=pandas.DataFrame(indf.to_dict(),index=[int(pat)])
    outdf=outdf.set_index("PATNO")
    outdf=outdf.append(new_df)

    outdf.to_csv("prog_data.csv")
    old_label.write(str(diag)+'\n')
    old_label.close()
else:
    pass
