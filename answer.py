def student_log(text: str):
    studentInfo: dict[int,dict] = {}

    for lines in text:
        studentID: int = int(lines[0])
        actionCode: str = lines[1]

        if not studentID in studentInfo.keys():
            studentInfo[studentID] = {'lowestPageID': None, 'latestPageID': None, 'totalScores':0, 'totalSubmitted':0, 'avgSubmissionScore': 0}
        
        match actionCode:
            case 'P':
                actionCode = 'P'
                pageID = int(lines[2])
                studentInfo[studentID]['latestPageID'] = pageID
                if studentInfo[studentID]['lowestPageID']:
                    if pageID > studentInfo[studentID]['lowestPageID']:
                        continue
                studentInfo[studentID]['lowestPageID'] = pageID
            case 'S':
                actionCode = 'S'
                submissionScore = int(lines[2])
                studentInfo[studentID]['totalScores'] += submissionScore
                studentInfo[studentID]['totalSubmitted'] += 1
    for studentID in list(studentInfo):
        if studentInfo[studentID]['lowestPageID'] == None or studentInfo[studentID]['totalSubmitted'] == 0:
            studentInfo.pop(studentID)
            continue
        studentInfo[studentID]['avgSubmissionScore'] = int(studentInfo[studentID]['totalScores'] / studentInfo[studentID]['totalSubmitted'])
    
    sortedStudentInfo = sorted(studentInfo, key=lambda studentID: (studentInfo[studentID]['lowestPageID'],studentInfo[studentID]['latestPageID'],studentInfo[studentID]['avgSubmissionScore']))
    
    return [studentInfo, sortedStudentInfo]


def main():
    # Get the filename from stdin
    filename = input()

    # Open the file and read in its contents
    with open(filename) as data_file:
        text = data_file.readlines() #read the rest of the lines
        for i in range(len(text)):
            text[i] = text[i].replace('\n','').split(" ")
    logs = text[0]
    text = text[1:]
    printableStudentInfo = student_log(text)
    studentInfo:dict[int, dict] = printableStudentInfo[0]
    sortedStudentInfo = printableStudentInfo[1]
    for studentID in sortedStudentInfo:
        lowestPageID = studentInfo[studentID]['lowestPageID']
        latestPageID = studentInfo[studentID]['latestPageID']
        avgSubmissionScore = studentInfo[studentID]['avgSubmissionScore']
        print(f'{studentID} {lowestPageID} {latestPageID} {avgSubmissionScore}')
    
        
if __name__ == "__main__":
    main()