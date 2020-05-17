# Restraining-Bolts-for-Reinforcement-Learning-using-Linear-Time-Logic
AIRO project. Elective in Artificial Intelligence course: Reasoning Agents
Università La Sapienza Roma

<a href="https://www.dis.uniroma1.it/"><img src="http://www.dis.uniroma1.it/sites/default/files/marchio%20logo%20eng%20jpg.jpg" width="500"></a>

## Approach (First Example)
Reasoning Agents project: Reinforcement Learning and Restraining Bolts with LTL specifications

ENV: chessboard: 5 colors ('green','blue','purple','black','grey'), 4 visits for each color; grid 5x7.

RL: learn the chess moves: Knight, King, Rock, Bishop, Queen with SARSA learning algorithm

RB specification: perform moves in the specified order (NB: order for the subject, i.e. first the Knight, then the King ...) (NB: each move is not random, i.e. start from 1,1 then goes to 1,2 ... the Knight moves from the bottom to the top...)

## Approach (Second Example) (abstract)
Pick And Place Robot (future work)

The environment is completed, but there is only the link with RL part: the Linear Temporal Logic is only sketched (so the Restraining Bolts specifications are not implemented)

RL + RB: the robot is fixed on yellow square: its end effector moves around the 3x3 grid, it must learn to take the current item from the green square each time and bring it on each red shelf, by following the order RB specification (not randomly)


## Team
* Flavio Lorenzi <a href="https://github.com/FlavioLorenzi"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/1024px-Octicons-mark-github.svg.png" width="30"></a>
<a href="https://www.linkedin.com/in/flavio-lorenzi-875982171/"><img src="https://www.tecnomagazine.it/tech/wp-content/uploads/2013/05/linkedin-aggiungere-immagini.png" width="30"></a>

* Nicolò Mantovani <a href="https://github.com/Nicodman"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/1024px-Octicons-mark-github.svg.png" width="30"></a>
* Sara Tozzo
* Giorgia Piernoli


## Documentation
You can see our final slide presentation about this project in Documents Folder

Here there is also the main reference paper of our work.



## Training the Chess Game (exp 1)
$ python game.py Chess4 Sarsa new_trainfile

## Plot the results
$ python plotresults.py -datafiles data/new_training

## References
Original Paper, Università La Sapienza Roma
- https://aaai.org/Papers/AAAI/2020GB/SCT-De%20GiacomoG.703.pdf

RL_GAMES: Iocchi,De giacomo, Patrizi, Università La Sapienza Roma
- https://sites.google.com/diag.uniroma1.it/restraining-bolt


