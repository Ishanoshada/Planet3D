# Planet3D: Solar System Visualization

## Introduction

Planet3D is a Python library that provides a simple yet powerful framework for visualizing a solar system in a 3D space. It utilizes the Pygame and OpenGL libraries to render planets, moons, and their orbits, allowing users to explore the celestial bodies of our solar system in an interactive 3D environment.

## Features

- **Realistic Rendering:** Planet3D employs OpenGL to create realistic 3D representations of planets and moons, complete with orbital paths.

- **Interactive Exploration:** Users can navigate through the solar system using keyboard controls, adjusting the viewpoint to observe planets and their orbits from different angles.

- **Configurability:** Easily customize the solar system by adding planets, moons, rings, and adjusting their properties such as size, orbit radius, rotation speed, and colors.

- **Fullscreen Mode:** Toggle between fullscreen and windowed modes for an immersive experience.

## Installation

Planet3D can be installed using the following command:

```bash
pip install Planet3D
```

## Getting Started

### Importing Planet3D

```python
from Planet3D import Planet, generate_solar_system
```

### Creating Planets

```python
# Create planets with specified properties
earth = Planet(name="Earth", radius=0.6, orbit_radius=12.0, rotation_speed=0.9, color=(0.0, 0.5, 1.0))
mars = Planet(name="Mars", radius=0.4, orbit_radius=18.0, rotation_speed=0.8, color=(1.0, 0.0, 0.0))
```

### Adding Moons

```python
# Add moons to a planet
earth.add_moon(name="Moon", radius=0.3, orbit_radius=3.0, rotation_speed=1.0, color=(0.8, 0.8, 0.8))
```

### Configuring Rings

```python
# Add rings to a planet
saturn.add_ring(radius=5.0, width=0.2, color=(0.8, 0.8, 0.8), transparency=0.3)
```

### Generating the Solar System

```python
# Generate and display the solar system
planets = [earth, mars]
generate_solar_system(planets)
```

To use Planet3D, create instances of the `Planet` class for each celestial body you want to include in the solar system. Customize properties such as radius, orbit radius, rotation speed, and color. Add rings or moons if desired. Finally, use the `generate_solar_system` function to display the solar system.

Here is a basic example:

```python
from Planet3D import Planet, generate_solar_system

if __name__ == "__main__":
    # Create instances of planets
    sun = Planet(name="Sun", radius=5.0, orbit_radius=0.0, rotation_speed=0.0, color=(1.0, 0.8, 0.0))
    mercury = Planet(name="Mercury", radius=0.2, orbit_radius=5.0, rotation_speed=5.0, color=(0.7, 0.7, 0.7))
    venus = Planet(name="Venus", radius=0.5, orbit_radius=8.0, rotation_speed=3.0, color=(0.9, 0.7, 0.0))
    # ... (create other planets)

    # Customize Saturn with rings
    saturn_rings_color = (0.8, 0.8, 0.8)
    saturn.add_ring(radius=5.0, width=0.2, color=saturn_rings_color, transparency=0.3)

    # Add Moon to Earth
    earth.add_moon(name="Moon", radius=0.3, orbit_radius=3.0, rotation_speed=1.0, color=(0.8, 0.8, 0.8))

    # List of planets in our solar system
    planets = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

    # To run in fullscreen mode, set fullscreen=True
    generate_solar_system(planets, display=(1200, 800), fullscreen=False)
```

This example demonstrates how to create a solar system with various planets and customization options.

![ex](https://github.com/Ishanoshada/Ishanoshada/blob/main/ss/ple.png?raw=true)

## Controls

- **Left/Right Arrow:** Move left/right
- **Up/Down Arrow:** Move up/down
- **W/S:** Move forward/backward
- **Z/X:** Move up/down faster

## Fullscreen Mode

To run the visualization in fullscreen mode, simply pass `fullscreen=True` to the `generate_solar_system` function:

```python
generate_solar_system(planets, fullscreen=True)
```

## Acknowledgements

Planet3D utilizes the Pygame and OpenGL libraries to create an interactive 3D solar system visualization.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, please contact [ishan.kodithuwakku@gmail.com].

Explore the wonders of our solar system with Planet3D!
