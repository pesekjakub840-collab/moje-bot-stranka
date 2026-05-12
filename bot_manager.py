import customtkinter as ctk
import google.generativeai as genai

# --- ZDE VLOŽ SVŮJ KLÍČ ---
MOJE_API_KLIC = "AIzaSyD8BLC5IR1WQyYtuY0l1gDHclgyztRe4DE"
genai.configure(api_key=MOJE_API_KLIC)
model = genai.GenerativeModel('gemini-1.5-flash')

class RobloxBotApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Roblox Bot Manager v1.0")
        self.geometry("450x600")
        
        # Design menu
        self.label = ctk.CTkLabel(self, text="ROBLOX \u0026 GEMINI BOT", font=("Impact", 24))
        self.label.pack(pady=20)

        self.user_entry = ctk.CTkEntry(self, placeholder_text="Jméno nového účtu", width=250)
        self.user_entry.pack(pady=10)

        self.pass_entry = ctk.CTkEntry(self, placeholder_text="Heslo", show="*", width=250)
        self.pass_entry.pack(pady=10)

        self.game_list = ctk.CTkOptionMenu(self, values=["Brookhaven", "Adopt Me", "BedWars", "Blox Fruits"])
        self.game_list.pack(pady=10)

        self.status_box = ctk.CTkTextbox(self, height=150, width=350)
        self.status_box.pack(pady=20)
        self.status_box.insert("0.0", "Systém připraven...\n")

        self.start_btn = ctk.CTkButton(self, text="SPUSTIT BOTY \u0026 GEMINI", command=self.start_all, fg_color="green")
        self.start_btn.pack(pady=10)

    def start_all(self):
        jmeno = self.user_entry.get()
        hra = self.game_list.get()
        
        self.status_box.insert("end", f"\nRegistruji účet {jmeno}...\n")
        
        # Simulace odpovědi ode mě (Gemini)
        response = model.generate_content(f"Jsem robotický asistent. Právě spouštím pro uživatele hru {hra} v Robloxu. Pozdrav ho krátce.")
        self.status_box.insert("end", f"Gemini: {response.text}\n")

app = RobloxBotApp()
app.mainloop()
