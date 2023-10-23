#@title Cars Listings by Brand
import pandas as pd              # Importing pandas library for data manipulation 
import matplotlib.pyplot as plt  # Importing matplotlib library for plotting 
import seaborn as sns            # Importing seaborn library for plotting 

# Read data from a local CSV file
df = pd.read_csv('bar_chart_data.csv')

# Basic settings and dimensions for the plot
fig = plt.figure(figsize=(12, 9), facecolor='lavender')  # Setting the figure size & background to lightgrey

# Set background and axis facecolors
sns.set(rc={'axes.facecolor':'green', 'figure.facecolor':'tan'})  # Setting the axis background to tan

# Font and size settings for the whole plot ["white", "dark", "whitegrid", "darkgrid", "ticks"]
sns.set_context("talk")    # ["paper", "notebook", "talk", "poster"]
sns.set_style("whitegrid", {
    "font.family": "serif",
    "font.serif": ["Times", "Palatino", "serif"]
})

# Create a barchart with individual colors, thicker dark blue edges and hatching
palette = sns.color_palette("husl", len(df))  # More vibrant color palette
ax = sns.barplot(x="Brand", y="Cars Listings", data=df, palette=palette, edgecolor="darkblue", linewidth=2.5)  # Plotting the barchart with dark blue edges 


hatches =  ['/', '\\', '/', '\\', '/', '\\', '/']   # ['/', '\\', '|', '-', '+', 'x', 'o']  List of hatch patterns
for i, bar in enumerate(ax.patches):
    bar.set_hatch(hatches[i % len(hatches)])  # Apply different hatch patterns in a loop


# Axis labels with red color, bold, and underline
ax.set(xlabel='', ylabel='')  # Setting the axis labels to empty strings 
ax.set_title('▪️ Cars Listings by Brand [v.2.0]', fontweight='bold')  # Setting the plot title with bold font 
xlabel = ax.set_xlabel('Car Brands', color='red', fontweight='bold', fontsize=14)  # Setting the x axis label with red color and bold font 
ylabel = ax.set_ylabel('Number of Listings', color='red', fontweight='bold', fontsize=14)  #  Setting the y axis label with red color and bold font

# Moving the xlabel a little lower
ax.xaxis.set_label_coords(0.5, -0.3)  # The numbers are in axis coordinate, so 0.5 is the center, -0.3 is a bit lower than the default
# Moving the ylabel a little to the left
ax.yaxis.set_label_coords(-0.1, 0.5)  # -0.1 is a bit to the left from the default center at 0.5

# Setting the x and y axis labels with dark blue edges and thicker bounding box
xlabel = ax.xaxis.get_label()
xlabel.set_bbox(dict(facecolor='white', edgecolor='darkblue', boxstyle='round,pad=0.5', lw=2))  # Setting the x axis label with dark blue edges and thick bounding box 
ylabel = ax.yaxis.get_label()
ylabel.set_bbox(dict(facecolor='white', edgecolor='darkblue', boxstyle='round,pad=0.5', lw=2))  # Setting the y axis label with dark blue edges and thick bounding box 


# Making all text bold
for label in ax.get_xticklabels() + ax.get_yticklabels(): # Looping through all labels  
    label.set_weight("bold")    # Making all text bold
    label.set_color("darkblue") # Making all text dark blue

# Values above bars
for i, val in enumerate(df["Cars Listings"].values):
    # Adjust the position to be higher above the bar
    # ax.text(i, val + 30, str(val), color='darkblue', ha='center', weight='bold')
    # Add a rounded rectangle around the text
    bbox_props = dict(boxstyle="round, pad=0.3", fc="white", ec="darkblue", lw=2)
    ax.text(i, val + 30, str(val), color='darkblue', ha='center', weight='bold', bbox=bbox_props, fontsize=10)

# Rotate x-axis labels to 45 degrees
# ax.set_xticklabels(ax.get_xticklabels(), rotation=45, weight='bold')
ax.set_xticklabels(df["Brand"], rotation=60, weight='bold')

# Rotate y-axis labels to 60 degrees
ax.set_yticks(ax.get_yticks())
ax.set_yticklabels(ax.get_yticklabels(), rotation=60, weight='bold')

# Legend with car names
car_names = df["Brand"].tolist()  # List of car names 
legend_labels = [plt.Rectangle((0,0),1,1,fc=color, edgecolor = "none") for color in palette]  # List of legend labels 
l = plt.legend(legend_labels, car_names, loc='upper right', ncol = 2, prop={'size':12}, bbox_to_anchor=(0.83, 0.97), fancybox=True, shadow=True)  # Creating the legend 
l.set_title('Car Brands', prop={'size': 14, 'weight': 'bold'})  # Setting the title of the legend 

# Save the plot to a file while ensuring that no text is cut off
plt.tight_layout()  # Making sure that no text is cut off 
plt.savefig("chart1_final.png", facecolor=fig.get_facecolor())  # Saving the figure to a PNG file with a white background 

# Show the plot
plt.show()
