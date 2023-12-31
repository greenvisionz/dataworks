# Create the years and durations lists
years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]

# Create a dictionary with the two lists
movie_dict = { 'years': years, 'durations': durations }

# Import pandas under its usual alias 
import pandas as pd 

# Create a DataFrame from the dictionary 
durations_df = pd.DataFrame(movie_dict)

# Import a matplotlib.pyplot under its usual alias and create a figure
import matplotlib.pyplot as plt 
fig = plt.figure()

# Draw a line plot of release_years and durations
plt.plot(durations_df['years'], durations_df['durations'])

# Create a title
plt.title("Netflix Movie Durations 2011-2020")


# Read in the CSV as a DataFrame
netflix_df = pd.read_csv("C:/netflix_data.csv")


# Show the plot
plt.show()

# Print the dictionary 
print(movie_dict) 

#Print the DataFrame 
print(durations_df) 









