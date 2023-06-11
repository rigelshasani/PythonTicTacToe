#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import font

class TicTacToeBoard(tk.Tk):
    def init(self):
        self.title("Tic-Tac-Toe Game")
        self.cells = {}
        

