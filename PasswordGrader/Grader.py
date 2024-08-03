from class_password import password
def runpoints(pssword):
    p1 = pssword
    p1 = password(p1)
    points = 0
#poits for length - it will award 2 points for each character up to 10 characters
    points = p1.length()*2
    if points >20:
        points = 20
#points for special char - it will award 10 points for each special character up to 2 characters
    if p1.num_special_char() >= 2:
        points += 20
    elif p1.num_special_char() == 1:
        points += 10
#points for upper case - it will award 10 points for each capital letter up to 3 capital letters
    if p1.num_capital_letters() >= 3:
        points += 30
    else: 
        points = points + (10*p1.num_capital_letters())
#points for numbers - it will award 10 points foe each number up to 3 numbers
    if p1.num_numbers() >= 3:
        points += 30
    else: 
        points = points + (10*p1.num_numbers())
#check with top 100k passwords - loops through our set of the top 100k most common passwords to make sure it is not in this leak.
    with open('/Users/maxnussbaum/Desktop/Python/Python Final Project/Password-Grader/passwords.txt', 'r') as passwords:
        for pword in passwords:
            pword = str(pword)
            if pword.strip() == p1.getword():
                return 0
    return points
