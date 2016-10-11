import tkinter as tk

class notebook(object):
	def __init__(self, master, side=tk.LEFT):
		self.active_fr = None
		self.count = 0
		self.choice = tk.IntVar(0)
		if side in (tk.TOP, tk.BOTTOM):
			self.side = tk.LEFT
		else: self.side = tk.TOP
		self.rb_fr = tk.Frame(master, borderwidth=2, relief=tk.GROOVE)
		self.rb_fr.pack(side=side, fill=tk.BOTH)
		self.screen_fr = tk.Frame(master, borderwidth=2, relief=tk.FLAT)
		self.screen_fr.pack(fill=tk.BOTH)

	def __call__(self):
		return self.screen_fr

	def add_screen(self, fr, title):
		b = tk.Radiobutton(self.rb_fr, text=title, indicatoron=0, variable=self.choice, value=self.count, command=lambda: self.display(fr))
		b.pack(fill=tk.BOTH, side=self.side)
		if not self.active_fr:
			fr.pack(fill=tk.BOTH, expand=1)
		self.active_fr = fr
		self.count += 1

	def display(self, fr):
		self.active_fr.forget( )
		fr.pack(fill=tk.BOTH, expand=1)
		self.active_fr = fr
