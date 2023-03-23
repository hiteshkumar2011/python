from tkinter import  *

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    kilo_meter_result_label.config(text=f"{km}")

window = Tk()
window.title("Miles to KM Converter")
window.config(padx=20,pady=20)
window.minsize(width=300, height=350)

miles_input = Entry()
miles_input.config(width=7)
miles_input.grid(column=1, row=0)

## Label
miles_label = Label(text="Miles")
miles_label.grid(column=2,row=0)
is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0,row=1)
kilo_meter_result_label = Label(text="0")
kilo_meter_result_label.grid(column=1,row=1)
kilometer_label = Label(text="Km")
kilometer_label.grid(column=2,row=1)

## Button
calculate_Button = Button(text="Calculate",command=miles_to_km)
calculate_Button.grid(column=1,row=2)

window.mainloop()