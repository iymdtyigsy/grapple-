import customtkinter as ctk
from tkintermapview import TkinterMapView

class RoadBumpApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Road Bump Counter with Map")
        self.geometry("600x500")
        ctk.set_appearance_mode("light")

        # Counter
        self.count = 0
        self.label = ctk.CTkLabel(self, text=f"Cars Passed: {self.count}", font=("Arial", 20))
        self.label.pack(pady=10)

        self.btn_count = ctk.CTkButton(self, text="Car Passed", command=self.increment)
        self.btn_count.pack(pady=5)

        self.btn_reset = ctk.CTkButton(self, text="Reset", command=self.reset)
        self.btn_reset.pack(pady=5)

        # Map Widget
        self.map_widget = TkinterMapView(self, width=500, height=300, corner_radius=10)
        self.map_widget.pack(pady=10)

        # Set Default Location (e.g., New York)
        self.map_widget.set_position(40.7128, -74.0060)  # Latitude, Longitude
        self.map_widget.set_zoom(13)

        # Add Marker Example
        self.marker = self.map_widget.set_marker(40.7128, -74.0060, text="Speed Bump Location")

    def increment(self):
        self.count += 1
        self.label.configure(text=f"Cars Passed: {self.count}")

    def reset(self):
        self.count = 0
        self.label.configure(text=f"Cars Passed: {self.count}")

if __name__ == "__main__":
    app = RoadBumpApp()
    app.mainloop()
