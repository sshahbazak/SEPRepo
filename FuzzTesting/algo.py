import numpy as np
import pandas as pd
import random
from sklearn.datasets import make_classification
import modelTrain as mt
import FuzzTest as ft

# from Fuzz import FuzzTestor

# Generate a synthetic dataset (replace this with your real dataset)
X, y = make_classification(n_samples=100, n_features=10, random_state=42)
data = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(10)])
data['target'] = y

# Parameters
# population_size = 50
num_generations = 10
# mutation_rate = 0.01
data_file = 'sample.csv'
num_parents = 30
num_mutants = 10

# Example feature dictionary
# Each key is a feature, and each value is a list of possible values or a range tuple
feature_dict = {
    'modes' : ['POSCTL','STABILIZED', 'OFFBOARD', 'ALTCTL', 'AUTO.LOITER', 'AUTO.RTL', 'AUTO.LAND'],
    'states' : ['Flying', 'Land', 'Disarm', 'Takeoff', 'Arm', 'Hover'],
    'GFACT' : [None, "Warning", "Hold mode", "Return mode", "Terminate", "Land mode"],
    'throttle' : [0, 225, -100, 260, 600, 100, 550, 445, 435, 450, 615, 570, 300, None]
}


# Initialize population
population = pd.read_csv(data_file)

# Fitness function (example: sum of features)
def fitness_function(chromosome):
    return get_anomaly_score(chromosome)  # Excluding the target

# Selection function: Tournament selection
def select_parents(parent_candidates_df, num_parents):
    print('[Genetic Algorithm] Selecting Parents for crossovers')
    
    parents_df = pd.DataFrame()
    
    for _ in range(num_parents):
        # Randomly select individuals for the tournament
        tournament = parent_candidates_df.sample(n=3)
        # Select the individual with the lowest anomaly score
        winner = tournament.loc[tournament['anomaly_score'].idxmin()]
        parents_df =  pd.concat([parents_df, winner.to_frame().transpose()], ignore_index=True)
        
    return parents_df[['states', 'GF', 'GFPRED', 'GFACT', 'modes', 'throttle']]


# Crossover function: Single-point crossover
def crossover(parent1, parent2, column_names):
    parent1 = np.array(parent1)
    parent2 = np.array(parent2)
    
    # Define the index range for 'GF', 'GFPRED', and 'GFACT' columns
    gf_indices = [column_names.index(col) for col in ['GF', 'GFPRED', 'GFACT']]
    
    # Define the crossover point
    crossover_point = random.randint(1, len(parent1) - 2)
    
    # Perform crossover
    child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
    child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
    
    # Ensure 'GF', 'GFPRED', and 'GFACT' are treated as a single column during swapping
    child1[gf_indices] = parent1[gf_indices]
    child2[gf_indices] = parent2[gf_indices]
    
    return child1, child2


def mutate(mutant_candidates_df):
    # Randomly sample 10 rows from mutant_candidates_df
    sample_indices = random.sample(range(len(mutant_candidates_df)), min(10, len(mutant_candidates_df)))
    sampled_df = mutant_candidates_df.iloc[sample_indices].copy()

    # Iterate over each sampled row
    for index, row in sampled_df.iterrows():
        #  Get the list of columns excluding 'modes'
        columns_excluding_modes = [col for col in mutant_candidates_df.columns if col != 'modes']

        # Randomly select a column from the filtered list   
        column_to_mutate = random.choice(columns_excluding_modes)
        # print(column_to_mutate)
        sampled_df.at[index, 'modes'] = random.choice(feature_dict['modes'])
        if column_to_mutate == 'GF':
            # Mutate GF, GFPRED, and GFACT specifically
            sampled_df.at[index, 'GF'] = random.choice(['Yes', 'No'])
            if sampled_df.at[index, 'GF'] == 'No':
                sampled_df.at[index, 'GFPRED'] = None
                sampled_df.at[index, 'GFACT'] = None
            else:
                sampled_df.at[index, 'GFPRED'] = random.choice(['Yes', 'No'])
                sampled_df.at[index, 'GFACT'] = random.choice(feature_dict['GFACT'])
        # Mutate other columns based on their dictionary of eligible values
        # elif column_to_mutate == 'modes':
            
        elif column_to_mutate == 'states':
            sampled_df.at[index, 'states'] = random.choice(feature_dict['states'])
        elif column_to_mutate == 'throttle':
            sampled_df.at[index, 'throttle'] = random.choice(feature_dict['throttle'])
        elif column_to_mutate == 'GFPRED':
            # Mutate GFPRED based on the value of GF
            if sampled_df.at[index, 'GF'] == 'Yes':
                sampled_df.at[index, 'GFPRED'] = random.choice(['Yes', 'No'])
            else:
                sampled_df.at[index, 'GFPRED'] = None
        elif column_to_mutate == 'GFACT':
            # Mutate GFPRED based on the value of GF
            if sampled_df.at[index, 'GF'] == 'Yes':
                sampled_df.at[index, 'GFACT'] = random.choice(feature_dict['GFACT'])
            else:
                sampled_df.at[index, 'GFACT'] = None
    return sampled_df

def run_probe(df):
    results = []
    for _, row in df.iterrows():
        fuzz_test_args = {'drone_id': 'Polkadot'}

        # Dynamically add arguments if they are not None
        # if not pd.isna(row['modes']):
        #     print(row['modes'])
        fuzz_test_args['modes'] = [row['modes']]
        if pd.isna(row['states']):
            fuzz_test_args['states'] = [row['states']]
        if pd.isna(row['GFACT']):
            fuzz_test_args['GFACT'] = [row['GFACT']]
        if pd.isna(row['throttle']):
            fuzz_test_args['throttle'] = [row['throttle']]

        print(fuzz_test_args)
        # Call the Fuzz_Test function with the unpacked dictionary
    #     result = ft.Fuzz_Test(**fuzz_test_args)
    #     results.append(result)
    
    # return results

# Genetic Algorithm
for generation in range(num_generations):
    model_instance = mt.Model()
    df = model_instance.train_model('sample.csv')
    # fitness_scores = [fitness_function(chromosome) for chromosome in population]

    # Eliteness
    # elite_df = df[df['anomaly'] == -1]


    normal_data = df[df['anomaly'] == 1]

    # Calculate the median anomaly score
    median_score = normal_data['anomaly_score'].median()

    column_names = ['states', 'GF', 'GFPRED', 'GFACT', 'modes', 'throttle']

    # Splitting dataframe into parent candidates and non-candidates based on median score
    parent_candidates_df = normal_data[normal_data['anomaly_score'] < median_score]
    mutant_candidates_df = normal_data[normal_data['anomaly_score'] >= median_score][column_names]

    # Crossover
    parents = select_parents(parent_candidates_df, num_parents)  # Ensure even number of parents

    print('[Genetic Algorithm] Crossing Over Parents')
      # Adjust column names as needed
    new_population = []
    for i in range(0, len(parents)-1, 2):
        parent1, parent2 = parents.iloc[i], parents.iloc[i + 1]
        child1, child2 = crossover(parent1, parent2, column_names)
        new_population.extend([child1, child2])

    # Convert list of children to DataFrame with headers
    crossover_df = pd.DataFrame(new_population, columns=column_names)

    # Mutation
    print('[Genetic Algorithm] Mutating chromosomes')
    mutated_df = mutate(mutant_candidates_df)

    # Run sim probes on mutated_df and crossover_df
    print('[Genetic Algorithm] Running probes')
    merged_df = pd.concat([crossover_df, mutated_df])
    # print(merged_df)
    results = run_probe(merged_df)
    # print('[Genetic Algorithm] Adding probe results into csv file')
    # # Flatten the list of lists into a single list of dictionaries
    # flattened_data = [item for sublist in results for item in sublist]

    # # Create DataFrame
    # result_df = pd.DataFrame(flattened_data)

    # # Rename DataFrame columns to match CSV columns
    # result_df = result_df.rename(columns={
    #     'mode': 'initial_mode',
    #     'state': 'states',
    #     'KillSwitch': 'kill_switch'
    # })

    # # Ensure the DataFrame columns are in the same order as the CSV file columns
    # result_df = result_df[['initial_mode', 'states', 'throttle', 'GF', 'GFPRED', 'GFACT', 'kill_switch', 'max_deviation', 'max_altitude', 'duration', 'final_landing_state', 'freefall_occurred', 'mission_complete']]

    # # print(result_df)
    # # Read the existing CSV file
    # csv_file_path = 'sample.csv'
    # csv_df = pd.read_csv(csv_file_path)

    # # Append the DataFrame data to the CSV data
    # combined_df = pd.concat([csv_df, result_df], ignore_index=True)
    # combined_df.fillna(value = 'None',inplace=True)
    # # Check for NaN values after filling
    # print("NaN values after filling:")
    # print(combined_df)

    # # Save the combined data back to the CSV file
    # # combined_df.to_csv(csv_file_path, index=False)

    # print("Data appended and saved to CSV file successfully.")

    
    
# print(results)

    # Add the sim results to the csv. 




#     # Update population
#     population = new_population

#     # Logging progress
#     best_fitness = max(fitness_scores)
#     print(f'Generation {generation + 1}, Best Fitness: {best_fitness}')

# # Final population
# final_fitness_scores = [fitness_function(chromosome) for chromosome in population]

# best_individual = population[np.argmax(final_fitness_scores)]
# print('Best Individual:', best_individual)
# print('Best Fitness Score:', max(final_fitness_scores))

# fuzz_test = Fuzz_Test(drone_id="Polkadot",
# modes=['POSCTL', 'OFFBOARD', 'STABILIZED'],
# states = ['BriarHover'],
# throttle=[2, 3]
# )
