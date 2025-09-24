import customtkinter as ctk
import serial
import threading

class App(ctk.CTk):
    def __init__(self, serial_port):
        super().__init__()
        self.title("Road Bump Counter")
        self.geometry("390x844")  # iPhone 14 Pro dimensions
        ctk.set_appearance_mode("light")
        self.minsize(320, 568)  # Minimum mobile size (iPhone SE)
        self.maxsize(430, 932)  # Maximum mobile size (iPhone 14 Pro Max)
        
        # Make window resizable for different mobile orientations
        self.resizable(True, True)

        self.count = 0
        self.label = ctk.CTkLabel(self, text="Cars Passed: 0", font=("Arial", 20))
        self.label.pack(pady=20)

        self.btn_reset = ctk.CTkButton(self, text="Reset", command=self.reset)
        self.btn_reset.pack(pady=10)

        # Start thread to read from Arduino
        self.serial_port = serial.Serial(serial_port, 9600)
        self.thread = threading.Thread(target=self.read_serial)
        self.thread.daemon = True
        self.thread.start()

    def read_serial(self):
        while True:
            try:
                data = self.serial_port.readline().decode().strip()
                if data.isdigit():
                    self.count = int(data)
                    self.label.configure(text=f"Cars Passed: {self.count}")
            except:
                break

    def reset(self):
        self.count = 0
        self.label.configure(text="Cars Passed: 0")

if __name__ == "__main__":
    # Change COM3 to your Arduino's port (on Mac it might be /dev/ttyUSB0)
    app = App("COM3")
    app.mainloop()
