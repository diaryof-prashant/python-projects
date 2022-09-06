import random

print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                        ''')


word_list=['hello','kitten','batsman','crater','bowl','brotherhood','iphone','android','pyth','baboon','deathnote']
word=random.choice(word_list)
blnk=[]

for i in word:
    blnk.append('_')
print(blnk)

err_count=0

while '_' in blnk and err_count!=8:
    if err_count==1:
        print('''
            +---+---+
            |       |
            |
            |
            |
            |
            |
        ____|____    
        ''')
    elif err_count==2:
        print('''
            +---+---+
            |       |
            |       O
            |
            |
            |
            |
        ____|____    
        ''')
    elif err_count==3:
        print('''
            +---+---+
            |       |
            |       O
            |       |
            |
            |
            |
        ____|____    
        ''')
    elif err_count==4:
        print('''
            +---+---+
            |       |
            |       O
            |      /|
            |
            |
            |
        ____|____    
        ''')
    elif err_count==5:
        print('''
            +---+---+
            |       |
            |       O
            |      /|\ 
            |
            |
            |
        ____|____    
        ''')
    elif err_count==6:
        print('''
            +---+---+
            |       |
            |       O
            |      /|\ 
            |      /
            |
            |
        ____|____    
        ''')
    elif err_count==7:
        print('''
            +---+---+
            |       |
            |       O
            |      /|\ 
            |      / \ 
            |
            |
        ____|____    
        ''')
        break
    guess=input('Guess a letter:')
    if guess in word:
        for i in range(len(word)):
            if word[i]==guess:
                blnk[i]=guess
        print(blnk)

    else:
        print('Try again')
        print(blnk)
        err_count+=1
s=''
for i in blnk:
    s+=i
if err_count==7:
    print("Game Over")
if word==s:
    print("You won")



