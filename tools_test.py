def add_class_to_schedule(timetable, day, time, course):
    day_map = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4}
    time_map = {'8:00': 0, '9:00': 1, '10:00': 2, '11:00': 3, '12:00': 4, '13:00': 5, '14:00': 6, '15:00': 7}

    
    if day in day_map and time in time_map:
        row, col = day_map[day], time_map[time]
        if not timetable[row][col]:
            timetable[row][col] = course
            print("Class added successfully!")
        else:
            print("Slot already taken!")
    else:
        print("Invalid input! Please enter a valid day and time.")



def remove_class_from_schedule(timetable, day, time):
    day_map = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4}
    time_map = {'8:00': 0, '9:00': 1, '10:00': 2, '11:00': 3, '12:00': 4, '13:00': 5, '14:00': 6, '15:00': 7}
    
    
    if day in day_map and time in time_map:
        row, col = day_map[day], time_map[time]
        if timetable[row][col]:
            timetable[row][col] = ''
            print("Class removed successfully!")
        else:
            print("No class scheduled at this slot!")
    else:
        print("Invalid input! Please enter a valid day and time.")
    

def check_class_taken(completed_courses, course_code):
    if course_code in completed_courses:
        print(f"{course_code} has already been taken.")
        return True
    else:
        print(f"{course_code} has not been taken yet.")
        return False

# Test add_class_to_schedule function
def test_add_class_to_schedule():
    print("\nRunning test_add_class_to_schedule...")

    timetable = [['' for _ in range(8)] for _ in range(5)]  # Empty 5x8 timetable
    add_class_to_schedule(timetable, 'Monday', '8:00', 'CS101')
    
    assert timetable[0][0] == 'CS101', "Test Failed: CS101 should be at Monday 8:00"
    
    # Try adding to an already occupied slot
    add_class_to_schedule(timetable, 'Monday', '8:00', 'MATH101')  # Should not overwrite
    assert timetable[0][0] == 'CS101', "Test Failed: Should not overwrite existing class"

    print("test_add_class_to_schedule passed!")


# Test remove_class_from_schedule function
def test_remove_class_from_schedule():
    print("\nRunning test_remove_class_from_schedule...")

    timetable = [['' for _ in range(8)] for _ in range(5)]
    timetable[0][0] = 'CS101'  # Monday 8:00 has CS101

    remove_class_from_schedule(timetable, 'Monday', '8:00')
    assert timetable[0][0] == '', "Test Failed: CS101 should be removed from Monday 8:00"

    print("test_remove_class_from_schedule passed!")


# Test check_class_taken function
def test_check_class_taken():
    print("\nRunning test_check_class_taken...")

    completed_courses = ['CS101', 'MATH101']
    
    assert check_class_taken(completed_courses, 'CS101') == True, "Test Failed: CS101 should be marked as taken"
    assert check_class_taken(completed_courses, 'CS202') == False, "Test Failed: CS202 should not be marked as taken"

    print("test_check_class_taken passed!")


# Run all tests

test_add_class_to_schedule()
test_remove_class_from_schedule()
test_check_class_taken()

print("\nAll tests passed successfully!")
