def calculate_love_score(name1, name2):
    set_words1 = set(['T', 'R', 'U', 'E'])
    set_words2 = set(['L', 'O', 'V', 'E'])
    dic1 = 0
    dic2 = 0
    name1Upper = name1.upper()
    name2Upper = name2.upper()
    for x in name1Upper:
        if (x in set_words1 ):
            dic1 = dic1 + 1
        if (x in set_words2):
            dic2 = dic2 +1 
    for x in name2Upper:
        if (x in set_words1 ):
            dic1 = dic1 + 1
        if (x in set_words2):
            dic2 = dic2 +1     
    concatenation = str(dic1) + str(dic2)
    return concatenation

result = calculate_love_score("Angela Yu", "Jack Bauer")
print("Your score is: " + result)   
result = calculate_love_score("Kanye West", "Kim Kardashian")
print("Your score is: " + result)   

