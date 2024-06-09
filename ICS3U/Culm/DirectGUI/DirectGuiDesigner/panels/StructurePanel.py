#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Fireclaw the Fox"
__license__ = """
Simplified BSD (BSD 2-Clause) License.
See License.txt or http://opensource.org/licenses/BSD-2-Clause for more info
"""

from panda3d.core import VBase4, TextNode, Point3, TransparencyAttrib

from direct.gui import DirectGuiGlobals as DGG
from direct.gui.DirectLabel import DirectLabel
from direct.gui.DirectScrolledFrame import DirectScrolledFrame
from direct.gui.DirectButton import DirectButton
from direct.gui.DirectCheckBox import DirectCheckBox

from DirectGuiExtension import DirectGuiHelper as DGH
from DirectGuiExtension.DirectBoxSizer import DirectBoxSizer
from DirectGuiExtension.DirectAutoSizer import DirectAutoSizer

class StructurePanel():
    def __init__(self, parent, getEditorRootCanvas, elementDict, selectedElement):
        height = DGH.getRealHeight(parent)
        self.collapsedElements = []

        self.parent = parent


        self.box = DirectBoxSizer(
            frameColor=(0.25, 0.25, 0.25, 1),
            autoUpdateFrameSize=False,
            orientation=DGG.VERTICAL)
        self.sizer = DirectAutoSizer(
            updateOnWindowResize=False,
            parent=parent,
            child=self.box,
            childUpdateSizeFunc=self.box.refresh)

        self.lblHeader = DirectLabel(
            text="Structure",
            text_scale=16,
            text_align=TextNode.ALeft,
            text_fg=(1,1,1,1),
            frameColor=VBase4(0, 0, 0, 0),
            )
        self.box.addItem(self.lblHeader)

        color = (
            (0.8, 0.8, 0.8, 1), # Normal
            (0.9, 0.9, 1, 1), # Click
            (0.8, 0.8, 1, 1), # Hover
            (0.5, 0.5, 0.5, 1)) # Disabled
        self.structureFrame = DirectScrolledFrame(
            # make the frame fit into our background frame
            frameSize=VBase4(
                self.parent["frameSize"][0], self.parent["frameSize"][1],
                self.parent["frameSize"][2]+DGH.getRealHeight(self.lblHeader), self.parent["frameSize"][3]),
            #canvasSize=VBase4(parent["frameSize"][0], parent["frameSize"][1]-20, height+30, 0),
            # set the frames color to transparent
            frameColor=VBase4(1, 1, 1, 1),
            scrollBarWidth=20,
            verticalScroll_scrollSize=20,
            verticalScroll_thumb_relief=DGG.FLAT,
            verticalScroll_incButton_relief=DGG.FLAT,
            verticalScroll_decButton_relief=DGG.FLAT,
            verticalScroll_thumb_frameColor=color,
            verticalScroll_incButton_frameColor=color,
            verticalScroll_decButton_frameColor=color,
            horizontalScroll_thumb_relief=DGG.FLAT,
            horizontalScroll_incButton_relief=DGG.FLAT,
            horizontalScroll_decButton_relief=DGG.FLAT,
            horizontalScroll_thumb_frameColor=color,
            horizontalScroll_incButton_frameColor=color,
            horizontalScroll_decButton_frameColor=color,
            state=DGG.NORMAL)
        self.box.addItem(self.structureFrame)
        self.structureFrame.bind(DGG.MWDOWN, self.scroll, [0.01])
        self.structureFrame.bind(DGG.MWUP, self.scroll, [-0.01])
        self.maxWidth = parent["frameSize"][1]-20
        self.getEditorRootCanvas = getEditorRootCanvas
        self.refreshStructureTree(elementDict, selectedElement)

    def scroll(self, scrollStep, event):
        self.structureFrame.verticalScroll.scrollStep(scrollStep)

    def recalcScrollSize(self):
        a = self.structureFrame["canvasSize"][2]
        b = abs(self.structureFrame["frameSize"][2]) + self.structureFrame["frameSize"][3]
        scrollDefault = 200
        s = -(scrollDefault / (a / b))

        self.structureFrame["verticalScroll_scrollSize"] = s
        self.structureFrame["verticalScroll_pageSize"] = s


    def resizeFrame(self):
        preSize = self.sizer["frameSize"]
        self.sizer.refresh()
        postSize = self.sizer["frameSize"]

        if preSize != postSize:
            self.structureFrame["frameSize"] = (
                    self.parent["frameSize"][0], self.parent["frameSize"][1],
                    self.parent["frameSize"][2]+DGH.getRealHeight(self.lblHeader), self.parent["frameSize"][3])

            self.recalcScrollSize()

        #posZ = 0
        #height = DGH.getRealHeight(parent)
        #self.lblHeader["frameSize"] = (self.parent["frameSize"][0], self.parent["frameSize"][1], -10, 20)
        #self.lblHeader["text_pos"] = (self.parent["frameSize"][0], 0)
        #self.lblHeader.setPos(0,0,posZ-20)
        #posZ -= 30
        #self.structureFrame["frameSize"] = (self.parent["frameSize"][0], self.parent["frameSize"][1], height+30, 0)
        #self.structureFrame.setPos(0,0,posZ)

    def refreshStructureTree(self, elementDict, selectedElement):
        self.elementDict = elementDict
        self.selectedElement = selectedElement

        # cleanup the structure tree
        for element in self.structureFrame.getCanvas().getChildren():
            element.removeNode()

        self.maxWidth = self.parent["frameSize"][1]-20
        self.itemCounter = 0

        # create the tree
        self.__fillStructureTree(self.getEditorRootCanvas(), 0, 0)

        self.structureFrame["canvasSize"] = (
            self.structureFrame["frameSize"][0], self.maxWidth,
            self.itemCounter*-16, 0)
        self.structureFrame.setCanvasSize()
        self.recalcScrollSize()

    def __fillStructureTree(self, root, level, z):
        if "DirectGrid" in root.getName(): return
        self.itemCounter += 1

        elementInfo = None
        if root.getName() in self.elementDict.keys():
            elementInfo = self.elementDict[root.getName()]
        elif len(root.getName().split("-")) > 1 and root.getName().split("-")[1] in self.elementDict.keys():
            elementInfo = self.elementDict[root.getName().split("-")[1]]

        if level > 0:
            self.__makeStructureFrameTreeItem(root, elementInfo, level, z)
        if hasattr(root, "getChildren") \
        and elementInfo not in self.collapsedElements:
            for child in root.getChildren():
                z=-16*self.itemCounter
                self.__fillStructureTree(child, level+1, z)

    def __makeStructureFrameTreeItem(self, elementNP, elementInfo, parentsLevel, z):
        if elementInfo is None:
            lbl = DirectLabel(
                text=elementNP.getName(),
                text_align=TextNode.ALeft,
                frameColor=(0,0,0,0),
                relief=DGG.FLAT,
                pos=(self.structureFrame["frameSize"][0] + 20*parentsLevel, 0, z),
                scale=16,
                parent=self.structureFrame.getCanvas())
            self.maxWidth = max(self.maxWidth, lbl.getX() + lbl.getWidth()*lbl.getScale()[0])
        else:
            margin = 5
            shift = 6

            if hasattr(elementNP, "getChildren"):
                if len(elementNP.getChildren()) > 0:
                    # Collapse Button
                    btnC = DirectCheckBox(
                        relief=DGG.FLAT,
                        pos=(self.structureFrame["frameSize"][0] + 20*parentsLevel - 16 + margin, 0, z+shift),
                        frameSize=(-8, 8, -8, 8),
                        frameColor=(0,0,0,0),
                        command=self.__collapseElement,
                        extraArgs=[elementInfo],
                        image="icons/Collapsed.png" if elementInfo in self.collapsedElements else "icons/Collapse.png",
                        uncheckedImage="icons/Collapse.png",
                        checkedImage="icons/Collapsed.png",
                        image_scale=8,
                        isChecked=elementInfo in self.collapsedElements,
                        parent=self.structureFrame.getCanvas())
                    btnC.setTransparency(TransparencyAttrib.M_alpha)
                    btnC.bind(DGG.MWDOWN, self.scroll, [0.01])
                    btnC.bind(DGG.MWUP, self.scroll, [-0.01])

            # Element Name
            btn = DirectButton(
                frameColor=(VBase4(1,1,1,1), #normal
                    VBase4(0.9,0.9,0.9,1), #click
                    VBase4(0.8,0.8,0.8,1), #hover
                    VBase4(0.5,0.5,0.5,1)), #disabled
                text=elementInfo.name,
                text_align=TextNode.ALeft,
                relief=DGG.FLAT,
                pos=(self.structureFrame["frameSize"][0] + 20*parentsLevel, 0, z),
                scale=16,
                command=self.__selectElement,
                extraArgs=[elementInfo],
                parent=self.structureFrame.getCanvas())
            btn.bind(DGG.MWDOWN, self.scroll, [0.01])
            btn.bind(DGG.MWUP, self.scroll, [-0.01])
            if self.selectedElement is not None and self.selectedElement == elementInfo:
                btn.setColorScale(1,1,0,1)

            x = self.structureFrame["frameSize"][0] + 8 + margin + 20*parentsLevel + btn.getWidth()*btn.getScale()[0]
            # Delete Button
            btnX = DirectButton(
                relief=DGG.FLAT,
                pos=(x, 0, z+shift),
                frameSize=(-8, 8, -8, 8),
                frameColor=(0,0,0,0),
                command=self.__removeElement,
                extraArgs=[elementInfo],
                image="icons/DeleteSmall.png",
                image_scale=8,
                parent=self.structureFrame.getCanvas())
            btnX.setTransparency(TransparencyAttrib.M_multisample)
            btnX.bind(DGG.MWDOWN, self.scroll, [0.01])
            btnX.bind(DGG.MWUP, self.scroll, [-0.01])

            x += margin + btnX.getWidth()
            # Visibility Button
            btnV = DirectCheckBox(
                relief=DGG.FLAT,
                pos=(x, 0, z+shift),
                frameSize=(-8, 8, -8, 8),
                frameColor=(0,0,0,0),
                command=self.__toggleElementVisibility,
                extraArgs=[elementInfo],
                image="icons/VisibilityOffSmall.png" if elementInfo.element.isHidden() else "icons/VisibilityOnSmall.png",
                uncheckedImage="icons/VisibilityOffSmall.png",
                checkedImage="icons/VisibilityOnSmall.png",
                image_scale=8,
                isChecked=not elementInfo.element.isHidden(),
                parent=self.structureFrame.getCanvas())
            btnV.setTransparency(TransparencyAttrib.M_multisample)
            btnV.bind(DGG.MWDOWN, self.scroll, [0.01])
            btnV.bind(DGG.MWUP, self.scroll, [-0.01])
            self.maxWidth = max(self.maxWidth, btnV.getX() + 8)

            x += margin + btnV.getWidth()
            # Move Up Button
            btnUp = DirectButton(
                relief=DGG.FLAT,
                pos=(x, 0, z+shift),
                frameSize=(-8, 8, -8, 8),
                frameColor=(0,0,0,0),
                command=self.__moveElementInStructure,
                extraArgs=[-2, elementInfo],
                image="icons/ArrowUpSmall.png",
                image_scale=8,
                parent=self.structureFrame.getCanvas())
            btnUp.setTransparency(TransparencyAttrib.M_multisample)
            btnUp.bind(DGG.MWDOWN, self.scroll, [0.01])
            btnUp.bind(DGG.MWUP, self.scroll, [-0.01])

            x += margin + btnUp.getWidth()
            # Move Down Button
            btnDown = DirectButton(
                relief=DGG.FLAT,
                pos=(x, 0, z+shift),
                frameSize=(-8, 8, -8, 8),
                frameColor=(0,0,0,0),
                command=self.__moveElementInStructure,
                extraArgs=[1, elementInfo],
                image="icons/ArrowDownSmall.png",
                image_scale=8,
                parent=self.structureFrame.getCanvas())
            btnDown.setTransparency(TransparencyAttrib.M_multisample)
            btnDown.bind(DGG.MWDOWN, self.scroll, [0.01])
            btnDown.bind(DGG.MWUP, self.scroll, [-0.01])

    def __selectElement(self, elementInfo, args=None):
        if elementInfo is not None:
            base.messenger.send("selectElement", [elementInfo, args])

    def __removeElement(self, elementInfo):
        if elementInfo is not None:
            base.messenger.send("removeElement", [elementInfo.element])

    def __toggleElementVisibility(self, toggle, elementInfo):
        if elementInfo is not None:
            base.messenger.send("toggleElementVisibility", [elementInfo.element])

    def __moveElementInStructure(self, direction, elementInfo):
        if elementInfo is not None:
            base.messenger.send("moveElementInStructure", [direction, elementInfo])

    def __collapseElement(self, collapse, elementInfo):
        if elementInfo is not None:
            if collapse:
                self.collapsedElements.append(elementInfo)
            else:
                self.collapsedElements.remove(elementInfo)
            base.messenger.send("refreshStructureTree")
