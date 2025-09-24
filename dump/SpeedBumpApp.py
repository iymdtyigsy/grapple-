import customtkinter as ctk
from PIL import Image

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
            text="Traffic Map",
            font=("Arial", 20)
        )
        self.traffic_label.pack(pady=10, padx=20)
        
        # Load and display the grapple map image
        try:
            # Load the image and resize it to fit mobile screen
            map_image = Image.open("grapple map.png")
            # Resize to fit mobile screen width with aspect ratio maintained
            map_image = map_image.resize((280, 200), Image.Resampling.LANCZOS)
            
            # Convert to CTkImage
            ctk_image = ctk.CTkImage(light_image=map_image, size=(280, 200))
            
            # Create image label
            self.map_image_label = ctk.CTkLabel(
                self.mainframe_holder,
                image=ctk_image,
                text=""
            )
            self.map_image_label.pack(pady=10, padx=20)
            
        except Exception as e:
            # If image loading fails, show error message
            error_label = ctk.CTkLabel(
                self.mainframe_holder,
                text=f"Could not load map image: {str(e)}",
                font=("Arial", 12)
            )
            error_label.pack(pady=10, padx=20)
        
        # Add back button
        self.back_btn = ctk.CTkButton(
            self.mainframe_holder,
            text="Back to Main Menu",
            font=("Arial", 14),
            height=40,
            command=self.main_menu
        )
        self.back_btn.pack(pady=20, padx=20, fill="x")
    
    def main_menu(self):
        """Return to main menu"""
        self.delete_current()
        
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

if __name__ == "__main__":
    app = RoadBumpApp()
    app.mainloop()
