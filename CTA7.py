# Anthony Le
# CSC500 - Principles of Programming
# Critical Thinking Assignment 7

# This program creates a dictionary containing course numbers and the room numbers where the courses are held.
# It also creates a dictionary containing course numbers and the names of the instructors teaching those courses.
# It also creates a dictionary containing course numbers and the times when the courses are held.
# The program allows the user to input a course number and retrieves and displays the corresponding room number, instructor name, and class time.
if __name__ == "__main__":
    # Dictionaries to hold course information
    # Course number to room number mapping
    course_rooms = {
        "CSC101": "3004",
        "CSC102": "4501",
        "CSC103": "6755",
        "NET110": "1244",
        "COM241": "1411"
    }
    # Course number to instructor name mapping
    course_instructors = {
        "CSC101": "Dr. Haynes",
        "CSC102": "Dr. Alvarado",
        "CSC103": "Dr. Rich",
        "NET110": "Dr. Burke",
        "COM241": "Dr. Lee"
    }
    #  Course number to class start time mapping
    course_times = {
        "CSC101": "8:00 AM",
        "CSC102": "9:00 AM",
        "CSC103": "10:00 AM",
        "NET110": "11:00 AM",
        "COM241": "1:00 PM"
    }

    # Prompt user for course number from the available courses
    course_number = input(
    "\n\tCSC101"
    "\n\tCSC102"
    "\n\tCSC103"
    "\n\tNET110"
    "\n\tCOM241"
    "\nEnter one of the above courses: ").strip().upper()

    # Retrieve and display course information
    if course_number in course_rooms:
        # Get corresponding room, instructor, and time
        room = course_rooms[course_number]
        instructor = course_instructors[course_number]
        time = course_times[course_number]

        # Display the course information
        print(f"Course Number: {course_number}")
        print(f"Room Number: {room}")
        print(f"Instructor: {instructor}")
        print(f"Class Time: {time}")
    else:
        print("Course not found.")