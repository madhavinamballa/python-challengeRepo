import os
import csv
#======main code snippet==============
csvpath = os.path.join('Resources', 'election_data.csv')   
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    candidate_list=[]
    total=0
    empty_list=[]
    for row in csvreader:
        total=total+1
        empty_list.append(row[2])
        candidate=row[2]
        if candidate not in candidate_list: 
            candidate_list.append(candidate)
            
    candidate1=(candidate_list[0])
    candidate2=(candidate_list[1])
    candidate3=(candidate_list[2])
    candidate4=(candidate_list[3])
    candidate1_count=0
    candidate2_count=0
    candidate3_count=0
    candidate4_count=0
    winner=""
    for i in range(total):
        if empty_list[i]==candidate1:
            candidate1_count=candidate1_count+1
        elif empty_list[i]==candidate2:
            candidate2_count=candidate2_count+1
        elif empty_list[i]==candidate3:
            candidate3_count=candidate3_count+1
        elif empty_list[i]==candidate4:
            candidate4_count=candidate4_count+1
    cand1_per=round(((candidate1_count/total)*100),3)
    cand2_per=round(((candidate2_count/total)*100),3)
    cand3_per=round(((candidate3_count/total)*100),3)
    cand4_per=round(((candidate4_count/total)*100),3)
    if (cand1_per>cand2_per)and (cand1_per>cand3_per)and (cand1_per>cand4_per):
        winner=candidate1
    elif (cand2_per>cand1_per)and (cand2_per>cand3_per)and (cand2_per>cand4_per):
        winner=candidate2
    elif (cand3_per>cand1_per)and (cand3_per>cand2_per)and (cand3_per>cand4_per):
        winner=candidate3
    elif (cand4_per>cand1_per)and (cand4_per>cand2_per)and (cand4_per>cand3_per):
        winner=candidate4
#============printing final result=====================
    print('candidtes list:')
    print(candidate_list)
    print("Election Results")
    print("----------------------")
    print("total votes:",total)
    print("----------------------")
    print(f'{candidate1}: {cand1_per}%({candidate1_count})')
    print(f'{candidate2}: {cand2_per}%({candidate2_count})')
    print(f'{candidate3}: {cand3_per}%({candidate3_count})')
    print(f'{candidate4}: {cand4_per}%({candidate4_count})')
    print("-------------------------")
    print(f'winner: {winner}')
    print("-------------------------")
    #print(candidate1_count+candidate2_count+candidate3_count+candidate4_count)
    
      
