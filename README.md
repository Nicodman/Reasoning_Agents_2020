# Restraining-Bolts-for-Reinforcement-Learning-using-Linear-Time-Logic
AIRO project. Elective in Artificial Intelligence course: Reasoning Agents
Università La Sapienza Roma

<a href="https://www.dis.uniroma1.it/"><img src="http://www.dis.uniroma1.it/sites/default/files/marchio%20logo%20eng%20jpg.jpg" width="500"></a>

## Approach
Reasoning Agents project: Reinforcement Learning and Restraining Bolts

ENV: chessboard: 5 colors ('green','blue','purple','black','grey'), 4 visits for each color

RL: learn the chess moves: Knight, King, Rock, Bishop, Queen. __
RB specification: perform moves in the specified order (NB: order for the subject, i.e. first the Knight, then the King ...) (NB: each move is not random, i.e. start from 1,1 then goes to 1,2 ...)


## Team
* Flavio Lorenzi <a href="https://github.com/FlavioLorenzi"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/1024px-Octicons-mark-github.svg.png" width="30"></a>
<a href="https://www.linkedin.com/in/flavio-lorenzi-875982171/"><img src="https://www.tecnomagazine.it/tech/wp-content/uploads/2013/05/linkedin-aggiungere-immagini.png" width="30"></a>

* Nicolò Mantovani 
* Sara Tozzo
* Giulia Piernoli


## Documentation
You can read our final technical documentation about this project here (report todo)



## Training
$ python game.py Chess4 Sarsa new_trainfile

## Plot the results
$ python plotresults.py -datafiles data/new_training

## Reference
RL_GAMES, Iocchi,De giacomo, Patrizi, Università La Sapienza Roma
https://sites.google.com/diag.uniroma1.it/restraining-bolt
