# dune-galactic-visualizer

🌌 Dune Universe Visualization

When reading the book, it’s very difficult to understand the network of planetary connections because of the sheer amount of information.

Interactive Plotly Map of Planets & Connections

This project visualizes the planets of the Dune universe and their interplanetary connections using Python and Plotly.
It loads a JSON model (data.json) that contains planets, coordinates, colors, sizes, and connection distances, and renders an interactive galactic map with hover tooltips and dynamic styling.

The map includes:

🪐 Planets — positioned on a 2D galactic grid

🔗 Connections — lines between planets with distances

✨ Dynamic rendering — planet sizes, colors, hover data

⭐ Starfield background — optional aesthetic enhancement

🌙 Dark theme — clean, modern space-style visuals

🚀 Features
🪐 Planet Visualization

Each planet has:

Name

Description (shown on hover)

X/Y coordinates

Color (visual category)

Size (relative visual importance)

🔗 Interplanetary Routes

Every connection shows:

Visual line between planets

Hover tooltip with distance

Smooth, semi-transparent styling

🖥 Interactive Map

Zoom & pan

Hover tooltips

Clean dark-space theme

Automatically scaled labels

Creates a deeper, immersive galactic effect.


🛠 Requirements

Install Python dependencies:

'''pip install plotly'''


▶️ Usage

Place data.json in the project directory.

Run the visualizer:

python duinaviz.py
