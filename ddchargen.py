# /usr/bin/python

# DnD Version 5e
# Script Version 2.0

# Imports
import random
import math
import itertools

# Lists and Dictionaries
race_desc = [
  "Dwarf              - Bold, hardy, warrior, miner, long memory and grudges",
  "Mountain Dwarf     - Strong, hardy, rugged, tall for a dwarf",
  "Hill Dwarf         - Keen senses, deep intuition, remarkable resilience",
  "Elf                - Magical people of otherworldly grace, in but not of the world",
  "Wood Elf           - Keen senses and intuition, fleet feet, and stealth",
  "High Elf           - Keen mind and master of basic magic",
  "Drow               - Follow the god Lolth down the path of evil and corruption",
  "Halfling           - You love peace, food, hearth, and home",
  "Lightfoot Halfling - You can easily hide, are inclined to get along with others",
  "Stout Halfling     - Hardier than average and may be part dwarven blood",
  "Human              - Young, short-lived race, innovators and achievers",
  "Dragonborn         - A servant to dragons, a warrior, or a drifter",
  "Gnome              - You delight in life, are an inventor, explorer, and explorer",
  "Forest Gnome       - Knack for illusion and inherent quickness and stealth",
  "Half-Elf           - Curious, inventive, ambitious, love nature, artistic",
  "Half-Orc           - Adventurer with savage fury and barbaric customs",
  "Tiefling           - Demonic heritage, self-reliant, suspicious, drifter"
]

race_short = [
  "Dwarf", "Mountain Dwarf", "Hill Dwarf", "Elf", "Wood Elf", "High Elf", "Drow", "Halfling", "Lightfoot Halfling", "Stout Halfling", "Human", "Dragonborn", "Gnome", "Forest Gnome", "Half-Elf", "Half-Orc", "Tiefling"
]

class_desc = [
  "Barbarian - The relentless combatant fueld by fury.",
  "Bard      - A story witty storyteller or musician.",
  "Cleric    - A holy man capable of helaing wounds.",
  "Druid     - A nomad devoted to the powers of Nature",
  "Fighter   - The skilled combatant and strategist.",
  "Monk      - A martial artist pulling bodily powers.",
  "Paladin   - A novice fighter bolstered by divine magic.",
  "Ranger    - One who blends wilderness knowledge and martial ability",
  "Rogue     - The theif, assassin, and stealthy character.",
  "Sorcerer  - A magic user who draws power from within.",
  "Warlock   - Pacted to a diety for empowering spells.",
  "Wizard    - Keeper of arcane secrets and manipulator of magic."
  ]
## Class Descriptions - https://redd.it/2e9vzl

class_short = [
  "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"
]

avg_stats = [
  "   Race        Hieght  Weight        Lifespan",
  "   ----        ------  ------        --------",
  "   Dwarf:      4-5'    150 lbs.      350 years",
  "   Elf:        5-6'+   150-170 lbs.  750 years",
  "   Halfling:   3-4'    40 lbs.       150 years",
  "   Human:      5-6'    130-200 lbs.  < 100 years",
  "   Dragonborn: > 6'    250 lbs.      < 100 years",
  "   Gnome:      3-4'    40 lbs.       350 years",
  "   Half-Elf:   5-6'    130-170 lbs.  180 years",
  "   Half-Orc:   5-6'+   150-230 lbs.  < 80 years",
  "   Tiefling:   5-6'    130-200 lbs.  100 years"
]
  
abilities = [
  "   Strength:      natural athleticism, bodily power",
  "   Dexterity:     physical agility, reflexes, balance, poise",
  "   Constitution:  health, stamina, vital force",
  "   Intelligence:  mental acuity, information recall, analytical skill",
  "   Wisdom:        awareness, intuition, insight",
  "   Charisma:      confidence, eloquence, leadership",
  ]

# Functions
def start_fn():
  print('   D&D 5e Character Generator version 2.0  ')
  print('            by Austin Haedicke             ')
  print('-------------------------------------------')
  print('  Feel free to use, edit, and distribute!  ')
  print('    But please give credit when reusing    ')
  print('')
  print('        1) (R)oll Dice                      ')
  print('        2) (C)reate Charcter                ')
  print('')
  option = input('What would you like to do? ')
  if option in ('R', 'r', '1'):
    dice = int(input('How many dice? '))
    sides = int(input('How many sides on each die? '))
    for _ in itertools.repeat(None, dice):
      print(random.randrange(1,sides))
      start_fn()
  elif option in ('C', 'c', '2'):
    pass
  else:
    start()

def race_fn():
  global char_race
  print('Available Races Include:')
  print('  (R)andom')
  for char_race in race_desc:
    print('  ',char_race)
  char_race = input('Enter Your Race (effects age, height, weight): ')
  if char_race in race_short:
    pass
  elif char_race in ('R', 'r', 'Random', 'random'):
    char_race = (random.choice(race_short))
  else:
    print('Race not available')
    race_fn()

def class_fn():
  def choose_class():
    global char_class
    print('Available Classes Include:')
    print('  (R)andom')
    for char_class in class_desc:
      print('  ',char_class)
    char_class = input('Enter Your Class: ')
    if char_class in ('R', 'r', 'Random', 'random'):
      char_class = (random.choice(class_short))
    elif char_class not in class_short:
      print('Class not available')
      choose_class()
    else:
      pass
  choose_class()

def height_fn ():
  def height_mod_fn ():
    global height_mod
    if char_race in ('Dwarf', 'Hill Dwarf', 'Mountain Dwarf', 'Lightfoot Halfling', 'Stout Halfling', 'Forest Gnome', 'Gnome'):
      height_mod = random.randrange(1,4) + random.randrange(1,4)
    elif char_race == 'Drow':
      height_mod = random.randrange(1,6) + random.randrange(1,6)
    elif char_race in ('Dragonborn', 'Half-Elf', 'Tiefling'):
      height_mod = random.randrange(1,8) + random.randrange(1,8)
    elif char_race in ('Human', 'High Elf', 'Wood Elf', 'Elf'):
      height_mod = random.randrange(1,10) + random.randrange(1,10)
    else: 
      pass

  def rnd_height_fn():
    if char_race == 'Human':
      height = 56 + height_mod
    elif char_race in ('Dwarf', 'Hill Dwarf'):
      height = 44 + height_mod
    elif char_race == 'Mountain Dwarf':
      height = 48 + height_mod
    elif char_race in ('Elf', 'High Elf', 'Wood Elf'):
      height =  54 + height_mod
    elif char_race == 'Drow':
      height = 53 + height_mod
    elif char_race in ('Halfling', 'Lightfoot Halfling', 'Stout Halfling'):
      height = 31 + height_mod
    elif char_race == 'Dragonborn':
      height = 66 + height_mod
    elif char_race in ('Gnome', 'Forest Gnome'):
      height = 35 + height_mod
    elif char_race in ('Half-Elf', 'Tiefling'):
      height = 57 + height_mod
    elif char_race == 'Half-Orc':
      height = 58 + height_mod
    else:
      pass
    global char_heightft
    global char_heightin
    char_heightft = math.trunc(height/12)
    char_heightin = height % 12

  print('Select Charcter Height:')
  for entry in avg_stats:
    print(entry)
  print('Your race is', char_race)
  height_mod_fn()
  rnd_height = input('Do you want a random height? ')
  if rnd_height in ('Y', 'y', 'Yes', 'yes'):
    rnd_height_fn()
  elif rnd_height in ('N', 'n', 'No', 'no'):
    height = int(input('Enter your height in total inches: '))
    global char_heightft
    global char_heightin
    char_heightft = math.trunc(height/12)
    char_heightin = height % 12
  else:
    print(rnd_height, ' is not a valid choice')
    height_fn()

def weight_fn():
  def weight_mod_fn():
    global weight_mod
    if  char_race in ('Human', 'Half-Elf', 'Tiefling'):
      weight_mod = height_mod * (random.randrange(1,4) + random.randrange(1,4))
    elif char_race in ('Hill Dwarf', 'Mountain Dwarf', 'Dragonborn', 'Half-Orc'):
      weight_mod = height_mod * (random.randrange(1,6) + random.randrange(1,6))
    elif char_race in ('High Elf', 'Wood Elf', 'Elf'):
      weight_mod = height_mod * random.randrange(1,4)
    elif char_race == 'Drow':
      weight_mod = height_mod * random.randrange(1,6)
    elif char_race in ('Halfling', 'Gnome', 'Forest Gnome'):
      weight_mod = height_mod
    else:
      pass

  def rnd_weight_fn():
    global char_weight
    if char_race in ('Human', 'Half-Elf', 'Tiefling'):
      char_weight = 110 + weight_mod
    if char_race in ('Dwarf', 'Hill Dwarf'):
      char_weight = 115 + weight_mod
    if char_race == 'Mountain Dwarf':
      char_weight = 130 + weight_mod
    if char_race in ('Elf', 'High Elf'):
      char_weight = 90 + weight_mod
    if char_race == 'Wood Elf':
      char_weight = 100 + weight_mod
    if char_race == 'Drow':
      char_weight = 75 + weight_mod
    if char_race in ('Halfling', 'Lightfoot Halfling', 'Stout Halfling', 'Gnome', 'Forest Gnome'):
      char_weight = 35 + weight_mod
    if char_race == 'Dragonborn':
      char_weight = 175 + weight_mod
    if char_race == 'Half-Orc':
      char_weight = 140 + weight_mod

  print('Select Charcter Weight:')
  for entry in avg_stats:
    print(entry)
  print('Your race is' , char_race)
  weight_mod_fn()
  global rnd_height
  rnd_weight = input('Do you want a random weight? ')
  if rnd_weight in ('Y', 'y', 'Yes', 'yes'):
    rnd_weight_fn()
  elif rnd_weight in ('N', 'n', 'No', 'no'):
    weight = int(input('Enter your weight in pounds: '))
  else:
    print(rnd_weight, ' is not a valid choice')
    weight_fn()

def misc_fn():
  global char_gender
  global char_age
  print('Miscelaneous Characteristics:')
  for entry in avg_stats:
    print(entry)
  rnd_age = input('Do you want a random age? ')
  if rnd_age in ('Y', 'y', 'Yes', 'yes'):
    if char_race in ('Dwarf', 'Mountain Dwarf', 'Hill Dwarf'):
      char_age = random.randrange(125,350)
    if char_race in ('Elf', 'Wood Elf', 'High Elf', 'Drow'):
      char_age = random.randrange(175,750)
    if char_race in ('Halfling', 'Lightfoot Halfling', 'Stout Halflingl'):
      char_age = random.randrange(50,150)
    if char_race == 'Human':
      char_age = random.randrange(18,100)
    if char_race == 'Dragonborn':
      char_age = random.randrange(18,100)
    if char_race in ('Gnome', 'Forest Gnome'):
      char_age = random.randrange(100,150)
    if char_race == 'Half-Elf':
      char_age = random.randrange(62,180)
    if char_race == 'Half-Orc':
      char_age = random.randrange(30,80)
    if char_race == 'Tiefling':
      char_age = random.randrange(18,100)
  elif rnd_age in ('N', 'n', 'No', 'no'):
    char_age = int(input('Enter character age: '))
  else:
    print('Not a valid choice')
    misc_fn()
  char_gender = input('Enter character gender: ')

def name_fn():
  global char_name
  global plyr_name
  plyr_name = input('Enter Player Name: ')
  char_name = input('Enter Character Name: ')

def abilities_fn():
  def stat_roll():
	    d1 = random.randrange(1,6)
	    d2 = random.randrange(1,6)
	    d3 = random.randrange(1,6)
	    d4 = random.randrange(1,6)
	    raw_rolls = [d1,d2,d3,d4]
	    sorted_rolls = sorted(raw_rolls)
	    del sorted_rolls[0]
	    total = sum(sorted_rolls)
	    return total
  def strength():
    global abl_str
    abl_str = int(input('Enter the score to use for Strength: '))
    if abl_str not in abl_scores:
      print('Score not valid')
      strength()
    else:
      abl_scores.remove(abl_str)
  def dexterity():
	  print('Remaining Scores: ', abl_scores)
	  global abl_dex
	  abl_dex = int(input('Enter the score to use for Dexterity: '))
	  if abl_dex not in abl_scores:
	     print('Score not valid')
	     dexterity()
	  else:
	     abl_scores.remove(abl_dex)
  def constitution():
	  print('Remaining Scores: ', abl_scores)
	  global abl_con
	  abl_con = int(input('Enter the score to use for Constitution: '))
	  if abl_con not in abl_scores:
	    print('Score not valid')
	    constitution()
	  else:
	     abl_scores.remove(abl_con)
  def intelligence():
	  print('Remaining Scores: ', abl_scores)
	  global abl_int
	  abl_int = int(input('Enter the score to use for Intelligence: '))
	  if abl_int not in abl_scores:
	    print('Score not valid')
	    intelligence()
	  else:
	    abl_scores.remove(abl_int)
  def wisdom():
	  print('Remaining Scores: ', abl_scores)
	  global abl_wis
	  abl_wis = int(input('Enter the score to use for Wisdom: '))
	  if abl_wis not in abl_scores:
	    print('Score not valid')
	    wisdom()
	  else:
	    abl_scores.remove(abl_wis)
  def charisma():
	  print('Remaining Scores: ', abl_scores)
	  global abl_cha
	  abl_cha = int(input('Enter the score to use for Charisma: '))
	  if abl_cha not in abl_scores:
	    print('Score not valid')
	    charisma()
	  else:
	    abl_scores.remove(abl_cha)
  def assign():
    rnd_assign = input('Do you want to randomly assign stat rolls? ')
    if rnd_assign in ('Y', 'y', 'Yes', 'yes'):
      abl_ls = ['str', 'dex', 'con', 'int', 'wis', 'char']
      random.shuffle(abl_scores)
      global abl_str
      global abl_dex
      global abl_int
      global abl_con
      global abl_wis
      global abl_cha
      abl_str = random.choice(abl_scores)
      abl_scores.remove(abl_str)
      abl_dex = random.choice(abl_scores)
      abl_scores.remove(abl_dex)
      abl_con = random.choice(abl_scores)
      abl_scores.remove(abl_con)
      abl_int = random.choice(abl_scores)
      abl_scores.remove(abl_int)
      abl_wis = random.choice(abl_scores)
      abl_scores.remove(abl_wis)
      abl_cha = random.choice(abl_scores)
    elif rnd_assign in ('N', 'n', 'No', 'no'):
      strength()
      dexterity()
      constitution()
      intelligence()
      wisdom()
      charisma()
    else:
      print('Invalid choice')
      assign()
  print('Rolling random ability scores...')
  score1 = stat_roll()
  score2 = stat_roll()
  score3 = stat_roll()
  score4 = stat_roll()
  score5 = stat_roll()
  score6 = stat_roll()
  abl_scores = [score1,score2,score3,score4,score5,score6]
  print('  Your Rolles Scores Are: ', abl_scores)
  reroll = input('  Do You Want to [C]ontinue or [R]eroll? ')
  if reroll in ('C', 'c', 'Continue', 'continue'):
    assign()
    print('The Scores You Assigned Were:')
    print('   Strength: ', abl_str)
    print('   Dexterity: ', abl_dex)
    print('   Constitution: ', abl_con)
    print('   Intelligence: ', abl_int)
    print('   Wisdom: ', abl_wis)
    print('   Charisma: ', abl_cha)
    choice = input('Do you want to (C)ontinue, Re(A)ssign, or (R)eroll? ')
    if choice in ('R', 'r', 'Reroll', 'reroll'):
      abilities_fn()
    elif choice in ('A', 'a', 'Reassign', 'reassign', 'ReAssign'):
      assign()
    else:
      pass
  else:
    abilities_fn()

def race_bonus_fn():
  global abl_str
  global abl_dex
  global abl_con
  global abl_int
  global abl_wis
  global abl_cha
  print('Specific races give bonuses to certain ability scores.')
  print('The race you selected was: ', char_race,)
  print('Checking for Strength Bonus...')
  if char_race in ('Mountain Dwarf', 'Dragonborn', 'Half-Orc', 'Human'):
    print('   ... you got a bonus!')
    if char_race == 'Human':
      abl_str = abl_str + 1
    else:
      abl_str = abl_str + 2
  else:
    pass
  print('Checking for Dexterity Bonus...')
  if char_race in ('Elf', 'Wood Elf', 'High Elf', 'Drow', 'Halfling', 'Lightfoot Halfling', 'Forest Gnome', 'Human'):
    print('   ... you got a bonus!')
    if char_race == 'Human':
      abl_dex = abl_dex + 1
    else:
      abl_dex = abl_dex + 2
  else:
    pass
  print('Checking for Constitution Bonus...')
  if char_race in ('Dwarf', 'Mountain Dwarf', 'Hill Dwarf', 'Stout Halfling', 'Rock Gnome', 'Half-Orc', 'Human'):
    print('   ... you got a bonus!')
    if char_race in ('Dwarf', 'Mountain Dwarf', 'Hill Dwarf'):
      abl_con = abl_con + 2
    else:
      abl_con = abl_con + 1
  else:
    pass
  print('Checking for Intelligence Bonus...')
  if char_race in ('High Elf', 'Gnome', 'Forest Gnome', 'Tiefling', 'Human'):
    print('   ... you got a bonus!')
    if char_race in ('Gnome', 'Forest Gnome'):
      abl_int = abl_int + 2
    else:
      abl_int = abl_int + 1
  else:
    pass
  print('Checking for Wisdom Bonus...')
  if char_race in ('Hill Dwarf', 'Wood Elf', 'Human'):
    print('   ... you got a bonus!')
    abl_wis = abl_wis + 1
  else:
    pass
  print('Checking for Charisma Bonus...')
  if char_race in ('Half-Elf', 'Drow', 'Lightfoot Halfling', 'Dragonborn', 'Human', 'Tiefling'):
    print('   ... you got a bonus!')
    if char_race in ('Half-Elf', 'Tiefling'):
      abl_cha = abl_cha + 2
    else:
      abl_cha = abl_cha + 2
  else:
    pass

def modifiers_fn():
  global mod_str
  global mod_dex
  global mod_con
  global mod_int
  global mod_wis
  global mod_cha
  global char_ac
  global prim_stat
  global atk_bonus
  print('Each ability score provides a modier score which benefits certain attributes.')
  def mod(ability):
    if ability == 1:
      mod = -5
      return mod
    elif ability in (2,3):
      mod = -4
      return mod
    elif ability in (4,5):
      mod = -3
      return mod
    elif ability in (6,7):
      mod = -2
      return mod
    elif ability in (8,9):
      mod = -1
      return mod
    elif ability in (10,11):
      mod = +0
      return mod
    elif ability in (12,13):
      mod = 1
      return mod
    elif ability in (14,15):
      mod = 2
      return mod
    elif ability in (16,17):
      mod = 3
      return mod
    elif ability in (18,10):
      mod = 4
      return mod
    elif ability in (20,21):
      mod = 5
      return mod
    elif ability in (22,23):
      mod = 6
      return mod
    elif ability in (24,25):
      mod = 7
      return mod
    elif ability in (26,27):
      mod = 8
      return mod
    elif ability in (28,29):
      mod = 9
      return mod
    elif ability == 30:
      mod = 10
      return mod
    else:
      pass
  mod_str = mod(abl_str)
  mod_dex = mod(abl_dex)
  mod_con = mod(abl_con)
  mod_int = mod(abl_int)
  mod_wis = mod(abl_wis)
  mod_cha = mod(abl_cha)
  char_ac = mod_dex + 10
  print('Here are your Ability Scores and (Modifier):')
  print('   Armor Class ', char_ac)
  print('   Strength    ', mod_str)
  print('   Dexterity   ', mod_dex)
  print('   Constitution', mod_con)
  print('   Intelligence', mod_int)
  print('   Wisdom      ', mod_wis)
  print('   Charisma    ', mod_cha)
  print('Each character also gets an attack modifier based on their proficiency bonus + main stat modifier')
  print('The proficiency bonus for Lvl 1 characters is 2')
  print('Your class is: ', char_class, '. Calculating attack bonus...')
  if char_class in ('Barbarian'):
    prim_stat = 'Strength'
  elif char_class in ('Bard', 'Sorcerer', 'Warlock'):
    prim_stat = 'Charisma'
  elif char_class in ('Cleric', 'Druid'):
    prim_stat = 'Wisdom'
  elif char_class == 'Fighter':
    prim_stat = input('Choose (S)trength or (D)exterity: ')
    if prim_stat in ('S', 's', 'Strength', 'strength'):
      prim_stat = 'Strength'
    elif prim_stat in ('D', 'd', 'Dexterity', 'dexterity'):
      prim_stat = 'Dexterity'
    else:
      print('Choice not valid')
      modifiers_fn()
  elif char_class in ('Monk', 'Ranger'):
    prim_stat = input('Choose (D)exterity or (W)isdom: ')
    if prim_stat in ('D', 'd', 'Dexterity', 'dexterity'):
      prim_stat = 'Dexterity'
    elif prim_stat in ('W', 'w', 'Wisdom', 'wisdom'):
      prim_stat = 'Wisdom'
    else:
      print('Choice not valid')
      modifiers_fn()
  elif char_class == 'Paladin':
    # str or cha
    prim_stat = input('Choose between (S)trength and (C)harisma: ')
    if prim_stat in ('S', 's', 'Strength', 'strength'):
      prim_stat = 'Strength'
    elif prim_stat in ('C', 'c', 'Charisma', 'charisma'):
      prim_stat = 'Charisma'
  elif char_class == 'Rogue':
    prim_stat = 'Dexterity'
  else:
    # Wizard
    prim_stat = 'Intelligence'
  if prim_stat == 'Strength':
    atk_bonus = mod_str + 2
  if prim_stat == 'Dexterity':
    atk_bonus = mod_dex + 2
  if prim_stat == 'Intelligence':
    atk_bonus = mod_int + 2
  if prim_stat == 'Wisdom':
    atk_bonus = mod_wis + 2
  if prim_stat == 'Charisma':
    atk_bonus = mod_cha + 2
  print('Your primary stat is: ', prim_stat)
  print('Your attack bonus is: ', atk_bonus)
  
def hp_fn():
  global char_hp
  print('Now we need to calculate hit points.')
  if char_class in ('Barbarian'):
    hit_die = random.randint(1,12)
    char_hp = mod_con + hit_die
    print('You scored ', char_hp, ' hit points')
  elif char_class in ('Fighter', 'Paladin', 'Ranger'):
    hit_die = random.randint(1,10)
    char_hp = mod_con + hit_die
    print('You scored ', char_hp, ' hit points')
  elif char_class in ('Wizard', 'Sorcerer'):
    hit_die = random.randint(1,6)
    char_hp = mod_con + hit_die
    print('You scored ', char_hp, ' hit points')
  else:
    hit_die = random.randint(1,8)
    char_hp = mod_con + hit_die
    print('You scored ', char_hp, ' hit points')
  
def alignment_fn():
  def lawchaos():
    global align_lawchaos
    align_lawchaos = input('Choose (L)awful, (C)haotic, or (N)eutral: ')
    if align_lawchaos in ('L', 'l', 'Lawful', 'lawful'):
      align_lawchaos = 'Lawful'
    elif align_lawchaos in ('C', 'c', 'Chaotic', 'chaotic'):
      align_lawchaos = 'Chaotic'
    elif align_lawchaos in ('N', 'n', 'Neutral', 'neutral'):
      align_lawchaos = 'Neutral'
    else:
      print('Invalid choice')
      lawchaos()
  def goodevil():
    global align_goodevil
    align_goodevil = input('Choose (G)ood, (E)vil, or (N)eutral: ')
    if align_goodevil in ('G', 'g', 'Good', 'good'):
      align_goodevil = 'Good'
    elif align_goodevil in ('E', 'e', 'Evil', 'evil'):
      align_goodevil = 'Evil'
    elif align_goodevil in ('N', 'n', 'Neutral', 'neutral'):
      align_goodevil = 'Neutral'
    else:
      print('Invalid choice')
      goodevil()
  def cont():
    choice = input('Is this correct? (y/n) ')
    if choice in ('Y', 'y', 'Yes', 'yes'):
      pass
    elif choice in ('N', 'n', 'No', 'no'):
      alignment_fn()
    else:
      cont()
  rnd_align = input('Finally choose alignment.  Do you want to use a random alignment? ')
  if rnd_align in ('Y', 'y', 'Yes', 'yes'):
    goodevil_ls = ['Good', 'Evil', 'Neutral']
    lawchaos_ls = ['Lawful', 'Chaotic', 'Neutral']
    global align_lawchaos
    global align_goodevil
    align_lawchaos = random.choice(lawchaos_ls)
    align_goodevil = random.choice(goodevil_ls)
  elif rnd_align in ('N', 'n', 'No', 'no'):
    lawchaos()
    goodevil()
  else:
    print ('Invalid choice')
    alignment_fn()
  print('Your alignment is ', align_lawchaos, '-', align_goodevil)

def summary_fn():
  print('##########################################')
  print('#                Summary                 #')
  print('##########################################')
  print(plyr_name, "'s: ", char_race, '-', char_class)
  print(char_name)
  print('##########################################')
  print('Height:         ', char_heightft, "'", char_heightin, '"')
  print('Weight:         ', char_weight, 'lbs.')
  print('Age:            ', char_age, 'years old')
  print('Gender:         ', char_gender)
  print('Alignment:      ', align_lawchaos, '-', align_goodevil)
  print('##########################################')
  print('Max Hit Points: ', char_hp)
  print('Armor Class:    ', char_ac)
  print('Attack Bonus:   ', atk_bonus)
  print('Primary Stat:   ', prim_stat)
  print('##########################################')
  print('Strength:       ', abl_str,  '(', mod_str, ')')
  print('Dexterity:      ', abl_dex,  '(', mod_dex, ')')
  print('Constitution:   ', abl_con,  '(', mod_con, ')')
  print('Intelligence:   ', abl_int,  '(', mod_int, ')')
  print('Wisdom:         ', abl_wis,  '(', mod_wis, ')')
  print('Charisma:       ', abl_cha,  '(', mod_cha, ')')

# Script
start_fn()
print('')
race_fn()
print('')
class_fn()
print('')
height_fn()
print('')
weight_fn()
print('')
misc_fn()
print('')
name_fn()
print('')
abilities_fn()
print('')
race_bonus_fn()
print('')
modifiers_fn()
print('')
hp_fn()
print('')
alignment_fn()
print('')
summary_fn()
