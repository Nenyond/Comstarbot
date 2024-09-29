About the Comstar Bot


Comstar bot requires the following modules:
Discord.py
dotenv
Random

the bot's default command syntax is the forward slash '/', this can be changed on line 10 of the main.py file.

I've paused working on this bot, I want to come back to it in the future, it works and covers most of the things a player 
would encounter in eras up to probably the Civil War era or Jihad. 

A note about the syntax of the commands: The /commands function includes a key for the required syntax, there is no punctuation, they're all values provided in order, separated by a space. 

It currently supports cluster hits for all normal SRMs, LRMS, those missile racks with Artemis IV, MMLs, and LB-x Autocanons. 
Ultra and Rotary autocannons can use the corresponding SRM/LRM command as an interim command. Unless you feel like adding it for your instance.

Comstar bot also handles basic Alpha Strike damage calculation functions via its ASDAM command (line 25), if you use the Variable Damage Optional rule. 

The to hit function (line 339) works for both Alpha Strike and Classic games, since it asks for the total Target Number, then rolls against that. 
In the future, I'll split the function into two buttons to allow it to show the Margin of Failure for Alpha Strike to enable special rules like FLAK. 

The charge function (line 326) is the most complicated function on the list. It has to keep track of five variables while it performs the function.
The syntax is /charge (The weight of the Charging unit) (The weight of the unit being charged) (The numver of hexes moved by the charging unit) (The context based target to hit number)
