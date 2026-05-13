''' a prgram that gives user questions about Lisa Carrington'''
#questions in the game
question_list = [ 
    {'question': 'What year was she born?',
     'option': ['A.1983  B.1989  C.2001  D.1994'],
     'answer':'B'},

    {'question' : 'How many olimpic gold medal did she gain?',
     'option' : ['A.5  B.6  C.7  D.8,'],
     'answer' :'D'},

    {'question': 'What is her birthday?',
     'option': ['A.November 8  B.September 13  C.June 23  D.May 1'],
     'answer':'C'},

    {'question': 'What sports does she play?',
     'option': ['A.Canoe   B.Badminton  C. Table tennis  D.Rock climbing'],
     'answer':'A'},

    {'question': 'What year did she get her first Olimpic gold medal?',
     'option': ['A.2020 Tokyo   B.2016 Rio de Janeiro  C.2012 London  D. 2008 Beijing'],
     'answer':'C'},

    {'question': 'What place was she born?',
     'option': ['A. Auckland  B.Tauranga  C.Christchurch  D.Dunedin,'],
     'answer':'B'},

    {'question': 'What year did she get her first Olimpic medal?',
     'option' : ['A.2012   B.2008  C.2016  D.2020,'],
     'answer' :'A'},
    
    {'question': 'What is the name of her partner?',
     'option' : ['A. George Bell  B. Ben Waine  C. Jayden Movold  D.Michael Buck,'],
     'answer' :'D'},
]

#asking user if they want to start the quiz
user_input_start = input('Do you want to start a quiz about Lisa Carrington?(Yes/No)\n').lower().strip()
start = user_input_start.replace ("!","").replace(".","")

while True:
    if start == "yes":

    #keeeping the score
        score = 0
        
        #printing the dictionary in the list
        for question in question_list:
            print(question['question'])

            for option in question['option']:
                print(option)

            #getting input from the user   
            while True:
                user_input = input('Enter your answer (A, B, C, or D)\n').upper().strip()
                if user_input in ['A','B','C','D']:
                    break
                else:
                    print('Please enter A,B,C,D only')
        
            if user_input == question['answer']:
                score = score+1
                print('You got it correct!\n')
            else:
                print('You got it wrong!\n')
    
        #calculating the score
        if score <= 2:
            print('Nice try, maybe better next time')
        elif score <= 4:
            print('Not too bad..')
        elif score <= 6:
            print('Great job!')
        else:
            print('You are a SUPERSTAR!!')
        print(f'Your score final is {score} out of 8')
        break

    elif start == "no":
        print('See you next time!')
        break
    else:
        print('Please only enter (yes/no)')
        start=input('Do you want to start a quiz about Lisa Carrington?(Yes/No)\n').lower().strip()