# WorldCup-Net
Using Deep Learning, this project predicts the winner of a football match. 

A self-build Neural Network is trained on the past data of footaball team (rating of the players) and the correspondig result.
Input to the network is a vector of shape 44 where first 22 elements are the ratings of players of home team and remaining 22 are the ratings of players of away teams.
Neural Network outputs one hot vector of shape 3, if first element is high home team wins, if second element is high the result is draw and if the third element is high
the away team wins.

The hyperparameters can be tuned. The optimizer used is SGD with CrossEntropyCost function. There are no dropouts and sparse connection, 
and no momentum is used in learning so if Deep Learning Libraries are used, the result would certainly be better.

### Requirements
* Numpy
* Matplotlib (optional)

### Execution
To train the network<br>
```$ python model.py```<br>
For prediction<br>
```$ python predict.py```

### Demo
![Screenshots](https://github.com/PrasangaDhungel/WorldCup-Net/blob/master/readme/demo.png)

#### Training
![Screenshots](https://github.com/PrasangaDhungel/WorldCup-Net/blob/master/readme/cost.png)

