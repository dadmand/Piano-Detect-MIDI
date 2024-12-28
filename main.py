import mido
from mido import Message
import time
import tkinter as tk
from tkinter import ttk
import threading

# Mapping MIDI note numbers to note names  
midi_notes = {  
    0: 'C-1', 1: 'C#-1/Db-1', 2: 'D-1', 3: 'D#-1/Eb-1', 4: 'E-1', 5: 'F-1', 6: 'F#-1/Gb-1', 7: 'G-1',  
    8: 'G#-1/Ab-1', 9: 'A-1', 10: 'A#-1/Bb-1', 11: 'B-1',  
    12: 'C0', 13: 'C#0/Db0', 14: 'D0', 15: 'D#0/Eb0', 16: 'E0', 17: 'F0', 18: 'F#0/Gb0', 19: 'G0',  
    20: 'G#0/Ab0', 21: 'A0', 22: 'A#0/Bb0', 23: 'B0',  
    24: 'C1', 25: 'C#1/Db1', 26: 'D1', 27: 'D#1/Eb1', 28: 'E1', 29: 'F1', 30: 'F#1/Gb1', 31: 'G1',  
    32: 'G#1/Ab1', 33: 'A1', 34: 'A#1/Bb1', 35: 'B1',  
    36: 'C2', 37: 'C#2/Db2', 38: 'D2', 39: 'D#2/Eb2', 40: 'E2', 41: 'F2', 42: 'F#2/Gb2', 43: 'G2',  
    44: 'G#2/Ab2', 45: 'A2', 46: 'A#2/Bb2', 47: 'B2',  
    48: 'C3', 49: 'C#3/Db3', 50: 'D3', 51: 'D#3/Eb3', 52: 'E3', 53: 'F3', 54: 'F#3/Gb3', 55: 'G3',  
    56: 'G#3/Ab3', 57: 'A3', 58: 'A#3/Bb3', 59: 'B3',  
    60: 'C4', 61: 'C#4/Db4', 62: 'D4', 63: 'D#4/Eb4', 64: 'E4', 65: 'F4', 66: 'F#4/Gb4', 67: 'G4',  
    68: 'G#4/Ab4', 69: 'A4', 70: 'A#4/Bb4', 71: 'B4',  
    72: 'C5', 73: 'C#5/Db5', 74: 'D5', 75: 'D#5/Eb5', 76: 'E5', 77: 'F5', 78: 'F#5/Gb5', 79: 'G5',  
    80: 'G#5/Ab5', 81: 'A5', 82: 'A#5/Bb5', 83: 'B5',  
    84: 'C6', 85: 'C#6/Db6', 86: 'D6', 87: 'D#6/Eb6', 88: 'E6', 89: 'F6', 90: 'F#6/Gb6', 91: 'G6',  
    92: 'G#6/Ab6', 93: 'A6', 94: 'A#6/Bb6', 95: 'B6',  
    96: 'C7', 97: 'C#7/Db7', 98: 'D7', 99: 'D#7/Eb7', 100: 'E7', 101: 'F7', 102: 'F#7/Gb7', 103: 'G7',  
    104: 'G#7/Ab7', 105: 'A7', 106: 'A#7/Bb7', 107: 'B7',  
    108: 'C8', 109: 'C#8/Db8', 110: 'D8', 111: 'D#8/Eb8', 112: 'E8', 113: 'F8', 114: 'F#8/Gb8', 115: 'G8',  
    116: 'G#8/Ab8', 117: 'A8', 118: 'A#8/Bb8', 119: 'B8',  
    120: 'C9', 121: 'C#9/Db9', 122: 'D9', 123: 'D#9/Eb9', 124: 'E9', 125: 'F9', 126: 'F#9/Gb9', 127: 'G9'  
}  

# Mapping MIDI note numbers to Persian note names
midi_notes = {
    0: 'Do-1', 1: 'Do#-1/Reb-1', 2: 'Re-1', 3: 'Re#-1/Mib-1', 4: 'Mi-1', 5: 'Fa-1', 6: 'Fa#-1/Sob-1', 7: 'Sol-1',
    8: 'Sol#-1/Lab-1', 9: 'La-1', 10: 'La#-1/Sib-1', 11: 'Si-1',
    12: 'Do0', 13: 'Do#0/Reb0', 14: 'Re0', 15: 'Re#0/Mib0', 16: 'Mi0', 17: 'Fa0', 18: 'Fa#0/Sob0', 19: 'Sol0',
    20: 'Sol#0/Lab0', 21: 'La0', 22: 'La#0/Sib0', 23: 'Si0',
    24: 'Do1', 25: 'Do#1/Reb1', 26: 'Re1', 27: 'Re#1/Mib1', 28: 'Mi1', 29: 'Fa1', 30: 'Fa#1/Sob1', 31: 'Sol1',
    32: 'Sol#1/Lab1', 33: 'La1', 34: 'La#1/Sib1', 35: 'Si1',
    36: 'Do2', 37: 'Do#2/Reb2', 38: 'Re2', 39: 'Re#2/Mib2', 40: 'Mi2', 41: 'Fa2', 42: 'Fa#2/Sob2', 43: 'Sol2',
    44: 'Sol#2/Lab2', 45: 'La2', 46: 'La#2/Sib2', 47: 'Si2',
    48: 'Do3', 49: 'Do#3/Reb3', 50: 'Re3', 51: 'Re#3/Mib3', 52: 'Mi3', 53: 'Fa3', 54: 'Fa#3/Sob3', 55: 'Sol3',
    56: 'Sol#3/Lab3', 57: 'La3', 58: 'La#3/Sib3', 59: 'Si3',
    60: 'Do4', 61: 'Do#4/Reb4', 62: 'Re4', 63: 'Re#4/Mib4', 64: 'Mi4', 65: 'Fa4', 66: 'Fa#4/Sob4', 67: 'Sol4',
    68: 'Sol#4/Lab4', 69: 'La4', 70: 'La#4/Sib4', 71: 'Si4',
    72: 'Do5', 73: 'Do#5/Reb5', 74: 'Re5', 75: 'Re#5/Mib5', 76: 'Mi5', 77: 'Fa5', 78: 'Fa#5/Sob5', 79: 'Sol5',
    80: 'Sol#5/Lab5', 81: 'La5', 82: 'La#5/Sib5', 83: 'Si5',
    84: 'Do6', 85: 'Do#6/Reb6', 86: 'Re6', 87: 'Re#6/Mib6', 88: 'Mi6', 89: 'Fa6', 90: 'Fa#6/Sob6', 91: 'Sol6',
    92: 'Sol#6/Lab6', 93: 'La6', 94: 'La#6/Sib6', 95: 'Si6',
    96: 'Do7', 97: 'Do#7/Reb7', 98: 'Re7', 99: 'Re#7/Mib7', 100: 'Mi7', 101: 'Fa7', 102: 'Fa#7/Sob7', 103: 'Sol7',
    104: 'Sol#7/Lab7', 105: 'La7', 106: 'La#7/Sib7', 107: 'Si7',
    108: 'Do8', 109: 'Do#8/Reb8', 110: 'Re8', 111: 'Re#8/Mib8', 112: 'Mi8', 113: 'Fa8', 114: 'Fa#8/Sob8', 115: 'Sol8',
    116: 'Sol#8/Lab8', 117: 'La8', 118: 'La#8/Sib8', 119: 'Si8',
    120: 'Do9', 121: 'Do#9/Reb9', 122: 'Re9', 123: 'Re#9/Mib9', 124: 'Mi9', 125: 'Fa9', 126: 'Fa#9/Sob9', 127: 'Sol9'
}

# Smaller ASCII piano representation
PIANO_ASCII = {
    'white_up':    '-',
    'white_down':  '▀',
    'black_up':    '|',
    'black_down':  '█',
    'empty':       ' '
}

# Piano key layout (0 = white key, 1 = black key)
KEY_LAYOUT = [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0]  # C to B

# Piano range (88 keys: from A0 to C8)
FIRST_KEY = 21  # A0
LAST_KEY = 108  # C8

class PianoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("MIDI Piano Visualizer")
        self.active_notes = set()
        
        # Configure main window
        self.root.geometry("1200x400")
        self.root.configure(bg='#f0f0f0')
        
        # Create main frame
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Create piano canvas
        self.canvas = tk.Canvas(self.main_frame, width=1160, height=200, bg='white')
        self.canvas.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Create status frame
        self.status_frame = ttk.LabelFrame(self.main_frame, text="Status", padding="5")
        self.status_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        # Status label
        self.status_label = ttk.Label(self.status_frame, text="Waiting for MIDI input...")
        self.status_label.grid(row=0, column=0, padx=5)
        
        # Active notes display
        self.notes_label = ttk.Label(self.status_frame, text="Active Notes: ")
        self.notes_label.grid(row=1, column=0, padx=5)
        
        # Create piano keys
        self.create_piano_keys()
        
        # Start MIDI listening thread
        self.running = True
        self.midi_thread = threading.Thread(target=self.midi_listener)
        self.midi_thread.daemon = True
        self.midi_thread.start()

    def create_piano_keys(self):
        # Constants for piano key dimensions
        white_key_width = 20
        white_key_height = 120
        black_key_width = 14
        black_key_height = 80
        
        # Create white keys
        self.white_keys = {}
        self.black_keys = {}
        x = 10
        
        for note in range(FIRST_KEY, LAST_KEY + 1):
            if not is_black_key(note):
                key = self.canvas.create_rectangle(
                    x, 10,
                    x + white_key_width, 10 + white_key_height,
                    fill='white', outline='black'
                )
                self.white_keys[note] = key
                x += white_key_width
        
        # Create black keys
        x = 10
        for note in range(FIRST_KEY, LAST_KEY + 1):
            if is_black_key(note):
                key = self.canvas.create_rectangle(
                    x + white_key_width - black_key_width//2, 10,
                    x + white_key_width + black_key_width//2, 10 + black_key_height,
                    fill='black'
                )
                self.black_keys[note] = key
            if not is_black_key(note):
                x += white_key_width

    def note_on(self, note):
        if note in self.white_keys:
            self.canvas.itemconfig(self.white_keys[note], fill='#add8e6')  # Light blue
        elif note in self.black_keys:
            self.canvas.itemconfig(self.black_keys[note], fill='#4169e1')  # Royal blue
        self.active_notes.add(note)
        self.update_active_notes()

    def note_off(self, note):
        if note in self.white_keys:
            self.canvas.itemconfig(self.white_keys[note], fill='white')
        elif note in self.black_keys:
            self.canvas.itemconfig(self.black_keys[note], fill='black')
        self.active_notes.discard(note)
        self.update_active_notes()

    def update_active_notes(self):
        active_note_names = [midi_notes[note] for note in sorted(self.active_notes)]
        self.notes_label.config(text=f"Active Notes: {', '.join(active_note_names)}")

    def midi_listener(self):
        try:
            with mido.open_input() as midi_input:
                self.status_label.config(text="Connected to MIDI device")
                while self.running:
                    for message in midi_input.iter_pending():
                        if message.type == 'note_on' and message.velocity > 0:
                            self.root.after(0, self.note_on, message.note)
                        elif message.type == 'note_off' or (message.type == 'note_on' and message.velocity == 0):
                            self.root.after(0, self.note_off, message.note)
                    time.sleep(0.001)
        except Exception as e:
            self.status_label.config(text=f"Error: {str(e)}")

    def on_closing(self):
        self.running = False
        self.root.destroy()

def is_black_key(note):
    """Determine if a note is a black key"""
    return note % 12 in [1, 3, 6, 8, 10]

def main():
    root = tk.Tk()
    app = PianoGUI(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()

if __name__ == "__main__":
    main()
