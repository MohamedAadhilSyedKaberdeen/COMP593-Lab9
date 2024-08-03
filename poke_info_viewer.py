"""
Description: 
  Graphical user interface that displays select information about a 
  user-specified Pokémon fetched from the PokeAPI 

Usage:
  python poke_info_viewer.py
"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import requests

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def get_pokemon_info(pokemon):
    """Gets information about a specified Pokémon from the PokeAPI.

    Args:
        pokemon (str): Pokémon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokémon information, if successful. Otherwise None.
    """
    pokemon = str(pokemon).strip().lower()
    if pokemon == '':
        print('Error: No Pokémon name specified.')
        return None

    url = POKE_API_URL + pokemon
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f'Error: {e}')
        return None

def get_info():
    """Button click event handler to fetch and display Pokémon information."""
    name = entry_name.get()
    data = get_pokemon_info(name)
    
    if data:
        # Extract Pokémon types
        types = [t['type']['name'] for t in data['types']]
        type_text = ', '.join(types)
        label_types.config(text=f"Types: {type_text}")

        # Extract height and weight
        height = data['height'] / 10  # Height in meters
        weight = data['weight'] / 10  # Weight in kilograms
        label_height.config(text=f"Height: {height} m")
        label_weight.config(text=f"Weight: {weight} kg")

        # Extract and update stats
        stats = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}
        progress_hp['value'] = stats.get('hp', 0)
        progress_attack['value'] = stats.get('attack', 0)
        progress_defense['value'] = stats.get('defense', 0)
        progress_special_attack['value'] = stats.get('special-attack', 0)
        progress_special_defense['value'] = stats.get('special-defense', 0)
        progress_speed['value'] = stats.get('speed', 0)
    else:
        messagebox.showerror("Error", "Invalid Pokémon name")

# Create the main window
root = Tk()
root.title("Pokémon Information Viewer")

# Create Top Frame for User Input
frame_top = Frame(root)
frame_top.pack(pady=10, fill=X)

label_name = Label(frame_top, text="Pokémon Name")
label_name.grid(row=0, column=0, padx=10, pady=10)
entry_name = Entry(frame_top)
entry_name.grid(row=0, column=1, padx=10, pady=10)

button_get_info = Button(frame_top, text="Get Info", command=get_info)
button_get_info.grid(row=0, column=2, padx=10, pady=10)

# Create Main Frame for Info and Stats
frame_main = Frame(root)
frame_main.pack(pady=10, fill=BOTH, expand=True)

# Create Info Frame
frame_info = Frame(frame_main, borderwidth=2, relief="groove", padx=10, pady=10)
frame_info.grid(row=0, column=0, sticky=N+S+E+W, padx=5, pady=5, columnspan=1)

# Add "Info" Label
label_info_title = Label(frame_info, text="Info", font=('Helvetica', 12, 'bold'))
label_info_title.grid(row=0, column=0, padx=10, pady=10, sticky=W)

# Create and place widgets in Info Frame
label_types = Label(frame_info, text="Types: ")
label_types.grid(row=1, column=0, padx=10, pady=5, sticky=W)

label_height = Label(frame_info, text="Height: ")
label_height.grid(row=2, column=0, padx=10, pady=5, sticky=W)

label_weight = Label(frame_info, text="Weight: ")
label_weight.grid(row=3, column=0, padx=10, pady=5, sticky=W)

# Create Stats Frame
frame_stats = Frame(frame_main, borderwidth=2, relief="groove", padx=10, pady=10)
frame_stats.grid(row=0, column=1, sticky=N+S+E+W, padx=5, pady=5, columnspan=1)

# Add "Stats" Label
label_stats_title = Label(frame_stats, text="Stats", font=('Helvetica', 12, 'bold'))
label_stats_title.grid(row=0, column=0, padx=10, pady=10, sticky=W)

# Create and place widgets in Stats Frame
label_hp = Label(frame_stats, text="HP")
label_hp.grid(row=1, column=0, padx=10, pady=5, sticky=W)
progress_hp = ttk.Progressbar(frame_stats, maximum=255)
progress_hp.grid(row=2, column=0, padx=10, pady=5, sticky=W)

label_attack = Label(frame_stats, text="Attack")
label_attack.grid(row=3, column=0, padx=10, pady=5, sticky=W)
progress_attack = ttk.Progressbar(frame_stats, maximum=255)
progress_attack.grid(row=4, column=0, padx=10, pady=5, sticky=W)

label_defense = Label(frame_stats, text="Defense")
label_defense.grid(row=5, column=0, padx=10, pady=5, sticky=W)
progress_defense = ttk.Progressbar(frame_stats, maximum=255)
progress_defense.grid(row=6, column=0, padx=10, pady=5, sticky=W)

label_special_attack = Label(frame_stats, text="Special Attack")
label_special_attack.grid(row=7, column=0, padx=10, pady=5, sticky=W)
progress_special_attack = ttk.Progressbar(frame_stats, maximum=255)
progress_special_attack.grid(row=8, column=0, padx=10, pady=5, sticky=W)

label_special_defense = Label(frame_stats, text="Special Defense")
label_special_defense.grid(row=9, column=0, padx=10, pady=5, sticky=W)
progress_special_defense = ttk.Progressbar(frame_stats, maximum=255)
progress_special_defense.grid(row=10, column=0, padx=10, pady=5, sticky=W)

label_speed = Label(frame_stats, text="Speed")
label_speed.grid(row=11, column=0, padx=10, pady=5, sticky=W)
progress_speed = ttk.Progressbar(frame_stats, maximum=255)
progress_speed.grid(row=12, column=0, padx=10, pady=5, sticky=W)

# Adjust grid configuration
frame_main.grid_columnconfigure(0, weight=1)
frame_main.grid_columnconfigure(1, weight=2)
frame_main.grid_rowconfigure(0, weight=1)

# Run the application
root.mainloop()
