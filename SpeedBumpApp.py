import customtkinter as ctk

class RoadBumpApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Road Bump Counter")
        self.geometry("320x568") 
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        self.minsize(320, 568)
        self.maxsize(320, 568)  
        
        self.mainframe = ctk.CTkFrame(
            self,
            fg_color="black",
            corner_radius=0
        )
        self.mainframe.pack(fill="both", expand=True)
        self.mainframe.pack_propagate(False)

        self.mainframe_holder = ctk.CTkFrame(
            self.mainframe,
            fg_color="#D9D9D9",
            width=320,
            height=568
        )
        self.mainframe_holder.pack(padx=10, pady=10, fill="both", expand=True)
        self.mainframe_holder.pack_propagate(False)

        self.traffic_btn = ctk.CTkButton(
            self.mainframe_holder,
            text="Traffic map",
            font=("Arial", 16),
            height=50,
            command=self.traffic_menu
        )
        self.traffic_btn.pack(pady=20, padx=20, fill="x")

        self.exit_btn = ctk.CTkButton(
            self.mainframe_holder,
            text="exit",
            font=("Arial", 16),
            height=50,
            command=self.destroy
        )
        self.exit_btn.pack(pady=10, padx=20, fill="x")

    def delete_current(self):
        """Clears all widgets from the mainframe_holder."""
        for widget in self.mainframe_holder.winfo_children():
            widget.forget()
    
    def traffic_menu(self):
        self.delete_current()
        self.traffic_label = ctk.CTkLabel(
            self.mainframe_holder,
            text="Traffic map",
            font=("Arial", 20)
        )
        self.traffic_label.pack(pady=20, padx=20)

if __name__ == "__main__":
    app = RoadBumpApp()
    app.mainloop()
