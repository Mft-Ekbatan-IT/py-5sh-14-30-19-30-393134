



def check_question_1(anwser:str,score:int) -> int:
    match anwser:
        case "2":
            print("corect")
            score += 10
        case _:
            print("incorect")
            print("corect anwser is 2")
            print()
            score -= 10
    return score

def check_question_2(anwser:str,score:int) -> int:
    match anwser:
        case "1":
            print("corect")
            score += 10
        case _:
            print("incorect")
            print("corect anwser is 1")
            print()
            score -= 10
    return score

def check_question_3(anwser:str,score:int) -> int:
    match anwser:
        case "4":
            print("corect")
            score += 10
        case _:
            print("incorect")
            print("corect anwser is 4")
            print()
            score -= 10
    return score


def check_question_4(anwser:str,score:int) -> int:
    match anwser:
        case "3":
            print("corect")
            score += 10
        case _:
            print("incorect")
            print("corect anwser is 3")
            print()
            score -= 10
    return score