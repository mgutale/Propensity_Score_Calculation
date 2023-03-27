import pandas as pd

def calculate_propensity_index(df, activity_col):
    # Group the data by Mosaic_profile and Activity
    grouped_data = df.groupby(['Mosaic_profile', activity_col])

    # Calculate the count of each Activity for each Mosaic_profile
    activity_counts = grouped_data.size().unstack(fill_value=0)

    # Calculate the total count of each Mosaic_profile
    total_counts = df['Mosaic_profile'].value_counts()

    # Calculate the propensity index for each Mosaic_profile and Activity
    propensity_index = activity_counts.div(total_counts, axis=0)

    # Find the most preferred and least preferred Activity for each Mosaic_profile
    most_preferred = propensity_index.apply(lambda x: x.sort_values(ascending=False).index.to_list(), axis=1)
    least_preferred = propensity_index.apply(lambda x: x.sort_values().index.to_list(), axis=1)

    # Create a DataFrame with the results
    results_df = pd.DataFrame({
        'Mosaic_profile': propensity_index.index,
        'Propensity Index': propensity_index.values.tolist(),
        'Most Preferred Activities': most_preferred,
        'Least Preferred Activities': least_preferred
    })

    return results_df


if __name__ == '__main__':
    # Read the data from CSV file
    df = pd.read_csv('datasets/dataset.csv')

    # Calculate the propensity index for each activity
    activity_propensity_index = calculate_propensity_index(df, 'Activity')

    # Write the results to a CSV file
    activity_propensity_index.to_csv('datasets/activity_output.csv', index=False)

    # Print the results
    print(activity_propensity_index)
