knowledge_assessment = 50

if knowledge_assessment <= 100:
    print("Your knowledge level is A")
elif knowledge_assessment >= 80:
    print("Your knowledge level is B")
elif knowledge_assessment >= 70:
    print("Your knowledge level is C")
elif knowledge_assessment >= 60:
    print("Your knowledge level is D")
elif knowledge_assessment >= 50:
    print("Your knowledge level is E")
elif knowledge_assessment >= 40:
    print("Your knowledge level is F")
elif knowledge_assessment >= 0:
    print("Your have problems")
else:
    print("Wrong")

"""
Последовательность исполнения операторов: not, and, or
    Первым исполняется:
        not
    
    Вторым исполняется:
        and
    
    Третим исполняется:
        or
"""
