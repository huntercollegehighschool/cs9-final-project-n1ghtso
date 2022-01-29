"""
Name(s): Sophia Li, Cal Chen
Name of Project: Escape Room Adventure
"""

#guitar = 0
#haveBatteries
haveKey = 0
#haveKey
note = 0
#ponderNote redo
paintings = 0
#painting redo
faith = 0
#restart game

def start():
  print(" \n There is an incessant ticking noise, flickering and sparking in your skull. You wake up. You sit up from the cold tile you\'ve been asleep on, and glance around. A trunk, swathed in chains connected with a padlock. Paintings on the wall, a locked door, a stringed instrument tucked in the corner. Aside from a dim, swaying light bulb hanging from the ceiling, the only source of light is from the blinking red light of a safe. \n")
  
  print("(Make sure you have something to take notes.) \n")
  
  print("A house-shaped clock on the wall chimes, and you jump to your feet. On the fourth chime, an animal comes out of one of the windows--a bird? You walk closer, and it\'s a python, with a note punctured by one of its fangs. You reach out and open it: it reads, 11011110110010101111.\n")
  
  choice = input("\nEnter P to ponder the note, D to analyze the door, K to look at the trunk, C to go check out the instrument in the corner, and L to look at the paintings.\n").lower()

  while choice != 'p'and choice != 'd' and choice != 'k' and choice != 'c' and choice != 'l':
    print("That's not a valid option.")
    choice = input("\nEnter P to ponder the note, D to analyze the door, K to look at the trunk, C to go check out the instrument in the corner, and L to look at the paintings.\n").lower()


  if choice == 'p':
    ponderNote()
  elif choice == 'c':
    checkGuitar()
  elif choice == 'd':
      analyzeDoor()
  elif choice == 'k':
      lookTrunk()
  elif choice == 'l':
      lookPaintings()

def goBack():
  choice = input("\nEnter P to ponder the note, D to analyze the door, K to look at the trunk, C to go check out the instrument in the corner, and L to look at the paintings.\n").lower()

  while choice != 'p'and choice != 'd' and choice != 'k' and choice != 'c' and choice != 'l':
    print("\nThat\'s not a valid option.\n")
    choice = input("\nEnter P to ponder the note, D to analyze the door, K to look at the trunk, C to go check out the instrument in the corner, and L to look at the paintings.\n").lower()
  
  while choice == 'c' and guitar == 1:
    checkGuitar1()
  while choice == 'p'  and note == 1:
    ponderNote1()
  while choice == 'l' and paintings == 1:
    lookPaintings1()

  if choice == 'p'and note != 1:
    ponderNote()
  elif choice == 'c' and guitar != 1:
    checkGuitar()
  elif choice == 'd':
      analyzeDoor()
  elif choice == 'k':
      lookTrunk()
  elif choice == 'l' and paintings != 1:
      lookPaintings()

def analyzeDoor():
  print("\n You walk to the door and run your fingertips across the rough wood until you reach the handle, silently hoping that it’s a way out. You jiggle the knob but it doesn\'t budge. What\'d you expect? \n")
  choice = input("\nEnter B to go back to exploring the room.\n").lower()
    
  while choice != 'b':
    print("\nThat\'s not a valid option.\n") 
    choice = input("\nEnter B to go back to exploring the room.\n").lower()
    
  if choice == 'b':
    goBack()
        

def lookTrunk():
  print("\n You walk over to the trunk. It\'s swathed in thick chains ending in a heavy silver padlock. You tried yanking the padlock open. It\'s locked. Did you think it was going to be that easy? \n")
  choice = input("\nEnter B to go back to exploring the room.\n").lower()
    
  while choice != 'b':
    print("\nThat\'s not a valid option.\n") 
    choice = input("\nEnter B to go back to exploring the room.\n").lower()
    
  if choice == 'b':
    goBack()
        

def ponderNote():
  print("\n You stare at the numbers of the note--ones and zeroes. It seems important but you\'re not sure what to do with it. You put it aside for now. You\'re still cold from waking up on the tile--you notice that there\'s a jacket thrown on the floor. You put it on. \n")

  global note
  note = 1

  choice = input("\nEnter I to investigate the pockets and C to check out the instrument in the corner.\n").lower()

  while choice != 'i' and choice != 'c':
    print("\nThat\'s not a valid option.\n")
    choice = input("\nEnter I to investigate the pockets and C to check out the instrument in the corner.\n").lower()

  while choice == 'i' and haveKey == 1:
    ponderNote1()

  if choice == "i" and haveKey != 1: 
    investigatePocket()
  elif choice == "c": 
    checkGuitar()

def ponderNote1():
  print("\nYou read over the note once again. The numbers haven't changed: 11011110110010101111. What is that supposed to mean?\n")

  choice = input("\nEnter B to go back to observing the room.\n").lower()

  while choice != 'b':
    print("\nThat\'s not a valid option.\n")
    choice = input("\nEnter B to go back to observing the room.\n").lower()

  if choice == 'b':
    goBack()



def checkGuitar():
  print("\n You shrug the note off, unable to figure it out. Looking around the room, you notice the instrument in the shadows of the room--you find that it\'s a guitar. \n")
  
  choice = input("\nEnter S to play the guitar and A to be annoyed by it.\n").lower()

  while choice != 's' and choice != 'a':
    print("\nThat\'s not a valid option.\n")
    choice = input("\nEnter S to play the guitar and A to be annoyed by it.\n").lower()

  if choice == "s": 
    playGuitar()
  elif choice == "a": 
    annoyedGuitar()

def checkGuitar1():
  print("\nYou look over the entire instrument: inside the guitar, around the back, under the strings, but there is no more clues or things to be found.\n")

  choice = input("\nEnter B to go back to observing the room.\n").lower()

  while choice != 'b':
    print("\nThat\'s not a valid option.\n")
    choice = input("\nEnter B to go back to observing the room.\n").lower()

  if choice == 'b':
    goBack()

    

def playGuitar(): 
  print("\n Might as well pass the time. You pick up the guitar to give it a strum--but it makes a rattling sound. You give it a shake, and there it is again. You turn the guitar upside down and continue shaking it--and two batteries fall out. These seem significant. You see a jacket on the floor. You pick it up and place the battery in one of its many pockets. \n")

  global guitar
  guitar = 1

  choice = input("\nEnter I to investigate the pockets and L to look at the paintings.\n").lower()

  while choice != 'i' and choice != 'l':
    print("\nThat\'s not a valid option.\n")
    choice = input("\nEnter I to investigate the pockets and L to look at the paintings.\n").lower()

  while choice == 'i' and haveKey == 1:
    investigatePocket1()

  while haveKey != 1:
    if choice == "i": 
      investigatePocket() 
    elif choice == "l": 
      lookPaintings()


def annoyedGuitar(): 
  print("\n What\'s the use of a guitar? You\'re trying to escape this room, not give a concert!")
  
  choice = input("\nEnter S to observe the guitar further and B to go back to observing the room.\n").lower()

  while choice != 's' and choice != 'b':
    print("\nThat\'s not a valid option.\n")
    choice = input("\nEnter S to observe the guitar further and B to go back to observing the room.\n").lower()

  if choice == 's':
    playGuitar()
  elif choice == 'b':
    goBack()



def investigatePocket(): 
  print("\n You\'re beginning to feel claustrophobic in this locked room--please, you think, let there be something helpful. As if your prayers were heard, you find a key in one of them. Where would this fit into? \n")
  
  global haveKey
  haveKey = 1

  choice = input("\nEnter L to look at the paintings and C to check out the instrument in the corner.\n").lower()

  while choice != 'l' and choice != 'c':
    print("\nThat\'s not a valid option.\n")
    choice = input("\nEnter L to look at the paintings and C to check out the instrument in the corner.\n").lower()
  
  if choice == "l": 
    lookPaintings() 
  elif choice == "c":
    checkGuitar()

def investigatePocket1():
  print("\nYou rumage through the pockets of the jacket again. Maybe you missed something the first time? You reach into a side pocket and feel something crinkle. You pull it out and--oh, it\'s just a candy wrapper.\n")

  choice = input("\nEnter L to look at the paintings.\n").lower()

  while choice != 'l':
    print("\nThat\'s not a valid option.\n")
    choice = input("\nEnter L to look at the paintings.\n").lower()

  if choice == 'l':
    lookPaintings()


def lookPaintings(): 
  print("\n You notice the paintings on the wall. Three portraits, old-looking, with the paint cracked but eyes eerily realistic. That is, except for one of them. Stepping towards them, you squint and find that it\'s shaped like a keyhole. Now, where to find the key? You remember the jacket. \n")

  global paintings
  paintings = 1

  choice = input("\nEnter I to investigate the jacket’s pockets and T to take out a key you have, if you do have one.\n").lower()

  while choice != 'i' and choice != 't':
    print("\nThat\'s not a valid option.\n")
    choice = input("\nEnter I to investigate the jacket\'s pockets and T to take out a key you have, if you do have one.\n").lower()

  while choice == 't' and haveKey != 1:
    print("\nThat\'s not a valid option.\n")
    choice = input("\nEnter I to investigate the jacket\'s pockets and T to take out a key you have, if you do have one.\n").lower()

  while choice == 'i' and haveKey == 1:
    investigatePocket1()

  if choice == "i" and haveKey != 1:
    investigatePocket()
  elif choice == 't' and haveKey == 1:
    tryKey()

def lookPaintings1():
  print("\nYou stare at the creepy, decayed paintings and take a closer look. You can barely make out the outline of a young girl. Something about the face seems off. The smile is faded, but even then you can tell it\'s abnormally wide. A chill runs down your arm, maybe it's time to observe the other objects in the room. \n")

  choice = input("\nEnter B to go back to observing the room.\n").lower()

  while choice != 'b':
    print("\nThat\'s not a valid option.\n")
    choice = input("\nEnter B to go back to observing the room.\n").lower()

  if choice == 'b':
    goBack()  



def tryKey():
  print("\nYou take the key out of your pocket. Crossing your fingers, you hope for the best--and the small key fits perfectly in the cleverly hidden lock. You twist, and a section of the portrait swings open, revealing a small flashlight tucked behind it. The light bulb seems as if it’s dangerously close to going out, so you\'re grateful for the new source of light. Still, it fails to turn on--you find that there are no batteries.\n")

  choice = input("\nEnter R to search for batteries and H to take out any batteries you already may have.\n").lower()

  while choice != 'r' and choice != 'h':
    print("\nThat\'s not a valid option.\n")
    choice = input("\nEnter R to search for batteries and H to take out any batteries you already may have.\n").lower()

  while choice == 'h' and guitar != 1:
    print("\nThat\'s not a valid option.\n")
    choice = input("\nEnter R to search for batteries and H to take out any batteries you already may have.\n").lower()


  if choice =='r':
    searchBatteries()
  elif choice == 'h'and guitar == 1:
    takeBatteries()

def searchBatteries():
  print("\nNow, where could they be? You’re feeling a little desperate; you scan the room for anything that may be able to store batteries inside it or take your mind off of escaping for a moment.\n")

  choice = input("\nEnter F to look in the safe or B to go back to exploring the room.\n").lower()
  
  while choice != 'f' and choice != 'b':
    print("\nThat\'s not a valid option.\n")
    choice = input("\nEnter F to look in the safe or B to go back to exploring the room.\n").lower()

  if choice == 'f':
    checkSafe()
  elif choice == 'b':
    goBack()

def checkSafe():
  print("\nIt\'s a safe, tucked away in the corner of the room. You wouldn\'t have spotted it if you didn\'t see the flash of light. The light is still blinking red, and you notice there\'s a letter keypad. It has five open spaces, but you didn\'t get any letter codes? Bummer! You’re getting more frustrated by the moment.\n")

  choice = input("\nEnter B to go back to exploring the room.\n").lower()

  while choice != 'b':
    print("\nThat\'s not a valid option.\n")
    choice = input("\nEnter B to go back to exploring the room.\n").lower()

  if choice == 'b':
    goBack()

def takeBatteries():
  print("\nYou take the batteries out of the pocket you previously stored them in and click them into the flashlight. You flip the switch, and, at last, it lights up! The light is odd, though, colored purple. Oh, you realize, it\'s a UV light! The question lies: what to use it for?\n")

  choice = input("\nEnter O to shine it on the door, N to shine it on the trunk, and G to shine it on the paintings.\n").lower()

  while choice != 'o'and choice != 'n'and choice != 'g':
    print("\nThat\'s not a valid option.\n")
    choice = input("\nEnter O to shine it on the door, N to shine it on the trunk, and G to shine it on the paintings.\n").lower()

  if choice == 'o':
    lightDoor()
  elif choice == 'n':
    lightTrunk()
  elif choice == 'g':
    lightPaintings()

def lightDoor():
  print("\nMaybe the door will be of help this time, you hope. You shine it all over the large, still-locked door, and get a glimpse of something--and it’s nothing but a graffiti tag.\n")

  choice = input("\nEnter N to shine the light on the trunk and G to shine it on the paintings\n").lower()

  while choice != 'n' and choice != 'g':
    print("\nThat\'s not a valid option.\n")
    choice = input("\nEnter N to shine the light on the trunk and G to shine it on the paintings\n").lower()

  if choice == 'n':
    lightTrunk()
  elif choice == 'g':
    lightPaintings()

def lightTrunk():
  print("\nYou walk over to the chain-clad trunk, and scan it for a sign, or a clue, or anything. You make out three words: LEAP OF FAITH. What on Earth?\n")

  choice = input("\nEnter O to shine the light on the door and G to shine it on the paintings.\n").lower()

  while choice != 'o' and choice != 'g':
    print("\nThat\'s not a valid option.\n")
    choice = input("\nEnter O to shine the light on the door and G to shine it on the paintings.\n").lower()

  if choice == 'o':
    lightDoor()
  elif choice == 'g':
    lightPaintings()

def lightPaintings():
  print("\nYou shine the light on the portraits. In the dark room, a rhyme glows, reading: TO TURN THE LIGHT FROM RED TO GREEN, GIVE AN ANSWER IN TERMS OF SIXTEEN.\n")

  choice = input("\nEnter O to see if the door says anything, N to shine the light on the trunk, and E to attempt to solve the riddle. \n").lower()

  while choice != 'o' and choice != 'n' and choice != 'e':
    print("\nThat\'s not a valid option.\n")
    choice = input("\nEnter O to see if the door says anything, N to shine the light on the trunk, and E to attempt to solve the riddle. \n").lower()

  if choice == 'o':
    lightDoor()
  elif choice == 'n':
    lightTrunk()
  elif choice == 'e':
    solveRiddle()
  
def solveRiddle():
  print("\nRed to green, what could that mean? What in the room needed an answer?\n")

  choice = input("\nEnter V to observe the paintings and X to examine the safe. \n").lower()

  while choice != 'v' and choice != 'x':
    print("\nThat\'s not a valid option.\n")
    choice = input("\nEnter V to observe the paintings and X to examine the safe. \n").lower()

  if choice == 'v':
    observePaintings()
  elif choice == 'x':
    examineSafe()

def observePaintings():
  print("\nYou look at the portraits--while you pace around in front of them, their eyes seem to follow you around. You\'re reminded of the keyhole that led to the flashlight. What if there’s something else hidden in the painting?\n")

  choice = input("\nEnter W to whisper an answer to the painting and X to examine the safe. \n").lower()

  while choice != 'w' and choice != 'x':
    print("\nThat\'s not a valid option.\n")
    choice = input("\nEnter W to whisper an answer to the painting and X to examine the safe. \n").lower()

  if choice == 'w':
    whisperPaintings()
  elif choice == 'x':
    examineSafe()

def whisperPaintings():
  print("\nWell, though it might\'ve been imagined, their eyes seemed to look right at you. What if their ears could listen? You feel a little stupid, but what is there to lose? It\'s not like anyone\'s watching, aside from the figures in the portraits.\n")

  choice = input("\nEnter M to whisper to a painting.\n").lower()

  while choice != 'm':
    print("\nThat\'s not a valid option.\n")
    choice = input("\nEnter M to whisper to a painting.\n").lower()

  if choice == 'm':
    whisperFunny()

def whisperFunny():
  print("\nThere\'s no answer. You feel your face heat up. It\'s just a painting, why did you expect it to talk?\n")

  choice = input("\nEnter X to examine the safe.\n").lower()

  while choice != 'x':
    print("\nThat\'s not a valid option.\n")
    choice = input("\nEnter X to examine the safe.\n").lower()

  if choice == 'x':
    examineSafe()

def examineSafe():
  print("\nThe blinking red light of the safe catches your eye. Of course--a right answer would change it to green! You stare at the keypad, and jog your memory for an answer.\n")

  code = input("\nEnter your answer into the keypad: ").lower()

  while code != "decaf":
    print("\nThe safe lets out a loud shriek. You guess that\'s the wrong answer. Might as well give it another try.\n")
    code = input("\nEnter your answer into the keypad: ").lower()

  if code == "decaf":
    print("\nThe safe opens! And there\'s…a paper cup of coffee. You are tired, after having abruptly woken up at four or so this morning. How long\'s it been? You drink the lukewarm coffee. As you drain the cup, an object falls into your mouth. You spit it out. It\'s a bronze key.\n")

    choice = input("Enter Y to see if it fits in the locked door and Z to see if it fits in the padlock of the trunk.").lower()

    while choice != 'y'and choice != 'z':
      print("\nThat\'s not a valid option.\n")
      choice = input("Enter Y to see if it fits in the locked door and Z to see if it fits in the padlock of the trunk.").lower()

    if choice == 'y':
      keyDoor()
    elif choice == 'z':
      keyTrunk()

def keyDoor():
  print("\nEnough of locks and boxes. You want out. You run to the door, and the lock fits. You turn it, with a satisfying click, and the door opens…to nothing but a wall. There\'s a neatly printed note taped on it. You lean closer to read it, and it says: NICE TRY, COWARD. LIFE ISN\'T THAT EASY. Oh, well. Left out of options, you continue this goose chase.\n")

  choice = input("\nEnter Z to try and unlock the padlock of the trunk.\n").lower()

  while choice != 'z':
    print("\nThat\'s not a valid option.\n")
    choice = input("\nEnter Z to try and unlock the padlock of the trunk.\n").lower()

  if choice == 'z':
    keyTrunk()

def keyTrunk():
  print("\nSighing, you fit the bronze key into the padlock, and it clicks, the heavy chains falling away. You open the lid, and see nothing but black. Reaching an arm in, you can’t seem to feel a bottom. There doesn\'t seem to be anything inside the chest, either. Mixed feelings about the nothingness: you were worried while opening the box--it\'s big enough to fit a person, and you\'d thought there could be a corpse inside. Wait--maybe that\'s it. Or not. Is it better to stay trapped in this room or to jump inside some suspicious trunk to who-knows-where?\n")

  choice = input("\nEnter J to just stay in the room and hunt for more clues and 0 to gather what’s left of your bravery and take a leap of faith.\n").lower()

  while choice != 'j' and choice != '0':
    print("\nThat\'s not a valid option.\n")
    choice = input("\nEnter J to just stay in the room and hunt for more clues and 0 to gather what’s left of your bravery and take a leap of faith.\n").lower()

  if choice == 'j':
    stayInside()
  if choice == '0':
    leapOfFaith()

def stayInside():
  print("\nMaybe you\'re sick and tired of this room and its countless puzzles. Aren\'t treasure hunts for kids? Nonetheless, you enjoy living. Or, at least, you\'re happier stuck here than dead in some alternate dimension. Yes, bravery gets rewarded, you suppose, but bravery also gets you killed. Still, what to do now?\n")

  choice = input("\nEnter Q to search the room for more clues and U to consider the trunk.\n").lower()

  while choice != 'q' and choice != 'u':
    print("\nThat\'s not a valid option.\n")
    choice = input("\nEnter Q to search the room for more clues and U to consider the trunk.\n").lower()

  if choice == 'q':
    lastSearch()
  elif choice == 'u':
    considerTrunk()

def lastSearch():
  print("\nYou examine the portraits on the wall until your eyes grow weary, shake the guitar to confirm there\'s nothing else in it, and pore over every surface of the room with the UV flashlight. And you repeat this, again and again. There doesn\'t seem to be anything left or another way out. Is there any other option?\n")

  choice = input("\nEnter U to consider the trunk.\n").lower()

  while choice != 'u':
    print("\nThat\'s not a valid option.\n")
    choice = input("\nEnter U to consider the trunk.\n").lower()

  if choice == 'u':
    considerTrunk()

def considerTrunk():
  print("\nYou\'re tired. You miss life outside of this nauseating, monotonic room. Remember that? You miss brick buildings and rooms full of computers. There\'s truly nothing left here. You take a deep breath.\n")

  choice = input("\nEnter 0 to take a leap of faith.\n").lower()

  while choice != '0':
    print("\nThat\'s not a valid option.\n")
    choice = input("\nEnter 0 to take a leap of faith.\n").lower()

  if choice == '0':
    leapOfFaith()

def leapOfFaith():
  print("\nYou carefully sit on the edge of the trunk, holding on as you lower yourself in. There\'s nothing but darkness and empty space. You let go.\n")

  global faith
  faith = 1

  for i in range(5):
    print("\n.")

  print("\nYou fall for what could be seconds or years, and you land in a field of grass, tumbling. You groan and sit upright, blinking hard a few times--it\'s so much brighter out here than in the room.\nThe sun is rising. ")





startKey = input("\nType [START] to begin your adventure! ").lower()

while startKey != "start":
  startKey = input("\nType [START] to begin your adventure! ").lower()

start()

#import page1  # uncomment if you're using page1
#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4
