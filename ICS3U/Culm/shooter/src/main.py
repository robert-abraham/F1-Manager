#!/usr/bin/python
# -*- coding: utf-8 -*-

from pandac.PandaModules import loadPrcFileData
loadPrcFileData("",
"""
    window-title GrimFang OWP - Shooter
    cursor-hidden 0
    show-frame-rate-meter 1
    model-path $MAIN_DIR/assets/
"""
)

from direct.showbase.ShowBase import ShowBase
from direct.showbase.DirectObject import DirectObject

from panda3d.core import VBase2
from panda3d.core import Vec4, ClockObject
from panda3d.ai import *

from player import Player
from enemy import Enemy
from level import Level

from mouse import Mouse
import random

class Main(ShowBase, DirectObject):
    def __init__(self):
        ShowBase.__init__(self)

        # Set the frame rate lock
        # We need to set globalClock rate to 30' because it looks
        # like the AI is affected by the frame rate.
        # the higher the rate the faster they move depending on
        # your pc.
        globalClock.setMode(ClockObject.MLimited)
        globalClock.setFrameRate(30)

        self.win.setClearColor(Vec4(0.12,0.43,0.18,1))
        self.disableMouse()
        self.player = Player(self)
        self.enemyList = []
        self.maxEnemyCount = 15

        self.level = Level()
        self.enemyParent = render.attachNewNode("EnemyParent")
        self.enemyParent.setH(180)
        self.enemyStrength = 0
        self.mouse = Mouse(self.level.planeNP)
        random.seed()

        self.gameStarted = False




        # Menu events
        self.accept("escape", self.quit)
        self.start()

        # ingame events
        self.accept("killEnemy", self.removeEnemy)

    # Start everything needed to play the game
    def start(self):
        self.gameStarted = True
        self.level.start()
        self.player.start(self.level.startPos, "pla")
        self.taskMgr.add(self.world, "MAIN TASK")
        self.accept("escape", self.stop)
        self.AiWorld = AIWorld(render)
        self.taskMgr.add(self.AIUpdate, "UPDATEAI")

    # When the game stops, we do some cleanups
    def stop(self):
        self.level.stop()

        self.player.stop()
        tempIDList = []
        for enemy in self.enemyList:
            tempIDList.append(enemy.id)
        for enemyID in tempIDList:
            self.removeEnemy(enemyID)
        tempIDList = []
        self.taskMgr.remove("MAIN TASK")
        self.accept("escape", self.quit)

    def quit(self):
        if self.appRunner:
            self.appRunner.stop()
        else:
            exit(0)

    def spawnEnemy(self):
        if len(self.enemyList) > self.maxEnemyCount: return False
        enemy = Enemy(self)

        x = self.player.model.getX()
        y = self.player.model.getY()
        while (x > self.player.model.getX() - 4.5 and x < self.player.model.getX() + 4.5):
            x = random.uniform(-9, 9)
        while (y > self.player.model.getY() - 4.5 and y < self.player.model.getY() + 4.5):
            y = random.uniform(-9, 9)
        position = VBase2(x, y)

        enemy.start(position, self.enemyParent)
        enemy.makeAi()
        self.enemyList.append(enemy)
        return True

    def removeEnemy(self, enemyID):
        for enemy in self.enemyList:
            if enemy.id == enemyID:
                enemy.stop()
                self.AiWorld.removeAiChar("Enemy"+str(enemyID))
                self.enemyList.remove(enemy)
                print("blah")
                return True
        return False



    def world(self, task):
        """MAIN TASK"""
        mul = int(self.player.points / 500)
        self.maxEnemyCount + (5 * mul)

        mul = int(self.player.points / 1000)

        mul = int(self.player.points / 1500)
        self.enemyStrength = 1 * mul

        self.spawnEnemy()
        self.player.playerTraverser.traverse(self.enemyParent)

        self.player.playerPushTraverser.traverse(self.level.planeNP)
        return task.cont

    def AIUpdate(self, task):
        if len(self.enemyList) <= 0:
            return False
        else:
            self.AiWorld.update()
            for enemy in self.enemyList:
                enemy.model.setP(-90)
        return task.cont

APP = Main()
APP.run()
