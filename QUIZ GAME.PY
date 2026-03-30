print ("welcome to my quiz game")

player = input("do you want to play ?")

if player.lower() != "yes":
    quit

print("okk!!  lets play :)")
score = 0

answer = input("who is the prime minister of india?")
if answer.lower() == "narendra modi":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("who is the chief minister of Maharashtra?")
if answer.lower() == "devendra fadanvis":
    print("correct!")
    score += 1

else:
    print("Incorrect!")


answer = input("who is the President  of india?")
if answer.lower() == "dropadi murmu":
    print("correct!")
    score +=1
else:
    print("Incorrect!")


answer = input("who is the Governer of Maharashtra?")
if answer.lower == "bishnu sharma":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("who is the deputy chief minister of Maharashtra?")
if answer.lower == "eknath shinde":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what is the capital of Maharashtra?")
if answer.lower == "mumbai":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("who is the principal of vdf?")
if answer.lower == "mahesh shinde":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("who is the MP of Latur Assembly ?")
if answer.lower == "Dr kalge":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("who is the MLA of Latur assembly?")
if answer.lower == "amit deshmukh":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

print("You got"  + str(score)+ "questions correct!")
print("You got"+ ((score / 4) * 100) + "%")