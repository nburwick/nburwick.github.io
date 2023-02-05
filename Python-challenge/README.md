# Unit 3 - Python Challenge
by Nathon Burwick

I have submitted a main.py file and a main_slow.py file both have similar performances in this instance. However, with larger data sets the main file would produce a much faster result due to multithreading. Multithreading allows for the CPU to run multiple processes concurrently therefore we don't have to wait as long for the python interpreter to ingest and process the data, only to then produce the output file this challenge required.

The "slower" version takes the threading out of the equation and generally performs the same if not a tenth of a second slower because of the size of each data set.

I then had a results_console function that would read the result files to the console after being processed by the respective functions.

There are other techniques that would make this process easier to code, but we have not used them in class yet. Therefore, I didn't use them in this case.

Here are screenshots of my results from the console and the text files (which I renamed to my name to show the reproducible effect the script has).

![Console Results](/Python-challenge/Images/Console%20Results.png)

![PyBank_Results.txt](/Python-challenge/Images/Financial%20Results.png)

![PyPoll_Results.txt](/Python-challenge/Images/Election%20Results.png)

I pushed myself to learn more about the multithreading package for this challenge and even found myself using it to request large data sets my employer has given me access to, to start practicing using the code in my analytics position. The main purpose for my work application is to connect to multiple datasources contained in the same report for our various divisions and merge them into a single dataset of 600,000 rows of data on average.