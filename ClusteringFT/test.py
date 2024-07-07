# Import necessary libraries
import pandas as pd
import json

# Define the compare function
def compare(row, fuzz_testor_output):
    # Extract necessary values from fuzz_testor_output
    output_dict = json.loads(fuzz_testor_output)
    expected_max_deviation = output_dict['max_deviation']
    expected_max_altitude = output_dict['max_altitude']
    expected_duration = pd.to_timedelta(output_dict['duration']).total_seconds()
    expected_final_landing_state = output_dict['final_landing_state']
    expected_freefall_occurred = output_dict['freefall_occurred']
    expected_mission_complete = output_dict['mission_complete']

    # Extract values from the row
    actual_max_deviation = row['max_deviation']
    actual_max_altitude = row['max_altitude']
    actual_duration = row['duration']
    actual_final_landing_state = row['final_landing_state']
    actual_freefall_occurred = row['freefall_occurred']
    actual_mission_complete = row['mission_complete']

    # Define tolerance for comparison (adjust as per your requirement)
    tolerance = 2  # Example tolerance of 0.1 units or seconds

    # Compare each attribute and return 1 if all are close, otherwise return 0
    max_deviation_close = abs(expected_max_deviation - actual_max_deviation) <= tolerance
    max_altitude_close = abs(expected_max_altitude - actual_max_altitude) <= tolerance
    duration_close = abs(expected_duration - actual_duration) <= tolerance
    final_landing_state_match = expected_final_landing_state == actual_final_landing_state
    freefall_occurred_match = expected_freefall_occurred == actual_freefall_occurred
    mission_complete_match = expected_mission_complete == actual_mission_complete

    if (max_deviation_close and max_altitude_close and duration_close and 
        final_landing_state_match and freefall_occurred_match and mission_complete_match):
        return 1
    else:
        return 0

# Example test
def test_compare_function():
    # Sample data for testing
    fuzz_testor_output = {
        "max_deviation": 14.73,
        "max_altitude": 8.44,
        "duration": "00:00:35",
        "final_landing_state": True,
        "freefall_occurred": False,
        "mission_complete": True
    }

    row = pd.DataFrame({
        "max_deviation": [14.73],
        "max_altitude": [8.43568],
        "duration": [35.0],
        "final_landing_state": [True],
        "freefall_occurred": [False],
        "mission_complete": [True]
    })

    # Call the compare function
    result = compare(row.iloc[0], fuzz_testor_output)

    # Print the result
    print(f"Test Result: {result}")

# Run the test
test_compare_function()
