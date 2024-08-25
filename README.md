## Overview

This project aims to use opencv to track line for robot car

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
- RPi.GPIO as gpio

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
### 2. Hardware	(Robot Car)

Robot car front:<br>
<img src="assets/car_front.HEIC" alt="Diagram" width="250">

Robot car top:<br>
<img src="assets/car_top.HEIC" alt="Diagram" width="250">

Robot car bottom:<br>
<img src="assets/car_bottom.HEIC" alt="Diagram" width="250">


## Next Steps
- **AI Model Deploy:**
 Experiment with neural network architectures to improve car self drive performance.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request to contribute to the project.

## License
This project is licensed under the MIT License.
