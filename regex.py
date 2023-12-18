import re
list = ["Mr. Anderson", "Ms. Thareja","Mrs. Morri","Mr. Roy","Ms. Gandhi","Mrs. Modi","https://www.google.co","http://www.udemy.co","www.udacity.com","https://www.stackoverflow.com", "http://www.djsce.ac.in", "https://plus.google.com","rishit.grover@gmail.com",
"kapeesh.grover@yahoo.co.in", "abhishek.shah@gmail.com", "shahp98@gmail.com", "demo_user@gmail.com", "rolflmoa@yahoo.co.in", "27777647", "233*333*88", "455-78-888","022-240-93836", "02642*221*381"]

for val in list:
    if re.search("\AM[rs].", val):
        x = val.split(".")
        print("Name: ", x[1])
    elif re.search("\Ahttp.", val):
        x = val.split(".")
        print("Website: ", x[1])
    elif re.search("@.*[.]co.*\Z", val ):
        print("Email id: ", val)
    elif re.search("(^([0-9]+))([-*].*)?(([0-9]+)$)", val ):
        print("Phone number: ", val)
        