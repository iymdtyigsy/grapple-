import customtkinter as ctk
from tkintermapview import TkinterMapView

class RoadBumpApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window setup
        self.title("Road Bump Counter with Map")
        self.geometry("600x500")
        ctk.set_appearance_mode("light")

        # Counter variable
        self.count = 0

        # Title
        self.label = ctk.CTkLabel(self, text=f"Cars Passed: {self.count}", font=("Arial", 20))
        self.label.pack(pady=10)

        # Buttons
        self.btn_count = ctk.CTkButton(self, text="Car Passed", command=self.increment)
        self.btn_count.pack(pady=5)

        self.btn_reset = ctk.CTkButton(self, text="Reset", command=self.reset)
        self.btn_reset.pack(pady=5)

        # Map Widget
        self.map_widget = TkinterMapView(self, width=500, height=300, corner_radius=10)
        self.map_widget.pack(pady=10)

        # Default map location (change to your city)
        lat, lon = -43.5309, 172.6390
        self.map_widget.set_position(lat, lon)
        self.map_widget.set_zoom(15)

        # Create initial marker
        self.marker = self.map_widget.set_marker(lat, lon, text=f"Cars Passed: {self.count}")

    def increment(self):
        self.count += 1
        self.update_display()

    def reset(self):
        self.count = 0
        self.update_display()

    def update_display(self):
        # Update both label and marker text
        self.label.configure(text=f"Cars Passed: {self.count}")
        self.marker.set_text(f"Cars Passed: {self.count}")

if __name__ == "__main__":
    app = RoadBumpApp()
    app.mainloop()
