# GUI frame for the stft_function.py

import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
import sys, os
from scipy.io.wavfile import read
import stft_function
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../models/'))
import utilFunctions as UF

class Stft_frame:
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
		self.filelocation.insert(0, '../../sounds/piano.wav')

		#BUTTON TO BROWSE SOUND FILE
		self.open_file = tk.Button(self.parent, text="Browse...", command=self.browse_file) #see: def browse_file(self)
		self.open_file.grid(row=1, column=0, sticky=tk.W, padx=(220, 6)) #put it beside the filelocation textbox

		#BUTTON TO PREVIEW SOUND FILE
		self.preview = tk.Button(self.parent, text=">", command=lambda:UF.wavplay(self.filelocation.get()), bg="gray30", fg="white")
		self.preview.grid(row=1, column=0, sticky=tk.W, padx=(306,6))

		## STFT

		#ANALYSIS WINDOW TYPE
		wtype_label = "Window type:"
		tk.Label(self.parent, text=wtype_label).grid(row=2, column=0, sticky=tk.W, padx=5, pady=(10,2))
		self.w_type = tk.StringVar()
		self.w_type.set("hamming") # initial value
		window_option = tk.OptionMenu(self.parent, self.w_type, "rectangular", "hanning", "hamming", "blackman", "blackmanharris")
		window_option.grid(row=2, column=0, sticky=tk.W, padx=(95,5), pady=(10,2))

		#WINDOW SIZE
		M_label = "Window size (M):"
		tk.Label(self.parent, text=M_label).grid(row=3, column=0, sticky=tk.W, padx=5, pady=(10,2))
		self.M = tk.Entry(self.parent, justify=tk.CENTER)
		self.M["width"] = 5
		self.M.grid(row=3,column=0, sticky=tk.W, padx=(115,5), pady=(10,2))
		self.M.delete(0, tk.END)
		self.M.insert(0, "1024")

		#FFT SIZE
		N_label = "FFT size (N) (power of two bigger than M):"
		tk.Label(self.parent, text=N_label).grid(row=4, column=0, sticky=tk.W, padx=5, pady=(10,2))
		self.N = tk.Entry(self.parent, justify=tk.CENTER)
		self.N["width"] = 5
		self.N.grid(row=4,column=0, sticky=tk.W, padx=(270,5), pady=(10,2))
		self.N.delete(0, tk.END)
		self.N.insert(0, "1024")

		#HOP SIZE
		H_label = "Hop size (H):"
		tk.Label(self.parent, text=H_label).grid(row=5, column=0, sticky=tk.W, padx=5, pady=(10,2))
		self.H = tk.Entry(self.parent, justify=tk.CENTER)
		self.H["width"] = 5
		self.H.grid(row=5,column=0, sticky=tk.W, padx=(95,5), pady=(10,2))
		self.H.delete(0, tk.END)
		self.H.insert(0, "512")

		#BUTTON TO COMPUTE EVERYTHING
		self.compute = tk.Button(self.parent, text="Compute", command=self.compute_model, bg="dark red", fg="white")
		self.compute.grid(row=6, column=0, padx=5, pady=(10,2), sticky=tk.W)

		#BUTTON TO PLAY OUTPUT
		output_label = "Output:"
		tk.Label(self.parent, text=output_label).grid(row=7, column=0, sticky=tk.W, padx=5, pady=(10,15))
		self.output = tk.Button(self.parent, text=">", command=lambda:UF.wavplay('output_sounds/' + os.path.basename(self.filelocation.get())[:-4] + '_stft.wav'), bg="gray30", fg="white")
		self.output.grid(row=7, column=0, padx=(60,5), pady=(10,15), sticky=tk.W)

		# define options for opening file
		self.file_opt = options = {}
		options['defaultextension'] = '.wav'
		options['filetypes'] = [('All files', '.*'), ('Wav files', '.wav')]
		options['initialdir'] = '../../sounds/'
		options['title'] = 'Open a mono audio file .wav with sample frequency 44100 Hz'

	def browse_file(self):

		self.filename = tkinter.filedialog.askopenfilename(**self.file_opt)

		#set the text of the self.filelocation
		self.filelocation.delete(0, END)
		self.filelocation.insert(0,self.filename)

	def compute_model(self):

		try:
			inputFile = self.filelocation.get()
			window = self.w_type.get()
			M = int(self.M.get())
			N = int(self.N.get())
			H = int(self.H.get())

			stft_function.main(inputFile, window, M, N, H)

		except ValueError as errorMessage:
			tkinter.messagebox.showerror("Input values error", errorMessage)
