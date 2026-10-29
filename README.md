# module-3
# Obesity Dataset Visualization (Matplotlib and Seaborn)

A Python script that visualises a public dataset on eating habits, physical condition and obesity levels. It produces five plots: a line plot, a scatter plot, a histogram and two box plots.

## Dataset

1. File:ObesityDataSet_raw_and_data_sinthetic.csv
2. Size:2,111 rows and 17 columns, with no missing values
3. Created by me:a BMI column, calculated in the script as weight divided by height squared. It is not in the original CSV, and the CSV file itself is not changed.


## Plots

1.  Line plot: Average weight at each age 
2.  Scatter plot: Height against weight, coloured by gender 
3.  Histogram: Age distribution of participants 
4.  Box plot: Weight by main mode of transport 
5.  Box plot: BMI at each obesity level 


## Findings

1. Average weight by age: weight climbs to a peak of about 105 kg around ages 26 to 31, then settles between roughly 80 and 90 kg. The line gets jumpy after about age 48 because there are very few older participants.
2. Height vs weight: taller participants tend to weigh more. The correlation I calculated earlier is about 0.46, which is moderate. Female participants reach the highest weights at a given height, while male participants reach the greatest heights.
3. Age distribution:most participants are in their early 20s, with a peak at about age 21 to 23. The distribution tails off to the right, which is why the mean age is higher than the median.
4. Weight by transport: public transportation has the highest median weight (about 85 kg) and by far the widest spread. Walking, motorbike and bike have lower medians.
5. BMI by obesity level: BMI rises steadily from insufficient weight (about 17.5) to obesity type III (about 42), with very little overlap between levels. This is expected, because the levels are defined by BMI ranges.

## Requirements

Python 
pandas, matplotlib and seaborn:
 

## How to run

1. Put the obesity dataset in the same folder as module3.py.
2. Open a terminal and go to that folder:
"cd Desktop\internship"
3. Run the script:
  "python module3.py"
4. Five plot windows open one after another. Close each one to see the next.

## How it works

The script loads the CSV with pandas and adds a BMI column calculated from weight and height.
Each plot is made by its own function, and the functions are called in order at the bottom of the file.
Every figure uses the same colour and size, and is saved as an image before it is shown.

## Project video links



