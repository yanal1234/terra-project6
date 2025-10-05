# 🌍 Terra – The Thermal Story of Earth

**Terra** is an interactive web platform that visualizes Earth's thermal data on a dynamic 3D globe. Users can explore temperature changes across different years and months through an intuitive heatmap interface.

The project aims to tell a scientific story about our planet in a visual and engaging way, raising awareness about climate change and its impact. Terra combines data-driven storytelling with an educational game (currently under development), where players run through a polluted environment, collect trees, and plant them at the end of each level—reinforcing the message that increasing green cover is essential to combat pollution and restore balance.

## 🎯 Project Goal

The primary goal of Terra is to make surface temperature data accessible to the general public, allowing users to understand how Earth's surface temperatures have changed over time. By visualizing this data in an intuitive and engaging way, the project aims to raise awareness about environmental transformations and their impact on our planet.

In addition, Terra includes an educational game (currently under development) designed to promote environmental consciousness—especially among children. Through interactive gameplay, players learn how pollution affects the Earth and how planting trees can help restore ecological balance.

## 🧪 NASA Challenge: Animation Celebration of Terra Data!

This project addresses the NASA Space Apps Challenge titled **"Animation Celebration of Terra Data!"**, which celebrates the 25th anniversary of NASA’s Terra satellite. Terra has collected over 9,000 days of Earth science data through five continuously operating instruments, offering insights into surface temperature, pollution, urban growth, and more.

The challenge invites participants to use data from any of Terra’s instruments to create an animated product that tells an Earth science story and highlights its impact on people, communities, or the environment.

**Terra (our project)** directly responds to this challenge by:
- **Visualizing surface temperature data** from Terra’s MODIS instrument on a 3D interactive globe.
- **Animating changes over time** by year and month, allowing users to explore how Earth's surface has warmed.
- **Making the data accessible to the public**, especially non-scientists, through intuitive design and storytelling.
- **Adding a gamified experience** (currently under development) where players avoid pollution and plant trees—reinforcing the environmental message in a playful, educational format.

By combining scientific data with visual storytelling and interactive gameplay, our project transforms raw datasets into a compelling experience that raises awareness and inspires action.

## 🗺️ Solution Description

Terra is a web-based platform that visualizes surface temperature data from NASA’s Terra satellite using the MOD11C2 dataset. The core of the solution is a 3D interactive globe that displays heatmap overlays based on the selected year and month, allowing users to explore how Earth's surface temperatures have changed over time.

The platform is designed to be intuitive and accessible to non-scientific audiences. Users can rotate the globe, zoom in and out, and select specific timeframes to explore thermal patterns across the planet. This visual storytelling approach helps bridge the gap between raw scientific data and public understanding.

To further enhance engagement and environmental awareness, Terra includes an educational game (currently under development). In the game, players run through a polluted environment, avoiding harmful elements and collecting trees. At the end of each level, they plant the trees they’ve gathered—reinforcing the message that increasing green cover is essential to restoring ecological balance.

Together, the visualization and game form a unified experience that educates, inspires, and empowers users to understand and act on the environmental changes affecting our planet.

## 🛰️ NASA Data Used

We used the **MOD11C2** dataset from NASA’s Terra satellite, specifically from the MODIS (Moderate Resolution Imaging Spectroradiometer) instrument. This dataset provides global 8-day composites of **Land Surface Temperature (LST)** and **Emissivity** at a spatial resolution of 0.05 degrees (~5.6 km).

Key properties:
- **Source:** MODIS instrument onboard Terra satellite  
- **Product Name:** MOD11C2 – Land Surface Temperature/Emissivity 8-Day L3 Global 0.05Deg CMG  
- **Temporal Coverage:** February 2000 – Present  
- **Temporal Resolution:** 8-day intervals  
- **Spatial Resolution:** 0.05° (~5.6 km)  
- **Format:** HDF, converted to JSON for visualization

We extracted and processed the surface temperature values from this dataset to generate heatmap overlays on a 3D globe. This allowed us to animate temperature changes over time and present them in a format that is both scientifically accurate and visually engaging.

To support data processing, we developed a lightweight analytical server capable of parsing MOD11C2 files, filtering temperature values, and preparing structured outputs for visualization. While this server is not publicly accessible through the website, it can analyze any valid dataset provided to it—making it a flexible backend tool for future expansion or integration.

## 🛠️ Technologies Used

Terra combines multiple technologies across web development, data analysis, animation, and game design:

### 🌐 Web Platform
- **HTML, CSS, JavaScript** – Core structure and styling of the interactive website.
- **Three.js** – Used to render the 3D globe and apply heatmap overlays based on surface temperature data.
- **GitHub Pages** – Hosting the public-facing version of the visualization.

### 🧪 Data Analysis
- **Python** – Used to build a separate analytical server capable of parsing MOD11C2 datasets, filtering temperature values, and preparing structured outputs.
- *Note:* This server is not publicly connected to the website but can analyze datasets when provided manually.

### 🎞️ Animation
- **Blender** – Used to create visual assets and animations for storytelling and presentation purposes.

### 🎮 Game Development
- **Unity** – Engine used to build the educational game.
- **C#** – Programming language used to implement game logic, interactions, and environmental effects.

This multi-layered tech stack allows Terra to deliver a rich, interactive experience that blends scientific data with visual storytelling and playful learning.

## 🎮 Educational Game

As part of Terra’s mission to raise environmental awareness, we are developing an educational game designed to engage users—especially children—in learning how pollution affects the planet and how planting trees can help restore ecological balance.

### 🧩 Game Concept
Players run through a polluted environment filled with obstacles and harmful elements. Along the way, they collect trees scattered throughout the level. At the end of each run, the collected trees are planted in a clean zone, visually reinforcing the idea that individual actions can contribute to healing the Earth.

The game is designed to be simple, intuitive, and emotionally impactful. It complements the scientific visualization by turning environmental awareness into an interactive experience.

### 🛠️ Technologies Used
- **Unity** – Game engine used to build the interactive experience.
- **C#** – Programming language used for game logic and mechanics.
- **Blender** – Used to create 3D assets and animations for the game environment and characters.

The game is currently under development and will be integrated into the Terra platform in future versions.

## 📦 How to Run the Project

### 🌐 Web Visualization

The public-facing visualization is hosted online and can be accessed directly through the browser. No installation is required.

#### 🔧 Features:
- **Year & Month Selection:** Users choose a specific year and month using dropdown menus.
- **Thermal Visualization:** Upon clicking "Submit," the platform displays a heatmap of global surface temperatures for the selected time period.
- **Interactive Globe:** Users can rotate and zoom the 3D globe to explore temperature patterns across different regions.
- **Color Legend:** Brighter colors indicate warmer areas, while darker tones represent cooler zones.

> ⚠️ Note: The visualization is based on preprocessed data. Real-time dataset uploads or anomaly detection are not supported in the current version.

---

### 🧪 Analytical Server (Local Use Only)

A separate Python-based server is available for internal data analysis. This server is not connected to the public website but can process MOD11C2 files manually.

#### 🛠️ Capabilities:
- Accepts MOD11C2 HDF files as input
- Parses and filters surface temperature values
- Outputs structured JSON data for visualization or further processing

> This tool is intended for backend use and future scalability. It enables the team to prepare new datasets or extend the visualization with additional layers.

---

### 🎮 Educational Game

The game is currently under development and not yet integrated into the website. It runs as a standalone Unity application.

#### 🕹️ To Run:
- Open the Unity project in the Unity Editor
- Build and run the game for your target platform (Windows recommended)
- Control the player to avoid pollution and collect trees

> The game will be linked to the Terra platform in future versions to create a unified educational experience.

## 📦 How to Run the Project

### 🌐 Web Visualization

The public-facing visualization is hosted online and can be accessed directly through the browser. No installation is required.

#### 🔧 Features:
- **Year & Month Selection:** Users choose a specific year and month using dropdown menus.
- **Thermal Visualization:** Upon clicking "Submit," the platform displays a heatmap of global surface temperatures for the selected time period.
- **Interactive Globe:** Users can rotate and zoom the 3D globe to explore temperature patterns across different regions.
- **Color Legend:** Brighter colors indicate warmer areas, while darker tones represent cooler zones.


---

### 🧪 Analytical Server (Local Use Only)

A separate Python-based server is available for internal data analysis. This server is not connected to the public website but can process MOD11C2 files manually.

#### 🛠️ Capabilities:
- Accepts MOD11C2 HDF files as input
- Parses and filters surface temperature values
- Outputs structured JSON data for visualization or further processing

> This tool is intended for backend use and future scalability. It enables the team to prepare new datasets or extend the visualization with additional layers.

---

### 🎮 Educational Game

The game is currently under development and not yet integrated into the website. It runs as a standalone Unity application.

#### 🕹️ To Run:
- Open the Unity project in the Unity Editor
- Build and run the game for your target platform (Windows recommended)
- Control the player to avoid pollution and collect trees

> The game will be linked to the Terra platform in future versions to create a unified educational experience.

## 🎥 Presentation Materials

To support and explain our project, we’ve prepared the following materials:

- **📽️ Presentation Video:** A recorded walkthrough of the Terra platform, explaining its features, data sources, and environmental goals.  
  [Watch the video here](https://your-video-link.com)

- **📊 Slide Deck:** The official slides submitted to NASA Space Apps, detailing the challenge, our solution, technologies used, and future roadmap.  
  [View the slides here][https://your-slides-link.com](https://drive.google.com/file/d/1qynu3EI18X5k18qKDNXbsiAOhwQ-wWmm/view?usp=sharing)

These materials provide a complete overview of Terra’s mission, design, and impact, and are intended to complement the technical documentation and user experience.

## 👥 Team Members

This project was built by a collaborative team of developers, designers, and creatives:

- **Omar** – Data analyst and backend logic  
- **Yanal** – Web developer and interface integrator  
- **Saif** – Game developer and Unity programmer  
- **Osama** – Animator and Blender asset creator  
- **Hananda** – Presenter and media coordinator  
- **Basel** – Graphic designer and visual identity lead

Each member contributed a unique skillset to bring Terra to life—from data processing and 3D visualization to gameplay and storytelling.


## 🏆 Why This Project Should Win

Terra isn’t just a technical solution—it’s a message, a mission, and a movement.

In a world facing rising temperatures, shrinking forests, and growing disconnection from nature, Terra brings Earth’s story back into focus. By visualizing real surface temperature data from NASA’s Terra satellite, we help people see what’s happening to their planet—not through charts or reports, but through an interactive globe they can explore, understand, and connect with.

But we didn’t stop there.

We added a game that turns environmental awareness into action. Players don’t just learn—they *feel* the urgency. They run through pollution, collect trees, and replant hope. It’s simple, powerful, and unforgettable—especially for the next generation.

Our project:
- **Serves the environment** by highlighting climate patterns and encouraging reforestation.
- **Protects the future** by educating users in a way that’s engaging and emotionally resonant.
- **Raises awareness** by making scientific data accessible to everyone, not just researchers.
- **Empowers action** by turning knowledge into gameplay, and gameplay into impact.

Terra is built with heart, science, and vision. It’s not just about winning a challenge—it’s about helping people win back their planet.
