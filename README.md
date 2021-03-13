#World of Warcraft's shittiest fishign bot

##TODO
    - figure out better way to score difference between frames
    - better method of finding bobber position (current pixel fiddling hack is bad)
    - add shortcut to disable & stop the bot 
    - add WoW window detection
    - Only run inside the WoW window

##Working:
     - take screen shots
     - transform to black and white
     - crop out the middle 3rd of width and height
     - find edges using Canny Edge detection.

##Almost working:
    - currently uses skimage structural_similarity to calculate score
    - score 1.0 i.e. the same image is used to cast a new fishing

##Not so working:
    - score below average score is used to move cursor to first white pixel of frame to right-click the bobber
