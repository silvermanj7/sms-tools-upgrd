# GUI frame for the stochasticModel_function.py

import tkinter as tk
import tkinter.filedialog, tkinter.messagebox
import sys, os
from scipy.io.wavfile import read
import stochasticModel_function
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../models/'))
import utilFunctions as UF

class StochasticModel_frame:

	def __init__(self, parent):

		self.parent = parent
		self.initUI()

	def initUI(self):

		choose_label = "Input file (.wav, mono and 44100 sampling rate):"
		tk.Label(self.parent, text=choose_label).grid(row=0, column=0, sticky=tk.W, padx=5, pady=(10,2))

		#TEXTBOX TO PRINT PATH OF THE SOUND FILE
		self.filelocation = tk.Entry(self.parent)
		self.filelocation.focus_set()
		self.filelocation["width"] = 25
		self.filelocation.grid(row=1,column=0, sticky=tk.W, padx=10)
		self.filelocation.delete(0, tk.END)
		self.filelocation.insert(0, '../../sounds/ocean.wav')

		#BUTTON TO BROWSE SOUND FILE
		self.open_file = tk.Button(self.parent, text="Browse...", command=self.browse_file) #see: def browse_file(self)
		self.open_file.grid(row=1, column=0, sticky=tk.W, padx=(220, 6)) #put it beside the filelocation textbox

		#BUTTON TO PREVIEW SOUND FILE
		self.preview = tk.Button(self.parent, text=">", command=lambda:UF.wavplay(self.filelocation.get()), bg="gray30", fg="white")
		self.preview.grid(row=1, column=0, sticky=tk.W, padx=(306,6))

		## STOCHASTIC MODEL

		#HOP SIZE
		H_label = "Hop size (H):"
		tk.Label(self.parent, text=H_label).grid(row=2, column=0, sticky=tk.W, padx=5, pady=(10,2))
		self.H = tk.Entry(self.parent, justify=tk.CENTER)
		self.H["width"] = 5
		self.H.grid(row=2, column=0, sticky=tk.W, padx=(90,5), pady=(10,2))
		self.H.delete(0, tk.END)
		self.H.insert(0, "256")

		#FFT size
		N_label = "FFT size (N):"
		tk.Label(self.parent, text=N_label).grid(row=3, column=0, sticky=tk.W, padx=5, pady=(10,2))
		self.N = tk.Entry(self.parent, justify=tk.CENTER)
		self.N["width"] = 5
		self.N.grid(row=3, column=0, sticky=tk.W, padx=(90,5), pady=(10,2))
		self.N.delete(0, tk.END)
		self.N.insert(0, "512")

		#DECIMATION FACTOR
		stocf_label = "Decimation factor (bigger than 0, max of 1):"
		tk.Label(self.parent, text=stocf_label).grid(row=4, column=0, sticky=tk.W, padx=5, pady=(10,2))
		self.stocf = tk.Entry(self.parent, justify=tk.CENTER)
		self.stocf["width"] = 5
		self.stocf.grid(row=4, column=0, sticky=tk.W, padx=(285,5), pady=(10,2))
		self.stocf.delete(0, tk.END)
		self.stocf.insert(0, "0.1")

		#BUTTON TO COMPUTE EVERYTHING
		self.compute = tk.Button(self.parent, text="Compute", command=self.compute_model, bg="dark red", fg="white")
		self.compute.grid(row=5, column=0, padx=5, pady=(10,2), sticky=tk.W)

		#BUTTON TO PLAY OUTPUT
		output_label = "Stochastic:"
		tk.Label(self.parent, text=output_label).grid(row=6, column=0, sticky=tk.W, padx=5, pady=(10,15))
		self.output = tk.Button(self.parent, text=">", command=lambda:UF.wavplay('output_sounds/' + os.path.basename(self.filelocation.get())[:-4] + '_stochasticModel.wav'), bg="gray30", fg="white")
		self.output.grid(row=6, column=0, padx=(80,5), pady=(10,15), sticky=tk.W)

		# define options for opening file
		self.file_opt = options = {}
		options['defaultextension'] = '.wav'
		options['filetypes'] = [('All files', '.*'), ('Wav files', '.wav')]
		options['initialdir'] = '../../sounds/'
		options['title'] = 'Open a mono audio file .wav with sample frequency 44100 Hz'

	def browse_file(self):

		self.filename = tk.filedialog.askopenfilename(**self.file_opt)

		#set the text of the self.filelocation
		self.filelocation.delete(0, tk.END)
		self.filelocation.insert(0,self.filename)

	def compute_model(self):

		try:
			inputFile = self.filelocation.get()
			H = int(self.H.get())
			N = int(self.N.get())
			stocf = float(self.stocf.get())

			stochasticModel_function.main(inputFile, H, N, stocf)

		except ValueError as errorMessage:
			tkinter.messagebox.showerror("Input values error", errorMessage)
