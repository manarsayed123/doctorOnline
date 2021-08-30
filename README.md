# doctorOnline
steps to get project running
1-git clone project
2-create venv
3- activate venv
4- run this command pip install -r requirements.txt
5- run this command ./manage.py generate_time_slot  ## this command to create all possible time slots from 1:12 am and from 1:12 pm

#Notes
on registeration you must define your role doctor or patient
i added swagger,soft delete,versioning
added unit test for app patient_reservation to test reservation process 

how to use app:
for doctor
first register with username,password,email,role(doctor)
can add clinic
add availble time slot for the clinic
list reservations etc
