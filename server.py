import json
import datetime

quiz_fp = open ("quiz.json")
quiz_json = json.load (quiz_fp)

def add_question ():
    data = {}
    qn = input ("\nEnter the question-> ")
    data = {"question" : qn}
    op = {'A': "", 'B': "", 'C': "", 'D': ""}
    for i in range (0, 4):
        opt = input ("Option " + list(op.keys())[i] + "-> ")
        op[list(op.keys())[i]] = opt
    data.update ({"options" : op})
    copt = input ("Enter the correct option-> ")
    data.update ({"correct_option" : copt})

    quiz_json["questions"].append (data)

    fp = open ("quiz.json", "w")
    json.dump (quiz_json, fp, indent = 4, separators=(',',': '))

    print ("\nQuestion-> " + qn)
    for key, value in op.items():
        print ("Option "+ f"{key}-> {value}")
    print ("Answer-> Option " + copt)


def ask_question (i, qn, op, copt):
    ca_score = 10
    wa_score = -5
    print ("\nQuestion " + str(i) + "-> " + qn)
    for key, value in op.items():
        print ("Option "+ f"{key}-> {value}")
    ans = input ("\nEnter your option-> ")
    if (ans.lower () == "pass"):
        return 0
    elif (ans.upper() == copt):
        print ("Correct Answer!\nYou are granted 10 points.")
        return ca_score
    elif (ans != copt):
        print ("Wrong Answer!\n5 points are deducted.")
        return wa_score


def quiz (name):
    print ("\nNote:" + 
    "\n* 10 points are granted for each correct answer." + 
    "\n* 5 points are deducted for each wrong answer." + 
    "\n* Also there is an option to skip questions (Your points are not affected). \nIf you want to skip, type pass.\n")

    score = 0
    for i in range (0, 10):
        question = quiz_json["questions"][i]
        score += ask_question (i+1, question["question"],question["options"] , question["correct_option"])
        print ("Current Score-> " + str (score))
        
    print ("\n\nFinal Score-> " + str (score))

    game_log = open ("log.txt", "a")
    game_log.write ("\nName-> " + name + "\nScore-> " + str (score) + "\n" + str (datetime.datetime.now ()) + "\n")


"""
{
    "questions": [
        {
            "question": "",
            "options": {
                "A": "",
                "B": "",
                "C": "",
                "D": ""
            },
            "correct_option": ""
        }
    ]
}
"""