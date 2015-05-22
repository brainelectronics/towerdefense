#!/usr/bin/env python
# ----------------------------------------------------------------------------
# Tower Defense
# Copyright XD (c) 2015 Python Course TUM
# Abid, Mohamed
# Eckl, Tobias
# Fauser, Jonas
# Scharpf, Jonas
# Schmid, Johannes
# All rights reserved.
# 
# 
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

# import ConfigHannes
# import GUI
# import KI
# import Queue

import pyglet
from TDGUI import WindowClass

myWindow = WindowClass("Klaus")
pyglet.clock.schedule(myWindow.update)#schedule_interval doesn't work for me 
pyglet.app.run()

"""
class GameLoop(object):
	def __init__(self):
	  # load config file
	  # load something else
	  '''
	  load the config files and init the window(s)
	  '''
	  '''
	  configThis = ConfigHannes.load() # add path later
	  GUI.generateWindow() # makes new window
	  KI(configThis)
	  '''
	  loadingComplete = True
	  gameRunning = False
	  print("Setup done")

	def update():
	 	# if(KI.running()):
	 	if (loadingComplete):
	 		'''
	 		Setup has been done, show start window now
	 		'''
	 		print()

	 	elif(gameRunning):
	    	'''
	    	start window has been passed, show and run game now
	    	'''
	    	KI.update() # tower/mob (position, rotation, bullet)
	    	GUI.redraw(KI.getObjects())   # dict{Map:mapArray2x2, Tower:towerList, KI:kiList, Bullet:bulletList, els:elseList}
	    	# towerList[0].getPosition -> (x,y)
	   		# towerList[0].getAngle -> (123)
	    	# mapArray2x2[123][65] -> TileObject
	    	# TileObject.type .texture
	  	else:
	  		print("Uploading scores now")
	    	# ConfigHannes.uploadScore()
	    	"""
"""
@ mouse
  KI.mouseClick(x,y)
  #eventQueue.append(event)
  
@ keyboard
    # space gedruckt
    ConfigHannes.uploadScore()
"""    
