turns = 0
pr1 = 0
pr2 = 0
ps1 = 0
ps2 = 0
pp1 = 0
pp2 = 0
p1 = 0
p2 = 0
while (turns<3):
  turns = turns + 1
  r = ['rock','scissors','paper']
  choice1 = input('Player one: Rock, scissors, paper?')
  while choice1 not in r:
    choice1 = input('please pick a valid choice:')
  while choice1 in r:
   choice2 = input('Player two: rock, scissors, paper?')
   while choice2 not in r:
     choice2 = input('please pick a valid option:')
   if choice1 == choice2:
     print("tie! no points given")
   elif choice1 == 'paper':
     if choice2 == 'scissors':
       print('p2 won with scissors!')
       ps2 = ps2 + 1
       p2 = p2 + 1
     else:
       print('p1 won with paper!')
       pp1 = pp1 + 1
       p1 = p1 + 1
   elif choice1 == 'scissors':
     if choice2 == 'rock':
       print('p2 won with rock!')
       pr2 = pr2 + 1
       p2 = p2 + 1
     else:
       print('p1 won with scissors!')
       ps1 = ps1 + 1
       p1 = p1 + 1
   elif choice1 == 'rock':
     if choice2 == 'paper':
       print('p2 won with paper!')
       pp2 = pp2 + 1
       p2 = p2 + 1
     else:
       print('p1 won with rock!')
       pr1 = pr1 + 1
       p1 = p1 + 1
   break

if p1 > p2:
  print('player one wins with',p1,'points!')
elif p1 < p2:
   print('player 2 won with',p2,'points!')
elif p1 == p2:
   print('you both tie with',p1,'points!')

print("p1 wins: rock:",pr1,"paper,",pp1,"scissors,",ps1)
print("p2 wins: rock:",pr2,"paper,",pp2,"scissors,",ps2)
