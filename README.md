# **_The Cave of Query_**

The Cave of Query is an interactive text-based adventure game filled with brain teasers and Indiana Jones trivia. 

It is built using Python and runs through the Code institute mock terminal on Heroku.


Welcome to <a href="https://cave-of-query.herokuapp.com/" target="_blank" rel="noopener">The Cave of Query</a>

![Responsive design](assets/images/screen-mockup.png)

# Contents

* [**User Experience UX**](<#user-experience-ux>)
    * [Game Design](<#game-design>)
    * [Flowchart](<#flowchart>)
* [**Current Features**](<#current-features>)
    * [Title Page](<#title-page>)
    * [Game Introduction](<#game-introduction>)
    * [Puzzle Rooms](<#puzzle-rooms>)
    * [End of Game Page](<#end-of-game-page>)
* [**Future Features**](<#future-features>)
* [**Technologies Used**](<#technologies-used>)
* [**Testing**](<#testing>)
* [**Deployment**](<#deployment>)
* [**Credits**](<#credits>)
    * [**Content**](<#content>)
    * [**Media**](<#media>)
*  [**Acknowledgements**](<#acknowledgements>)


# User Experience (UX)

## Game Design

Initially, I had the idea that I wanted to create a text-based adventure game based around the famous character of Indiana Jones with a treasure-hunting theme. This would be mixed with the recently fashionable 'escape room' games where players have to solve puzzles or brain teasers in order to move forward in the game. 

I sketched out a basic cave system to base my coding on, so that I could better visualize the path the user would take through the game. 

![Cave Map](assets/images/cave-map.png)

Originally, I set up a Google Spreadsheet in the background to collect the explorer and letter data, and to pull the diary data as and when needed to help solve the puzzles. However, although being dynamic content, my mentor pointed out that this data could all be stored and displayed inside the run.py file, so in the end, I removed the link to the Google Sheets, and kept the data inside the GitPod run.py file. 


[Back to top](<#contents>)

## Flowchart

The Cave of Query flowchart was designed using the free flowchart website [Diagrams.Net](https://www.diagrams.net/)

The user enters the game by inputting their name. This input is validated to make sure that at least one alpha character is entered, and then it is stored in a Name variable and the user enters the Cave.

The Cave of Query consists of seven puzzle rooms and a treasure room. The user has to work their way through each of the puzzles to reach the treasure. This is the 'escape room' concept but turned on it's head as the user is trying to get in, not out. 

Each puzzle room contains a different brain teaser for the user to solve. if they input the correct answer, they win a letter which is stored in a variable and they are given the option to move forward to the next room or give up.

If they give up, the game ends and resets back to the Home Page. If they continue on through each puzzle room, they will reach the treasure chest. In order to open the chest and gain access to the treasure, they have to use all the letters they have collected along the way which form a word.

At the end of the game, they can choose to play again, or not.

![Cave Flowchart](assets/images/cave-flowchart.drawio.png)

[Back to top](<#contents>)


# Current Features

  
## Title Page

Across the main home page screen, when you run the program, you are introduced to the game title 'The Cave of Query' and you are asked to enter your name, which starts the game. 

![Homepage image](assets/images/title-page.png)

[Back to top](<#contents>)

## Game Introduction

Once the user has entered their name, they enter the cave and they are given an introduction to the user story. The player is the grandchild of the infamous Indiana Jones. In his last will and testament, he leaves you an old key and his diary, where he used to write all his treasure-hunting information. In the diary, you find information about the Caves of Query, a quest Indiana never managed to complete. 

In his stead, you decide to travel to the Caves of Query and try your luck, after all you have the Jones' explorer genes. You have brought the diary and the key with you. 

I used [Ascii Art](https://emojicombos.com/cave-entrance-dot-art) to print an image of a cave in this introduction section. I didn't want to bog the user down with a whole page of introduction text to get them into the spirit of the game, but at the same time, I wanted to give them something to let them visualise going into the game area. A text-based game like this relys a lot on the user's imagination so at least this gives them a little prompt. 

![Rules Page image](assets/images/game-intro.png)

[Back to top](<#contents>)

## Puzzle Rooms

Each puzzle room contains a different type of puzzle. These range from maths puzzles, to anagrams, to deciphering strange languages. If the user types in the wrong answer, I have tried to give them a hint to steer them in the right direction towards the correct answer. This is printed in green.

The validation makes the input not case sensitive, so if they type the correct word in either upper or lower case, it will still pass as correct. 

The validation is printed in red to stand out to the user.

![Validation and Hints](assets/images/validation-and-hint.png)

A lot of the puzzles contain Indiana Jones trivia. Both the two language decipher puzzles are Indiana quotes, and also the library book challenge is one of Indiana's most famous quotes as well. 

The letters collected throughout the game spell: 'Pythonic'. This is both a play on the language I have been using throughout this project to build the game but also Indiana Jones' greatest fear; snakes!

After each puzzle is correctly answered, the user is awarded a letter. They are then shown all the letters that they have won and collected up to this point, and these are printed in yellow.

At the end of each puzzle they are give the option to continue or give up. If they continue, the next puzzle room is displayed, otherwise the game is over and the user is taken back to the Home Page.

![Continue or Quit Page](assets/images/hint-and-letters.png)

[Back to top](<#contents>)

## End of Game Page

Once eight puzzles have been completed, and all the collected letters re-arranged and typed correctly into the treasure chest crpytex, the treasure chest key hole is revealed. 

I used [Ascii Art](https://emojicombos.com/key) to print a picture of a key and the user wins the game and is rewarded with the treasure. Amongst the treasure, they also find another treasure map, and they have the option to continue their new found treasure hunting skills, or quit while they are ahead. If they choose to quit, the game ends. If they choose to continue the treasure hunt, the user is taken back to the Home Page to begin the game again. With future developement, this option would take them to a new adventure with alternative brain teasers to complete, using the newly acquired treasure map. 

![End of Game Page](assets/images/end-game.png)

[Back to top](<#contents>)

## Future Features 

In the future, I would like to add more features to the Cave of Query game. These could include:

* Difficulty levels
* More puzzle rooms
* The option to choose various doors after each puzzle, similar to in my original map design, see [Game Design](<#game-design>).
* Additional levels, to make use of the treasure map found at the end of the Game, as described previously.

One day, when I'm an expert Full Stack Software Developer, I would love to be able to add graphics, music, characters, etc. to this game, and make it more than just text-based if my abilities in the future will allow me. 


[Back to top](<#contents>)

# Technologies Used

I used the following technologies to create this website:

* Python – Content and structure
* Gitpod – Website deployment
* Github – Website code repository
* Heroku - Hosting platform for the game
* Diagrams.net - Create the game layout and flowchart


[Back to top](<#contents>)

# Testing

Please click [**_here_**](TESTING.md) to read more information about testing The Cave of Query

[Back to top](<#contents>)

# Deployment

### **To deploy the project**
The game was deployed via an online platform called as Heroku, used to improve user experience when viewing a program written in code such as Python. The deployment process is as follows:

1. Create new Heroku app from Heroku dashboard
2. Choose an app name that is available.
3. Choose the region where you are working from (Europe)
4. Select the create app button
5. Select 'Settings' from the main menu
6. Scroll to 'Config Vars' section and select 'Reveal Config Vars'
7. In the 'Key' field input 'PORT' in the 'Value' field input '8000'
8. Press 'Add' to add the value just entered
9. Repeat this process to create a key called 'CREDS' and paste the values in from the CREDS.Json file in Gitpod to hide sensetive data from the user.
10. Scroll down to 'Add buildpack' and select it
11. Select 'Python' and save changes
12. Select 'Add buildpack' again and do the same with 'NodeJs'
13. Link the App to your matching GitHub repository 
13. Select Automatic deploy

![Deploy image](assets/images/deploy-githubconnect.png)
![Deploy image](assets/images/deployment.png)

  The live link to the Github repository can be found here - https://cave-of-query.herokuapp.com/

### **To fork the repository using GitHub**
A copy of the GitHub Repository can be made by forking the GitHub account. This copy can be viewed and changes can be made to the copy without affecting the original repository. Take the following steps to fork the repository:
1. Log in to **GitHub** and locate the [repository](https://github.com/quiltingcode/cave-of-query).
2. On the right hand side of the page inline with the repository name is a button called **'Fork'**, click on the button to create a copy of the original repository in your GitHub Account.

![GitHub fork image](assets/images/cave-fork.png)

### **To create a local clone of this project**
The method from cloning a project from GitHub is below:

1. Under the repository’s name, click on the **code** tab.
2. In the **Clone with HTTPS** section, click on the clipboard icon to copy the given URL.

![Cloning image](assets/images/cave-clone.png)

3. In your IDE of choice, open **Git Bash**.
4. Change the current working directory to the location where you want the cloned directory to be made.
5. Type **git clone**, and then paste the URL copied from GitHub.
6. Press **enter** and the local clone will be created.

[Back to top](<#contents>)

# Credits
### Content

* I researched how to begin creating a text-based adventure game through [www.makeuseof.com](https://www.makeuseof.com/python-text-adventure-game-create/)
* I got brain teaser puzzle ideas from [teambuilding.com](https://teambuilding.com/blog/escape-room-puzzles)
* I found the Morse Code dictionary at [morsedecoder.com](https://morsedecoder.com/)
* I researched Indiana Jones trivia at [thoughtcatalog.com](https://thoughtcatalog.com/oliver-miller/2013/03/50-quotes-from-the-indiana-jones-movies-in-order-of-awesomeness/)
* I researched classic books at [oclc.org](https://www.oclc.org/en/worldcat/library100/top500.html)
* I learnt how to print lists into multiple columns and prevent empty user input through the [Bobby Hadz Blog](https://bobbyhadz.com/blog/python-print-list-in-columns)
* I learnt how to print lists  in a user friendly format through [pythonpool.com](https://www.pythonpool.com/remove-brackets-from-list-python/)
* I learnt how to compare two lists to validate multiple word user input using this article from [Stack Overflow](https://stackoverflow.com/questions/8866652/determine-if-2-lists-have-the-same-elements-regardless-of-order)
 
### Media

* The ascii art images used in this game were sourced from [emojicombos.com](https://emojicombos.com/)
 

[Back to top](<#contents>)

# Acknowledgements
The site was completed as a Portfolio Project 3 piece for the Full Stack Software Developer (e-Commerce) Diploma at the [Code Institute](https://codeinstitute.net/). As such I would like to thank my mentor [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/) for his continuous support in both this project and throughout the course, the Slack community, and all at the Code Institute for their help and support. I love Indiana Jones and the first thing I remember wanting to be when I was little was an archaeologist (basically a treasure hunter!) and so it was a joy to be able to create a game dedicated to something I love to dream about doing.

Kelly Hutchison 2022.

[Back to top](<#contents>)