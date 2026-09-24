# Arduino based Robotic Arm  
> **A Hack Club Stardance project**

### Demo Link: https://youtu.be/8yHq4bUqn0A

<img width="675" height="900" alt="grafik" src="https://github.com/user-attachments/assets/67ba8f8c-3e67-4c80-ac8e-9897883fbf6a" />

### Hello,


This robotic arm was born out of a simple idea. I saw a video of a cycloidal drive on TikTok and decided to try building one myself — and maybe turn it into a robotic arm like the ones I saw online. 

*How hard could it be, right?*

**7 months later:** Let's just say it was *slightly* harder than expected. 

It started with a tiny 28BYJ-48 stepper motor from an Arduino starter kit. After a first weekend of designing, printing, and testing for 12 hours a day, I finished Version 1 — which, of course, was terrible.

<img width="783" height="546" alt="Early Cycloidal Prototype" src="https://github.com/user-attachments/assets/524dd1d0-a87d-4184-aa46-f75ce96287f2" />

From there, I gradually upgraded: I bought my first NEMA stepper motors, dedicated power supply, stepper drivers, and additional hardware. The first working cycloidal drive capable of actual torque output slowly evolved into a full robotic arm. 

When I discovered **Stardance**, it gave me a massive push of motivation to finally finish this pro

### Technical specs:

- Powered by Arduino

- Controlled on your PC in Python

- 3  360° joints, two of them working with my cycloidal drive

- 320mm of total, 360° range

- Uses ~10 Watts of power during operation

- Every joint is Homable via Hall-effect sensors

- Every joint is independently controllabe down to about 0.5° steps



### Allthough I got myself a cool robotic arm on my desk now, the most important thing is what i learned.
**I Basically learned everything I know at this point from just this project:**

* CAD modelling (with 3d-printing and ease of assembly in mind)

* 3d-printing

* Soldering

* Planing and understanding circuits
  
* Design research, Parts research/logistics

Along with many more soft-skills like a general intuition of systems, designs and assemblys



##  Build & Assembly Notes
<img width="1018" height="736" alt="grafik" src="https://github.com/user-attachments/assets/cfc25d25-0680-4093-a6a2-3462367cb488" />

To be honest, it isn't the most intuitive design. However, the assembly view in the CAD files and the provided pictures should help you figure everything out.

* **Hardware:** Uses standard M3 screws, nuts, and washers. I recommend an assortment with multiple lengths (listed in the BOM).
* **3D Printing:** Most parts print fine in standard PLA with default settings. **Exception:** The two **"wave" components** in the cycloidal drive **must be printed with 100% infill**.
* **Assembly Tip:** The housing of Joint 2 requires force to slide onto the base due to heavy structural load — consider using a rubber mallet/hammer carefully.

<img width="1383" height="948" alt="grafik" src="https://github.com/user-attachments/assets/52285b35-9c20-4bde-83ae-5275f845d1f1" />


>  **Circuit Warning:** This project requires working knowledge of electrical circuits and stepper motors so you don't fry your motors or drivers *(ask me how I know... :D)*.

*This is not a plug-and-play kit. It takes real assembly time and some patience to understand how everything works together. If you have questions, please leave a message in the **Discussions** tab!*


## ***Operating the arm & Software***
### Setup
1. Download the software files. You should have 3 files. 2 Python files and one C++ file.
2. Just open the Python files in you code editor and upload the C++ file to your Arduino
3. Connect the Arduino to yor PC via USB and run the Python file titled "arm_control_3.py". It should say "Succesfuly connected to Arduino

Done! You should be ready to go! The next steps:


### Zeroing the joints
Before using the "target point" app, you have to zero all of the joints as seen in the render below as horizontal as possible using the *manual joint control*.
<img width="979" height="607" alt="grafik" src="https://github.com/user-attachments/assets/7cd10a4e-b2de-4386-b7e4-84324badba67" />
once done, zero all the joints in the UI by pressing **Zero** (see UI below)
 
### UI & Control
* The GUI is fairly straightforward. 
* The hardware homing via Hall-sensors works, but could be modified to automatically drive to the exact zero point after triggering (varies depending on magnet/sensor placement). 
* Pay close attention to error messages in the Python terminal and the UI itself.
* Check the comments in the Python code to get a better understanding of the control software (probalby optional).
  
<img width="899" height="826" alt="Screenshot 2026-09-23 190438" src="https://github.com/user-attachments/assets/80efc921-688d-4048-b2c7-52cf0a1f2425" />



If anyone wants to work on it, I recommend working on the software as it is extremely rudimentary at this point only being able to perform the most basic things.

### AI usage:

**This project was done by me. AI assisted me.** This project introduced me to many new challanges like complex electric circuits, cimplicated coding (for me) as well as new physics concepts and many more.
**I used AI for some research for parts, solving hard problems and to assist my decision making process here and there**. I am sure that I would not have solved the big problems I faced if I hadnt used any AI. 
But I definitely did the work by myself and did ***not*** just do what the AI told me to do. 

(AI in this context means LLMs, i.e. Chatgpt, Gemini, Grok etc)
