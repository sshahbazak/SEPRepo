import numpy as np
import pandas as pd
import gower
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.express as px
# import geomstats.backend as gs
# import geomstats.visualization as visualization
# from geomstats.geometry.hypersphere import Hypersphere
# from geomstats.learning.kmeans import RiemannianKMeans
# from geomstats.geometry.special_orthogonal import SpecialOrthogonal
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import PCA
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score
from sklearn.manifold import TSNE
from scipy import stats

def main():
    # Add file to computer and use the following to run this code
    # df = pd.read_csv(r"Insert file path here")
    df = pd.read_csv(r"C:\Users\Porte\Desktop\notredame_files\L1_TESTS_FINAL_SUBMISSION.csv")

    #DATA CLEANING
    #Clean data byB renaming columns
    df.rename(columns={'MSN State': 'msn_state'}, inplace=True)
    df.rename(columns={'Mode': 'mode'}, inplace=True)
    df.rename(columns={'GF': 'gf'}, inplace=True)
    df.rename(columns={'GFPRED': 'gf_pred'}, inplace=True)
    df.rename(columns={'GFACT': 'gf_act'}, inplace=True)
    df.rename(columns={'Wind': 'wind'}, inplace=True)

    # Clean data by turning duration into seconds
    df['duration'] = pd.to_timedelta(df['duration']).dt.total_seconds()

    # Remove outlier data
    df = df[df['msn_state'] != 'ReceiveMission']

    # Remove unnamed ID column
    df = df.drop(df.columns[0], axis=1)

    # Split the data set for full view
    df_split_point1 = len(df) // 3
    df_split_point2 = 2 * len(df) // 3
    df_first_third = df.iloc[:df_split_point1]
    df_second_third = df.iloc[df_split_point1:df_split_point2]
    df_third_third = df.iloc[df_split_point2:]

    #Clean data by turning NaN values to 'None'
    df['throttle'] = df['throttle'].fillna(0)

    # Normalize boolean values to integers (False=0, True=1)
    # df['gf'] = df['gf'].astype(int)
    # df['gf_pred'] = df['gf_pred'].astype(int)
    # df['gf_act'] = df[ 'gf_act'].astype(int)
    # df['kill_switch'] = df['kill_switch'].astype(int)
    # df['final_landing_state'] = df['final_landing_state'].astype(int)
    # df['freefall_occurred'] = df['freefall_occurred'].astype(int)
    # df['mission_complete'] = df['mission_complete'].astype(int)
    # df['wind'] = df['wind'].replace('5 North', 1)
    number_mapping = {
        'True': 1,
        'False': 0,
        'NaN': 0.5,
        'None': 0.5,
        'Yes': 1,
        'No': 0
    }
    number_mapping0 = {
        '5 North': 1,
        'None': 0,
        'NaN': 0    
    }
    number_mapping1 = {
        'arm': 0.15,
        'takeoff': 0.65,
        'hover': 0.7,
        'flying': 0.9,
        'land': 0.4,
        'disarm': 0.1
    }
    number_mapping2 = {
        'POSTCTL': 0.625,
        'OFFBOARD': 0.7,
        'STABILIZED': 0.3,
        'ALTCTL': 0.45,
        'AUTO.RTL': 0.575,
        'AUTO.LOITER': 0.525,
        'AUTO.LAND': 0.6
    }
    number_mapping3 = {
        'RETURN_MODE': 0.8,
        'HOLD_MODE': 0.65,
        'WARNING': 0.45,
        'LAND_MODE': 0.55,
        'NaN': 0.2
    }
    
    df['gf'] = df['gf'].replace(number_mapping)
    df['gf_pred'] = df['gf_pred'].replace(number_mapping)
    df['kill_switch'] = df['kill_switch'].replace(number_mapping)
    df['final_landing_state'] = df['final_landing_state'].astype(int)
    df['freefall_occurred'] = df['freefall_occurred'].astype(int)
    df['mission_complete'] = df['mission_complete'].astype(int)
    df['wind'] = df['wind'].replace(number_mapping0)
    df['msn_state'] = df['msn_state'].replace(number_mapping1)
    df['mode_switch'] = df['mode_switch'].replace(number_mapping2)
    df['gf_act'] = df['gf_act'].replace(number_mapping3)
    # df_mean_values = df.mean()
    df['wind'].fillna(0, inplace=True)
    df['gf_pred'].fillna(0.5, inplace=True)
    df['gf_act'].fillna(0.2, inplace=True)

    print(pd.isnull(df).sum())

    # DATA ANALYSIS

    # Displays unique values for each column (df_display_unique_values)
    def df_display_unique_values():
        unique_values = df.apply(lambda x: x.unique())
        print("Unique values for data set")
        print(unique_values)

#Displays count for unique values for each column (df_display_unique_values_count)
    def df_display_unique_values_count():
        unique_counts = df.apply(lambda x: x.nunique())
        print("Unique values count for data set")
        print(unique_counts)

#Displays unique values and count for msn_state (df_msn_state)
    def df_msn_state():
        msn_state_values = sorted(df['msn_state'].unique())
        msn_state_unique_values_count = df['msn_state'].value_counts()        
        msn_state_total_count = df['msn_state'].count() + df['msn_state'].isna().sum()
        msn_state_percentages = msn_state_unique_values_count / msn_state_total_count * 100
        msn_state_summary = pd.DataFrame({
            'Count': msn_state_unique_values_count,
            'Percentage': msn_state_percentages.map('{:.2f}%'.format)  # Format percentages to 2 decimal places
        })
        print("Mission state values for data set: ")
        print(msn_state_values)
        print()
        print("Count for unique values in data set column")
        print(msn_state_summary)

#Displays unique values and unique values count for mode_switch (df_mode_switch)
    def df_mode_switch():
        mode_switch_values = sorted(df['mode_switch'].unique())
        mode_switch_unique_values_count = df['mode_switch'].value_counts()       
        mode_switch_total_count = df['mode_switch'].count() + df['mode_switch'].isna().sum()
        mode_switch_percentages = mode_switch_unique_values_count / mode_switch_total_count * 100
        mode_switch_summary = pd.DataFrame({
            'Count': mode_switch_unique_values_count,
            'Percentage': mode_switch_percentages.map('{:.2f}%'.format)  # Format percentages to 2 decimal places
        })      
        print("Mode switch values for data set")
        print(mode_switch_values)
        print()
        print("Count for data set column")
        print(mode_switch_summary)

#Displays range, unique values, count, and unique values count for throttle (df_throttle)
    def df_throttle():
        df['throttle'] = df['throttle'].fillna(0)
        df['throttle'] = pd.to_numeric(df['throttle'], errors='coerce')
        min_value = df['throttle'].min()
        max_value = df['throttle'].max()
        throttle_range = (f"{min_value} to {max_value}")
        throttle_values = sorted(df['throttle'].unique())
        throttle_unique_values_count_including_nan = df['throttle'].nunique(dropna=False)
        throttle_unique_values_count = df['throttle'].value_counts(dropna=False)
        total_count = df['throttle'].count() + df['throttle'].isna().sum()
        throttle_percentages = throttle_unique_values_count / total_count * 100
        throttle_summary = pd.DataFrame({
            'Count': throttle_unique_values_count,
            'Percentage': throttle_percentages.map('{:.2f}%'.format)  # Format percentages to 2 decimal places
        })

        print("Throttle range for data set")
        print(throttle_range)
        print()
        print("Throttle values for data set")
        print(throttle_values)
        print()
        print("Count for unique values in throttle column")
        print(throttle_unique_values_count_including_nan)
        print()
        print("Count for data set column")
        print(throttle_summary)

#Displays range, unique values, count, unique values count for greater than 1 max_deviation (df_max_deviation)
    def df_max_deviation():
        min_value = df['max_deviation'].min()
        max_value = df['max_deviation'].max()
        max_deviation_range = (f"{min_value} to {max_value}")
        max_deviation_values = sorted(df['max_deviation'].unique())
        max_deviation_unique_values_count = df['max_deviation'].nunique()
        max_deviation_values_count = df['max_deviation'].value_counts()
        values_count_max_deviation_greater_than_1 = max_deviation_values_count[max_deviation_values_count > 1]        
        max_deviation_total_count = df['max_deviation'].count() + df['max_deviation'].isna().sum()
        max_deviation_percentages = values_count_max_deviation_greater_than_1 / max_deviation_total_count * 100
        max_deviation_summary = pd.DataFrame({
            'Count': values_count_max_deviation_greater_than_1,
            'Percentage': max_deviation_percentages.map('{:.2f}%'.format)  # Format percentages to 2 decimal places
        })

        print("Max Deviation range for data set")
        print(max_deviation_range)
        print()
        print("Max deviation values for data set")
        print(max_deviation_values)
        print()
        print("Count for unique values in max deviation column")
        print(max_deviation_unique_values_count)
        print()
        print("Count for unique values greater than 1 in data set column (Currently 0 values have a count of more than 1)")
        print(max_deviation_summary)

#Displays range, unique values, count, and unique values count for greater than 1 max_altitude (df_max_altitude)
    def df_max_altitude():
        min_value = df['max_altitude'].min()
        max_value = df['max_altitude'].max()
        max_altitude_range = (f"{min_value} to {max_value}")
        max_altitude_values = sorted(df['max_altitude'].unique())
        max_altitude_unique_values_count = df['max_altitude'].nunique()
        max_altitude_values_count = df['max_altitude'].value_counts()
        values_count_max_altitude_greater_than_1 = max_altitude_values_count[max_altitude_values_count > 1]
        max_altitude_total_count = df['max_altitude'].count() + df['max_altitude'].isna().sum()
        max_altitude_percentages = values_count_max_altitude_greater_than_1 / max_altitude_total_count * 100
        max_altitude_summary = pd.DataFrame({
            'Count': values_count_max_altitude_greater_than_1,
            'Percentage': max_altitude_percentages.map('{:.2f}%'.format)  # Format percentages to 2 decimal places
        })

        print("Max altitude range for data set")
        print(max_altitude_range)
        print()
        print("Max altitude values for data set")
        print(max_altitude_values)
        print()
        print("Count for unique values in max altitude column")
        print(max_altitude_unique_values_count)
        print()
        print("Count for unique values that are greater than 1")
        print(max_altitude_summary)
    
# Displays range, unique values, count, and unique values count for duration (df_duration)
    def df_duration():
        min_value = df['duration'].min()
        max_value = df['duration'].max()
        duration_range = (f"{min_value} to {max_value}")
        duration_values = sorted(df['duration'].unique())
        duration_unique_values_count = df['duration'].nunique()
        duration_values_count = df['duration'].value_counts()
        values_count_duration_greater_than_1 = duration_values_count[duration_values_count > 1]
        #values_count_duration_equal_to_2 = duration_values_count[duration_values_count == 2]
        duration_total_count = df['duration'].count() + df['duration'].isna().sum()
        duration_percentages = values_count_duration_greater_than_1 / duration_total_count * 100
        duration_summary = pd.DataFrame({
            'Count': values_count_duration_greater_than_1,
            'Percentage': duration_percentages.map('{:.2f}%'.format)  # Format percentages to 2 decimal places
        })

        pd.set_option('display.max_rows', None)

        print("Duration range for data set")
        print(duration_range)
        print()
        print("Duration values for data set")
        print(duration_values)
        print()
        print("Count for unique duration values in data set")
        print(duration_unique_values_count)
        print()
        print("Count for data set column (Greater than 2)")
        print(duration_summary)
        # print()
        # print("Count for data set column (Equal to 2)")
        # print(values_count_duration_equal_to_2)

        pd.reset_option('display.max_rows')

    def cluster_df_display_unique_values():
        df_display_unique_values()
        unique_values = cluster_choice.apply(lambda x: x.unique())
        print("Unique values for cluster")
        print(unique_values)
        
    def cluster_df_display_unique_values_count():
        df_display_unique_values_count()
        unique_counts = cluster_choice.apply(lambda x: x.nunique())
        print("Unique values count for cluster")
        print(unique_counts)             

    def cluster_df_msn_state(cluster_choice):
        msn_state_values = cluster_choice['msn_state'].unique()
        msn_state_values_sorted = sorted(msn_state_values)
        msn_state_unique_values_count = cluster_choice['msn_state'].value_counts()        
        msn_state_total_count = cluster_choice['msn_state'].count() + cluster_choice['msn_state'].isna().sum()
        msn_state_percentages = msn_state_unique_values_count / msn_state_total_count * 100
        msn_state_summary = pd.DataFrame({
            'Count': msn_state_unique_values_count,
            'Percentage': msn_state_percentages.map('{:.2f}%'.format)  # Format percentages to 2 decimal places
        })

        df_msn_state()
        print("Mission state values for cluster: ")
        print(msn_state_values_sorted)
        print()
        print("Count for unique values in cluster column")
        print(msn_state_summary)

    def cluster_df_mode_switch():
        mode_switch_values = sorted(cluster_choice['mode_switch'].unique())
        mode_switch_unique_values_count = cluster_choice['mode_switch'].value_counts()       
        mode_switch_total_count = cluster_choice['mode_switch'].count() + cluster_choice['mode_switch'].isna().sum()
        mode_switch_percentages = mode_switch_unique_values_count / mode_switch_total_count * 100
        mode_switch_summary = pd.DataFrame({
            'Count': mode_switch_unique_values_count,
            'Percentage': mode_switch_percentages.map('{:.2f}%'.format)  # Format percentages to 2 decimal places
        })

        df_mode_switch()
        print("Mode switch values for cluster")
        print(mode_switch_values)
        print()
        print("Count for cluster column")
        print(mode_switch_summary)

    def cluster_df_throttle():
        cluster_choice['throttle'] = pd.to_numeric(cluster_choice['throttle'], errors='coerce')
        min_value = cluster_choice['throttle'].min()
        max_value = cluster_choice['throttle'].max()
        throttle_range = (f"{min_value} to {max_value}")
        throttle_values = sorted(cluster_choice['throttle'].unique())
        throttle_unique_values_count_including_nan = cluster_choice['throttle'].nunique(dropna=False)
        throttle_unique_values_count = cluster_choice['throttle'].value_counts(dropna=False)
        total_count = cluster_choice['throttle'].count() + cluster_choice['throttle'].isna().sum()
        throttle_percentages = throttle_unique_values_count / total_count * 100
        throttle_summary = pd.DataFrame({
            'Count': throttle_unique_values_count,
            'Percentage': throttle_percentages.map('{:.2f}%'.format)  # Format percentages to 2 decimal places
        })

        df_throttle()
        print("Throttle range for cluster")
        print(throttle_range)
        print()
        print("Throttle values for cluster")
        print(throttle_values)
        print()
        print("Count for unique values in throttle column for cluster")
        print(throttle_unique_values_count_including_nan)
        print()
        print("Count for cluster column")
        print(throttle_summary)

    def cluster_df_max_deviation():
        min_value = cluster_choice['max_deviation'].min()
        max_value = cluster_choice['max_deviation'].max()
        max_deviation_range = (f"{min_value} to {max_value}")
        max_deviation_values = sorted(cluster_choice['max_deviation'].unique())
        max_deviation_unique_values_count = cluster_choice['max_deviation'].nunique()
        max_deviation_values_count = cluster_choice['max_deviation'].value_counts()
        values_count_max_deviation_greater_than_1 = max_deviation_values_count[max_deviation_values_count > 1]        
        max_deviation_total_count = cluster_choice['max_deviation'].count() + cluster_choice['max_deviation'].isna().sum()
        max_deviation_percentages = values_count_max_deviation_greater_than_1 / max_deviation_total_count * 100
        max_deviation_summary = pd.DataFrame({
            'Count': values_count_max_deviation_greater_than_1,
            'Percentage': max_deviation_percentages.map('{:.2f}%'.format)  # Format percentages to 2 decimal places
        })

        df_max_deviation()
        print("Max Deviation range for cluster")
        print(max_deviation_range)
        print()
        print("Max deviation values for cluster")
        print(max_deviation_values)
        print()
        print("Count for unique values in max deviation column for cluster")
        print(max_deviation_unique_values_count)
        print()
        print("Count for unique values in cluster greater than 1 in data set column (Currently 0 values have a count of more than 1)")
        print(max_deviation_summary)
    def cluster_df_max_altitude():
        min_value = cluster_choice['max_altitude'].min()
        max_value = cluster_choice['max_altitude'].max()
        max_altitude_range = (f"{min_value} to {max_value}")
        max_altitude_values = sorted(cluster_choice['max_altitude'].unique())
        max_altitude_unique_values_count = cluster_choice['max_altitude'].nunique()
        max_altitude_values_count = cluster_choice['max_altitude'].value_counts()
        values_count_max_altitude_greater_than_1 = max_altitude_values_count[max_altitude_values_count > 1]
        max_altitude_total_count = cluster_choice['max_altitude'].count() + cluster_choice['max_altitude'].isna().sum()
        max_altitude_percentages = values_count_max_altitude_greater_than_1 / max_altitude_total_count * 100
        max_altitude_summary = pd.DataFrame({
            'Count': values_count_max_altitude_greater_than_1,
            'Percentage': max_altitude_percentages.map('{:.2f}%'.format)  # Format percentages to 2 decimal places
        })

        df_max_altitude()
        print("Max altitude range for cluster")
        print(max_altitude_range)
        print()
        print("Max altitude values for cluster")
        print(max_altitude_values)
        print()
        print("Count for unique values in max altitude column for cluster")
        print(max_altitude_unique_values_count)
        print()
        print("Count for unique values in cluster that are greater than 1")
        print(max_altitude_summary)

    def cluster_df_duration():
        min_value = cluster_choice['duration'].min()
        max_value = cluster_choice['duration'].max()
        duration_range = (f"{min_value} to {max_value}")
        duration_values = sorted(cluster_choice['duration'].unique())
        duration_unique_values_count = cluster_choice['duration'].nunique()
        duration_values_count = cluster_choice['duration'].value_counts()
        values_count_duration_greater_than_1 = duration_values_count[duration_values_count > 1]
        #values_count_duration_equal_to_2 = duration_values_count[duration_values_count == 2]
        duration_total_count = cluster_choice['duration'].count() + cluster_choice['duration'].isna().sum()
        duration_percentages = values_count_duration_greater_than_1 / duration_total_count * 100
        duration_summary = pd.DataFrame({
            'Count': values_count_duration_greater_than_1,
            'Percentage': duration_percentages.map('{:.2f}%'.format)  # Format percentages to 2 decimal places
        })

        pd.set_option('display.max_rows', None)

        df_duration()
        print("Duration range for cluster")
        print(duration_range)
        print()
        print("Duration values for cluster")
        print(duration_values)
        print()
        print("Count for unique duration values in cluster")
        print(duration_unique_values_count)
        print()
        print("Count for cluster column (Greater than 2)")
        print(duration_summary)

    # def data_set_analysis():
    #     print ("\nOptions:")
    #     print("A. I want information on the full data set analysis.")
    #     print("B. I want to start clustering the data set.")
    #     print("Q. I want to quit this program.")

    #     #choice = input("Enter your choice (A, B, or Q): ")

    # def data_set_analysis_A():
    #     while choice != '9':

    #         print("\nOptions:")
    #         print("1. Display data set unique values")
    #         print("2. Display data set unique values count")
    #         print("3. Display data set information for mission state column")
    #         print("4. Display data set information for mode switch column")
    #         print("5. Display data set information for throttle column")
    #         print("6. Display data set information for max deviation column")
    #         print("7. Display data set information for max altitude column")
    #         print("8. Display data set information for duration column")
    #         print("9. Go back to main menu")

    # def data_set_analysis_A_choices():
    #     if choice == '1':
    #         if not df_display_unique_values():
    #             print()
    #     elif choice == '2':
    #         if not df_display_unique_values_count():
    #             print()
    #     elif choice == '3':
    #         if not df_msn_state():
    #             print()
    #     elif choice == '4':
    #         if not df_mode_switch():
    #             print()
    #     elif choice == '5':
    #         if not df_throttle():
    #             print()
    #     elif choice == '6':
    #         if not df_max_deviation():
    #             print()
    #     elif choice == '7':
    #         if not df_max_altitude():
    #             print()
    #     elif choice == '8':
    #         if not df_duration():
    #             print()
    #     elif choice == '9':
    #         print("Back to main menu...")
    #     else:
    #         print("Invalid choice. Please try again by entering A1 through A9.")


    # Main Menu Options (A, B, or Quit)
    while True:
        print(df)
        input("Press enter to continue.")
        print ("\nOptions:")
        print("A. I want information on the full data set analysis.")
        print("B. I want to start clustering the data set.")
        print("Q. I want to quit this program.")

        choice = input("Enter your choice (A, B, or Q): ")

        # Define choices (Add lowercase options?)
        if choice == 'A':
            while choice != '11':

                print("\nOptions:")
                print("1. Display data set header (First 5 rows & last 5 rows)")
                print("2. Display full data set results")
                print("3. Display data set unique values")
                print("4. Display data set unique values count")
                print("5. Display data set information for mode column")
                print("6. Display data set information for mission state column")
                print("7. Display data set information for wind column")
                print("8. Display data set information for gf column")
                print("9. Display data set information for gf pred column")
                print("10. Display data set information for gf act column")
                print("11. Display data set information for kill switch column")
                print("12. Display data set information for mode switch column")
                print("13. Display data set information for throttle column")
                print("14. Display data set information for max deviation column")
                print("15. Display data set information for max altitude column")
                print("16. Display data set information for duration column")
                print("17.Display data set information for final landing state column")
                print("18. Display data set information for freefall occurred column")
                print("19. Display data set information for mission complete column")
                print("20. Go back to main menu")

                choice = input("Enter your choice (1 - 11): ")

                # Define choices for data set analysis
                
                if choice == '1':
                    pd.set_option('display.max_columns', None)
                    pd.set_option('display.max_colwidth', None)
                    print(df.head)
                    pd.reset_option('display.max_columns')
                    pd.reset_option('display.max_colwidth')
                elif choice == '2':
                    pd.set_option('display.max_rows', None)
                    pd.set_option('display.max_columns', None)
                    pd.set_option('display.max_colwidth', None)
                    print(df_first_third)
                    input("Press enter to continue")
                    print(df_second_third)
                    input("Press enter to continue")
                    print(df_third_third)
                    pd.reset_option('display.max_rows')
                    pd.reset_option('display.max_columns')
                    pd.reset_option('display.max_colwidth')
                elif choice == '3':
                    if not df_display_unique_values():
                        print()
                elif choice == '4':
                    if not df_display_unique_values_count():
                        print()
                elif choice == '5':
                    if not df_mode():
                        print()
                elif choice == '6':
                    if not df_msn_state():
                        print()
                elif choice == '7':
                    if not df_wind():
                        print()
                elif choice == '8':
                    if not df_gf():
                        print()
                elif choice == '9':
                    if not df_gf_pred():
                        print()
                elif choice == '10':
                    if not df_gf_act():
                        print()
                elif choice == '11':
                    if not df_kill_switch():
                        print()
                elif choice == '12':
                    if not df_mode_switch():
                        print()
                elif choice == '13':
                    if not df_throttle():
                        print()
                elif choice == '14':
                    if not df_max_deviation():
                        print()
                elif choice == '15':
                    if not df_max_altitude():
                        print()
                elif choice == '16':
                    if not df_duration():
                        print()
                elif choice == '17':
                    if not df_final_landing_state():
                        print()
                elif choice == '18':
                    if not df_freefall_occurred():
                        print()
                elif choice == '19':
                    if not df_mission_complete():
                        print()
                elif choice == '20':
                    print("Back to main menu...")
                    break
                else:
                    print("Invalid choice. Please try again by entering 1 through 20.")

        elif choice == 'B':
            while choice != 'E':
                df.fillna(value='None', inplace=True)

                print("\nOptions: Do you want to remove any columns?")
                print("Y. Yes, I want to remove columns")
                print("N. No, I do not want to remove columns")

                while True:
                    choice = input("Enter your choice Y or N: ")

                    if choice == 'Y':
                        # Prompt the user for input
                        columns = input("Enter the column names to drop, separated by commas (mode, msn_state, wind, gf, gf_pred, gf_act, kill_switch, mode_switch, throttle, max_deviation, max_altitude, duration, final_landing_state, freefall_occurred, mission_complete): ")

                        # Convert the input string to a list of column names
                        columns_to_drop = [col.strip() for col in columns.split(',')]

                        # Check if columns exist in the DataFrame
                        valid_columns = [col for col in columns_to_drop if col in df.columns]
                        invalid_columns = [col for col in columns_to_drop if col not in df.columns]

                        # Drop the columns
                        if valid_columns:
                            df = df.drop(columns=valid_columns)
                            print(f"Columns dropped: {', '.join(valid_columns)}")
                        else:
                            print("No valid columns to drop.")

                        if invalid_columns:
                            print(f"Invalid columns ignored: {', '.join(invalid_columns)}")

                        #Call the function and drop specified columns
                        print("Updated data set:")
                        print(df)
                        print()

                    elif choice == "N":
                        print("You chose not to remove any columns")
                    
                    elif choice != 'Y' or 'N':
                        print("Invalid choice you must chose Y or N.")
                        continue
                    break

                while True:
                    print("\nOptions: Do you want to visualize using the elbow method?")
                    print("Y. Yes, I want to see the elbow method graph")
                    print("N. No, I do not want to see the elbow method graph")

                    # Compute the Gower distance matrix (df)
                    gower_dist = gower.gower_matrix(df)
                    
                    choice = input("Enter your choice Y or N: ")
                    if choice == 'Y':
                    #Implement Elbow Approach

                        # Function to calculate KMeans inertia on the Gower distance matrix
                        def calculate_inertia(dist_matrix, max_k):
                            inertias = []
                            for k in range(1, max_k + 1):
                                kmeans = KMeans(n_clusters=k, random_state=0)
                                kmeans.fit(dist_matrix)
                                inertias.append(kmeans.inertia_)
                            return inertias

                        # Determine the optimal number of clusters using the elbow method
                        max_k = 10
                        inertias = calculate_inertia(gower_dist, max_k)

                        # Plot the elbow graph
                        plt.figure(figsize=(8, 6))
                        plt.plot(range(1, max_k + 1), inertias, marker='o')
                        plt.xlabel('Number of clusters (k)')
                        plt.ylabel('Inertia')
                        plt.title('Elbow Method For Optimal k')
                        plt.xticks(range(1, max_k + 1))
                        plt.grid(True)
                        plt.show()

                    elif choice == 'N':
                        print()
                            
                    elif choice != 'Y' or 'N':
                        print("Invalid choice. Please chose Y or N.")
                        continue
                    break

                while True:
                    print("\nOptions: How many clusters would you like (2 - 10)?")

                    choice = input("Enter your choice between 2 and 10: ")

                    if choice == '2':
                        k = 2
                    elif choice == '3':
                        k = 3
                    elif choice == '4':
                        k = 4 
                    elif choice == '5':
                        k = 5
                    elif choice == '6':
                        k = 6
                    elif choice == '7':
                        k = 7
                    elif choice == '8':
                        k = 8
                    elif choice == '9':
                        k = 9
                    elif choice == '10':
                        k = 10
                    elif choice not in [2 - 10]: 
                        print("Invalid choice, please select a number between 2 and 10 to represent the number of clusters you want.")
                        continue
                    break
                
                while True:
                    print("\nOptions: What clustering method do you want to implement?")
                    print("1. Implement K-Means clustering.")
                    print("2. Implement DBSCAN clustering.")
                    print("3. Implement SPK-Means clustering.")
                    print("4. Implement AGNES clusting.")

                    choice = input("Enter your choice (1 - 4): ")
                    if choice == '1':
                        
                        #Applying the optimal k value to perform k-means clustering (df)
                        # Compute the Gower distance matrix
                        gower_dist = gower.gower_matrix(df)

                        # Perform KMeans clustering
                        kmeans = KMeans(n_clusters=k, random_state=0)

                        # Fit the model on the Gower distance matrix
                        kmeans.fit(gower_dist)

                        # Get cluster labels
                        labels = kmeans.labels_


                        df_with_clusters = df.copy()
                        df_with_clusters['cluster'] = labels

                        print(df_with_clusters)

                    elif choice == '2':
                            # Compute the Gower distance matrix
                            gower_dist = gower.gower_matrix(df)

                            mixed_columns = []
                            for column in df.columns:
                                unique_types = set(type(val) for val in df[column])
                                if len(unique_types) > 1:
                                    mixed_columns.append(column)

                            # Check and convert non-numeric columns
                            label_encoders = {}
                            for column in df.select_dtypes(include=['object', 'float', 'int']).columns:
                                if df[column].dtype == 'object' or column in mixed_columns:
                                    df[column] = df[column].astype(str)  # Convert to string if mixed or object
                                le = LabelEncoder()
                                df[column] = le.fit_transform(df[column])
                                label_encoders[column] = le
                            
                            # Convert dataframe to numpy array
                            X = df.values
                            
                            # Initialize DBSCAN
                            dbscan = DBSCAN(eps=1.5, min_samples=2)
                            
                            # Fit DBSCAN
                            clusters = dbscan.fit_predict(X)
                            print(f"Debug: {clusters}")
                            
                            # Add the cluster labels to the dataframe
                            df['cluster'] = clusters

                            # Get cluster labels
                            labels = dbscan.labels_

                            df_with_clusters = df.copy()
                            df_with_clusters['cluster'] = labels
                            print(df_with_clusters)

                    elif choice == '3':
                        print("Implement SPK-Means algorithm")

                    elif choice == '4':
                        print("Implement AGNES algorithm")

                    elif choice not in [1-4]:
                        print("Invalid choice: Please select a number between 1 - 4")
                        continue
                    break

                while True:
                    print("\nOptions: How would you like to score the clusters?")
                    print("1. Silhouette score")
                    print("2. Davies-Boulding score")                
                    print("3. Calinski Harabasz_score")
                    print("4. Skip scoring the clusters.")

                    choice = input("Enter your choice (1-4): ")

                    if choice == '1':
            # Calculate silhouette score to evaluate the clustering performance using distance matrix

                        sil_score = silhouette_score(gower_dist, labels, metric='precomputed')

                        print(f"Silhouette Score: {sil_score}")

                    elif choice == '2':
                        print()

                    elif choice == '3':
                        print()

                    elif choice == '4':
                        print()

                    elif choice not in [1 -4]:
                        print("Invalid choice: Please select a number between 1 - 4 ")
                        continue
                    break

                while True:
                    print("\nOptions: Would you like to see data about the centroids?")
                    print("Y. Show me the cluster centroids.")
                    print("N. Don't show me the cluster centroids.")
                    
                    choice = input("Enter your choice Y or N: ")
                    
            # Calculate centroid coordinates
                    centroids = kmeans.cluster_centers_

            # Initialize a list to store closest points to centroids
                    closest_points_to_centroids = []

            # Find closest points to each centroid
                    for i, centroid in enumerate(centroids):
            # Calculate distances from each point to the centroid
                        distances_to_centroid = gower_dist[:, i]
            # Find the index of the closest point
                        closest_index = np.argmin(distances_to_centroid)
            # Get the point and its distance
                        closest_point = df.iloc[closest_index]
                        distance_to_centroid = distances_to_centroid[closest_index]
            # Append to list
                        closest_points_to_centroids.append(closest_point)

            # Convert the list of dictionaries to a DataFrame
                    closest_points_to_centroids_df = pd.DataFrame(closest_points_to_centroids)

                    if choice == 'Y':
                        print(closest_points_to_centroids_df)

                    elif choice == 'N':
                        print()

                    elif choice != 'Y' or 'N':
                        print("Invalid choice. Please chose Y or N.")
                        continue
                    break

                while True:
                    print("\nOptions: How would you like to visualize the clusters?")
                    print("2. Show me a 2D rendering of the clusters.")
                    print("3. Show me a 3D rendering of the clusters.")
                    print("S. Skip cluster visualizations.")
                    
                    choice = input("Enter your choice 2, 3, or S: ")
                    
                    if choice == '2':
                        # Visualization with Grower and KMeans clustering

                        # Compute the Gower distance matrix
                        gower_dist = gower.gower_matrix(df)

                        # Perform KMeans clustering
                        kmeans = KMeans(n_clusters=k, random_state=0)
                        kmeans.fit(gower_dist)

                        # Get cluster labels
                        labels = kmeans.labels_

                        # Apply t-SNE for dimensionality reduction
                        tsne = TSNE(n_components=2, random_state=0)
                        X_tsne = tsne.fit_transform(gower_dist)

                        # Visualize clusters
                        plt.figure(figsize=(8, 6))
                        for i in range(k):
                            plt.scatter(X_tsne[labels == i, 0], X_tsne[labels == i, 1], label=f'Cluster {i}')
                        plt.title('t-SNE Visualization of Clusters')
                        plt.xlabel('t-SNE Component 1')
                        plt.ylabel('t-SNE Component 2')
                        plt.legend()
                        plt.show()

                    elif choice == '3':
            # Compute the Gower distance matrix
                        gower_dist = gower.gower_matrix(df)

            # Perform KMeans clustering
                        kmeans = KMeans(n_clusters=k, random_state=0)
                        kmeans.fit(gower_dist)

            # Get cluster labels
                        labels = kmeans.labels_

            # Apply t-SNE for dimensionality reduction
                        tsne = TSNE(n_components=3, random_state=0)
                        X_tsne = tsne.fit_transform(gower_dist)

            # Normalize the points to project them onto a unit sphere
                        norms = np.linalg.norm(X_tsne, axis=1)
                        X_sphere = X_tsne / norms[:, np.newaxis]

            # Compute the centroids for each cluster in the t-SNE space
                        centroids = np.array([X_tsne[labels == i].mean(axis=0) for i in range(k)])
            # Normalize the centroids to project them onto the hypersphere
                        centroid_norms = np.linalg.norm(centroids, axis=1)
                        centroids_sphere = centroids / centroid_norms[:, np.newaxis]

            # Create wireframe for the outline of the sphere
                        phi = np.linspace(0, np.pi, 50)
                        theta = np.linspace(0, 2 * np.pi, 50)
                        phi, theta = np.meshgrid(phi, theta)
                        x = np.sin(phi) * np.cos(theta)
                        y = np.sin(phi) * np.sin(theta)
                        z = np.cos(phi)

            # Create traces for horizontal lines
                        horizontal_lines = []
                        for i in range(len(phi)):
                            horizontal_lines.append(go.Scatter3d(
                                x=x[i],
                                y=y[i],
                                z=z[i],
                                mode='lines',
                                line=dict(color='gray', width=0.4),
                                opacity=1,
                                showlegend=False
                            ))

            # Create traces for vertical lines
                        vertical_lines = []
                        for i in range(len(theta)):
                            vertical_lines.append(go.Scatter3d(
                                x=x[:, i],
                                y=y[:, i],
                                z=z[:, i],
                                mode='lines',
                                line=dict(color='gray', width=0.4),
                                opacity=1,
                                showlegend=False
                            ))

            # Create 3D scatter plot with Plotly
                        trace = []
                        for i in range(k):
                            trace.append(go.Scatter3d(
                                x=X_sphere[labels == i, 0],
                                y=X_sphere[labels == i, 1],
                                z=X_sphere[labels == i, 2],
                                mode='markers',
                                marker=dict(size=5),
                                name=f'Cluster {i}'
                            ))

            # Add cluster centroid indicators
                        centroid_trace = go.Scatter3d(
                            x=centroids_sphere[:, 0],
                            y=centroids_sphere[:, 1],
                            z=centroids_sphere[:, 2],
                            mode='markers',
                            marker=dict(size=8, color='yellow', ),
                            name='Cluster Centroids'
                        )

                        layout = go.Layout(
                            title='3D t-SNE Visualization of Clusters on a Hypersphere with Sphere Outline',
                            scene=dict(
                                xaxis_title='t-SNE Component 1',
                                yaxis_title='t-SNE Component 2',
                                zaxis_title='t-SNE Component 3',
                            )
                        )

            # Combine the wireframe outline, scatter plot, and cluster centroids
                        fig = go.Figure(data=trace + horizontal_lines + vertical_lines + [centroid_trace], layout=layout)
                        fig.show()
                        
                    elif choice == 'S':
                        print("Skipping this step...")
                        print()
                            
                    elif choice not in [2, 3, 'S']:
                        print("Invalid choice. Please chose 2, 3 or S.")
                        continue
                    break

                while True:
                    print("\nOptions: Do you want to view cluster analysis?")
                    print("Y. Yes, I want to see cluster analysis information")
                    print("N. No, I do not want to see cluster analysis information")

                    choice = input("Enter your choice Y or N: ")
                    if choice == 'Y':

#                        df.fillna(value='None', inplace=True)

            #Applying the optimal k value to perform k-means clustering (Filtered)

            # Compute the Gower distance matrix
                        gower_dist = gower.gower_matrix(df)

            # Perform KMeans clustering
            # Number of clusters (k) - choose appropriate value
                        #k = 
                        kmeans = KMeans(n_clusters=k, random_state=0)

            # Fit the model on the Gower distance matrix
                        kmeans.fit(gower_dist)

            # Get cluster labels
                        labels = kmeans.labels_


                        df_with_clusters = df.copy()
                        df_with_clusters['cluster'] = labels

                        pd.set_option('display.max_rows', None)
                        print(df_with_clusters)
                            
                        cluster_0 = df_with_clusters[df_with_clusters['cluster'] == 0].copy()
                        cluster_1 = df_with_clusters[df_with_clusters['cluster'] == 1].copy()
                        cluster_2 = df_with_clusters[df_with_clusters['cluster'] == 2].copy()
                        cluster_3 = df_with_clusters[df_with_clusters['cluster'] == 3].copy()
                        cluster_4 = df_with_clusters[df_with_clusters['cluster'] == 4].copy()
                        cluster_5 = df_with_clusters[df_with_clusters['cluster'] == 5].copy()
                        cluster_6 = df_with_clusters[df_with_clusters['cluster'] == 6].copy()
                        cluster_7 = df_with_clusters[df_with_clusters['cluster'] == 7].copy()
                        cluster_8 = df_with_clusters[df_with_clusters['cluster'] == 8].copy()
                        cluster_9 = df_with_clusters[df_with_clusters['cluster'] == 9].copy()

                        while True:
                            print("\nOptions: Which cluster would you like to analyze?")
                    
                            unique_clusters = df_with_clusters['cluster'].unique()
                            #choice = input("Enter your choice (")(df_with_clusters['cluster'].unique())"())")
                            choice = input(f"Enter your choice ({unique_clusters}): ")

                            if choice == '0':
                                cluster_choice = cluster_0
                            elif choice == '1':
                                cluster_choice = cluster_1
                            elif choice == '2':
                                cluster_choice = cluster_2
                            elif choice == '3':
                                cluster_choice = cluster_3
                            elif choice == '4':
                                cluster_choice = cluster_4
                            elif choice == '5':
                                cluster_choice = cluster_5
                            elif choice == '6':
                                cluster_choice = cluster_6
                            elif choice == '7':
                                cluster_choice = cluster_7
                            elif choice == '8':
                                cluster_choice = cluster_8
                            elif choice == '9':
                                cluster_choice = cluster_9
                            elif choice not in [{unique_clusters}]: # Will this work?
                                print("Invalid choice. Please select a number between ({unique_clusters})")
                                continue
                            break
                        while True:
                            print ("\nOptions:")
                            print("1. Display unique values for cluster")
                            print("2. Display unique values count for cluster")
                            print("3. Display cluster information for mission state column")
                            print("4. Display cluster information for mode switch column")
                            print("5. Display cluster information for throttle column")
                            print("6. Display cluster information for max deviation column")
                            print("7. Display cluster information for max altitude column")
                            print("8. Display cluster information for duration column")
                            print("9. Change cluster choice")
                            print("10. Exit back to main menu")

                            choice = input("Enter your choice (1 - 10): ")

            # Define choices for data set analysis
                            if choice == '1':
                                if not cluster_df_display_unique_values():
                                    print()
                            elif choice == '2':
                                if not cluster_df_display_unique_values_count():
                                    print()
                            elif choice == '3':
                                if not cluster_df_msn_state(cluster_choice):
                                    print()
                            elif choice == '4':
                                if not cluster_df_mode_switch():
                                    print()
                            elif choice == '5':
                                if not cluster_df_throttle():
                                    print()
                            elif choice == '6':
                                if not cluster_df_max_deviation():
                                    print()
                            elif choice == '7':
                                if not cluster_df_max_altitude():
                                    print()
                            elif choice == '8':
                                if not cluster_df_duration():
                                    print()
                            elif choice == '9':
                                while True:
                                    print("\nOptions: Which cluster would you like to analyze?")
                            
                                    unique_clusters = df_with_clusters['cluster'].unique()
                                    #choice = input("Enter your choice (")(df_with_clusters['cluster'].unique())"())")
                                    choice = input(f"Enter your choice ({unique_clusters}): ")

                                    if choice == '0':
                                        cluster_choice = cluster_0
                                    elif choice == '1':
                                        cluster_choice = cluster_1
                                    elif choice == '2':
                                        cluster_choice = cluster_2
                                    elif choice == '3':
                                        cluster_choice = cluster_3
                                    elif choice == '4':
                                        cluster_choice = cluster_4
                                    elif choice == '5':
                                        cluster_choice = cluster_5
                                    elif choice == '6':
                                        cluster_choice = cluster_6
                                    elif choice == '7':
                                        cluster_choice = cluster_7
                                    elif choice == '8':
                                        cluster_choice = cluster_8
                                    elif choice == '9':
                                        cluster_choice = cluster_9
                                    elif choice not in [{unique_clusters}]: # Will this work?
                                        print("Invalid choice. Please select a number between ({unique_clusters})")
                                        continue
                                    break
                            elif choice == '10':
                                print("Back to main menu...")
                                break
                            else:
                                print("Invalid choice. Please try again by entering 1 through 10.")

                    elif choice == 'N':
                        print("You chose to skip clustering analysis.")
                    elif choice != 'Y' or 'N':
                        print("Invalid choice. Please select Y or N.")
                        continue
                    break

                # while True:
                #     print("\nOptions: Do you want to start clustering over from the beginning?")
                #     print("Y. Yes, I want to start clustering over from the beginning")
                #     print("N. No, I want to exit the program")

                    
                #     choice = input("Please enter only Y or N to make your choice: ")
                #     if choice == 'Y':
                #         print("Returning to start clustering over from the beginning ")
                #     elif choice == 'N':
                #         print("Back to main menu...")
                #         break
                # # break (Use this in place of the last break and delete last elif?)
                #     elif choice != 'Y' or 'N':
                #         print("Invalid choice. Please chose Y or N")
                #         continue
                #     break
                break
        
        elif choice == 'Q':
            print("Exiting program...")
            break
        elif choice not in ['A', 'B', 'Q']:
            print("Invalid choice. Please try again by entering A, B, or Q.")
            

if __name__ == "__main__":
    main()