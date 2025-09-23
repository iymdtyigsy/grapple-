import customtkinter as ctk

class RoadBumpApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window settings
        self.title("Road Bump Counter")
        self.geometry("400x300")
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        # Counter variable
        self.count = 0

        # Header Label
        self.header = ctk.CTkLabel(self, text="Road Bump Counter", font=("Arial", 24))
        self.header.pack(pady=20)

        # Counter Display
        self.label = ctk.CTkLabel(self, text=f"Cars Passed: {self.count}", font=("Arial", 20))
        self.label.pack(pady=10)

        # Increment Button
        self.btn_count = ctk.CTkButton(self, text="Car Passed", command=self.increment)
        self.btn_count.pack(pady=10)

        # Reset Button
        self.btn_reset = ctk.CTkButton(self, text="Reset", command=self.reset)
        self.btn_reset.pack(pady=10)

    # Increment counter
    def increment(self):
        self.count += 1
        self.label.configure(text=f"Cars Passed: {self.count}")

    # Reset counter
    def reset(self):
        self.count = 0
        self.label.configure(text=f"Cars Passed: {self.count}")

if __name__ == "__main__":
    app = RoadBumpApp()
    app.mainloop()
