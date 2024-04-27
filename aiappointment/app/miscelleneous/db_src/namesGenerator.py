import csv
import random

first_names = ["Aarav", "Aarushi", "Abhijit", "Aditi", "Advait", "Aishwarya", "Akshay", "Alia", "Amara", "Amardeep", "Amrita", "Ananya", "Anika", "Anil", "Anisha", "Ankita", "Anshul", "Anuradha", "Aparna", "Arjun", "Arvind", "Asha", "Ashish", "Asmita", "Ayush", "Bhavesh", "Bhavya", "Chetan", "Deepak", "Devansh", "Devika", "Dhananjay", "Disha", "Divya", "Ekta", "Falguni", "Gaurav", "Gayathri", "Geeta", "Gopal", "Gouri", "Harsha", "Hema", "Isha", "Jai", "Janaki", "Jasmin", "Jatin", "Jaya", "Jyoti", "Kajal", "Kalyani", "Kamala", "Kanika", "Kavita", "Keshav", "Khushi", "Kiran", "Kirti", "Komal", "Krisha", "Kumar", "Lata", "Lavanya", "Leela", "Madhav", "Madhu", "Mahesh", "Manisha", "Manju",
               "Manohar", "Meena", "Meera", "Mohan", "Monica", "Mukesh", "Nandini", "Naveen", "Neelam", "Neha", "Nidhi", "Nikita", "Nilam", "Nisha", "Nithin", "Pallavi", "Pankaj", "Pooja", "Pradeep", "Prakash", "Prerna", "Priya", "Rahul", "Rajan", "Rajeev", "Rajesh", "Rakhi", "Ramesh", "Ranjan", "Rashmi", "Rekha", "Rishi", "Ritu", "Rohan","Rohit", "Rupali", "Sagar", "Sangeeta", "Sanjay", "Sapna", "Sarika", "Seema", "Shaila", "Shalini", "Shankar", "Shanta", "Shashi", "Shikha", "Shivani", "Shobha", "Shyam", "Simran", "Sneha","Sowmya", "Suman", "Sunita", "Suresh", "Swati", "Tanuja", "Tarun", "Uma", "Usha", "Vani", "Varun", "Veena", "Vibha", "Vidya", "Vijay", "Vikas", "Vimal", "Vishal", "Yamini", "Yash", "Yashoda"]
last_names = ["Sharma", "Patel", "Singh", "Choudhary", "Reddy", "Gupta", "Kumar", "Verma", "Rao",
              "Yadav", "Das", "Joshi", "Nair", "Khan", "Hegde", "Srinivasan", "Iyer", "Banerjee", "Mehta", "Thakur"]

num_names = 5000

print(len(first_names))
print(len(last_names))
names_list = []

for _ in range(num_names):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    full_name = f"{first_name} {last_name}"
    names_list.append(full_name)

with open("indian_names.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name"])  
    for name in names_list:
        writer.writerow([name])

print(f"{num_names} Indian names have been generated and saved to 'indian_names.csv'.")
