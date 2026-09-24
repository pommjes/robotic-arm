# robotic-arm  |  Stardance, Hack Club project

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

<img width="783" height="546" alt="grafik" src="https://github.com/user-attachments/assets/524dd1d0-a87d-4184-aa46-f75ce96287f2" />


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


### Allthough I got myself a cool robotic arm on my desk now, the most important thing is what i learned.
**I Basically learned everything I know at this point from just this project:**

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

***About the 3d printing***, all parts can probalby just be printed in plain pla with completely default settings. ***!Except!*** for the two "waves", which should be printed with 100% infill.
The housing of joint 2 is supposed to take a lot of force to slide on the base. Consider using a hammer.

<img width="1383" height="948" alt="grafik" src="https://github.com/user-attachments/assets/52285b35-9c20-4bde-83ae-5275f845d1f1" />


The build requires knowledge about elctric circuits specifically some experience with stepper motors is very handy so you dont fry your motors and drivers... (ask me how i know :D )
***If any questions occur, please leave a message in the discussions tab so I can help you!***
But you have to understand that this is not the print and play robotic arm you are looking for. It takes some assembly time and a little time to understand 
everything.


### ***To operate***, move all joints to their zero position using the manual joint movements:
<img width="979" height="607" alt="grafik" src="https://github.com/user-attachments/assets/7cd10a4e-b2de-4386-b7e4-84324badba67" />
this should be as accuarate as possible. 

**Once youre done**, zero every joint in the UI. 
The UI is pretty straight forward in my opinion. The homing feature is more or less useless as is, but could be modified to automatically move to the exact zero position after homing, but this will be different for every arm 
depending on the exact placement of the sensors and the magnets. I also realized that the home all feature is pretty unlogical to have, so its not bound to any command right now. 
**I would advise you to read the comments in 
the arduino code** to get a better understanding of the controls, but I dont think its all too important. 
**Definetly** pay attention to the messages in the UI itself aswell as in the python terminal.
<img width="899" height="826" alt="Screenshot 2026-09-23 190438" src="https://github.com/user-attachments/assets/80efc921-688d-4048-b2c7-52cf0a1f2425" />



If anyone wants to work on it, I recommend working on the software as it is extremely rudimentary at this point only being able to perform the most basic things.
