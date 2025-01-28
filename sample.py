def update_schedule(slots, completed_courses, available_courses):
    """
    Updates and displays the course schedule based on available slots and courses
    
    Args:
        slots: List of tuples containing (day, time) for available slots
            Example: [('Monday', '8:00'), ('Tuesday', '10:00')]
        completed_courses: List of course codes already completed 
            Example: ['CS101', 'MATH201']
        available_courses: List of course codes available to take based on prerequisites
            Example: ['CS201', 'CS202']
            
    Returns:
        timetable: 2D list representing the schedule matrix where each cell contains
                  either a course code or empty string
    """
    # Initialize empty 5x8 timetable matrix
    # 5 rows for weekdays (Mon-Fri) and 8 columns for time slots (8am-4pm)
    # Each cell will contain either a course code or empty string
    timetable = [['' for _ in range(8)] for _ in range(5)]
    
    # Dictionary mapping days to row indices for easy lookup
    # This allows converting day names to matrix row positions
    day_map = {
        'Monday': 0,    # First row
        'Tuesday': 1,   # Second row
        'Wednesday': 2, # Third row
        'Thursday': 3,  # Fourth row
        'Friday': 4,     # Fifth row
        'Saturday': 5
    }
    
    # Dictionary mapping time slots to column indices
    # This allows converting time strings to matrix column positions
    time_map = {
        '8:00': 0,   # 8am = first column
        '9:00': 1,   # 9am = second column
        '10:00': 2,  # And so on...
        '11:00': 3,
        '12:00': 4,
        '13:00': 5,
        '14:00': 6,
        '15:00': 7,
        '16:00': 8,
        '17:00': 9   # 3pm = last column
    }
    
    # First, mark completed courses in the timetable
    completed_slots = slots[:len(completed_courses)]
    for (day, time), course in zip(completed_slots, completed_courses):
        if day in day_map and time in time_map:
            row = day_map[day]
            col = time_map[time]
            timetable[row][col] = f"{course} (C)"
    
    # Then, assign available courses to remaining slots
    remaining_slots = slots[len(completed_courses):]
    course_index = 0
    for day, time in remaining_slots:
        if course_index < len(available_courses):
            if day in day_map and time in time_map:
                row = day_map[day]
                col = time_map[time]
                # Only assign if slot is not taken by a completed course
                if not timetable[row][col]:
                    timetable[row][col] = available_courses[course_index]
                    course_index += 1
            
    # Prepare data for display
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    times = ['8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00']
    
    # Print the header row with time slots
    print('\nUpdated Timetable:')
    print('Time', end='\t')  # Left corner cell
    for time in times:
        print(f'{time}', end='\t')  # Print each time slot
    print()  # New line after header
    
    # Print each row of the timetable
    for i, day in enumerate(days):
        print(f'{day}', end='\t')  # Print day name at start of row
        for j in range(8):
            cell = timetable[i][j]
            # Print course code if cell is filled, otherwise print "-"
            print(f'{cell if cell else "-"}', end='\t')
        print()  # New line after each row
    
    return timetable  # Return the matrix for potential further use

def test_update_schedule():
    # Test data
    slots = [
        ('Monday', '8:00'),    # Will contain completed course CS101
        ('Monday', '10:00'),   # Will contain completed course MATH101
        ('Tuesday', '9:00'),   # Will contain CS201
        ('Wednesday', '14:00'), # Will contain CS202
        ('Friday', '11:00')    # Will contain CS303
    ]
    
    completed_courses = ['CS101', 'MATH101']
    available_courses = ['CS201', 'CS202', 'CS303', 'MATH202', 'PHY101']
    
    # Run the function
    timetable = update_schedule(slots, completed_courses, available_courses)
    
    # Assertions to verify the results
    assert timetable[0][0] == 'CS101 (C)'    # Monday 8:00 (completed)
    assert timetable[0][2] == 'MATH101 (C)'  # Monday 10:00 (completed)
    assert timetable[1][1] == 'CS201'        # Tuesday 9:00
    assert timetable[2][6] == 'CS202'        # Wednesday 14:00
    assert timetable[4][3] == 'CS303'        # Friday 11:00
    
    # Test empty slots
    assert timetable[0][1] == ''  # Monday 9:00 should be empty
    assert timetable[3][0] == ''  # Thursday 8:00 should be empty
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_update_schedule()

