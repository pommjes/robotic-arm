# robotic-arm

Demo Link: https://youtu.be/8yHq4bUqn0A

<img width="675" height="900" alt="grafik" src="https://github.com/user-attachments/assets/67ba8f8c-3e67-4c80-ac8e-9897883fbf6a" />

### Hello,


This robotic arm is a project born out of a simple idea.
I saw a video of a cycloidal drive on tiktok and just decided to try and build one myself and maybe build something like 
one of these robotic arm like the ones on tiktok. How hard could it be right?
7 months later and a lot has happened. Let me just say: it was slightly harder than expected.
From building the very first version of a cycloidal drive based on the stepper motor that comes with the arduino kit.
After the first weekend of just building, testing and designing 12h a day of many to come, I had the first design which of course
was very shit.

<img width="1079" height="1083" alt="Screenshot_20260923_201655_Gallery" src="https://github.com/user-attachments/assets/6c02216f-13f0-4880-ae91-c997e7fdd1b9" />

After that I slowly started upgrading: I got my first Nema stepper motor along with a power supply, stepper drivers and some other supplies.
The first real working cycloidal drive turned into a design which could actually put out some tourque which slowly turned into a real robotic arm.
When I discovered **Stardance** the I got a huge push of motivation to finally finish this project which thankfully still motivates me to this day!


### These are the technical specs:

-Powered by Arduino

-Controlled on your PC in Python

-3  360° joints, two of them working with my cycloidal drive

-320mm of total, 360° range

-Uses ~10 Watts of power during operation

-Every joint is Homable via Hall-effect sensors

-Every joint is independently controllabe down to about 0.5° steps


Allthough I got myself a cool robotic arm on my desk now, the most important thing is what i learned.
Basically learned everything I know at this point from just this project:

-CAD modelling (with 3d-printing and ease of assembly in mind)

-3d-printing

-Soldering

-Planing and understanding circuits

-Design research, Parts research/logistics

Along with many more soft-skills like a general intuition of systems, designs and assemblys


### ***If you were to decide to build this arm for yourself:***
<img width="1018" height="736" alt="grafik" src="https://github.com/user-attachments/assets/cfc25d25-0680-4093-a6a2-3462367cb488" />

It isnt the most intuitive design to be honest. But the assembly in the cad files as well as the provided pics should help you to figure everything out.
The whole build uses m3 screws, nuts and washers. I recommend an assortment of multiple lenghts of m3 screws, such as the one listed on the BOM.

The build requires knowledge about elctric circuits specifically some experience with stepper motors is very handy so you dont fry your motors and drivers... (ask me how i know :D )
***If any questions occur, please leave a message in the discussions tab so I can help you!***
But you have to understand that this is not the print and play robotic arm you are looking for. It takes some assembly time and a little time to understand 
everything.


If anyone wants to work on it, I recommend working on the software as it is extremely rudimentary at this point only being able to perform the most basic things.
