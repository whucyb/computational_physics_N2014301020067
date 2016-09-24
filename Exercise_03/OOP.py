# -*- coding: utf-8 -*-
class pet(object):
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return 'It is a '+self.name+'.'
class cat(pet):
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return self.name+' is a cat.'
    def NAME(self):
        print self.name
class white_cat(cat): 
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return self.name+' is a white cat.'
    def color(self):
        print 'white'
   