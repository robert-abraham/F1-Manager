"""
Robert
ICS3UO
game.py
June 14

the main game, a tug of war like game (this is not the run file)
"""
from direct.showbase.ShowBase import ShowBase
from panda3d.core import LineSegs, NodePath, Point3, CardMaker
from direct.gui.OnscreenText import OnscreenText
from direct.task import Task
import sys
from stageflow import Stage
from Scenes.owned_countries import claim_country
from time import sleep

class Game(Stage):
    def enter(self, d):
        self.battledemp = d
        base.setBackgroundColor(0.5, 0.5, 0.5)
        base.disableMouse()


        # Create a line to represent the rope
        base.rope = LineSegs()
        base.rope.setThickness(10)
        base.rope.moveTo(-1.5, 0, 0)
        base.rope.drawTo(1.5, 0, 0)
        base.rope_node = base.rope.create()
        base.rope_node_path = NodePath(base.rope_node)
        base.rope_node_path.reparentTo(base.render)
        base.rope_node_path.setPos(0, 10, 0)  # Position the rope in front of the camera

        # Create a marker to show the rope's current position
        base.marker = CardMaker("marker")
        base.marker.setFrame(-0.1, 0.1, -0.04  , 0.04)
        base.marker_node = base.render.attachNewNode(base.marker.generate())
        base.marker_node.setPos(0, 9, 0)
        base.marker_node.setColor(1, 0, 0, 1)  # Red color

        # Create text entities for instructions and win/lose messages
        self.instructions = OnscreenText(text="Click Space as fast as you can!", pos=(0, 0.9), scale=0.07, fg=(1, 1, 1, 1))
        self.result_text = OnscreenText(text="", pos=(0, 0), scale=0.1, fg=(1, 0, 0, 1), mayChange=True)

        # Set up click zones, an event handler than looks for player clicks
        base.accept("space", self.player_click)
        base.accept("escape", sys.exit)

        self.rope_position = 0  # Starting in the middle
        self.speed = 0.01 #baseline speed
        self.max_position = 0.2 #max postion of marker

        base.taskMgr.add(self.update_game, "updateGameTask")
        self.entities = [self.instructions, self.result_text]

    def player_click(self): #called when the space bar is clicked, adds to the rope postion, updates, and cheks the win condition
        self.rope_position += self.speed
        self.update_rope_position()
        self.check_win_condition()

    def update_rope_position(self):
        base.marker_node.setX(self.rope_position * 7)  # Adjust multiplier for visual scale

    def check_win_condition(self):
        if self.rope_position >= self.max_position: #if the rope got to the users max postion, then the user has won
            self.result_text.setText("You Win!") # tells user they won
            claim_country(self.battledemp, won=True)
            base.taskMgr.remove("updateGameTask")
            base.ignoreAll()
            #call task to exit game in 1.5 seconds
            base.taskMgr.doMethodLater(1.5, self.exit_game, "exitGame")
           
        elif self.rope_position <= -self.max_position: #if computer wins
            self.result_text.setText(f"{self.battledemp} Wins!") #tells user computer won
            base.taskMgr.remove("updateGameTask")
            base.ignoreAll()
            #call task to exit game in 1.5 seconds
            base.taskMgr.doMethodLater(1.5, self.exit_game, "exitGame")

    def update_game(self, task):
        # Simulate computer clicks
        self.rope_position -= self.speed / 100  # Adjust difficulty as needed (the higher the easier)
        self.update_rope_position() #update the rope postion to play against the user
        self.check_win_condition() #check win condition every time game is updated
        return Task.cont
    
    #begins the proccess to exit the game
    def exit_game(self, task):
        base.flow.transition('MainMenu')  # go back to main menu
        return Task.done

    def exit(self, data):
        for entity in self.entities:
            entity.destroy()
        
        base.marker_node.removeNode()

        return data