import customtkinter as ctk

class BatteryApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Battery Progress Bar")
        self.geometry("400x200")
        ctk.set_appearance_mode("light")

        # Canvas for custom battery shape
        self.canvas = ctk.CTkCanvas(self, width=300, height=100, bg="white", highlightthickness=0)
        self.canvas.pack(pady=20)

        # Draw battery outline (rect + small terminal)
        self.canvas.create_rectangle(20, 30, 260, 80, outline="black", width=3)  # battery body
        self.canvas.create_rectangle(260, 40, 270, 70, fill="black")  # battery tip

        # Fill (progress) – store ID so we can update later
        self.fill = self.canvas.create_rectangle(22, 32, 22, 78, fill="green", width=0)

        # Button to simulate battery charging
        self.charge = 0.0
        self.button = ctk.CTkButton(self, text="Charge +10%", command=self.charge_battery)
        self.button.pack()

    def charge_battery(self):
        if self.charge < 1.0:
            self.charge += 0.1
            self.update_battery()

    def update_battery(self):
        # Map 0-1 to battery width (22 to 258)
        max_width = 258
        min_width = 22
        current_width = min_width + (max_width - min_width) * self.charge

        # Update fill rectangle
        self.canvas.coords(self.fill, 22, 32, current_width, 78)

        # Change color based on level
        color = "red" if self.charge < 0.3 else "yellow" if self.charge < 0.7 else "green"
        self.canvas.itemconfig(self.fill, fill=color)

if __name__ == "__main__":
    app = BatteryApp()
    app.mainloop()
