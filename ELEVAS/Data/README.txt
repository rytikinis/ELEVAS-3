------------------ELEVAS--------------------


             ELEVAS KEYWORDS

sfr - star formation rate
em - every mega year
op - orange %
yp - yellow %
wp - white %
bp - blue %
ybp - yellow binary %
mry - megayears

s_alive - stars alive
s_born - stars born
s_died - stars died

o_alive - orange stars alive
o_born - orange stars born
o_died - orange stars died

y_alive - yellow stars alive
y_born - yellow stars born
y_died - yellow stars died

w_alive - white stars alive
w_born - white stars born
w_died - white stars died

b_alive - blue stars alive
b_born - blue stars born
b_died - blue stars died

                COMANDS

Base commands(ELEVAS\>):
	- new_simulation (creates new simulation that will not be saved)
	- new_file (creates new simulation file so you can repeate simulations with the same specs)
	- open_fle (runs an .elv file)

Simulation commands(ELEVAS\SIMULATION\>):
	- add_output (program will create an .csv file and output the simulation numbers by selected timesteps)
	- add_gass_amount (a gass usage limit will be created) 
	- add_time_speed (time speed will be changed to an user selected speed per myr)

			GASS_USAGE

Gass is set to infinity by default but user can add amount

orange stars: 400
yellow stars: 500
white stars: 900
blue stars: 1000

			.elv FILES

.elv files is an ELEVAS file type and it is used to store simulation specs.

			OUTPUTS

All ELEVAS outputs will be created as .csv files and will be found at "Data/Outputs".
All files has an ID, the ID is said when simulation stars (only if you selected to create outputs).
If you want to store your .csv file I reccomend to move it from outputs folder and rename it.
You can use TopCat or any other software to visualize the outputs.

			REQUIREMENTS

- pyhton 3
- pygame
- pickle
- csv