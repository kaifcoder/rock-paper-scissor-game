import random
choices = ["rock", "paper", "scissor"]
def username():
    name = input("please enter your name : ")
    return name

def comp_choices():
    c_choice = choices[random.randint(0, 2)]
    return c_choice

print("*********************** ROCK , PAPER , SCISSOR ******************************")
while(True):
    p = username()
    if p.isalpha() and len(p)>3:
        break
p1 = 0
c2 = 0
for i in range(5):
    print('!! ROUND '+str(i+1)+' !!')
    p_choice = input('enter your choice : ')
    if p_choice.lower() == 'rock' and comp_choices().lower() == 'paper':
        print(p+" lose, computer selected paper")
        c2 += 1
    elif p_choice.lower() == 'paper' and comp_choices().lower() == 'rock':
        print(p+" won, computer selected rock")
        p1 += 1
    elif p_choice.lower() == 'rock' and comp_choices().lower() == 'scissor':
        print(p+" won, computer selected scissor")
        p1 += 1
    elif comp_choices().lower() == 'rock' and p_choice.lower() == 'scissor':
        print(p + " lose, computer selected rock")
        c2 += 1
    elif p_choice.lower() == 'scissor' and comp_choices().lower() == 'paper':
        print(p + " won, computer selected paper")
        p1 += 1
    elif comp_choices().lower() == 'scissor' and p_choice.lower() == 'paper':
        print(p + " lose, computer selected paper")
        c2 += 1
    else:
        print("Its a tie both selected "+p_choice)

print("Final points after 5 rounds --> ")
print("your points = "+str(p1))
print("computer points ="+str(c2))
if p1>c2:
    print("congratulations "+p+" you won")
elif p1 == c2:
    print("Its a tie")
else:
    print("Better Luck next time , computer won")

