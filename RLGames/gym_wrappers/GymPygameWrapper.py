import os
from abc import ABC
from time import sleep

import cv2
from gym import Env, Wrapper
from gym.utils import EzPickle
from gym.wrappers import Monitor

import pygame

class GymPygameWrapper(ABC, Env, EzPickle):

    def __init__(self, *args, delay=0.01, **kwargs):
        Env.__init__(self)
        EzPickle.__init__(self, *args, **kwargs)

        self.delay = delay

    @property
    def PygameEnvClass(self):
        raise NotImplementedError

    def step(self, action):
        self.update(action)
        obs = self.getstate()
        reward = self.getreward()
        done = self.finished
        info = {"goal": self.goal_reached()}
        return obs, reward, done, info

    def render(self, mode='human'):
        self.draw()
        sleep(self.delay)


    def getreward(self):
        r = self.current_reward
        return r

    def reset(self):
        self.PygameEnvClass.reset(self)
        return self.getstate()


class PygameVideoRecorder(Wrapper):
    def __init__(self, env: GymPygameWrapper, directory, fps=30):
        super().__init__(env)

        self.episode = -1

        self.directory = directory
        if not os.path.isdir(self.directory):
            os.makedirs(self.directory, exist_ok=True)

        self.shape = (self.env.win_width, self.env.win_height)
        self.vid = None
        self.fps = fps

    def render(self, mode='human'):
        self.env.render()

        img = pygame.surfarray.array3d(self.env.screen)
        img = img.swapaxes(1, 0)
        # https://github.com/ContinuumIO/anaconda-issues/issues/223
        # from RGB to BGR
        img = img[:, :, ::-1].copy()
        self.vid.write(img)
        return img

    def reset(self, *args, **kwargs):
        self.episode += 1
        if self.vid is not None:
            self.vid.release()
        self.vid = cv2.VideoWriter(self.directory + '/episode_{}.avi'.format(self.episode),
                                   cv2.VideoWriter_fourcc(*"XVID"), self.fps, self.shape, 1)

        return self.env.reset(*args, **kwargs)


