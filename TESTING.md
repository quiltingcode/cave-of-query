# **_The Cave of Query_**

# Testing

## Code Validation

The Cave of Query site has been passed through the internal PEP8 validation tests which I installed into GitPod. The method I used to do this was as per the Slack Article written by kevin_ci on the 28th September 2022 in #announcements, since the PEP8online website no longer works:

1. Run the command 'pip3 install pycodestyle'
2. Press Ctrl+Shift+P
3. Type 'linter' into the search field
4. Select 'Python: Select Linter
5. Select 'pycodestyle' from the list
6. Select the 3 lines menu in the top left hand corner. Select 'View' and then 'Problems'. 
6. PEP8 errors are now displayed in a list as well as being underlined in red in the central editor window. 





## Browser Compatibility 

The Cave of Query was tested on the following browsers:

- Google Chrome
- Microsoft Edge
- Mozilla Firefox

I do not have any Apple devices available to carry out testing on a Safari browser. Appearance and functionality appear to be consistent throughout all browsers.


## Known Bugs

### Resolved

1. As a result of the PEP8 validation in GitPod the following 29 problems were detected: 

![PEP8 Errors](assets/images/pep8errors.png)



### Unresolved

1. In the console log, I can see that when the End Page is loaded, the countdown function is called, and the timer counts down and then times out. This makes no difference to the overall game functionality and the user can't see that this is happening unless they open the console. I have set the clearInterval function within the endGame function and the nextQuestion function if the user has reached question number 12, but this doesn't seem to work correctly. 

## Additional Testing



## Peer Review

In addition to the above tests, I asked my peers to play this quiz and their overall response was very positive. 
 

Please click [**_here_**](README.md) to return to the Cave of Query README file.