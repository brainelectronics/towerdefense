#!/usr/bin/env python
# ----------------------------------------------------------------------------
# Tower Defense GUI File
# Copyright XD (c) 2015 Python Course TUM
# Scharpf, Jonas
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

import pyglet

window = pyglet.window.Window(caption="Tower Defense")
image = pyglet.resource.image('blue-dot.png')

class WindowClass(object):
	'''docstring for WindowClass'''
	def __init__(self, labelText):
		self.time = 0
		self.labelText = labelText
		self.label = pyglet.text.Label(text='%s' % (self.labelText),
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
	def update(self, dt):
		window.clear()
		image.width, image.height = 10, 10
		image.blit(100, 100)
		self.time += dt
		self.label.text = '%02d %s' % (self.time, self.labelText)
		self.label.draw()
		#print(self.time)