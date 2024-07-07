import pandas as pd
from itertools import combinations
import Clustering as clt
import random
import FaultTree as ft
import json


THROTTLE_DICT = {0: 1, 260: 2, 550: 3, 600: 4, 615: 5}
GEOFENCE_ACTION = {"None" : 0, "Warning": 1, "Hold mode" : 2, "Return mode" : 3, "Terminate" : 4, "Land mode" : 5}
STATES_DICT = {'Flying': lambda: random.choice(['BriarWaypoint','BriarWaypoint2','BriarWaypoint3']), 'Land': 'Land', 'Disarm': 'Disarm', 'Takeoff': 'Takeoff', 'Arm': 'Takeoff', 'Hover': 'BriarHover'}


closest_points_to_centroids_df = clt.Clustering()
print(closest_points_to_centroids_df)

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


# Select specific columns
columns_to_consider = ['states', 'Wind', 'GFACT', 'kill_switch', 'modes', 'throttle']
df_selected = closest_points_to_centroids_df[columns_to_consider]

# Convert boolean columns to integers
bool_cols = df_selected.select_dtypes(include=['bool']).columns
df_selected[bool_cols] = df_selected[bool_cols].astype(int)

# Handle object columns by encoding them as category codes
object_cols = df_selected.select_dtypes(include=['object']).columns
df_selected[object_cols] = df_selected[object_cols].apply(lambda x: x.astype('category').cat.codes)

# Calculate standard deviation for each column
std_devs = df_selected.std()

# Sort columns by standard deviation in descending order
sorted_columns = std_devs.sort_values(ascending=False)

# Select the top N varying columns (you can adjust N as needed)
top_varying_columns = list(sorted_columns.index[:3])

fuzz_test_args = {'drone_id': 'Polkadot'}
for index, row in closest_points_to_centroids_df.iterrows():
    if 'GFACT' in top_varying_columns:
        fuzz_test_args['geofence'] = [GEOFENCE_ACTION.get(row['GFACT'])]
    elif 'states' in top_varying_columns:
        if row['states'] == 'Flying':
            fuzz_test_args['states'] = [STATES_DICT['Flying']()]
        else:
            fuzz_test_args['states'] = [STATES_DICT[row['states']]]

    if 'throttle' in top_varying_columns:
        if int(row['throttle']) not in [0, 260, 550, 600, 615]:
            fuzz_test_args['throttle'] = None
        else:
            fuzz_test_args['throttle'] = [THROTTLE_DICT.get(int(row['throttle']))]

    if 'modes' in top_varying_columns:
       fuzz_test_args['modes'] = [row['modes']]
    
    # if fuzz_test_args['throttle'] is None:
    #     fuzz_test_args.pop('throttle')

    print('Args - ' +str(fuzz_test_args))

    # Example input dictionary
    input_dict = fuzz_test_args

    # Extract the keys for combinations, excluding 'drone_id'
    keys = list(input_dict.keys())
    keys.remove('drone_id')

    # Generate all combinations of keys
    combinations_list = []
    for r in range(len(keys) + 1):  # Include all possible combinations
        combinations_list.extend(combinations(keys, r))

    # Generate truth table data
    data1 = []
    data2 = []
    for combo in combinations_list:
        # Create a dictionary for each combination
        call_dict = {k: input_dict[k] for k in input_dict if k == 'drone_id' or k in combo}
        data1.append(call_dict)
        if 'geofence' not in call_dict and 'geofence' in input_dict:
            if row['states'] == 'Flying':
                call_dict['states'] = [STATES_DICT['Flying']()]
            else:
                call_dict['states'] = [STATES_DICT[row['states']]]
        if 'states' not in call_dict and 'states' in input_dict:
            call_dict['geofence'] = random.choice(GEOFENCE_ACTION)
        print(call_dict)
        '''
        fuzz_test = ft.Fuzz_Test(call_dict)
        self.fuzz_testor.run_test(fuzz_test)
        self.fuzz_testor.test_complete.wait()

        var = compare(row, fuzz_testor.output)
        os.system("rm executed_tests.pkl")
        os.system("rm Fuzz_Test_Logs.txt")
        self.fuzz_testor.test_complete.clear()
        '''
        row_dict = {k: 1 if k in combo else 0 for k in keys}
        data2.append(row_dict)
        # row_dict['result'] = var
        row_dict['result'] = random.choice([0, 1])


    df_truth = pd.DataFrame(data2)

    print('Truth table')
    print(df_truth)

    exp = ft.minLogicFunc(df_truth)
    print(exp)
    logic_expr = ft.convert_logic_to_boolean(exp)
    print(logic_expr)
    ft.drawFaultTree(logic_expr)
    mincut = ft.mincutSets(logic_expr)
    print(mincut)

    