a = int(input("Enter no. of over: "))
print("total ball:",a*6 )
import random

comp_runs = random.randint(0,36)
print("computer's run:" ,comp_runs)
comp_runs = comp_runs+1
print("runs need to win:",comp_runs)
chances_1 = a*6
no_of_chances_1 = 0
your_runs = 0

print("-----------------------------------------------\nYour Batting\n")
while no_of_chances_1 < chances_1:

    runs = int(input("Enter Runs for Your Batting Turn: "))
    comp_bowl = random.randint(1,6)

    if runs == comp_bowl:
        print("Computer Guess: ", comp_bowl)
        print("You are Out. Your Total Runs= ", your_runs, "\n")
        break
    elif runs > 10:
        print("ALERT!! Support No only till 10\n")
        continue
    else:
        your_runs = your_runs + runs
        print("Computer Guess: ", comp_bowl)
        print("Your runs Now are: ", your_runs, "\n")
        if comp_runs < your_runs:
            break

    no_of_chances_1 = no_of_chances_1 + 1

#after the over ends now result time

print("\n-----------------------------------------------\nRESULTS: ")

if comp_runs < your_runs:
    print("You won the Game.")

elif comp_runs == your_runs:
    print("The Game is a Tie")

else:
    print("Computer won the Game.")

