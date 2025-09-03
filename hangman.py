import random
ascii=['''
=========
  +---+
  |   |
      |
      |
      |
      |

=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |

=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |

=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |

=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |

=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |

=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
words=["ant","happy","engener","book"]
random_word=random.choice(words)
# انشاء مسافات بنفس عدد حروف الكلمة
display=[]
for letter in random_word:
  display+="_"
print(" ".join(display))
# طريقة اخري بدل for لوب
# display=["_"]* len(random_word)

# عمل قائمة بالمحاولات
lives=6
# عمل قائمة لتخزين الحروف 
guessed_letter=[]
print(ascii[6-lives])
# عمل اللوب 
while "_" in display and lives > 0:  
  # طلب من المستخدم ادخال الحرف
  guessed=input("\nplease enter the letter:").lower()
  # تحقق هل الحرف تم تخمينه من قبل
  if guessed in guessed_letter:
    print("\nYou already guessed that.Try again:\n") 
    print(f"\nYou have {lives} more tries:\n ")
    continue
  # في حالة عدم تكرار الحر يتم اضافتة لقائمة الحروف
  guessed_letter.append(guessed)
    # تحقق هل الحرف صحيح 
  if guessed not in random_word:
    lives-=1
    print(f"\nYou have {lives} more tries\n")
    print(ascii[6-lives])
  else: 
    # في حال ان الحرف صحيح يتم تبديل الحرف بالمسافة
    for position in range(len(random_word)):
      if random_word[position] == guessed:
        display[position]=guessed
        print(" ".join(display))
        print(f"\nYou have {lives} more tries:\n")

# عندما ينتهي اللوب نتحقق لو اكمل الكلمة نظهر انت فائز والعكس 
if lives == 0 :
  print("You lost!")
  print("😓😓😓😓")
  print(f"The word is {random_word}")
else:
  print('''
  ********
  YOU WIN!
  👏👏👏
  ********''')
      
        
          
