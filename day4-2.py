# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 10:43:38 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random
x,y,z = mc.player.getTilePos()
for i in range(20):
    r=random.randrange(1,5)
    
    if r==1:
        mc.setBlocks(x,y,z,x+4,y,z,120)
        x=x+4
    elif r==2:
        mc.setBlocks(x,y,z,x-4,y,z,116)
        x=x-4
    elif r==3:
        mc.setBlocks(x,y,z,x,y,z+4,138)
        z=z+4
    elif r==4:
        mc.setBlocks(x,y,z,x,y,z-4,130)
        z=z-4
     elif r==5:
        mc.setBlocks(x,y,z,x,y+4,z,139)
        y=y+1
      elif r==6:
        mc.setBlocks(x,y,z,x,y-4,z,135)
        y=y-1
        
        