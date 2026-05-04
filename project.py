''' a prgram that gives user questions about Lisa Carrington'''
#questions in the game
question_list=[ 
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
start=input('Do you want to start a quiz about Lisa Carrington?(Yes/No)\n')
if start == "yes":
    score=0
    for question in question_list:
        print(question['question'])
        for option in question['option']:
            print(option)
        user_input=input('Enter the anwser you think is right\n')
