quiz = {
    'question1' : {
        'question' : 'What is the capital of Bangladesh?',
        'answer' : 'Dhaka'
    },
    'question2' : {
        'question' : 'What is the capital of Japan?',
        'answer' : 'Tokyo'
    },
    'question3' : {
        'question' : 'What is the capital of China?',
        'answer' : 'Beijing'
    },
    'question4' : {
        'question' : 'What is the capital of Taiwan?',
        'answer' : 'Teipai'
    },
    'question5' : {
        'question' : 'What is the capital of Indonesia?',
        'answer' : 'Jakarta'
    },
    'question6' : {
        'question' : 'What is the capital of Malaysia?',
        'answer' : 'Kualalampur'
    }
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    inputt = input('Answer: ')
    if inputt.lower() == value['answer'].lower():
        print('Correct')
        score += 1
        print('you score is : ', score)
    else: 
        print('Wrong answer')
        print('Correct answer is : ', value['answer'])
        print('you score is : ', score)
        
print('you got ', score , 'out of 6')
print((score/6) * 100 , '%' + 'score')
       