# GUI frame for the harmonicModel_function.py

import tkinter as tk
import tkinter.filedialog, tkinter.messagebox
import sys, os
from scipy.io.wavfile import read
import harmonicModel_function
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../models/'))
import utilFunctions as UF

class HarmonicModel_frame:

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
		self.filelocation.insert(0, '../../sounds/vignesh.wav')

		#BUTTON TO BROWSE SOUND FILE
		self.open_file = tk.Button(self.parent, text="Browse...", command=self.browse_file) #see: def browse_file(self)
		self.open_file.grid(row=1, column=0, sticky=tk.W, padx=(220, 6)) #put it beside the filelocation textbox

		#BUTTON TO PREVIEW SOUND FILE
		self.preview = tk.Button(self.parent, text=">", command=lambda:UF.wavplay(self.filelocation.get()), bg="gray30", fg="white")
		self.preview.grid(row=1, column=0, sticky=tk.W, padx=(306,6))

		## HARMONIC MODEL

		#ANALYSIS WINDOW TYPE
		wtype_label = "Window type:"
		tk.Label(self.parent, text=wtype_label).grid(row=2, column=0, sticky=tk.W, padx=5, pady=(10,2))
		self.w_type = tk.StringVar()
		self.w_type.set("blackman") # initial value
		window_option = tk.OptionMenu(self.parent, self.w_type, "rectangular", "hanning", "hamming", "blackman", "blackmanharris")
		window_option.grid(row=2, column=0, sticky=tk.W, padx=(95,5), pady=(10,2))

		#WINDOW SIZE
		M_label = "Window size (M):"
		tk.Label(self.parent, text=M_label).grid(row=3, column=0, sticky=tk.W, padx=5, pady=(10,2))
		self.M = tk.Entry(self.parent, justify=tk.CENTER)
		self.M["width"] = 5
		self.M.grid(row=3,column=0, sticky=tk.W, padx=(115,5), pady=(10,2))
		self.M.delete(0, tk.END)
		self.M.insert(0, "1201")

		#FFT SIZE
		N_label = "FFT size (N) (power of two bigger than M):"
		tk.Label(self.parent, text=N_label).grid(row=4, column=0, sticky=tk.W, padx=5, pady=(10,2))
		self.N = tk.Entry(self.parent, justify=tk.CENTER)
		self.N["width"] = 5
		self.N.grid(row=4,column=0, sticky=tk.W, padx=(270,5), pady=(10,2))
		self.N.delete(0, tk.END)
		self.N.insert(0, "2048")

		#THRESHOLD MAGNITUDE
		t_label =  "Magnitude threshold (t) (in dB):"
		tk.Label(self.parent, text=t_label).grid(row=5, column=0, sticky=tk.W, padx=5, pady=(10,2))
		self.t = tk.Entry(self.parent, justify=tk.CENTER)
		self.t["width"] = 5
		self.t.grid(row=5, column=0, sticky=tk.W, padx=(205,5), pady=(10,2))
		self.t.delete(0, tk.END)
		self.t.insert(0, "-90")

		#MIN DURATION SINUSOIDAL TRACKS
		minSineDur_label = "Minimum duration of harmonic tracks:"
		tk.Label(self.parent, text=minSineDur_label).grid(row=6, column=0, sticky=tk.W, padx=5, pady=(10,2))
		self.minSineDur = tk.Entry(self.parent, justify=tk.CENTER)
		self.minSineDur["width"] = 5
		self.minSineDur.grid(row=6, column=0, sticky=tk.W, padx=(250,5), pady=(10,2))
		self.minSineDur.delete(0, tk.END)
		self.minSineDur.insert(0, "0.1")

		#MAX NUMBER OF HARMONICS
		nH_label = "Maximum number of harmonics:"
		tk.Label(self.parent, text=nH_label).grid(row=7, column=0, sticky=tk.W, padx=5, pady=(10,2))
		self.nH = tk.Entry(self.parent, justify=tk.CENTER)
		self.nH["width"] = 5
		self.nH.grid(row=7, column=0, sticky=tk.W, padx=(210,5), pady=(10,2))
		self.nH.delete(0, tk.END)
		self.nH.insert(0, "100")

		#MIN FUNDAMENTAL FREQUENCY
		minf0_label = "Minimum fundamental frequency:"
		tk.Label(self.parent, text=minf0_label).grid(row=8, column=0, sticky=tk.W, padx=5, pady=(10,2))
		self.minf0 = tk.Entry(self.parent, justify=tk.CENTER)
		self.minf0["width"] = 5
		self.minf0.grid(row=8, column=0, sticky=tk.W, padx=(220,5), pady=(10,2))
		self.minf0.delete(0, tk.END)
		self.minf0.insert(0, "130")

		#MAX FUNDAMENTAL FREQUENCY
		maxf0_label = "Maximum fundamental frequency:"
		tk.Label(self.parent, text=maxf0_label).grid(row=9, column=0, sticky=tk.W, padx=5, pady=(10,2))
		self.maxf0 = tk.Entry(self.parent, justify=tk.CENTER)
		self.maxf0["width"] = 5
		self.maxf0.grid(row=9, column=0, sticky=tk.W, padx=(220,5), pady=(10,2))
		self.maxf0.delete(0, tk.END)
		self.maxf0.insert(0, "300")

		#MAX ERROR ACCEPTED
		f0et_label = "Maximum error in f0 detection algorithm:"
		tk.Label(self.parent, text=f0et_label).grid(row=10, column=0, sticky=tk.W, padx=5, pady=(10,2))
		self.f0et = tk.Entry(self.parent, justify=tk.CENTER)
		self.f0et["width"] = 5
		self.f0et.grid(row=10, column=0, sticky=tk.W, padx=(265,5), pady=(10,2))
		self.f0et.delete(0, tk.END)
		self.f0et.insert(0, "7")

		#ALLOWED DEVIATION OF HARMONIC TRACKS
		harmDevSlope_label = "Max frequency deviation in harmonic tracks:"
		tk.Label(self.parent, text=harmDevSlope_label).grid(row=11, column=0, sticky=tk.W, padx=5, pady=(10,2))
		self.harmDevSlope = tk.Entry(self.parent, justify=tk.CENTER)
		self.harmDevSlope["width"] = 5
		self.harmDevSlope.grid(row=11, column=0, sticky=tk.W, padx=(285,5), pady=(10,2))
		self.harmDevSlope.delete(0, tk.END)
		self.harmDevSlope.insert(0, "0.01")

		#BUTTON TO COMPUTE EVERYTHING
		self.compute = tk.Button(self.parent, text="Compute", command=self.compute_model, bg="dark red", fg="white")
		self.compute.grid(row=12, column=0, padx=5, pady=(10,2), sticky=tk.W)

		#BUTTON TO PLAY OUTPUT
		output_label = "Output:"
		tk.Label(self.parent, text=output_label).grid(row=13, column=0, sticky=tk.W, padx=5, pady=(10,15))
		self.output = tk.Button(self.parent, text=">", command=lambda:UF.wavplay('output_sounds/' + os.path.basename(self.filelocation.get())[:-4] + '_harmonicModel.wav'), bg="gray30", fg="white")
		self.output.grid(row=13, column=0, padx=(60,5), pady=(10,15), sticky=tk.W)

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
			window = self.w_type.get()
			M = int(self.M.get())
			N = int(self.N.get())
			t = int(self.t.get())
			minSineDur = float(self.minSineDur.get())
			nH = int(self.nH.get())
			minf0 = int(self.minf0.get())
			maxf0 = int(self.maxf0.get())
			f0et = int(self.f0et.get())
			harmDevSlope = float(self.harmDevSlope.get())

			harmonicModel_function.main(inputFile, window, M, N, t, minSineDur, nH, minf0, maxf0, f0et, harmDevSlope)

		except ValueError as errorMessage:
			tkinter.messagebox.showerror("Input values error", errorMessage)
