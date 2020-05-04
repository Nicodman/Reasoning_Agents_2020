import os
import sys

import numpy as np
from gym import Env
from gym.spaces import Discrete, Box, Dict

from RLGames.gym_wrappers.GymPygameWrapper import GymPygameWrapper

from RLGames.Chess import Chess
import RLGames.Chess as s
from RLGames.utils import DummyAgent, get_locals_no_self


class GymChess(GymPygameWrapper, Chess):
    """Wrapper for the Chess pygame"""

    PygameEnvClass = Chess

    def __init__(self, rows=5, cols=7, trainsessionname='test', ncol=7, nvisitpercol=2, differential=False):
        GymPygameWrapper.__init__(self, **get_locals_no_self(locals()))
        Chess.__init__(self, rows, cols, trainsessionname, ncol, nvisitpercol)
        self.differential = differential
        self.sound_enabled = False
        self.init(DummyAgent())

        self.observation_space = Dict({
            "x": Discrete(self.cols),
            "y": Discrete(self.rows),
            "theta": Discrete(4),                           # four directions: North - South - East - West
            "color": Discrete(len(s.COLORS) + 1),           # number of colors + no-color
            "cell": Discrete(len(s.TOKENS) + 1),           # from encode_colors()
            # "RAState": Discrete(self.RA.nRAstates + 2)      # RA states + goal + fail state

        })
        self.action_space = Discrete(self.nactions)


    def getstate(self):
        return {
            "x":        self.pos_x,
            "y":        self.pos_y,
            "theta":    int(self.pos_th/90),
            "color":    self.get_color(),
            "cell":     self.encode_color(),
            # "RAState":  int(self.RA.current_node)
        }

    def getreward(self):
        return Chess.getreward(self)

    def encode_color(self):
        for idx, t in enumerate(s.TOKENS):
            if (self.pos_x == t[2] and self.pos_y == t[3]):
                return idx
        return len(s.TOKENS)

    def get_color(self):
        t = self.encode_color()
        try:
            tok = s.TOKENS[t]
            color = s.COLORS.index(tok[1])
        except:
            # no color found
            color = len(s.COLORS)
        return color

    def step(self, action):
        obs, reward, done, info = super().step(action)
        if self.numactions > (self.cols * self.rows) * 10:
            done = True
        else:
            done = False
        info["goal"] = True
        return obs, reward, done, info

    def goal_reached(self):
        return True

    def reset(self):
        self.RA.init(self)
        return GymPygameWrapper.reset(self)