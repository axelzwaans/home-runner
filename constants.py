quiz_questions = [
    "\nWhat is the collective noun for a group of pandas?\n" +
    "(a) A group\n(b) A bunch \n(c) An embarrassment\n\n",
    "\nWhich country do kiwifruit originate from?\n" +
    "(a) New Zealand\n(b) China\n(c) Australia\n\n",
    "\nWhat is a Rocky Mountain oyster?\n(a) Bull testicles\n" +
    "(b) An oyster from Rocky Mountain\n(c) A fish\n\n",
    "\nWhat is the correct term for a question mark combined with an " +
    "exclamation mark?\n(a) An exlamuestion mark\n" +
    "(b) An interrobang\n(c) An interrogamation\n\n",
    "\nWhat is the highest-grossing Broadway show of all time?\n" +
    "(a) The Lion King\n(b) Wicked\n(c) Hamilton\n\n",
    "\nOn average, how many seeds are located on the outside " +
    "of a strawberry?\n(a) 100\n(b) 200\n(c) 500\n\n",
    "\nIn what country do more than half of people believe " +
    "in elves?\n(a) Norway\n(b) Russia\n(c) Iceland\n\n",
    "\nWhat is yellowtail fish called in Japanese?\n" +
    "(a) Ahi\n(b) Ikura\n(c) Hamachi\n\n",
    "\nWho was the first Disney Princess?\n" +
    "(a) Snow White\n(b) Cinderella\n(c) Jasmine\n\n",
    "\nWhat’s the heaviest organ in the human body?\n" +
    "(a) Brain\n(b) Skin\n(c) Liver\n\n",
]

INTRO_TEXT = """
Welcome to...

====================
    HOME RUNNER
====================

What is your name, traveller?

"""

TEXT_1 = """
It's %s
you just woke up in your bedroom somewhere in Europe
As you slowly get up, you realise something...
You are supposed to be in Dublin for a family event
Which starts in 7 hours!
If you don't make it, you'll be in big trouble...

You better hurry up, how do you want to get to the airport, bus or taxi?

"""

TAKE_BUS_TEXT = """
You took a bus!

You sit down next to a peculiar looking gentleman
You notice the man is staring at you, but you don't respond...
As the bus makes its way to the airport
you continue to ignore the staring man...
Finally, you decided you've had enough, and you confront him!

{0}: "Can I help you???"
Man: ...
Man: ...
Man: "Are you talking to me?"
{0}: "Yes obviously I'm talking to you! You're staring at me!"
Man: "Oh yes, I was, but I was really just wondering something..."
{0}: "Wondering what?"
Man: "Well, you look very smart, and I need help with something"
Man: "I forgot the security questions for my Disney+ account...
Man: "and now I can't log in"
{0}: "We've all been there..."
Man: "Would you mind helping me out?"
{0}: *reluctantly takes headphones out of ears* "sure..."
Man: "Thanks! Here are the questions!..."
Man: "You'll need to get at least 2 out of 3 right!"
"""

TAKE_TAXI_TEXT = """
You took a taxi

{0}: "To the airport please, and step on it!"
Taxi driver: "Speed limit is 55mph..."
{0}: "Yeah okay never mind..."

As you make your way to the airport
The driver seems to be a chatty one!
So you smile and nod and look out the window
As the city landscape passes you by...

Taxi driver: "Here we are!"
{0}: "Great, how much will that be?"
Taxi driver: "55 euros please"

You slide your credit card into the machine
And you realise you forgot the last digit of your pin code
You start to sweat
If you guess wrong, the taxi driver will probably drive you to a police station
You have 3 guesses before your card gets blocked!

{0}: "Here goes nothing, I am sure that it is a number between 0 and 4..."

"""

QUIZ_GAME_WIN = """

The man is grateful that he's now able to log into his Disney+ account

Man: "Now I can catch up on my favourite cartoons! Thank you!"

You say goodbye to the man
And you make your way into the airport...
"""

NUMBERS_GAME_WIN = """
PIN CORRECT

You can't believe it, you got it in %s guesses!
You say goodbye to the chatty taxi driver
And you make your way into the airport...

"""

NUMBERS_GAME_LOSE = """
Your card is blocked!

You slowly look up to the taxi driver
He knows you can't pay the fare

Taxi driver: "I am taking you to the cops!"
Taxi driver: "They'll know what to with you"

"""

QUIZ_GAME_LOSE = """
Man: "You fool! Thanks to you...
Man: I have been locked out of my Disney+ account forever!"
Man: "As punishment, you shall never leave this bus!"

The man quickly grabs some cable ties from under his tall hat!
He ties you to the seat in front of you!
You realise you're stuck to the bus!
You're now doomed to ride this bus for eternity...
And you'll never make it to your family meeting...
"""

BATTLE_GAME_TEXT = """
Fortunately, you booked a ticket during the ride
So you go straight through to your gate...
But first you need to get through security!
As you go through the security check
You are pulled aside into a separate room
And when you and the security officer are alone
They tell you they want to battle you!!!

Security officer: "If you want to get on this plane..."
Security officer: "you'll have to defeat me in battle!"
{0}: "I knew airport security checks are a pain in the ass...
{0}: "but this is getting ridiculous!!!"

This is a turn based battle
You can choose between 3 moves:

a) Karate-chop (30 to 40 damage, selected at random)
b) Judo-kick (15 to 60 damage, selected at random)
c) HP Boost (Boosts HP between 10 to 30 points, selected at random)

The first person to lose all their HP is the loser

First go is decided at random

Good luck!
"""

GAME_WIN_TEXT = """

Congratulations on passing all your challenges!

As you board the plane
You take your seat as the engines fire up
The plane starts to head towards the runway
And before you know it... 
you're in the skies
With a whole new adventure waiting for you...

Thank you for playing...

====================
    HOME RUNNER
====================

"""