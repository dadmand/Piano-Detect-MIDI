import mido  

def list_midi_ports():  
    print("Available MIDI Input Ports:")  
    for port in mido.get_input_names():  
        print(port)  

if __name__ == "__main__":  
    list_midi_ports()  