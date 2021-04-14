from students import Student

def main():

    W01234 = Student('Jayden', 'Owings')
    W01235 = Student('Waldo', 'Wildcat')

    # print("Passing Grade:", W01234.passing_grade, W01234.first)
    # print("Passing Grade:", W01235.passing_grade, W01235.first)

    # Student.setPassingGrade(65)

    # print("Passing Grade:", W01234.passing_grade, W01234.first)
    # print("Passing Grade:", W01235.passing_grade, W01235.first)

    print ('Start of the Semester')
    print ('---------------------')
    W01234.printSutdentInfo()
    W01235.printSutdentInfo()

    print ('Middle of the Semester')
    print ('---------------------')

    W01234.setGrade(45)
    W01235.setGrade(75)

    W01234.printSutdentInfo()
    W01235.printSutdentInfo()

    print ('End of the Semester')
    print ('---------------------')

    W01235.extraCredit(10)

    W01234.printSutdentInfo()
    W01235.printSutdentInfo()

if __name__ == "__main__":
    main()