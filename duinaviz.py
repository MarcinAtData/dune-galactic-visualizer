import json
import plotly.graph_objects as go

# Load planet data from JSON
with open("data.json", "r") as f:
    data = json.load(f)

planets = data["planets"]
connections = data["connections"]

# Extract planet details
planet_names = [planet["name"] for planet in planets]
x_coords = [planet["x"] for planet in planets]
y_coords = [planet["y"] for planet in planets]
descriptions = [planet["description"] for planet in planets]
colors = [planet["color"] for planet in planets]
sizes = [planet["size"] for planet in planets]

# ⭐ Optional: Generate background stars
import random
star_x = [random.randint(-2000, 2000) for _ in range(300)]
star_y = [random.randint(-2000, 2000) for _ in range(300)]

stars = go.Scatter(
    x=star_x,
    y=star_y,
    mode="markers",
    marker=dict(size=2, color="white", opacity=0.5),
    hoverinfo="none"
)

# Create planet scatter (dynamic sizes + colors)
planet_scatter = go.Scatter(
    x=x_coords,
    y=y_coords,
    mode="markers+text",
    text=planet_names,
    textposition="top center",
    marker=dict(
        size=[s * 0.7 for s in sizes],
        color=colors,
        line=dict(width=2, color="black")
    ),
    hovertemplate=(
        "<b>%{text}</b><br><br>"
        "<i>%{customdata}</i><br><br>"
        "Coordinates: (%{x}, %{y})<extra></extra>"
    ),
    customdata=descriptions
)

# Add connections as lines
connection_lines = []
for connection in connections:
    start_idx = planet_names.index(connection["from"])
    end_idx = planet_names.index(connection["to"])

    connection_lines.append(
        go.Scatter(
            x=[x_coords[start_idx], x_coords[end_idx]],
            y=[y_coords[start_idx], y_coords[end_idx]],
            mode="lines",
            line=dict(color="rgba(150,150,150,0.5)", width=1),
            hovertemplate=f"Distance: {connection['distance']}<extra></extra>"
        )
    )

# Layout adjustments
layout = go.Layout(
    title="<b>Dune Universe: Planet Connections</b>",
    title_x=0.5,
    xaxis=dict(visible=False),
    yaxis=dict(visible=False),
    showlegend=False,
    plot_bgcolor="black",
    paper_bgcolor="black",
    margin=dict(l=0, r=0, t=50, b=0),
    font=dict(color="white")
)

# Final figure (stars behind everything)
fig = go.Figure(data=[stars] + connection_lines + [planet_scatter], layout=layout)

fig.show()
