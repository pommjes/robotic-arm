import customtkinter as ctk
import math
from math import*
from arduino_connection import ArduinoController


#CTK settings and init
ctk.set_appearance_mode("dark")                 #"light"- for light mode
ctk.set_default_color_theme("green")            #"blue"- to turn Ui blue

app = ctk.CTk()
app.title("Hello CustomTkinter")
app.geometry("900x800")
app.minsize(900, 800)

#main_frame = ctk.CTkFrame(app)
#main_frame.pack(fill="both", expand=True, padx=10, pady=10)

down_panel = ctk.CTkFrame(app, height=270)
down_panel.pack(side = "bottom",fill = "x", padx=10, pady=10  )

#errors and messages for user
error_label0 = ctk.CTkLabel(down_panel, text="Messages:", font=("Helvetica", 18))
error_label0.place(x = 200, y = 150)

error_label1 = ctk.CTkLabel(down_panel, text_color = "red" ,text="", font=("Helvetica", 16))
error_label1.place(x = 320, y = 180)

error_label2 = ctk.CTkLabel(down_panel, text_color= "grey",text = "make sure to also keep an eye on the terminal for additional error messages" ,font = ("Helvetica", 14))
error_label2.place(x = 200, y=  210)

L1, L2 = 16,16

#alt = old, neu = new
pos1_alt, pos2_alt, pos3_alt = 0.0, 0.0, 0.0

def gui_logger(message: str, is_error: bool):
    color = "red" if is_error else "green"
    error_label1.configure(text=message, text_color=color)

port = 'COM5'#                                                           <---- put the usb port as the one your arduino is connected to. Also do this in "arduino.connection.py"
arduino = ArduinoController(port=(port), baudrate=115200)

if arduino.connect():
    error_label1.configure(text = "succesfuly connected to arduino!", text_color = "green")
else:
    error_label1.configure(text = "arduino not connected.", text_color = "red")

#sending all the inputs to the arduino
def send_data1():
    arduino.send_angles(delta1, delta2, delta3)

def send_data2():
    global pos1_alt,pos2_alt,pos3_alt, j1move, j2move, j3move

    arduino.send_angles(j1move, j2move, j3move)

    if j1move is not None:
            pos1_neu = round(pos1_alt + j1move, 4)
            pos1_alt = pos1_neu
    if j2move is not None:
            pos2_neu = round(pos2_alt + j2move, 4)
            pos2_alt = pos2_neu
    if j3move is not None:
            pos3_neu = round(pos3_alt + j3move, 4)
            pos3_alt = pos3_neu

def home_joint1():
    global pos1_alt
    arduino.home(joint="1", callback=lambda: reset_pos(1))

def home_joint2():
    global pos2_alt
    arduino.home(joint="2", callback=lambda: reset_pos(2))

def home_joint3():
    global pos3_alt
    arduino.home(joint="3", callback=lambda: reset_pos(3))

def home_joint_all():
    arduino.home(joint="ALL", callback=lambda: reset_pos("ALL"))

def reset_pos(joint):
    global pos1_alt, pos2_alt, pos3_alt
    if joint == 1 or joint == "ALL":
        pos1_alt = 0.0
    if joint == 2 or joint == "ALL":
        pos2_alt = 0.0
    if joint == 3 or joint == "ALL":
        pos3_alt = 0.0 


def zero_joint1():
    global pos1_alt
    pos1_alt = 0.0

def zero_joint2():
    global pos2_alt
    pos2_alt = 0.0

def zero_joint3():
    global pos3_alt
    pos3_alt = 0.0

def update_pos_display():
    pos_label.configure(text = f"Positions: \n\n Joint 1: {pos1_alt}°\n\n Joint 2: {pos2_alt}°\n\n Joint 3: {pos3_alt}°")
    app.after(200, update_pos_display)


def get_val(entry):
    try:
        return float(entry.get())
    except ValueError:
        return None

def calculate():
    global pos1_alt, pos2_alt, pos3_alt, delta1, delta2, delta3

    L1,L2 = 16,16

    int_x = get_val(xentry)
    int_y = get_val(yentry)
    int_z = get_val(zentry)

    if int_x is not None and int_y is not None and int_z is not None:
        #calculating base angle
        theta1 = atan2(int_z, int_x)

        y_2d = sqrt(int_x*int_x + int_z*int_z)
        x_2d = int_y

        #calculating value for the angle calculations
        value = (x_2d*x_2d+y_2d*y_2d-L1*L1-L2*L2)/(2*L1*L2)

        #calculating the joint angles. a and b are different models while theta 2&3 are the two different joints
        theta3_a = acos(value)
        theta2_a = atan2(y_2d,x_2d) - atan2(L2 * sin(theta3_a), L1+L2*cos(theta3_a))

        theta3_b = -acos(value)
        theta2_b = atan2(y_2d,x_2d) - atan2(L2 * sin(theta3_b), L1+L2*cos(theta3_b))

        #checking if the calculated angles are actually possible
        elbow_y_a = L1 * sin(theta2_a)
        end_y_a = (L1 * sin(theta2_a)+ L2 * sin(theta2_a + theta3_a))

        elbow_y_b = L1 * sin(theta2_b)
        end_y_b = (L1 * sin(theta2_b)+ L2 * sin(theta2_b + theta3_b))

        min_height = 0

        legal_a = elbow_y_a >= min_height and end_y_a >= min_height
        legal_b = elbow_y_b >=min_height and end_y_b >= min_height

        deg1 = round(degrees(theta1), 4)
        deg2a = round(degrees(theta2_a), 4)
        deg2b = round(degrees(theta2_b), 4)
        deg3a= round(degrees(theta3_a), 4)
        deg3b = round(degrees(theta3_b), 4)

        if legal_a:
            output_label1.configure(text = f"θA1: {deg1}° | θA2: {deg2a}° | θA3: {deg3a}°")
            pos1_neu,pos2_neu,pos3_neu = deg1, deg2a, deg3a
        elif legal_b:
            output_label1.configure(text = f"θB1: {deg1}° | θB2: {deg2b}° | θB3: {deg3b}°")
            pos1_neu,pos2_neu,pos3_neu = deg1, deg2b, deg3b
        else:
            output_label1.configure(text = f"no possible positions found")

        #calculating the angle wich would result in the new position.          ###THIS IS THE DATA NEEDED TO SEND TO ARDUINO AND CONTROLL THE JOINTS!
        delta1 = round(pos1_neu - pos1_alt, 4)
        delta2 = round(pos2_neu - pos2_alt, 4)
        delta3 = round(pos3_neu - pos3_alt, 4)

        output_label2.configure(text = f"∆1:{delta1}° | ∆2:{delta2}° | ∆3:{delta3}°")

        pos1_alt, pos2_alt, pos3_alt = pos1_neu, pos2_neu, pos3_neu

        error_label1.configure(text = "All inputs seem to be valid!", text_color = "green")
    else:
        error_label1.configure(text = "All 3 inputs must be filled out", text_color = "red")
        delta1 = None
        delta2 = None
        delta3 = None

def move():
    global pos1_alt,pos2_alt,pos3_alt, j1move, j2move, j3move

    j1move = get_val(j1entry)
    j2move = get_val(j2entry)                                                           #### THE VALUES FOR SINGLE JOINT MOVEMENTS ARE HERE
    j3move = get_val(j3entry)


    output_label3.configure(text = f"∆1: {j1move}° | ∆2: {j2move}° | ∆3: {j3move}°")
    output_label4.configure(text = "Make sure to delete unwanted commands before sending!!")

main_label = ctk.CTkLabel(app, text="UI for 3DOF robotic arm", font=("Helvetica", 23))
main_label.place(x = 340, y = 20)

pos_label = ctk.CTkLabel(app, text = "", font = ("Helvetica", 20))
pos_label.place(x = 380, y = 100)

#widgets for first function
label_1 = ctk.CTkLabel(app, text="Inputs for target point:", font=("Helvetica", 18))
label_1.place(x = 90, y= 100)

xentry = ctk.CTkEntry(app, placeholder_text="Target x-value. (depth,cm)", width= 170)
xentry.place(x = 90, y= 150)

yentry = ctk.CTkEntry(app, placeholder_text="Target y-value. (height,cm)", width= 170)
yentry.place(x = 90, y = 185)

zentry = ctk.CTkEntry(app, placeholder_text="Target z-value. (width,cm)", width= 170)
zentry.place(x = 90, y = 220)

button1 = ctk.CTkButton(app, text="Submit", command=calculate,)
button1.place(x = 100, y = 255)

output_label1 = ctk.CTkLabel(app, text="", font=("Helvetica", 17))
output_label1.place(x = 60, y = 350)

output_label2 = ctk.CTkLabel(app, text="", font=("Helvetica", 17))
output_label2.place(x = 60, y = 380)

send_button1 = ctk.CTkButton(app, text="Move", command= lambda:(send_data1(), calculate()))
send_button1.place(x = 100, y = 470)

#widgets for second function
label_2 = ctk.CTkLabel(app, text="Inputs for joint movement:", font=("Helvetica", 18))
label_2.place(x= 620, y = 100)

j1entry = ctk.CTkEntry(app, placeholder_text= "Joint 1 Delta (degrees)", width= 170)
j1entry.place(x = 650, y = 150)

j2entry = ctk.CTkEntry(app, placeholder_text= "Joint 2 Delta (degrees)", width= 170)
j2entry.place(x = 650, y = 185)

j3entry = ctk.CTkEntry(app, placeholder_text= "Joint 3 Delta (degrees)", width= 170)
j3entry.place(x = 650, y = 220)

button2 = ctk.CTkButton(app, text="Submit", command= move)
button2.place(x = 660, y = 255)

output_label3 = ctk.CTkLabel(app, text="", font = ("Helvetica", 17))
output_label3.place(x = 630, y = 350)

output_label4 = ctk.CTkLabel(app, text="", font= ("Helvetica", 17))
output_label4.place(x = 450, y = 380)

send_button2 = ctk.CTkButton(app, text="Move", command=send_data2)
send_button2.place(x = 660, y = 470)

#homing buttons
homing_label = ctk.CTkLabel(down_panel, text= "Homing:", font=("Helvetica", 18))
homing_label.place(x = 420, y = 5)

home_button1 = ctk.CTkButton(down_panel, text="Home joint 1", command = home_joint1)
home_button1.place(x = 90, y = 35)

home_button2 = ctk.CTkButton(down_panel, text = "Home joint 2", command = home_joint2)
home_button2.place(x = 390, y = 35)

home_button3 = ctk.CTkButton(down_panel, text = "Home joint 3", command = home_joint3)
home_button3.place(x = 650, y = 35)

home_button_all = ctk.CTkButton(down_panel, text="Home all joints", fg_color="red")             #not linked to a command yet
home_button_all.place(x = 390, y = 125)

#zero-ing buttons
zero_button1 = ctk.CTkButton(down_panel, text = "Zero joint 1", command = zero_joint1)
zero_button1.place(x = 90, y = 80)

zero_button2 = ctk.CTkButton(down_panel, text = "Zero joint 2", command = zero_joint2)
zero_button2.place(x = 390, y = 80)

zero_button3 = ctk.CTkButton(down_panel, text = "Zero joint 3", command = zero_joint3)
zero_button3.place(x = 650, y = 80)


update_pos_display()
app.mainloop()