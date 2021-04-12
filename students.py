class Student:
    def __init__(self, first, last, status):
        self.first = first #These are instance variables
        self.last = last
        self.status = status
        self.email = first + last +'@mail.weber.edu'

    #Behaviors
    def printSutdentInfo(self):
        print('Full Name:', self.first, self.last, '\n Email:', self.email, '\n Course Status:', self.status)

W01234 = Student('Jayden', 'Owings', 'Pass')
W01235 = Student('Waldo', 'Wildcat', 'Pass')

W01234.printSutdentInfo()
W01235.printSutdentInfo()

