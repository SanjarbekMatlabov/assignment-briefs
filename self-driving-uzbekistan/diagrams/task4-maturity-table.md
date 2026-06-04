# Task 4 — Technology maturity classification (Appendix D, Step 5)

The diagram in `task4-technology-connections.mmd` contains **24 technology blocks**.
Each block is colour-coded by maturity. The table below justifies each classification
with a short, real reason (no random classification, per the brief).

| # | Technology | Maturity | Colour | Reason |
|---|-----------|----------|--------|--------|
| 1 | Self-Driving Vehicle System (SAE L0–L5) | Emerging | 🟢 | Growing fast, real pilots, not yet a stable mass standard |
| 2 | LiDAR sensors | Emerging | 🟢 | Rapidly improving and falling in price, still not in every car |
| 3 | Radar sensors | Mature | 🔵 | Standard automotive component for decades |
| 4 | Cameras / Computer Vision | Mature | 🔵 | Widely used, stable hardware; AI use is what is new |
| 5 | GPS / GNSS positioning | Mature | 🔵 | Global, stable standard |
| 6 | IMU / wheel odometry | Mature | 🔵 | Established navigation sensors |
| 7 | Ultrasonic parking sensors | Mature | 🔵 | Common in current cars |
| 8 | AI accelerators / GPUs / SoC | Emerging | 🟢 | New automotive-grade chips evolving quickly |
| 9 | Edge computing | Emerging | 🟢 | Growing fast for low-latency processing |
| 10 | Cloud computing & data centres | Mature | 🔵 | Established, widely used |
| 11 | Big data pipelines | Mature | 🔵 | Standard in modern software |
| 12 | Deep learning / neural networks | Emerging | 🟢 | Core, fast-moving field driving autonomy |
| 13 | Sensor fusion algorithms | Emerging | 🟢 | Active research, central to self-driving |
| 14 | SLAM & path planning | Emerging | 🟢 | Maturing but still advancing |
| 15 | HD maps | Emerging | 🟢 | Growing, expensive to build and maintain |
| 16 | Digital twin / simulation | Emerging | 🟢 | Increasingly used to train and test models |
| 17 | V2X connectivity | Future | 🟠 | Early stage; needs roadside and network rollout |
| 18 | 5G networks | Emerging | 🟢 | Rolling out, not yet universal in Uzbekistan |
| 19 | OTA software updates | Mature | 🔵 | Proven in modern connected cars |
| 20 | Automotive cybersecurity | Emerging | 🟢 | Growing field as cars become software platforms |
| 21 | EV / electric drivetrain platform | Emerging | 🟢 | Scaling fast (e.g. BYD–UzAuto in Jizzakh) |
| 22 | Intelligent Transport Systems | Emerging | 🟢 | Tashkent Traffic Management Center launched Dec 2025 |
| 23 | Human-only driving | Obsolete | ⚪ | The practice automation aims to replace |
| 24 | Paper maps / manual navigation | Obsolete | ⚪ | Replaced by digital and HD maps |

**Maturity counts:** Obsolete = 2, Mature = 8, Emerging = 13, Future = 1 (total = 24).

**Connection types used in the diagram (with labels):**
- **Dependency** (`needs`) — what the technology cannot work without (e.g. *needs LiDAR*, *needs deep learning*).
- **Combination** (`combines`) — technologies used together (e.g. *combines* EV platform, V2X, ITS).
- **Enhancement** (`improves`) — technologies that make it better (e.g. edge computing *improves speed*, 5G *improves data*).
- **Disruption** (`replaces`) — what it makes obsolete (e.g. *replaces* human-only driving; HD maps *replace* paper maps).
