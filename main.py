#Ford Heston Philip Bruce
#1/18/2019
#Version 3.6.1
#To give the user a fun experience hearing knock knock jokes
from joke import joke
from question import question
import random
from restart import retry

 

jokes = ["robbers","tanks","pencils"]
randomjoke = random.choice(jokes)
joke()
question(randomjoke)
joke = input("Do you want to hear another joke or are you finished? ")
retry(joke)
question(randomjoke)


 


