# WebScrape
This is a web scraper that pulls weekly fantasy sport stats.
demo.py will give you a list of players you can search from at a given position.
run.py allows you to quickly search one or two players to compare from the command line.

I made this to get experience using bs4 and using the data from it.
You can use this program to search players during fantasy football drafts
and compare stats.

<h2>Sample Output (demo.py)</h2>

<pre  style="font-family:arial;font-size:12px;border:1px dashed #CCCCCC;width:99%;height:auto;overflow:auto;background:#f0f0f0;;background-image:URL(http://2.bp.blogspot.com/_z5ltvMQPaa8/SjJXr_U2YBI/AAAAAAAAAAM/46OqEP32CJ8/s320/codebg.gif);padding:0px;color:#000000;text-align:left;line-height:20px;"><code style="color:#000000;word-wrap:normal;">
  Which position would you like to search: (QB, RB, WR)
   ---&gt; qb
  -----------------------------
  |           Name            |
  -----------------------------
    0)	 Aaron Rodgers
    1)	 Drew Brees
    2)	 Matt Ryan
    3)	 Andrew Luck
    4)	 Kirk Cousins
    5)	 Philip Rivers
    6)	 Matthew Stafford
    7)	 Blake Bortles
    8)	 Dak Prescott
    9)	 Jameis Winston
    10)	 Russell Wilson
    11)	 Andy Dalton
    12)	 Marcus Mariota
    13)	 Carson Palmer
    14)	 Cam Newton
    15)	 Derek Carr
    16)	 Ben Roethlisberger
    17)	 Joe Flacco
    18)	 Tyrod Taylor
    19)	 Eli Manning
    20)	 Tom Brady
    21)	 Carson Wentz
    22)	 Sam Bradford
    23)	 Alex Smith
    24)	 Ryan Tannehill
    25)	 Trevor Siemian
    26)	 Colin Kaepernick
    27)	 Brock Osweiler
    28)	 Ryan Fitzpatrick
    29)	 Case Keenum
    30)	 Matt Barkley
    31)	 Blaine Gabbert
    32)	 Brian Hoyer
    33)	 Cody Kessler
    34)	 Robert Griffin III
    35)	 Jared Goff
    36)	 Josh McCown
    37)	 Jay Cutler
    38)	 Matt Moore
    39)	 Bryce Petty
    40)	 Landry Jones
    41)	 Jimmy Garoppolo
    42)	 Paxton Lynch
    43)	 Jacoby Brissett
    44)	 Nick Foles
    45)	 Derek Anderson
    46)	 Tom Savage
    47)	 Matt Cassel
    48)	 Kevin Hogan
    49)	 Drew Stanton
  Which players stats would you like to find? : carson wentz

  *------------| Carson Wentz |---------------*

  Team 			                PHI
  Games Played 		          16
  Pass TDs 		              16
  Pass Yd 		              3,782
  Ints 			                14
  Attempts 		              607
  Completions 		          379
  Rush Yds 		              150
  Rush TDs 		              2
  Rush Attempts 		        46
  FANTASY POINTS 		        280.1

  Carson Wentz  scored  17.5  points per game played
  *---------------------------------------------*

  Would you like to search another players stats? (Y/N): n
  Goodbye!

</code></pre>
