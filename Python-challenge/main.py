#this python script will process both the PyBank and PyPoll Projects and their accompaning csv files
# import packages
import os, csv, threading

#store file paths
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
    with open(file_in, 'r') as pybank_csv_reader:
        #read lines into list of lists
        header = next(pybank_csv_reader)
        print("Financial Analysis")
        print("------------------------------------------------")
        for row in pybank_csv_reader:
            lines = pybank_csv_reader.read()
        print(lines)
        
        #get total months
        total_months = len(lines)
        
        #get statistics from data
        #get total dollars
        total = 0
        dollars_index = header.index('Profit/Losses')
        for line in lines:
            total += line[dollars_index]
        
        

#define a function for threading PyPoll
def pypoll(file_in, file_out):

    #create reader
    with open(file_in,'r') as pypoll_csv_reader:
        #read lines into list of lists
        header = next(pypoll_csv_reader)
        print(header)
        print("------------------------------------------------")
        for row in pypoll_csv_reader:
            lines = pypoll_csv_reader.read()
        print(lines)
        
        #Header column is Ballot ID,County,Candidate
        
        #get statistics:
        votes_cast = len(lines)
        canidate_dict = {}
        canidate_index = header.index('Canidate')
        for line in lines:
            if 
            
    
#thread processes for effeciency
t1 = threading.Thread(target=pybank,args=(py_bank_csv,py_bank_txt))
t2 = threading.Thread(target=pypoll,args=(py_poll_csv,py_poll_txt))
t1.start()
t2.start()
t1.join()
t2.join()

results_console(py_bank_txt)
results_console(py_poll_txt)

