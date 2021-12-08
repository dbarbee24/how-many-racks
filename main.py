

#def wrk_cntr_807():

print(" Hello Welcome to the racks generator!\n ") 

planned_labor_time = (float(input(" What is the planned labor time?\n"))) 
hrs_worked = int(input(" How many hours will you work today? \n"))
parts_on_rack = int(input(" How many parts for a full rack? \n"))


pc_per_hour = round((60 / planned_labor_time)) 
parts_needed = (hrs_worked * pc_per_hour)
racks_needed = round((parts_needed / parts_on_rack))

 
print(f" You will need {racks_needed} racks for a 100% day!") 