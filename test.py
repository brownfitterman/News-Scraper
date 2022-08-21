import json
user_lists=[]
main_list=open("user_list.txt","r").read()
# print(mai)
News_user=['Charles Jordan', 'Cody Knapp', 'Maria Boyer', 'Yvonne Boyd', 'Chris Morgan', 'Alex Lyons', 'Carmen Franco', 'Toni Winters', 'Cameron Horne', 'William Williams', 'Grace Graham', 'James Miller', 'Crystal Marquez', 'Shirley Leonard', 'Madison Lewis', 'Sean Lindsey', 'David Howell', 'Donald Davis', 'Brittany Nguyen', 'Matthew Miller', 'Stephanie Klein', 'Christopher Reyes', 'Scott Nunez', 'Jennifer Bird', 'Alicia Tyler', 'Lisa Dodson', 'Troy Perez', 'Kevin Smith', 'Gary Thomas', 'Amanda Newman', 'Tracy Jimenez', 'David Carson', 'Jeffrey Johnston', 'Brandi Valdez', 'Sonia Murphy', 'Amy Benjamin', 'Valerie Duran', 'Corey Patel', 'Shannon Buck', 'Cristian Mcconnell', 'Alicia Holmes', 'Jennifer Hensley', 'Philip Hendricks', 'Vanessa Norris', 'Melissa Hernandez', 'Lisa Blake', 'Cheryl Mendoza', 'Rebecca Calderon', 'Amanda Walker', 'Joseph Shaw', 'Andrea Ross', 'Victoria Davis', 'Erin Yang', 'Nancy Dixon', 'Erin Ramos', 'Latoya Mcguire', 'Cynthia Wood', 'Richard Ross', 'Bruce Coleman', 'Katrina Hall', 'Jonathan Koch', 'Shawn Stewart', 'Jimmy Vargas', 'Elaine Sherman', 'Matthew Pollard', 'Michele Dickerson', 'Joseph Frazier', 'Kimberly Wilson', 'Anna Gonzales', 'Anthony Lee', 'Dr. Veronica Cochran MD', 'Jamie Jones', 'Teresa Johnson', 'Pamela Owens', 'Allen Clark', 'Jim Brown', 'Robert Perez', 'Austin Stevenson', 'Chelsea Moore', 'Kimberly Lynn', 'Tammy Sanford', 'Shane Smith', 'Nicholas Wilson', 'Megan Scott', 'Teresa Miller', 'William Wiggins', 'Makayla Gonzalez', 'Rachel Scott', 'Lisa Hawkins', 'Julia Avila', 'Jason Gonzalez', 'Patricia Palmer', 'Ryan Cordova DDS', 'Crystal Liu', 'John Lee', 'Nicole Garrison', 'Briana Simmons', 'Lori Jackson', 'Shannon Franco', 'Eric Parker']
user_dict={}
user_dict=open("user_dict.json","r").read().replace("'",'"')
print(user_dict)
user_dict=json.loads(user_dict)
print(type(user_dict))
# user_dict=
print(type(user_dict))
row=0
for r in range(100):
    if News_user[row] in main_list:
        f=user_dict[News_user[row]]
        user_lists.append(News_user[row])
        print(" user already inserted")
    else:
        f="dj"
        user_lists.append(News_user[row])
        user_dict[News_user[row]]=f
    row+=1
f1= open("user_list.txt","w")
f1.write(str(user_lists))
f2= open("user_dict.json","w")
f2.write(str(user_dict))