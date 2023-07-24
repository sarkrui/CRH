from PIL import Image
import pytesseract
import pandas as pd

# Load the image from the file
img = Image.open('data.jpg')  # Replace with your local file path

# Use pytesseract to do OCR on the image
text = pytesseract.image_to_string(img)

# Clean the text and split it into lines
lines = text.split('\n')
lines = [line for line in lines if line.strip() != '']

# Create a dataframe
df = pd.DataFrame(lines, columns=['Data'])

# Split the 'Data' column into 'Code' and 'Start' based on the space
df[['Code', 'Start']] = df['Data'].str.split(' ', expand=True)

# Create an 'End' column by shifting the 'Start' column up by one
df['End'] = df['Start'].shift(-1)

# Remove the last row as it doesn't have an 'End' time
df = df[:-1]

# Remove the rows where 'Code' is NaN (these are the rows where 'Start' was NaN in the previous step)
df = df[df['Code'].str.startswith('G')]

# Save the dataframe to a CSV file
df.to_csv('table.csv', index=False)  # Replace with your preferred local file path