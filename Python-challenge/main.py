#this python script will process both the PyBank and PyPoll Projects and their accompaning csv files
# import packages
import os, csv, threading

#store file paths for script arguments to thread (run concurrently)
py_bank_csv = os.path.join('PyBank','budget_data.csv')
py_bank_txt = os.path.join('outputs','PyBank_Results.txt')
py_poll_csv = os.path.join('PyPoll','election_data.csv')
py_poll_txt = os.path.join('outputs', 'PyPoll_Results.txt')

#define a reader that displays results of each analysis into the console
def results_console(output_file):
    with open(output_file, 'r') as results_reader:
        for line in results_reader:
            print(line)

#define a function for threading PyBank
def pybank(file_in, file_out):

    #create reader
    with open(file_in,'r') as pybank:
        pybank_csv_reader = csv.reader(pybank,delimiter=',')
        
         #store header for finding index of column headers since we know them
        header = next(pybank_csv_reader)
        
         #read and store rows into memory
        for row in pybank_csv_reader:
            lines = pybank_csv_reader.read()
            
    #header row is Date, Profit/Loss

    #get pybank statistics from line memory
    dollar_index = header.index('Profit/Loss')
    date_index = header.index('Date')        

    #instanciate empty lists for moving average
    month_list, p_and_l = map(list, zip(*lines))
    change_list = []
    
    #get total months:
    total_months = len(month_list)
    
    #get net total from lines
    total_net = sum(p_and_l)
    
    #get changes
    for index in range(1, len(p_and_l)):
        change = p_and_l[index] - p_and_l[index - 1]
        change_list.append(change)
        
    #create average change
    avg_change = (sum(change_list)/len(change_list))
    
    #create dict of changes
    change_months = month_list.pop(0)
    change_dict = dict(zip(change_months, change_list))
    
    #find greatest increase/decrease keys and values
    increase_month = max(change_dict,key=change_dict.get)
    increase_value = change_dict.get(increase_month)
    decrease_month = min(change_dict,key=change_dict.get)
    decrease_value = change_dict.get(decrease_month)
        
    #define writer to write analysis results from pybank
    with open(file_out,'w',newline="") as writer:
        writer.write("Financial Analysis\n")
        writer.write("-----------------------------------\n")
        writer.write(f"Total Months: {total_months}\n")
        writer.write(f"Total: ${"{:,.2f}".format(total_net)}\n")
        writer.write(f"Average Change: ${"{:,.2f}".format(avg_change)}\n")
        writer.write(f"Greatest Increase in Profits: {increase_month} (${"{:,.2f}".format(increase_value)})\n")
        writer.write(f"Greatest Decrease in Profits: {decrease_month} (${"{:,.2f}".format(decrease_value)})\n")
        writer.write("-----------------------------------\n")

#define a function for threading PyPoll
def pypoll(file_in, file_out):

    #create reader
    with open(file_in,'r') as pypoll:
        pypoll_csv_reader = csv.reader(pypoll, delimiter=",")
        
        #store header for finding index of column headers since we know them
        header = next(pypoll_csv_reader)
        
        #Read and store rows into memory
        for row in pypoll_csv_reader:
            lines = pypoll_csv_reader.read()
        
    #Header row is Ballot ID,County,Candidate
    
    #get pypoll statistics from line memory:
    votes_cast_total = len(lines)
    canidate_dict = {}
    canidate_index = header.index('Canidate')
    
    #count canidate votes with loop:
    for line in lines:
        canidate = line[canidate_index]
        if canidate not in canidate_dict.keys():
            canidate_dict[canidate] = 1
        else:
            canidate_dict[canidate] +=1
        
    #get winner from the maximum value of vote counts per canidate in the dictionary
    winner = max(canidate_dict, key=canidate_dict.get)
    
    #define writer to write analysis results from pypoll    
    with open(file_out,'w') as writer:
        writer.write("Election Results\n")
        writer.write("-----------------------------------\n")
        writer.write(f"Total Votes: {votes_cast_total}")
        writer.write("-----------------------------------\n")
        for canidate, votes in canidate_dict.items():
            writer.write(f"{canidate}: {round(((votes/votes_cast_total)*100),ndigits=2)}% ({'{:,.0f}'.format(votes)})\n")
        writer.write("-----------------------------------\n")
        writer.write(f"Winner: {winner}")
        writer.write("-----------------------------------")
        
    
            
    
#thread processes for effeciency
t1 = threading.Thread(target=pybank,args=(py_bank_csv,py_bank_txt))
t2 = threading.Thread(target=pypoll,args=(py_poll_csv,py_poll_txt))
t1.start()
t2.start()
t1.join()
t2.join()

results_console(py_bank_txt)
results_console(py_poll_txt)

