Main():

This function takes a file input that contains log data from various students. The lines are split using replace() and split() to create a new array containing the information needed (without \n characters or spaces). The total logs is also read from the first line and not considered with the rest of the students information. The sorted data is then iterated through to print out the lowest page ID, latest page ID, and average submission score for each student.

student_log():

This function uses the array of student logs and creates a dictionary to store the data. The dictionary has a key of the student ID's and the values as dictionaries containing the information from the student's logs. A new studentID and dictionary is created when the student exists, updating each variable based on the action code that is in the student log. As the logs are processed, the average scores and pages visited are also kept track of and updated. When all valid student info is gone through, the information is sorted in ascending order and returned as a sorted dictionary. 

Time Complexity:

sortedStudentInfo has a time complexity of O(s log s), s = the number of students that are being sorted

When sorting through the logs, the time complexity is O(L), L = number of logs that are being iterated through to fill our new dictionary. 

Overall, the time complexity is O(s log s + L) due to the time complexity when sorting through each specific students data and iterating and extracting data from the logs. 