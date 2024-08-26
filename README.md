## Overview

This project focuses on developing a line-following robot car using OpenCV, powered by a Raspberry Pi 4 B and controlled via an Adeept Motor Hat V2. The robot, based on the Adeept 2-wheel robot car, will autonomously follow a line by processing visual input, employing motor control, and integrating object detection and tracking. This endeavor serves as a foundational step towards creating a fully functional AI-driven autonomous robot car.

## Project Structure
```plaintext
Car_Line_Tracking/
│
├── src/
│   ├── One_Line_Tracking.py               
│   ├── motor.py    
│   ├── function.py  
│   ├── Forward.py
│   ├── Backward.py 
│   ├── Left.py 
│   ├── Right.py                       
│   └── model.py                         
│
└── README.md                             # Project overview and instructions
```

## Requirements

- Python 3.7+
- opencv
- RPi.GPIO

You can install the necessary packages using the following command:

```bash
pip install opencv-python 
```

## How to Run

### 1. Run Line Tracking 

Run car with one cmd:

```bash
python src/One_Line_Tracking.py
```
### 2. Hardware	
#### Control Board
Raspberry pi 4 B:<br>
<img src="assets/Raspberry_pi_4.png" alt="Diagram" width="250">

Adeept Motor Hat V2:<br>
<img src="assets/Adeept Motor Hat V2.png" alt="Diagram" width="250">

#### Robot Car
Robot car front:<br>
<img src="assets/car_front.png" alt="Diagram" width="250">

Robot car top:<br>
<img src="assets/car_top.png" alt="Diagram" width="250">

Robot car bottom:<br>
<img src="assets/car_bottom.png" alt="Diagram" width="250">

## Results
Follow Line Moving:

https://github.com/user-attachments/assets/ff69ae37-35f4-49bf-8366-5d5ad6ffc160

## Next Steps
- **AI Model Deploy :**
 Experiment with neural network architectures to improve car self drive performance.
- **End-to-End AI System :**
Consider exploring end-to-end learning approaches where a neural network directly controls the robot based on raw camera input.
- **Reinforcement Learning :**
Experiment with reinforcement learning to further advance your project into a more complex AI-driven system.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request to contribute to the project.

## License
This project is licensed under the MIT License.
