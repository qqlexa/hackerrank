class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores
        # print(f"Grade: {self.calculate()}")

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here

    def calculate(self):
        sum_scores = 0
        for score in scores:
            sum_scores += score 
        if len(self.scores):
            sum_scores /= len(self.scores)
        
        if sum_scores >= 90:
            return "O"
        elif sum_scores >= 80:
            return "E"
        elif sum_scores >= 70:
            return "A"
        elif sum_scores >= 55:
            return "P"       
        elif sum_scores >= 40:
            return "D"    
        else:
            return "T"
        
    
