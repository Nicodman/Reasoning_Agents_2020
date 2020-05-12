#!/bin/env/python

import os
import time

def doExperiment(game, gameext, agent, gamma, epsilon, lambdae, alpha, nstep, niter, maxtime, stopongoal, exp_seeds):

    gameshortname = game[0]
    agentshortname = agent[0]
    gamecfg = '%s%s' %(game,gameext) 
    basetrainfilename = '%s%s_%s' %(gameshortname, gameext, agentshortname)
    if (gamma<1):
        basetrainfilename = basetrainfilename + '_g%03d' %(int(gamma*100))
    if (epsilon>0):
        basetrainfilename = basetrainfilename + '_e%02d' %(int(epsilon*100))
    if (lambdae>0):
        basetrainfilename = basetrainfilename + '_l%02d' %(int(lambdae*100))
    if (alpha>0):
        basetrainfilename = basetrainfilename + '_a%02d' %(int(alpha*100))
    if (nstep>1):
        basetrainfilename = basetrainfilename + '_n%d' %(nstep)

    str_stopongoal = ""
    if (stopongoal):
        str_stopongoal = "--stopongoal"

    for i in exp_seeds:
        cmd = "python3 game.py %s %s %s_%03d -seed %d -gamma %f -epsilon %f -lambdae %f -alpha %f -nstep %d -niter %d -maxtime %d %s" %(gamecfg,agent,basetrainfilename,i,i, gamma,epsilon,lambdae,alpha,nstep,niter,maxtime,str_stopongoal)
        print(cmd)
        os.system('xterm -geometry 100x20+0+20 -e "'+cmd+'"')
        # use -hold and & at the end for parallel execution and monitoring
        time.sleep(1)



agent = 'Sarsa'
gamma = 0.99
epsilon = -2
lambdae = -1
alpha = -1
niter = -1
stopongoal = False
       

        
# Chess
nstep = 20

maxtime = 200
doExperiment('Chess','4',agent, gamma, epsilon, lambdae, alpha, nstep, niter, maxtime, stopongoal, [101,102,103]) 



