# GUI frame for the stochasticTransformations_function.py

import tkinter as tk
import tkinter.filedialog, tkinter.messagebox
import sys, os
from scipy.io.wavfile import read
import numpy as np
import stochasticTransformations_function as sT
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../models/'))
import utilFunctions as UF

class StochasticTransformations_frame:

	def __init__(self, parent):

		self.parent = parent
		self.initUI()

	def initUI(self):

		choose_Label = "inputFile:"
		tk.Label(self.parent, text=choose_Label).grid(row=0, column=0, sticky=tk.W, padx=5, pady=(10,2))

		#TEXTBOX TO PRINT PATH OF THE SOUND FILE
		self.filelocation = tk.Entry(self.parent)
		self.filelocation.focus_set()
		self.filelocation["width"] = 25
		self.filelocation.grid(row=0,column=0, sticky=tk.W, padx=(70, 5), pady=(10,2))
		self.filelocation.delete(0, tk.END)
		self.filelocation.insert(0, '../../sounds/rain.wav')

		#BUTTON TO BROWSE SOUND FILE
		open_file = tk.Button(self.parent, text="...", command=self.browse_file) #see: def browse_file(self)
		open_file.grid(row=0, column=0, sticky=tk.W, padx=(280, 6), pady=(10,2)) #put it beside the filelocation textbox

		#BUTTON TO PREVIEW SOUND FILE
		preview = tk.Button(self.parent, text=">", command=lambda:UF.wavplay(self.filelocation.get()), bg="gray30", fg="white")
		preview.grid(row=0, column=0, sticky=tk.W, padx=(325,6), pady=(10,2))

		## STOCHASTIC TRANSFORMATIONS ANALYSIS

		#DECIMATION FACTOR
		stocf_Label = "stocf:"
		tk.Label(self.parent, text=stocf_Label).grid(row=1, column=0, sticky=tk.W, padx=(5,5), pady=(10,2))
		self.stocf = tk.Entry(self.parent, justify=tk.CENTER)
		self.stocf["width"] = 5
		self.stocf.grid(row=1, column=0, sticky=tk.W, padx=(47,5), pady=(10,2))
		self.stocf.delete(0, tk.END)
		self.stocf.insert(0, "0.1")

		#TIME SCALING FACTORS
		timeScaling_Label = "Time scaling factors (time, value pairs):"
		tk.Label(self.parent, text=timeScaling_Label).grid(row=2, column=0, sticky=tk.W, padx=5, pady=(5,2))
		self.timeScaling = tk.Entry(self.parent, justify=tk.CENTER)
		self.timeScaling["width"] = 35
		self.timeScaling.grid(row=3, column=0, sticky=tk.W+tk.E, padx=5, pady=(0,2))
		self.timeScaling.delete(0, tk.END)
		self.timeScaling.insert(0, "[0, 0, 1, 2]")

		#BUTTON TO DO THE SYNTHESIS
		self.compute = tk.Button(self.parent, text="Apply Transformation", command=self.transformation_synthesis, bg="dark green", fg="white")
		self.compute.grid(row=13, column=0, padx=5, pady=(10,15), sticky=tk.W)

		#BUTTON TO PLAY TRANSFORMATION SYNTHESIS OUTPUT
		self.transf_output = tk.Button(self.parent, text=">", command=lambda:UF.wavplay('output_sounds/' + os.path.basename(self.filelocation.get())[:-4] + '_stochasticModelTransformation.wav'), bg="gray30", fg="white")
		self.transf_output.grid(row=13, column=0, padx=(165,5), pady=(10,15), sticky=tk.W)

		# define options for opening file
		self.file_opt = options = {}
		options['defaultextension'] = '.wav'
		options['filetypes'] = [('All files', '.*'), ('Wav files', '.wav')]
		options['initialdir'] = '../../sounds/'
		options['title'] = 'Open a mono audio file .wav with sample frequency 44100 Hz'

	def browse_file(self):

		self.filename = tkinter.filedialog.askopenfilename(**self.file_opt)

		#set the text of the self.filelocation
		self.filelocation.delete(0, tk.END)
		self.filelocation.insert(0,self.filename)

	def transformation_synthesis(self):

		try:
			inputFile = self.filelocation.get()
			stocf = float(self.stocf.get())
			timeScaling = np.array(eval(self.timeScaling.get()))

			sT.main(inputFile, stocf, timeScaling)

		except ValueError as errorMessage:
			tkinter.messagebox.showerror("Input values error", errorMessage)
