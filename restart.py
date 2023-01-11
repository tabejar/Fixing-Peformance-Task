def retry(joke):
  if joke == "another joke":
    print("ok! restarting now!")
  if joke == "finished":
    rate = int(input("Please rate our game 1-10! "))
    final_score = int((rate * 10))
    print(str(final_score)  +  " percent satisfaction rate")
    friend = input("Would you recommend this game to a friend? ")
    if friend == "yes" or friend == "maybe" :
      print("Thanks, we appreciate it. ")
    else:
      print("Sorry you did not enjoy it. ")
    exit()