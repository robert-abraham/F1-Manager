from direct.showbase.ShowBase import ShowBase
from panda3d.core import LineSegs, NodePath, Point3, CardMaker
from direct.gui.OnscreenText import OnscreenText
from direct.task import Task
import sys
from stageflow import Stage


class Game(Stage):
    def enter(self, d):

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

        # Create text nodes for instructions and win/lose messages
        self.instructions = OnscreenText(text="Click as fast as you can!", pos=(0, 0.9), scale=0.07, fg=(1, 1, 1, 1))
        self.result_text = OnscreenText(text="", pos=(0, 0), scale=0.1, fg=(1, 0, 0, 1), mayChange=True)

        # Set up click zones
        base.accept("space", self.player_click)
        base.accept("escape", sys.exit)

        self.rope_position = 0  # Starting in the middle
        self.speed = 0.01
        self.max_position = 0.2

        base.taskMgr.add(self.update_game, "updateGameTask")

    def player_click(self):
        self.rope_position += self.speed
        self.update_rope_position()
        self.check_win_condition()

    def update_rope_position(self):
        base.marker_node.setX(self.rope_position * 6)  # Adjust multiplier for visual scale

    def check_win_condition(self):
        if self.rope_position >= self.max_position:
            self.result_text.setText("Player Wins!")
            base.taskMgr.remove("updateGameTask")
        elif self.rope_position <= -self.max_position:
            self.result_text.setText("Computer Wins!")
            base.taskMgr.remove("updateGameTask")

    def update_game(self, task):
        # Simulate computer clicks
        self.rope_position -= self.speed / 10  # Adjust difficulty as needed
        self.update_rope_position()
        self.check_win_condition()
        return Task.cont


