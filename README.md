If you want to execute the statement git log --numstat > testFile.txt within the my-repo folder (outside the .git folder), you can follow these steps:

Open a terminal or command prompt.

Navigate to the root directory of your Git repository using the cd command. For example, if your repository is located at C:\my-repo, you would run:

   `cd C:\my-repo`
   
Once you are in the my-repo folder, execute the command git log --numstat > testFile.txt.

Wait for the command to finish executing. It will generate the testFile.txt file containing the commit history and the number of lines added and removed for each file in each commit.

You can then use the contents of the testFile.txt file as input for the above programs by replacing the file path 'testFile.txt' with 'testFile.txt' in the respective programs.

By executing the statement within the my-repo folder, you ensure that the testFile.txt file is generated in the root directory of your Git repository.


--------------------------------------------------------------
Descriptions per each file : 
------------------------------------
LineAddedHist.py: 

The provided code appears to read a file named 'testFile.txt' and extract information about lines added per user from a series of commits. It uses the matplotlib library to create a bar chart showing the number of lines added by each user.

Here's a summary of what the code does:

1.It imports the necessary modules: random for generating random colors and matplotlib for creating the chart.

2.It initializes a dictionary called lines_added_per_user to store the total number of lines added by each user.

3.It opens the 'testFile.txt' file and reads its contents.

4.It splits the file content into separate commits using the 'commit' keyword as a delimiter.

5.For each commit, it extracts the user's name and calculates the number of lines added.

6.It updates the lines_added_per_user dictionary with the number of lines added by each user.

7.It creates lists of users and lines added from the dictionary.

8.It generates a random color for each user.

9.It creates a bar chart using plt.bar() with the users on the x-axis and the lines added on the y-axis.

10.It adds labels, a title, and text annotations to the chart.

11.It rotates the x-axis labels for better readability.

12.It displays the chart using plt.show().


------------------------------------
lineAddedHistAllFileInDirectory.py

This code seems to iterate over files in the "C:\BO" directory, read their contents, and analyze the number of lines added per user in a series of commits. It then visualizes the data using a bar chart, similar to the previous code.


------------------------------------
ActivityPerecentage.py: 

1.It imports the necessary modules: random for generating random colors, matplotlib for creating the chart, and os for working with the operating system.

2.It initializes a dictionary called lines_added_per_user to store the total number of lines added by each user.

3.It iterates over the files in the directory "C:\Users\Emamyari\PycharmProjects\GradeStatistics\BO" using os.listdir().

4.For each file, it creates the full file path using os.path.join() and opens the file.

5.It splits the file content into separate commits using the 'commit' keyword as a delimiter.

6.For each commit, it extracts the user's name and calculates the number of lines added.

7.It updates the lines_added_per_user dictionary with the number of lines added by each user.

8.It creates lists of users and lines added from the dictionary.

9.It generates a random color for each user.

10.It creates a pie chart using ax.pie() with the lines added as the data, user names as labels, and percentage values as autopct.

11.It sets the start angle of the pie chart to 90 degrees and adds white edges to the wedges.

12.It adds a title to the chart.

13.It adjusts the layout to prevent overlapping labels.

14.It displays the chart using plt.show().

This code seems to iterate over files in a specific directory, read their contents, and analyze the number of lines added per user in a series of commits. It then visualizes the data using a pie chart, where each user's contribution is represented as a slice of the pie.


------------------------------------
ActivityperecentageAllFile.py:
This code seems to iterate over files in the "C:\BO" directory, read their contents, and analyze the number of lines added per user in a series of commits. It then visualizes the data using a bar chart, similar to the previous examples.
