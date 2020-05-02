#!/usr/bin/env python


class Domino(object):
    def __init__(self, end1=None, end2=None):
        self.end1 = end1
        self.end2 = end2

    def printVertical(self):
        print("[", self.end1, "|", self.end2, "]", sep='', end='')
