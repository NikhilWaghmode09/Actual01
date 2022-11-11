import random
cryptocurrencies = ["1000 DOGE", "0.005 BTC", "108 Matic", "0.076 ETH", "3.75 SOL"]
users = ["Parag", "Jack ", "Biz", "Noah", "Evan"]

def myfunction():
  return 0.1


random.shuffle(cryptocurrencies, myfunction)
random.shuffle(users,myfunction)


students_dict = dict(zip(cryptocurrencies, users))
print(students_dict)
