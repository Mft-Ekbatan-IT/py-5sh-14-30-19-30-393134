


from soal import *


score = 0

question_1 = "2 + 2"
question_2 = "formol water"
question_3 = "5 * 4"
question_4 = "77 * 46"

while True:
    
# question_1

    print(question_1)
    anwser_1 = input("""
1.6
2.4
3.5
4.7
                     
corect anwser:""")
    score = check_question_1(anwser_1,score)
    
# question_1

    print(question_2)
    anwser_2 = input("""
1.H2O
2.NaF
3.NaCl
4.Cu
                     
corect anwser:""")
    score = check_question_2(anwser_2,score)
    
# question_3

    print(question_3)
    anwser_3 = input("""
1.27
2.32
3.17
4.20
                     
corect anwser:""")
    score = check_question_3(anwser_3,score)

# question_4

    print(question_4)
    anwser_4 = input("""
1.2602
2.1868
3.3542
4.4184
                     
corect anwser:""")
    score = check_question_4(anwser_4,score)
    
# end 

    print(f"your score is {score}")
    break