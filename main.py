from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    if bid > highest_bid:
      highest_bid = bid
      winner = name
  print(F"The winner is {winner} with a bid of ${highest_bid}.")
    

while not bidding_finished:
  print(logo)
  name = input("What is you name?: ")
  bid = int(input("How much do you want to bid?: $"))
  bids[name] = bid
  more_bidders = input("Does someone else want to bid? Type 'yes' or 'no'. \n")
  if more_bidders == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif more_bidders == "yes":
    clear()
    




