import customtkinter as ctk
from PIL import Image

class SimBoatApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Boat Collecting Oil")
        self.geometry("700x500")
        ctk.set_appearance_mode("light")
        self.minsize(700, 500)
        self.maxsize(700, 500)

        # Main container
        self.mainframe = ctk.CTkFrame(self, fg_color="black", corner_radius=0)
        self.mainframe.pack(fill="both", expand=True)
        self.mainframe.pack_propagate(False)

        # Content holder
        self.mainframe_holder = ctk.CTkFrame(self.mainframe, fg_color="white", width=700, height=500)
        self.mainframe_holder.pack(padx=10, pady=10, fill="both", expand=True)
        self.mainframe_holder.pack_propagate(False)
        
        # Boat cam image
        cam_image = Image.open("boat cam.png")
        cam_image = cam_image.resize((380, 300), Image.Resampling.LANCZOS)
        ctk_image = ctk.CTkImage(light_image=cam_image, size=(380, 300))
        
        self.cam_image_label = ctk.CTkLabel(self.mainframe_holder, image=ctk_image, text="")
        self.cam_image_label.pack(pady=10, padx=20)

        # Battery canvas
        self.canvas = ctk.CTkCanvas(self.mainframe_holder, width=300, height=100, highlightthickness=0)
        self.canvas.place(relx=0.05, rely=0.81)
        self.canvas_bg = self.canvas.create_rectangle(0, 0, 300, 100, fill="white", width=0)

        self.battery_warning_label = ctk.CTkLabel(self.mainframe_holder, text="", font=ctk.CTkFont(size=20, weight="bold"))
        self.battery_warning_label.place(relx=0.05, rely=0.75)
        self.flash_job = None

        self.canvas.create_rectangle(20, 30, 260, 80, outline="black", width=3) # Battery outline
        self.canvas.create_rectangle(260, 40, 270, 70, fill="black") # Battery tip
        self.canvas.create_rectangle(22, 32, 258, 78, fill="white", width=0) # Battery background
        
        self.fill = self.canvas.create_rectangle(22, 32, 22, 78, fill="green", width=0) # Battery fill
        self.battery_text = self.canvas.create_text(145, 55, text="0%", font=("Arial", 16, "bold"))

        self.charge = 1.0
        self.update_battery()

        # Buttons
        self.plusbutton = ctk.CTkButton(self.mainframe_holder, text="Charge +10%", command=self.charge_battery)
        self.plusbutton.place(relx=0.12, rely=0.67)

        self.minusbutton = ctk.CTkButton(self.mainframe_holder, text="Discharge -10%", command=self.discharge_battery)
        self.minusbutton.place(relx=0.12, rely=0.74)

        # Oil Level
        self.oil_label = ctk.CTkLabel(self.mainframe_holder, text="Oil: 80%", font=ctk.CTkFont(size=20, weight="bold"))
        self.oil_label.place(relx=0.6, rely=0.8)

        self.oil_progress = ctk.CTkProgressBar(self.mainframe_holder, height=20)
        self.oil_progress.place(relx=0.5, rely=0.9, relwidth=0.4)
        self.oil_progress.set(0)

        self.oil_slider = ctk.CTkSlider(self.mainframe_holder, from_=0, to=1, command=self.update_oil)
        self.oil_slider.place(relx=0.5, rely=0.85, relwidth=0.4)
        self.oil_slider.set(0)

        # Optional reset screen button
        self.reset_button = ctk.CTkButton(self.mainframe_holder, text="Reset Screen", command=self.reset_screen)
        self.reset_button.place(relx=0.8, rely=0.05)

        # Run initial alerts
        self.oil_alert()
        self.battery_alert()

    def flash_alert(self, widget, times=6):
        """Flashes the background of a widget to draw attention, then restores normal."""
        original_color = widget.cget("fg_color")

        def do_flash(count):
            if count > 0:
                new_color = "red" if count % 2 == 0 else original_color
                widget.configure(fg_color=new_color)
                self.after(300, do_flash, count - 1)
            else:
                widget.configure(fg_color="white")  # Always restore to white

        do_flash(times)

    def oil_alert(self):
        oil_level = self.oil_progress.get()
        if oil_level >= 0.99:  # Full
            self.oil_label.configure(text="OIL: FULL!", text_color="green")
            self.flash_alert(self.mainframe_holder)
            self.show_popup("✅ Oil tank is full!")
        else:
            self.oil_label.configure(text=f"Oil: {int(oil_level * 100)}%", text_color="black")
    
    def flash_canvas_alert(self, color="red", times=6):
        """Flashes the background of the canvas."""
        def do_flash(count):
            if count > 0:
                new_color = color if count % 2 == 0 else "white"
                self.canvas.itemconfig(self.canvas_bg, fill=new_color)
                self.after(300, do_flash, count - 1)
            else:
                self.canvas.itemconfig(self.canvas_bg, fill="white")
        do_flash(times)

    def flash_label_alert(self, label, times=6):
        """Flashes the text color of a label."""
        def do_flash(count):
            if count > 0:
                new_color = "red" if count % 2 == 0 else "white"
                label.configure(text_color=new_color)
                self.flash_job = self.after(300, do_flash, count - 1)
            else:
                label.configure(text="")

        do_flash(times)

    def battery_alert(self):
        if self.charge < 0.2:
            self.canvas.itemconfig(self.battery_text, text="LOW!", fill="red")
            self.flash_canvas_alert()
            self.battery_warning_label.configure(text="WARNING!")
            self.flash_label_alert(self.battery_warning_label)
            self.show_popup("⚠️ Warning: Battery critically low!")
        else:
            self.canvas.itemconfig(self.battery_text, text=f"{int(self.charge*100)}%", fill="black")
            if self.flash_job:
                self.after_cancel(self.flash_job)
                self.flash_job = None
            self.battery_warning_label.configure(text="")

    def show_popup(self, message):
        """Show a small popup warning window."""
        popup = ctk.CTkToplevel(self)
        popup.title("ALERT")
        popup.geometry("300x100")
        popup.attributes("-topmost", True)
        popup.grab_set()

        label = ctk.CTkLabel(popup, text=message, text_color="red", font=ctk.CTkFont(size=16, weight="bold"))
        label.pack(pady=10)

        ok_button = ctk.CTkButton(popup, text="OK", command=popup.destroy)
        ok_button.pack(pady=5)

    def update_oil(self, value):
        self.oil_progress.set(value)
        self.oil_alert()

    def charge_battery(self):
        self.charge = min(1.0, self.charge + 0.1)
        self.update_battery()

    def discharge_battery(self):
        self.charge = max(0.0, self.charge - 0.1)
        self.update_battery()

    def update_battery(self):
        max_width = 258
        min_width = 22
        current_width = min_width + (max_width - min_width) * self.charge
        self.canvas.coords(self.fill, 22, 32, current_width, 78)

        color = "red" if self.charge < 0.3 else "yellow" if self.charge < 0.7 else "green"
        self.canvas.itemconfig(self.fill, fill=color)
        self.battery_alert()

    def reset_screen(self):
        """Restore screen to default state manually."""
        self.charge = 1.0
        self.oil_slider.set(0)
        self.update_battery()
        self.update_oil(0)
        self.mainframe_holder.configure(fg_color="white")
        self.canvas.itemconfig(self.canvas_bg, fill="white")

if __name__ == "__main__":
    app = SimBoatApp()
    app.mainloop()
