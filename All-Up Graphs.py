# 1 - Histograms

# 1a Histogram over all data - commercial success and critical acclaim - same as 2a2

import pandas as pd
import matplotlib.pyplot as plt
from statistics import mode

# Load the data from the uploaded files
file_paths = [
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Year-End Charts Number Ones.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Best-Selling Albums.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Best-Selling Singles.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Artists.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Producers.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Songwriters.csv'
]

age_columns = ['Artist Age', 'Artist Age', 'Artist Age', 'Artist Age', 'Producer Age', 'Songwriter Age']
all_ages = []

# Combine data from relevant columns into one list
for file_path, age_column in zip(file_paths, age_columns * 2):
    df = pd.read_csv(file_path)
    if age_column in df.columns:
        all_ages.extend(pd.to_numeric(df[age_column], errors='coerce').dropna().tolist())

# Create a Series for processing
all_ages_series = pd.Series(all_ages)

# Calculate statistics
mean_age = all_ages_series.mean()
median_age = all_ages_series.median()
try:
    mode_age = mode(all_ages_series)
except:
    mode_age = 'N/A'
stdev_age = all_ages_series.std()
variance_age = all_ages_series.var()
min_age = all_ages_series.min()
max_age = all_ages_series.max()
range_age = max_age - min_age

# Plot histogram
plt.figure(figsize=(10, 6))
counts, bins, patches = plt.hist(all_ages_series, bins=range(int(min_age), int(max_age) + 2, 5),
                                 color='#1f77b4', edgecolor='black', alpha=0.7)

# Annotate counts and percentages
total = len(all_ages_series)
for count, bin_start, bin_end in zip(counts, bins[:-1], bins[1:]):
    percentage = (count / total) * 100
    plt.text((bin_start + bin_end) / 2, count + 1, f'{int(count)}\n({percentage:.1f}%)',
             ha='center', va='bottom', fontsize=9, color='black')
    plt.text((bin_start + bin_end) / 2, -5, f'{int(bin_start)}-{int(bin_end)}',
             ha='center', va='top', fontsize=9, color='darkblue', rotation=45)

# Add vertical lines for statistics
plt.axvline(mean_age, color='red', linestyle='--', linewidth=1.5, label=f'Mean: {mean_age:.2f}')
plt.axvline(median_age, color='green', linestyle='-', linewidth=1.5, label=f'Median: {median_age}')
if mode_age != 'N/A':
    plt.axvline(mode_age, color='blue', linestyle='-', linewidth=1.5, label=f'Mode: {mode_age}')
plt.axvline(mean_age + stdev_age, color='orange', linestyle=':', linewidth=1.5, label=f'Stdev: {stdev_age:.2f}')
plt.axvline(mean_age - stdev_age, color='orange', linestyle=':', linewidth=1.5)

# Add a vertical line for the 30-year-old mark
plt.axvline(30, color='gray', linestyle='-.', linewidth=1.5, label='30-Year-Old Mark')

# Add statistics box
stats_text = (
    f"Variance: {variance_age:.2f}\n"
    f"Standard Deviation: {stdev_age:.2f}\n"
    f"Range: {range_age}\n"
    f"Min Age: {min_age}\n"
    f"Max Age: {max_age}"
)
plt.text(0.98, 0.95, stats_text, ha='right', va='top', transform=plt.gca().transAxes,
         bbox=dict(facecolor='white', alpha=0.7))

# Adjust legend position
plt.legend(loc='upper left')

# Add labels, title, and grid
plt.title('Histogram of Age Distributions - All Data')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75, linestyle='--')
plt.grid(axis='x', alpha=0.75, linestyle='--')
plt.tight_layout()

# Display the plot
plt.show()


# 1b Histogram over artists only (excl. producers and songwriters) - commercial success and critical acclaim - same as 2b2

import pandas as pd
import matplotlib.pyplot as plt
from statistics import mode

# Load the data from the uploaded files
file_paths = [
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Year-End Charts Number Ones.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Best-Selling Albums.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Best-Selling Singles.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Artists.csv'    
]

age_columns = ['Artist Age', 'Artist Age', 'Artist Age', 'Artist Age']
all_ages = []

# Combine data from relevant columns into one list
for file_path, age_column in zip(file_paths, age_columns * 2):
    df = pd.read_csv(file_path)
    if age_column in df.columns:
        all_ages.extend(pd.to_numeric(df[age_column], errors='coerce').dropna().tolist())

# Create a Series for processing
all_ages_series = pd.Series(all_ages)

# Calculate statistics
mean_age = all_ages_series.mean()
median_age = all_ages_series.median()
try:
    mode_age = mode(all_ages_series)
except:
    mode_age = 'N/A'
stdev_age = all_ages_series.std()
variance_age = all_ages_series.var()
min_age = all_ages_series.min()
max_age = all_ages_series.max()
range_age = max_age - min_age

# Plot histogram
plt.figure(figsize=(10, 6))
counts, bins, patches = plt.hist(all_ages_series, bins=range(int(min_age), int(max_age) + 2, 5),
                                 color='#1f77b4', edgecolor='black', alpha=0.7)

# Annotate counts and percentages
total = len(all_ages_series)
for count, bin_start, bin_end in zip(counts, bins[:-1], bins[1:]):
    percentage = (count / total) * 100
    plt.text((bin_start + bin_end) / 2, count + 1, f'{int(count)}\n({percentage:.1f}%)',
             ha='center', va='bottom', fontsize=9, color='black')
    plt.text((bin_start + bin_end) / 2, -5, f'{int(bin_start)}-{int(bin_end)}',
             ha='center', va='top', fontsize=9, color='darkblue', rotation=45)

# Add vertical lines for statistics
plt.axvline(mean_age, color='red', linestyle='--', linewidth=1.5, label=f'Mean: {mean_age:.2f}')
plt.axvline(median_age, color='green', linestyle='-', linewidth=1.5, label=f'Median: {median_age}')
if mode_age != 'N/A':
    plt.axvline(mode_age, color='blue', linestyle='-', linewidth=1.5, label=f'Mode: {mode_age}')
plt.axvline(mean_age + stdev_age, color='orange', linestyle=':', linewidth=1.5, label=f'Stdev: {stdev_age:.2f}')
plt.axvline(mean_age - stdev_age, color='orange', linestyle=':', linewidth=1.5)

# Add a vertical line for the 30-year-old mark
plt.axvline(30, color='gray', linestyle='-.', linewidth=1.5, label='30-Year-Old Mark')

# Add statistics box
stats_text = (
    f"Variance: {variance_age:.2f}\n"
    f"Standard Deviation: {stdev_age:.2f}\n"
    f"Range: {range_age}\n"
    f"Min Age: {min_age}\n"
    f"Max Age: {max_age}"
)
plt.text(0.98, 0.95, stats_text, ha='right', va='top', transform=plt.gca().transAxes,
         bbox=dict(facecolor='white', alpha=0.7))

# Adjust legend position
plt.legend(loc='upper left')

# Add labels, title, and grid
plt.title('Histogram of Age Distributions - Artists Only')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75, linestyle='--')
plt.grid(axis='x', alpha=0.75, linestyle='--')
plt.tight_layout()

# Display the plot
plt.show()


# 1c Histogram - commercial success only - same as 2c2

import pandas as pd
import matplotlib.pyplot as plt
from statistics import mode

# Load the data from the uploaded files
file_paths = [
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Year-End Charts Number Ones.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Best-Selling Albums.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Best-Selling Singles.csv'    
]

age_columns = ['Artist Age', 'Artist Age', 'Artist Age']
all_ages = []

# Combine data from relevant columns into one list
for file_path, age_column in zip(file_paths, age_columns * 2):
    df = pd.read_csv(file_path)
    if age_column in df.columns:
        all_ages.extend(pd.to_numeric(df[age_column], errors='coerce').dropna().tolist())

# Create a Series for processing
all_ages_series = pd.Series(all_ages)

# Calculate statistics
mean_age = all_ages_series.mean()
median_age = all_ages_series.median()
try:
    mode_age = mode(all_ages_series)
except:
    mode_age = 'N/A'
stdev_age = all_ages_series.std()
variance_age = all_ages_series.var()
min_age = all_ages_series.min()
max_age = all_ages_series.max()
range_age = max_age - min_age

# Plot histogram
plt.figure(figsize=(10, 6))
counts, bins, patches = plt.hist(all_ages_series, bins=range(int(min_age), int(max_age) + 2, 5),
                                 color='#1f77b4', edgecolor='black', alpha=0.7)

# Annotate counts and percentages
total = len(all_ages_series)
for count, bin_start, bin_end in zip(counts, bins[:-1], bins[1:]):
    percentage = (count / total) * 100
    plt.text((bin_start + bin_end) / 2, count + 1, f'{int(count)}\n({percentage:.1f}%)',
             ha='center', va='bottom', fontsize=9, color='black')
    plt.text((bin_start + bin_end) / 2, -5, f'{int(bin_start)}-{int(bin_end)}',
             ha='center', va='top', fontsize=9, color='darkblue', rotation=45)

# Add vertical lines for statistics
plt.axvline(mean_age, color='red', linestyle='--', linewidth=1.5, label=f'Mean: {mean_age:.2f}')
plt.axvline(median_age, color='green', linestyle='-', linewidth=1.5, label=f'Median: {median_age}')
if mode_age != 'N/A':
    plt.axvline(mode_age, color='blue', linestyle='-', linewidth=1.5, label=f'Mode: {mode_age}')
plt.axvline(mean_age + stdev_age, color='orange', linestyle=':', linewidth=1.5, label=f'Stdev: {stdev_age:.2f}')
plt.axvline(mean_age - stdev_age, color='orange', linestyle=':', linewidth=1.5)

# Add a vertical line for the 30-year-old mark
plt.axvline(30, color='gray', linestyle='-.', linewidth=1.5, label='30-Year-Old Mark')

# Add statistics box
stats_text = (
    f"Variance: {variance_age:.2f}\n"
    f"Standard Deviation: {stdev_age:.2f}\n"
    f"Range: {range_age}\n"
    f"Min Age: {min_age}\n"
    f"Max Age: {max_age}"
)
plt.text(0.98, 0.95, stats_text, ha='right', va='top', transform=plt.gca().transAxes,
         bbox=dict(facecolor='white', alpha=0.7))

# Adjust legend position
plt.legend(loc='upper left')

# Add labels, title, and grid
plt.title('Histogram of Age Distributions - Commercial Success Only')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75, linestyle='--')
plt.grid(axis='x', alpha=0.75, linestyle='--')
plt.tight_layout()

# Display the plot
plt.show()


# 1d Histogram - critical acclaim only - same as 2d2

import pandas as pd
import matplotlib.pyplot as plt
from statistics import mode

# Load the data from the uploaded files
file_paths = [    
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Artists.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Producers.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Songwriters.csv'
]

age_columns = ['Artist Age', 'Producer Age', 'Songwriter Age']
all_ages = []

# Combine data from relevant columns into one list
for file_path, age_column in zip(file_paths, age_columns * 2):
    df = pd.read_csv(file_path)
    if age_column in df.columns:
        all_ages.extend(pd.to_numeric(df[age_column], errors='coerce').dropna().tolist())

# Create a Series for processing
all_ages_series = pd.Series(all_ages)

# Calculate statistics
mean_age = all_ages_series.mean()
median_age = all_ages_series.median()
try:
    mode_age = mode(all_ages_series)
except:
    mode_age = 'N/A'
stdev_age = all_ages_series.std()
variance_age = all_ages_series.var()
min_age = all_ages_series.min()
max_age = all_ages_series.max()
range_age = max_age - min_age

# Plot histogram
plt.figure(figsize=(10, 6))
counts, bins, patches = plt.hist(all_ages_series, bins=range(int(min_age), int(max_age) + 2, 5),
                                 color='#1f77b4', edgecolor='black', alpha=0.7)

# Annotate counts and percentages
total = len(all_ages_series)
for count, bin_start, bin_end in zip(counts, bins[:-1], bins[1:]):
    percentage = (count / total) * 100
    plt.text((bin_start + bin_end) / 2, count + 1, f'{int(count)}\n({percentage:.1f}%)',
             ha='center', va='bottom', fontsize=9, color='black')
    plt.text((bin_start + bin_end) / 2, -5, f'{int(bin_start)}-{int(bin_end)}',
             ha='center', va='top', fontsize=9, color='darkblue', rotation=45)

# Add vertical lines for statistics
plt.axvline(mean_age, color='red', linestyle='--', linewidth=1.5, label=f'Mean: {mean_age:.2f}')
plt.axvline(median_age, color='green', linestyle='-', linewidth=1.5, label=f'Median: {median_age}')
if mode_age != 'N/A':
    plt.axvline(mode_age, color='blue', linestyle='-', linewidth=1.5, label=f'Mode: {mode_age}')
plt.axvline(mean_age + stdev_age, color='orange', linestyle=':', linewidth=1.5, label=f'Stdev: {stdev_age:.2f}')
plt.axvline(mean_age - stdev_age, color='orange', linestyle=':', linewidth=1.5)

# Add a vertical line for the 30-year-old mark
plt.axvline(30, color='gray', linestyle='-.', linewidth=1.5, label='30-Year-Old Mark')

# Add statistics box
stats_text = (
    f"Variance: {variance_age:.2f}\n"
    f"Standard Deviation: {stdev_age:.2f}\n"
    f"Range: {range_age}\n"
    f"Min Age: {min_age}\n"
    f"Max Age: {max_age}"
)
plt.text(0.98, 0.95, stats_text, ha='right', va='top', transform=plt.gca().transAxes,
         bbox=dict(facecolor='white', alpha=0.7))

# Adjust legend position
plt.legend(loc='upper left')

# Add labels, title, and grid
plt.title('Histogram of Age Distributions - Critical Acclaim Only')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75, linestyle='--')
plt.grid(axis='x', alpha=0.75, linestyle='--')
plt.tight_layout()

# Display the plot
plt.show()


# 1e Histogram - critical acclaim only - grammy artists only - same as 2e2

import pandas as pd
import matplotlib.pyplot as plt
from statistics import mode

# Load the data from the uploaded files
file_paths = [
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Artists.csv'    
]

age_columns = ['Artist Age']
all_ages = []

# Combine data from relevant columns into one list
for file_path, age_column in zip(file_paths, age_columns * 2):
    df = pd.read_csv(file_path)
    if age_column in df.columns:
        all_ages.extend(pd.to_numeric(df[age_column], errors='coerce').dropna().tolist())

# Create a Series for processing
all_ages_series = pd.Series(all_ages)

# Calculate statistics
mean_age = all_ages_series.mean()
median_age = all_ages_series.median()
try:
    mode_age = mode(all_ages_series)
except:
    mode_age = 'N/A'
stdev_age = all_ages_series.std()
variance_age = all_ages_series.var()
min_age = all_ages_series.min()
max_age = all_ages_series.max()
range_age = max_age - min_age

# Plot histogram
plt.figure(figsize=(10, 6))
counts, bins, patches = plt.hist(all_ages_series, bins=range(int(min_age), int(max_age) + 2, 5),
                                 color='#1f77b4', edgecolor='black', alpha=0.7)

# Annotate counts and percentages
total = len(all_ages_series)
for count, bin_start, bin_end in zip(counts, bins[:-1], bins[1:]):
    percentage = (count / total) * 100
    plt.text((bin_start + bin_end) / 2, count + 1, f'{int(count)}\n({percentage:.1f}%)',
             ha='center', va='bottom', fontsize=9, color='black')
    plt.text((bin_start + bin_end) / 2, -5, f'{int(bin_start)}-{int(bin_end)}',
             ha='center', va='top', fontsize=9, color='darkblue', rotation=45)

# Add vertical lines for statistics
plt.axvline(mean_age, color='red', linestyle='--', linewidth=1.5, label=f'Mean: {mean_age:.2f}')
plt.axvline(median_age, color='green', linestyle='-', linewidth=1.5, label=f'Median: {median_age}')
if mode_age != 'N/A':
    plt.axvline(mode_age, color='blue', linestyle='-', linewidth=1.5, label=f'Mode: {mode_age}')
plt.axvline(mean_age + stdev_age, color='orange', linestyle=':', linewidth=1.5, label=f'Stdev: {stdev_age:.2f}')
plt.axvline(mean_age - stdev_age, color='orange', linestyle=':', linewidth=1.5)

# Add a vertical line for the 30-year-old mark
plt.axvline(30, color='gray', linestyle='-.', linewidth=1.5, label='30-Year-Old Mark')

# Add statistics box
stats_text = (
    f"Variance: {variance_age:.2f}\n"
    f"Standard Deviation: {stdev_age:.2f}\n"
    f"Range: {range_age}\n"
    f"Min Age: {min_age}\n"
    f"Max Age: {max_age}"
)
plt.text(0.98, 0.95, stats_text, ha='right', va='top', transform=plt.gca().transAxes,
         bbox=dict(facecolor='white', alpha=0.7))

# Adjust legend position
plt.legend(loc='upper left')

# Add labels, title, and grid
plt.title('Histogram of Age Distributions - Critical Acclaim Artists Only')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75, linestyle='--')
plt.grid(axis='x', alpha=0.75, linestyle='--')
plt.tight_layout()

# Display the plot
plt.show()


# 1f Histogram - critical acclaim only - one all-up data line only - same as 2f2

import pandas as pd
import matplotlib.pyplot as plt
from statistics import mode

# Load the data from the uploaded files
file_paths = [    
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Producers.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Songwriters.csv'
]

age_columns = ['Producer Age', 'Songwriter Age']
all_ages = []

# Combine data from relevant columns into one list
for file_path, age_column in zip(file_paths, age_columns * 2):
    df = pd.read_csv(file_path)
    if age_column in df.columns:
        all_ages.extend(pd.to_numeric(df[age_column], errors='coerce').dropna().tolist())

# Create a Series for processing
all_ages_series = pd.Series(all_ages)

# Calculate statistics
mean_age = all_ages_series.mean()
median_age = all_ages_series.median()
try:
    mode_age = mode(all_ages_series)
except:
    mode_age = 'N/A'
stdev_age = all_ages_series.std()
variance_age = all_ages_series.var()
min_age = all_ages_series.min()
max_age = all_ages_series.max()
range_age = max_age - min_age

# Plot histogram
plt.figure(figsize=(10, 6))
counts, bins, patches = plt.hist(all_ages_series, bins=range(int(min_age), int(max_age) + 2, 5),
                                 color='#1f77b4', edgecolor='black', alpha=0.7)

# Annotate counts and percentages
total = len(all_ages_series)
for count, bin_start, bin_end in zip(counts, bins[:-1], bins[1:]):
    percentage = (count / total) * 100
    plt.text((bin_start + bin_end) / 2, count + 1, f'{int(count)}\n({percentage:.1f}%)',
             ha='center', va='bottom', fontsize=9, color='black')
    plt.text((bin_start + bin_end) / 2, -5, f'{int(bin_start)}-{int(bin_end)}',
             ha='center', va='top', fontsize=9, color='darkblue', rotation=45)

# Add vertical lines for statistics
plt.axvline(mean_age, color='red', linestyle='--', linewidth=1.5, label=f'Mean: {mean_age:.2f}')
plt.axvline(median_age, color='green', linestyle='-', linewidth=1.5, label=f'Median: {median_age}')
if mode_age != 'N/A':
    plt.axvline(mode_age, color='blue', linestyle='-', linewidth=1.5, label=f'Mode: {mode_age}')
plt.axvline(mean_age + stdev_age, color='orange', linestyle=':', linewidth=1.5, label=f'Stdev: {stdev_age:.2f}')
plt.axvline(mean_age - stdev_age, color='orange', linestyle=':', linewidth=1.5)

# Add a vertical line for the 30-year-old mark
plt.axvline(30, color='gray', linestyle='-.', linewidth=1.5, label='30-Year-Old Mark')

# Add statistics box
stats_text = (
    f"Variance: {variance_age:.2f}\n"
    f"Standard Deviation: {stdev_age:.2f}\n"
    f"Range: {range_age}\n"
    f"Min Age: {min_age}\n"
    f"Max Age: {max_age}"
)
plt.text(0.98, 0.95, stats_text, ha='right', va='top', transform=plt.gca().transAxes,
         bbox=dict(facecolor='white', alpha=0.7))

# Adjust legend position
plt.legend(loc='upper left')

# Add labels, title, and grid
plt.title('Histogram of Age Distributions - Critical Acclaim Producers & Songwriters Only')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75, linestyle='--')
plt.grid(axis='x', alpha=0.75, linestyle='--')
plt.tight_layout()

# Display the plot
plt.show()


# 2 - KDEs

# 2a1 KDE over all data - commercial success and critical acclaim - 7 lines

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import mode

# Load the uploaded data for each file
file_paths = [
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Year-End Charts Number Ones.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Best-Selling Albums.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Best-Selling Singles.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Artists.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Producers.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Songwriters.csv'
]

# Corresponding columns for ages in each file
age_columns = [
    'Artist Age',
    'Artist Age',
    'Artist Age',
    'Artist Age',
    'Producer Age',
    'Songwriter Age'
]

# Load data into a dictionary
age_data = {}
for file_path, age_column in zip(file_paths, age_columns):
    df = pd.read_csv(file_path)
    if age_column in df.columns:
        age_data[file_path] = pd.to_numeric(df[age_column], errors='coerce').dropna()

# Combine all age data into a single series for overall statistics
all_ages = pd.concat(age_data.values())
all_ages_cleaned = all_ages.reset_index(drop=True)  # Removed .drop_duplicates()

# Calculate overall statistics
mean_all = all_ages_cleaned.mean()
median_all = all_ages_cleaned.median()
try:
    mode_all = mode(all_ages_cleaned)
except:
    mode_all = 'N/A'
std_dev_all = all_ages_cleaned.std()
variance_all = all_ages_cleaned.var()
range_all = all_ages_cleaned.max() - all_ages_cleaned.min()
min_age_all = all_ages_cleaned.min()
max_age_all = all_ages_cleaned.max()

# Set up the plot
plt.figure(figsize=(14, 10))

# Plot KDE for each dataset
colors = ['red', 'blue', 'green', 'purple', 'orange', 'magenta']
for i, (file_path, ages) in enumerate(age_data.items()):
    label = file_path.split('\\')[-1].replace('.csv', '').replace('-', ' ')
    sns.kdeplot(ages, label=label, linewidth=2, color=colors[i % len(colors)])

# Plot KDE for all-up data
sns.kdeplot(all_ages_cleaned, label='All-Up Data', linewidth=2.5, color='black')

# Add vertical lines for all-up statistics
plt.axvline(mean_all, color='red', linestyle='--', linewidth=1.5, label='All-Up Mean')
plt.axvline(median_all, color='green', linestyle='-', linewidth=1.5, label='All-Up Median')
if mode_all != 'N/A':
    plt.axvline(mode_all, color='blue', linestyle='-', linewidth=1.5, label='All-Up Mode')
plt.axvline(mean_all - std_dev_all, color='orange', linestyle=':', linewidth=1.5, label='All-Up Mean - 1 Std Dev')
plt.axvline(mean_all + std_dev_all, color='orange', linestyle=':', linewidth=1.5, label='All-Up Mean + 1 Std Dev')

# Add a vertical line for the 30-year-old mark
plt.axvline(30, color='gray', linestyle='-.', linewidth=1.5, label='30-Year-Old Mark')

# Add statistics box for all-up data
stats_text_all = (
    f"Mean: {mean_all:.2f}\n"
    f"Median: {median_all:.2f}\n"
    f"Mode: {mode_all}\n"
    f"Variance: {variance_all:.2f}\n"
    f"Std Dev: {std_dev_all:.2f}\n"
    f"Range: {range_all}\n"
    f"Min Age: {min_age_all}\n"
    f"Max Age: {max_age_all}"
)
plt.text(0.02, 0.98, stats_text_all, ha='left', va='top', transform=plt.gca().transAxes,
         bbox=dict(facecolor='white', alpha=0.7))

# Adding labels, title, and legend
plt.title('Kernel Density Estimate (KDE) Plot of Age Distributions - All Data', fontsize=16)
plt.xlabel('Age')
plt.ylabel('Density')
plt.legend(title='Legend', loc='upper right')
plt.grid(axis='y', alpha=0.5)

# Display the KDE plot
plt.show()


# 2a2 KDE over all data - commercial success and critical acclaim - one all-up data line

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import mode

# Load the uploaded data for each file
file_paths = [
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Year-End Charts Number Ones.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Best-Selling Albums.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Best-Selling Singles.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Artists.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Producers.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Songwriters.csv'
]

# Corresponding columns for ages in each file
age_columns = [
    'Artist Age',
    'Artist Age',
    'Artist Age',
    'Artist Age',
    'Producer Age',
    'Songwriter Age'
]

# Load data into a dictionary
all_ages = []
for file_path, age_column in zip(file_paths, age_columns):
    df = pd.read_csv(file_path)
    if age_column in df.columns:
        all_ages.extend(pd.to_numeric(df[age_column], errors='coerce').dropna().tolist())

# Combine all age data into a single series for overall statistics
all_ages_cleaned = pd.Series(all_ages)  # Removed .drop_duplicates()

# Calculate overall statistics
mean_all = all_ages_cleaned.mean()
median_all = all_ages_cleaned.median()
try:
    mode_all = mode(all_ages_cleaned)
except:
    mode_all = 'N/A'
std_dev_all = all_ages_cleaned.std()
variance_all = all_ages_cleaned.var()
range_all = all_ages_cleaned.max() - all_ages_cleaned.min()
min_age_all = all_ages_cleaned.min()
max_age_all = all_ages_cleaned.max()

# Set up the plot
plt.figure(figsize=(14, 10))

# Plot KDE for all-up data
sns.kdeplot(all_ages_cleaned, label='All-Up Data', linewidth=2.5, color='black')

# Add vertical lines for all-up statistics
plt.axvline(mean_all, color='red', linestyle='--', linewidth=1.5, label='All-Up Mean')
plt.axvline(median_all, color='green', linestyle='-', linewidth=1.5, label='All-Up Median')
if mode_all != 'N/A':
    plt.axvline(mode_all, color='blue', linestyle='-', linewidth=1.5, label='All-Up Mode')
plt.axvline(mean_all - std_dev_all, color='orange', linestyle=':', linewidth=1.5, label='All-Up Mean - 1 Std Dev')
plt.axvline(mean_all + std_dev_all, color='orange', linestyle=':', linewidth=1.5, label='All-Up Mean + 1 Std Dev')

# Add a vertical line for the 30-year-old mark
plt.axvline(30, color='gray', linestyle='-.', linewidth=1.5, label='30-Year-Old Mark')

# Add statistics box for all-up data
stats_text_all = (
    f"Mean: {mean_all:.2f}\n"
    f"Median: {median_all:.2f}\n"
    f"Mode: {mode_all}\n"
    f"Variance: {variance_all:.2f}\n"
    f"Std Dev: {std_dev_all:.2f}\n"
    f"Range: {range_all}\n"
    f"Min Age: {min_age_all}\n"
    f"Max Age: {max_age_all}"
)
plt.text(0.02, 0.98, stats_text_all, ha='left', va='top', transform=plt.gca().transAxes,
         bbox=dict(facecolor='white', alpha=0.7))

# Adding labels, title, and legend
plt.title('Kernel Density Estimate (KDE) Plot of Age Distributions - All Data', fontsize=16)
plt.xlabel('Age')
plt.ylabel('Density')
plt.legend(title='Legend', loc='upper right')
plt.grid(axis='y', alpha=0.5)

# Display the KDE plot
plt.show()


# 2b1 KDE over artists only (excl. producers and songwriters) - commercial success and critical acclaim - 5 lines

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import mode

# Load the uploaded data for each file
file_paths = [
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Year-End Charts Number Ones.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Best-Selling Albums.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Best-Selling Singles.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Artists.csv'    
]

# Corresponding columns for ages in each file
age_columns = [
    'Artist Age',
    'Artist Age',
    'Artist Age',
    'Artist Age',
]

# Load data into a dictionary
age_data = {}
for file_path, age_column in zip(file_paths, age_columns):
    df = pd.read_csv(file_path)
    if age_column in df.columns:
        age_data[file_path] = pd.to_numeric(df[age_column], errors='coerce').dropna()

# Combine all age data into a single series for overall statistics
all_ages = pd.concat(age_data.values())
all_ages_cleaned = all_ages.reset_index(drop=True)  # Removed .drop_duplicates()

# Calculate overall statistics
mean_all = all_ages_cleaned.mean()
median_all = all_ages_cleaned.median()
try:
    mode_all = mode(all_ages_cleaned)
except:
    mode_all = 'N/A'
std_dev_all = all_ages_cleaned.std()
variance_all = all_ages_cleaned.var()
range_all = all_ages_cleaned.max() - all_ages_cleaned.min()
min_age_all = all_ages_cleaned.min()
max_age_all = all_ages_cleaned.max()

# Set up the plot
plt.figure(figsize=(14, 10))

# Plot KDE for each dataset
colors = ['red', 'blue', 'green', 'purple']
for i, (file_path, ages) in enumerate(age_data.items()):
    label = file_path.split('\\')[-1].replace('.csv', '').replace('-', ' ')
    sns.kdeplot(ages, label=label, linewidth=2, color=colors[i % len(colors)])

# Plot KDE for all-up data
sns.kdeplot(all_ages_cleaned, label='All-Up Data', linewidth=2.5, color='black')

# Add vertical lines for all-up statistics
plt.axvline(mean_all, color='red', linestyle='--', linewidth=1.5, label='All-Up Mean')
plt.axvline(median_all, color='green', linestyle='-', linewidth=1.5, label='All-Up Median')
if mode_all != 'N/A':
    plt.axvline(mode_all, color='blue', linestyle='-', linewidth=1.5, label='All-Up Mode')
plt.axvline(mean_all - std_dev_all, color='orange', linestyle=':', linewidth=1.5, label='All-Up Mean - 1 Std Dev')
plt.axvline(mean_all + std_dev_all, color='orange', linestyle=':', linewidth=1.5, label='All-Up Mean + 1 Std Dev')

# Add a vertical line for the 30-year-old mark
plt.axvline(30, color='gray', linestyle='-.', linewidth=1.5, label='30-Year-Old Mark')

# Add statistics box for all-up data
stats_text_all = (
    f"Mean: {mean_all:.2f}\n"
    f"Median: {median_all:.2f}\n"
    f"Mode: {mode_all}\n"
    f"Variance: {variance_all:.2f}\n"
    f"Std Dev: {std_dev_all:.2f}\n"
    f"Range: {range_all}\n"
    f"Min Age: {min_age_all}\n"
    f"Max Age: {max_age_all}"
)
plt.text(0.02, 0.98, stats_text_all, ha='left', va='top', transform=plt.gca().transAxes,
         bbox=dict(facecolor='white', alpha=0.7))

# Adding labels, title, and legend
plt.title('Kernel Density Estimate (KDE) Plot of Age Distributions - Artists only', fontsize=16)
plt.xlabel('Age')
plt.ylabel('Density')
plt.legend(title='Legend', loc='upper right')
plt.grid(axis='y', alpha=0.5)

# Display the KDE plot
plt.show()


# 2b2 KDE over artists only (excl. producers and songwriters) - commercial success and critical acclaim - one all-up data line 

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import mode

# Load the uploaded data for each file
file_paths = [
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Year-End Charts Number Ones.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Best-Selling Albums.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Best-Selling Singles.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Artists.csv'
]

# Corresponding columns for ages in each file
age_columns = [
    'Artist Age',
    'Artist Age',
    'Artist Age',
    'Artist Age',
]

# Combine all data into a single list
all_ages = []
for file_path, age_column in zip(file_paths, age_columns):
    df = pd.read_csv(file_path)
    if age_column in df.columns:
        all_ages.extend(pd.to_numeric(df[age_column], errors='coerce').dropna().tolist())

# Create a clean series from the combined data
all_ages_cleaned = pd.Series(all_ages)  # Removed .drop_duplicates()

# Calculate overall statistics
mean_all = all_ages_cleaned.mean()
median_all = all_ages_cleaned.median()
try:
    mode_all = mode(all_ages_cleaned)
except:
    mode_all = 'N/A'
std_dev_all = all_ages_cleaned.std()
variance_all = all_ages_cleaned.var()
range_all = all_ages_cleaned.max() - all_ages_cleaned.min()
min_age_all = all_ages_cleaned.min()
max_age_all = all_ages_cleaned.max()

# Set up the plot
plt.figure(figsize=(14, 10))

# Plot KDE for the combined data
sns.kdeplot(all_ages_cleaned, label='Artists Only Data', linewidth=2.5, color='black')

# Add vertical lines for the combined data statistics
plt.axvline(mean_all, color='red', linestyle='--', linewidth=1.5, label='Mean')
plt.axvline(median_all, color='green', linestyle='-', linewidth=1.5, label='Median')
if mode_all != 'N/A':
    plt.axvline(mode_all, color='blue', linestyle='-', linewidth=1.5, label='Mode')
plt.axvline(mean_all - std_dev_all, color='orange', linestyle=':', linewidth=1.5, label='Mean - 1 Std Dev')
plt.axvline(mean_all + std_dev_all, color='orange', linestyle=':', linewidth=1.5, label='Mean + 1 Std Dev')

# Add a vertical line for the 30-year-old mark
plt.axvline(30, color='gray', linestyle='-.', linewidth=1.5, label='30-Year-Old Mark')

# Add a statistics box for the combined data
stats_text_all = (
    f"Mean: {mean_all:.2f}\n"
    f"Median: {median_all:.2f}\n"
    f"Mode: {mode_all}\n"
    f"Variance: {variance_all:.2f}\n"
    f"Std Dev: {std_dev_all:.2f}\n"
    f"Range: {range_all}\n"
    f"Min Age: {min_age_all}\n"
    f"Max Age: {max_age_all}"
)
plt.text(0.02, 0.98, stats_text_all, ha='left', va='top', transform=plt.gca().transAxes,
         bbox=dict(facecolor='white', alpha=0.7))

# Adding labels, title, and legend
plt.title('Kernel Density Estimate (KDE) Plot of Age Distributions - Artists Only', fontsize=16)
plt.xlabel('Age')
plt.ylabel('Density')
plt.legend(title='Legend', loc='upper right')
plt.grid(axis='y', alpha=0.5)

# Display the KDE plot
plt.show()


# 2c1 KDE - commercial success only - 4 lines

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import mode

# Load the uploaded data for each file
file_paths = [
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Year-End Charts Number Ones.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Best-Selling Albums.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Best-Selling Singles.csv'    
]

# Corresponding columns for ages in each file
age_columns = [
    'Artist Age',
    'Artist Age',
    'Artist Age',    
]

# Load data into a dictionary
age_data = {}
for file_path, age_column in zip(file_paths, age_columns):
    df = pd.read_csv(file_path)
    if age_column in df.columns:
        age_data[file_path] = pd.to_numeric(df[age_column], errors='coerce').dropna()

# Combine all age data into a single series for overall statistics
all_ages = pd.concat(age_data.values())
all_ages_cleaned = all_ages.reset_index(drop=True)  # Removed .drop_duplicates()

# Calculate overall statistics
mean_all = all_ages_cleaned.mean()
median_all = all_ages_cleaned.median()
try:
    mode_all = mode(all_ages_cleaned)
except:
    mode_all = 'N/A'
std_dev_all = all_ages_cleaned.std()
variance_all = all_ages_cleaned.var()
range_all = all_ages_cleaned.max() - all_ages_cleaned.min()
min_age_all = all_ages_cleaned.min()
max_age_all = all_ages_cleaned.max()

# Set up the plot
plt.figure(figsize=(14, 10))

# Plot KDE for each dataset
colors = ['red', 'blue', 'green']
for i, (file_path, ages) in enumerate(age_data.items()):
    label = file_path.split('\\')[-1].replace('.csv', '').replace('-', ' ')
    sns.kdeplot(ages, label=label, linewidth=2, color=colors[i % len(colors)])

# Plot KDE for all-up data
sns.kdeplot(all_ages_cleaned, label='All-Up Data', linewidth=2.5, color='black')

# Add vertical lines for all-up statistics
plt.axvline(mean_all, color='red', linestyle='--', linewidth=1.5, label='All-Up Mean')
plt.axvline(median_all, color='green', linestyle='-', linewidth=1.5, label='All-Up Median')
if mode_all != 'N/A':
    plt.axvline(mode_all, color='blue', linestyle='-', linewidth=1.5, label='All-Up Mode')
plt.axvline(mean_all - std_dev_all, color='orange', linestyle=':', linewidth=1.5, label='All-Up Mean - 1 Std Dev')
plt.axvline(mean_all + std_dev_all, color='orange', linestyle=':', linewidth=1.5, label='All-Up Mean + 1 Std Dev')

# Add a vertical line for the 30-year-old mark
plt.axvline(30, color='gray', linestyle='-.', linewidth=1.5, label='30-Year-Old Mark')

# Add statistics box for all-up data
stats_text_all = (
    f"Mean: {mean_all:.2f}\n"
    f"Median: {median_all:.2f}\n"
    f"Mode: {mode_all}\n"
    f"Variance: {variance_all:.2f}\n"
    f"Std Dev: {std_dev_all:.2f}\n"
    f"Range: {range_all}\n"
    f"Min Age: {min_age_all}\n"
    f"Max Age: {max_age_all}"
)
plt.text(0.02, 0.98, stats_text_all, ha='left', va='top', transform=plt.gca().transAxes,
         bbox=dict(facecolor='white', alpha=0.7))

# Adding labels, title, and legend
plt.title('Kernel Density Estimate (KDE) Plot of Age Distributions - Commercial Success only', fontsize=16)
plt.xlabel('Age')
plt.ylabel('Density')
plt.legend(title='Legend', loc='upper right')
plt.grid(axis='y', alpha=0.5)

# Display the KDE plot
plt.show()


# 2c2 KDE - commercial success only - one all-up data line only

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import mode

# Load the uploaded data for each file
file_paths = [
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Year-End Charts Number Ones.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Best-Selling Albums.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Best-Selling Singles.csv'    
]

# Corresponding columns for ages in each file
age_columns = [
    'Artist Age',
    'Artist Age',
    'Artist Age',    
]

# Combine all data into a single list
all_ages = []
for file_path, age_column in zip(file_paths, age_columns):
    df = pd.read_csv(file_path)
    if age_column in df.columns:
        all_ages.extend(pd.to_numeric(df[age_column], errors='coerce').dropna().tolist())

# Create a clean series from the combined data
all_ages_cleaned = pd.Series(all_ages)  # Removed .drop_duplicates()

# Calculate overall statistics
mean_all = all_ages_cleaned.mean()
median_all = all_ages_cleaned.median()
try:
    mode_all = mode(all_ages_cleaned)
except:
    mode_all = 'N/A'
std_dev_all = all_ages_cleaned.std()
variance_all = all_ages_cleaned.var()
range_all = all_ages_cleaned.max() - all_ages_cleaned.min()
min_age_all = all_ages_cleaned.min()
max_age_all = all_ages_cleaned.max()

# Set up the plot
plt.figure(figsize=(14, 10))

# Plot KDE for the combined data
sns.kdeplot(all_ages_cleaned, label='Commercial Success Data', linewidth=2.5, color='black')

# Add vertical lines for the combined data statistics
plt.axvline(mean_all, color='red', linestyle='--', linewidth=1.5, label='Mean')
plt.axvline(median_all, color='green', linestyle='-', linewidth=1.5, label='Median')
if mode_all != 'N/A':
    plt.axvline(mode_all, color='blue', linestyle='-', linewidth=1.5, label='Mode')
plt.axvline(mean_all - std_dev_all, color='orange', linestyle=':', linewidth=1.5, label='Mean - 1 Std Dev')
plt.axvline(mean_all + std_dev_all, color='orange', linestyle=':', linewidth=1.5, label='Mean + 1 Std Dev')

# Add a vertical line for the 30-year-old mark
plt.axvline(30, color='gray', linestyle='-.', linewidth=1.5, label='30-Year-Old Mark')

# Add a statistics box for the combined data
stats_text_all = (
    f"Mean: {mean_all:.2f}\n"
    f"Median: {median_all:.2f}\n"
    f"Mode: {mode_all}\n"
    f"Variance: {variance_all:.2f}\n"
    f"Std Dev: {std_dev_all:.2f}\n"
    f"Range: {range_all}\n"
    f"Min Age: {min_age_all}\n"
    f"Max Age: {max_age_all}"
)
plt.text(0.02, 0.98, stats_text_all, ha='left', va='top', transform=plt.gca().transAxes,
         bbox=dict(facecolor='white', alpha=0.7))

# Adding labels, title, and legend
plt.title('Kernel Density Estimate (KDE) Plot of Age Distributions - Commercial Success Only', fontsize=16)
plt.xlabel('Age')
plt.ylabel('Density')
plt.legend(title='Legend', loc='upper right')
plt.grid(axis='y', alpha=0.5)

# Display the KDE plot
plt.show()


# 2d1 KDE - critical acclaim only - 4 lines

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import mode

# Load the uploaded data for each file
file_paths = [
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Artists.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Producers.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Songwriters.csv'
]

# Corresponding columns for ages in each file
age_columns = [
    'Artist Age',
    'Producer Age',
    'Songwriter Age',    
]

# Load data into a dictionary
age_data = {}
for file_path, age_column in zip(file_paths, age_columns):
    df = pd.read_csv(file_path)
    if age_column in df.columns:
        age_data[file_path] = pd.to_numeric(df[age_column], errors='coerce').dropna()

# Combine all age data into a single series for overall statistics
all_ages = pd.concat(age_data.values())
all_ages_cleaned = all_ages.reset_index(drop=True)  # Removed .drop_duplicates()

# Calculate overall statistics
mean_all = all_ages_cleaned.mean()
median_all = all_ages_cleaned.median()
try:
    mode_all = mode(all_ages_cleaned)
except:
    mode_all = 'N/A'
std_dev_all = all_ages_cleaned.std()
variance_all = all_ages_cleaned.var()
range_all = all_ages_cleaned.max() - all_ages_cleaned.min()
min_age_all = all_ages_cleaned.min()
max_age_all = all_ages_cleaned.max()

# Set up the plot
plt.figure(figsize=(14, 10))

# Plot KDE for each dataset
colors = ['purple', 'orange', 'magenta']
for i, (file_path, ages) in enumerate(age_data.items()):
    label = file_path.split('\\')[-1].replace('.csv', '').replace('-', ' ')
    sns.kdeplot(ages, label=label, linewidth=2, color=colors[i % len(colors)])

# Plot KDE for all-up data
sns.kdeplot(all_ages_cleaned, label='All-Up Data', linewidth=2.5, color='black')

# Add vertical lines for all-up statistics
plt.axvline(mean_all, color='red', linestyle='--', linewidth=1.5, label='All-Up Mean')
plt.axvline(median_all, color='green', linestyle='-', linewidth=1.5, label='All-Up Median')
if mode_all != 'N/A':
    plt.axvline(mode_all, color='blue', linestyle='-', linewidth=1.5, label='All-Up Mode')
plt.axvline(mean_all - std_dev_all, color='orange', linestyle=':', linewidth=1.5, label='All-Up Mean - 1 Std Dev')
plt.axvline(mean_all + std_dev_all, color='orange', linestyle=':', linewidth=1.5, label='All-Up Mean + 1 Std Dev')

# Add a vertical line for the 30-year-old mark
plt.axvline(30, color='gray', linestyle='-.', linewidth=1.5, label='30-Year-Old Mark')

# Add statistics box for all-up data
stats_text_all = (
    f"Mean: {mean_all:.2f}\n"
    f"Median: {median_all:.2f}\n"
    f"Mode: {mode_all}\n"
    f"Variance: {variance_all:.2f}\n"
    f"Std Dev: {std_dev_all:.2f}\n"
    f"Range: {range_all}\n"
    f"Min Age: {min_age_all}\n"
    f"Max Age: {max_age_all}"
)
plt.text(0.02, 0.98, stats_text_all, ha='left', va='top', transform=plt.gca().transAxes,
         bbox=dict(facecolor='white', alpha=0.7))

# Adding labels, title, and legend
plt.title('Kernel Density Estimate (KDE) Plot of Age Distributions - Critical Acclaim only', fontsize=16)
plt.xlabel('Age')
plt.ylabel('Density')
plt.legend(title='Legend', loc='upper right')
plt.grid(axis='y', alpha=0.5)

# Display the KDE plot
plt.show()


# 2d2 KDE - critical acclaim only - one all-up data line only

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import mode

# Load the uploaded data for each file
file_paths = [
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Artists.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Producers.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Songwriters.csv'
]

# Corresponding columns for ages in each file
age_columns = [
    'Artist Age',
    'Producer Age',
    'Songwriter Age',
]

# Combine all data into a single list
all_ages = []
for file_path, age_column in zip(file_paths, age_columns):
    df = pd.read_csv(file_path)
    if age_column in df.columns:
        all_ages.extend(pd.to_numeric(df[age_column], errors='coerce').dropna().tolist())

# Create a clean series from the combined data
all_ages_cleaned = pd.Series(all_ages)  # Removed .drop_duplicates()

# Calculate overall statistics
mean_all = all_ages_cleaned.mean()
median_all = all_ages_cleaned.median()
try:
    mode_all = mode(all_ages_cleaned)
except:
    mode_all = 'N/A'
std_dev_all = all_ages_cleaned.std()
variance_all = all_ages_cleaned.var()
range_all = all_ages_cleaned.max() - all_ages_cleaned.min()
min_age_all = all_ages_cleaned.min()
max_age_all = all_ages_cleaned.max()

# Set up the plot
plt.figure(figsize=(14, 10))

# Plot KDE for the combined data
sns.kdeplot(all_ages_cleaned, label='Critical Acclaim Data', linewidth=2.5, color='black')

# Add vertical lines for the combined data statistics
plt.axvline(mean_all, color='red', linestyle='--', linewidth=1.5, label='Mean')
plt.axvline(median_all, color='green', linestyle='-', linewidth=1.5, label='Median')
if mode_all != 'N/A':
    plt.axvline(mode_all, color='blue', linestyle='-', linewidth=1.5, label='Mode')
plt.axvline(mean_all - std_dev_all, color='orange', linestyle=':', linewidth=1.5, label='Mean - 1 Std Dev')
plt.axvline(mean_all + std_dev_all, color='orange', linestyle=':', linewidth=1.5, label='Mean + 1 Std Dev')

# Add a vertical line for the 30-year-old mark
plt.axvline(30, color='gray', linestyle='-.', linewidth=1.5, label='30-Year-Old Mark')

# Add a statistics box for the combined data
stats_text_all = (
    f"Mean: {mean_all:.2f}\n"
    f"Median: {median_all:.2f}\n"
    f"Mode: {mode_all}\n"
    f"Variance: {variance_all:.2f}\n"
    f"Std Dev: {std_dev_all:.2f}\n"
    f"Range: {range_all}\n"
    f"Min Age: {min_age_all}\n"
    f"Max Age: {max_age_all}"
)
plt.text(0.02, 0.98, stats_text_all, ha='left', va='top', transform=plt.gca().transAxes,
         bbox=dict(facecolor='white', alpha=0.7))

# Adding labels, title, and legend
plt.title('Kernel Density Estimate (KDE) Plot of Age Distributions - Critical Acclaim Only', fontsize=16)
plt.xlabel('Age')
plt.ylabel('Density')
plt.legend(title='Legend', loc='upper right')
plt.grid(axis='y', alpha=0.5)

# Display the KDE plot
plt.show()


# 2e1 KDE - critical acclaim only - grammy artists only - 2 lines

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import mode

# Load the uploaded data for each file
file_paths = [
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Artists.csv'    
]

# Corresponding columns for ages in each file
age_columns = [
    'Artist Age'    
]

# Load data into a dictionary
age_data = {}
for file_path, age_column in zip(file_paths, age_columns):
    df = pd.read_csv(file_path)
    if age_column in df.columns:
        age_data[file_path] = pd.to_numeric(df[age_column], errors='coerce').dropna()

# Combine all age data into a single series for overall statistics
all_ages = pd.concat(age_data.values())
all_ages_cleaned = all_ages.reset_index(drop=True)  # Removed .drop_duplicates()

# Calculate overall statistics
mean_all = all_ages_cleaned.mean()
median_all = all_ages_cleaned.median()
try:
    mode_all = mode(all_ages_cleaned)
except:
    mode_all = 'N/A'
std_dev_all = all_ages_cleaned.std()
variance_all = all_ages_cleaned.var()
range_all = all_ages_cleaned.max() - all_ages_cleaned.min()
min_age_all = all_ages_cleaned.min()
max_age_all = all_ages_cleaned.max()

# Set up the plot
plt.figure(figsize=(14, 10))

# Plot KDE for the dataset
colors = ['purple']
for i, (file_path, ages) in enumerate(age_data.items()):
    label = file_path.split('\\')[-1].replace('.csv', '').replace('-', ' ')
    sns.kdeplot(ages, label=label, linewidth=2, color=colors[i % len(colors)])

# Add vertical lines for statistics
plt.axvline(mean_all, color='red', linestyle='--', linewidth=1.5, label='Mean')
plt.axvline(median_all, color='green', linestyle='-', linewidth=1.5, label='Median')
if mode_all != 'N/A':
    plt.axvline(mode_all, color='blue', linestyle='-', linewidth=1.5, label='Mode')
plt.axvline(mean_all - std_dev_all, color='orange', linestyle=':', linewidth=1.5, label='Mean - 1 Std Dev')
plt.axvline(mean_all + std_dev_all, color='orange', linestyle=':', linewidth=1.5, label='Mean + 1 Std Dev')

# Add a vertical line for the 30-year-old mark
plt.axvline(30, color='gray', linestyle='-.', linewidth=1.5, label='30-Year-Old Mark')

# Add statistics box for the data
stats_text_all = (
    f"Mean: {mean_all:.2f}\n"
    f"Median: {median_all:.2f}\n"
    f"Mode: {mode_all}\n"
    f"Variance: {variance_all:.2f}\n"
    f"Std Dev: {std_dev_all:.2f}\n"
    f"Range: {range_all}\n"
    f"Min Age: {min_age_all}\n"
    f"Max Age: {max_age_all}"
)
plt.text(0.02, 0.98, stats_text_all, ha='left', va='top', transform=plt.gca().transAxes,
         bbox=dict(facecolor='white', alpha=0.7))

# Adding labels, title, and legend
plt.title('Kernel Density Estimate (KDE) Plot of Age Distributions - Critical Acclaim Artists Only', fontsize=16)
plt.xlabel('Age')
plt.ylabel('Density')
plt.legend(title='Legend', loc='upper right')
plt.grid(axis='y', alpha=0.5)

# Display the KDE plot
plt.show()


# 2e2 KDE - critical acclaim only - one all-up data line only

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import mode

# Load the uploaded data for each file
file_paths = [
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Artists.csv'    
]

# Corresponding columns for ages in each file
age_columns = [
    'Artist Age'
]

# Combine all data into a single list
all_ages = []
for file_path, age_column in zip(file_paths, age_columns):
    df = pd.read_csv(file_path)
    if age_column in df.columns:
        all_ages.extend(pd.to_numeric(df[age_column], errors='coerce').dropna().tolist())

# Create a clean series from the combined data
all_ages_cleaned = pd.Series(all_ages)  # Removed .drop_duplicates()

# Calculate overall statistics
mean_all = all_ages_cleaned.mean()
median_all = all_ages_cleaned.median()
try:
    mode_all = mode(all_ages_cleaned)
except:
    mode_all = 'N/A'
std_dev_all = all_ages_cleaned.std()
variance_all = all_ages_cleaned.var()
range_all = all_ages_cleaned.max() - all_ages_cleaned.min()
min_age_all = all_ages_cleaned.min()
max_age_all = all_ages_cleaned.max()

# Set up the plot
plt.figure(figsize=(14, 10))

# Plot KDE for the combined data
sns.kdeplot(all_ages_cleaned, label='Critical Acclaim Data', linewidth=2.5, color='black')

# Add vertical lines for the combined data statistics
plt.axvline(mean_all, color='red', linestyle='--', linewidth=1.5, label='Mean')
plt.axvline(median_all, color='green', linestyle='-', linewidth=1.5, label='Median')
if mode_all != 'N/A':
    plt.axvline(mode_all, color='blue', linestyle='-', linewidth=1.5, label='Mode')
plt.axvline(mean_all - std_dev_all, color='orange', linestyle=':', linewidth=1.5, label='Mean - 1 Std Dev')
plt.axvline(mean_all + std_dev_all, color='orange', linestyle=':', linewidth=1.5, label='Mean + 1 Std Dev')

# Add a vertical line for the 30-year-old mark
plt.axvline(30, color='gray', linestyle='-.', linewidth=1.5, label='30-Year-Old Mark')

# Add a statistics box for the combined data
stats_text_all = (
    f"Mean: {mean_all:.2f}\n"
    f"Median: {median_all:.2f}\n"
    f"Mode: {mode_all}\n"
    f"Variance: {variance_all:.2f}\n"
    f"Std Dev: {std_dev_all:.2f}\n"
    f"Range: {range_all}\n"
    f"Min Age: {min_age_all}\n"
    f"Max Age: {max_age_all}"
)
plt.text(0.02, 0.98, stats_text_all, ha='left', va='top', transform=plt.gca().transAxes,
         bbox=dict(facecolor='white', alpha=0.7))

# Adding labels, title, and legend
plt.title('Kernel Density Estimate (KDE) Plot of Age Distributions - Critical Acclaim Artists Only', fontsize=16)
plt.xlabel('Age')
plt.ylabel('Density')
plt.legend(title='Legend', loc='upper right')
plt.grid(axis='y', alpha=0.5)

# Display the KDE plot
plt.show()


# 2f1 KDE - critical acclaim only - grammy producers and songwriters only - 3 lines

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import mode

# Load the uploaded data for each file
file_paths = [    
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Producers.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Songwriters.csv'
]

# Corresponding columns for ages in each file
age_columns = [    
    'Producer Age',
    'Songwriter Age'
]

# Load data into a dictionary
age_data = {}
for file_path, age_column in zip(file_paths, age_columns):
    df = pd.read_csv(file_path)
    if age_column in df.columns:
        age_data[file_path] = pd.to_numeric(df[age_column], errors='coerce').dropna()

# Combine all age data into a single series for overall statistics
all_ages = pd.concat(age_data.values())
all_ages_cleaned = all_ages.reset_index(drop=True)  # Removed .drop_duplicates()

# Calculate overall statistics
mean_all = all_ages_cleaned.mean()
median_all = all_ages_cleaned.median()
try:
    mode_all = mode(all_ages_cleaned)
except:
    mode_all = 'N/A'
std_dev_all = all_ages_cleaned.std()
variance_all = all_ages_cleaned.var()
range_all = all_ages_cleaned.max() - all_ages_cleaned.min()
min_age_all = all_ages_cleaned.min()
max_age_all = all_ages_cleaned.max()

# Set up the plot
plt.figure(figsize=(14, 10))

# Plot KDE for each dataset
colors = ['orange', 'magenta']
for i, (file_path, ages) in enumerate(age_data.items()):
    label = file_path.split('\\')[-1].replace('.csv', '').replace('-', ' ')
    sns.kdeplot(ages, label=label, linewidth=2, color=colors[i % len(colors)])

# Plot KDE for all-up data
sns.kdeplot(all_ages_cleaned, label='All-Up Data', linewidth=2.5, color='black')

# Add vertical lines for all-up statistics
plt.axvline(mean_all, color='red', linestyle='--', linewidth=1.5, label='All-Up Mean')
plt.axvline(median_all, color='green', linestyle='-', linewidth=1.5, label='All-Up Median')
if mode_all != 'N/A':
    plt.axvline(mode_all, color='blue', linestyle='-', linewidth=1.5, label='All-Up Mode')
plt.axvline(mean_all - std_dev_all, color='orange', linestyle=':', linewidth=1.5, label='All-Up Mean - 1 Std Dev')
plt.axvline(mean_all + std_dev_all, color='orange', linestyle=':', linewidth=1.5, label='All-Up Mean + 1 Std Dev')

# Add a vertical line for the 30-year-old mark
plt.axvline(30, color='gray', linestyle='-.', linewidth=1.5, label='30-Year-Old Mark')

# Add statistics box for all-up data
stats_text_all = (
    f"Mean: {mean_all:.2f}\n"
    f"Median: {median_all:.2f}\n"
    f"Mode: {mode_all}\n"
    f"Variance: {variance_all:.2f}\n"
    f"Std Dev: {std_dev_all:.2f}\n"
    f"Range: {range_all}\n"
    f"Min Age: {min_age_all}\n"
    f"Max Age: {max_age_all}"
)
plt.text(0.02, 0.98, stats_text_all, ha='left', va='top', transform=plt.gca().transAxes,
         bbox=dict(facecolor='white', alpha=0.7))

# Adding labels, title, and legend
plt.title('Kernel Density Estimate (KDE) Plot of Age Distributions - Critical Acclaim Producers & Songwriters', fontsize=16)
plt.xlabel('Age')
plt.ylabel('Density')
plt.legend(title='Legend', loc='upper right')
plt.grid(axis='y', alpha=0.5)

# Display the KDE plot
plt.show()


# 2f2 KDE - critical acclaim only - one all-up data line only

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import mode

# Load the uploaded data for each file
file_paths = [    
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Producers.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Songwriters.csv'
]

# Corresponding columns for ages in each file
age_columns = [    
    'Producer Age',
    'Songwriter Age'
]

# Combine all data into a single list
all_ages = []
for file_path, age_column in zip(file_paths, age_columns):
    df = pd.read_csv(file_path)
    if age_column in df.columns:
        all_ages.extend(pd.to_numeric(df[age_column], errors='coerce').dropna().tolist())

# Create a clean series from the combined data
all_ages_cleaned = pd.Series(all_ages)  # Removed .drop_duplicates()

# Calculate overall statistics
mean_all = all_ages_cleaned.mean()
median_all = all_ages_cleaned.median()
try:
    mode_all = mode(all_ages_cleaned)
except:
    mode_all = 'N/A'
std_dev_all = all_ages_cleaned.std()
variance_all = all_ages_cleaned.var()
range_all = all_ages_cleaned.max() - all_ages_cleaned.min()
min_age_all = all_ages_cleaned.min()
max_age_all = all_ages_cleaned.max()

# Set up the plot
plt.figure(figsize=(14, 10))

# Plot KDE for the combined data
sns.kdeplot(all_ages_cleaned, label='Critical Acclaim Data', linewidth=2.5, color='black')

# Add vertical lines for the combined data statistics
plt.axvline(mean_all, color='red', linestyle='--', linewidth=1.5, label='Mean')
plt.axvline(median_all, color='green', linestyle='-', linewidth=1.5, label='Median')
if mode_all != 'N/A':
    plt.axvline(mode_all, color='blue', linestyle='-', linewidth=1.5, label='Mode')
plt.axvline(mean_all - std_dev_all, color='orange', linestyle=':', linewidth=1.5, label='Mean - 1 Std Dev')
plt.axvline(mean_all + std_dev_all, color='orange', linestyle=':', linewidth=1.5, label='Mean + 1 Std Dev')

# Add a vertical line for the 30-year-old mark
plt.axvline(30, color='gray', linestyle='-.', linewidth=1.5, label='30-Year-Old Mark')

# Add a statistics box for the combined data
stats_text_all = (
    f"Mean: {mean_all:.2f}\n"
    f"Median: {median_all:.2f}\n"
    f"Mode: {mode_all}\n"
    f"Variance: {variance_all:.2f}\n"
    f"Std Dev: {std_dev_all:.2f}\n"
    f"Range: {range_all}\n"
    f"Min Age: {min_age_all}\n"
    f"Max Age: {max_age_all}"
)
plt.text(0.02, 0.98, stats_text_all, ha='left', va='top', transform=plt.gca().transAxes,
         bbox=dict(facecolor='white', alpha=0.7))

# Adding labels, title, and legend
plt.title('Kernel Density Estimate (KDE) Plot of Age Distributions - Critical Acclaim Producers & Songwriters Only', fontsize=16)
plt.xlabel('Age')
plt.ylabel('Density')
plt.legend(title='Legend', loc='upper right')
plt.grid(axis='y', alpha=0.5)

# Display the KDE plot
plt.show()


# 3 - Bar charts all-up

# 3a - < 30 and >= 30 All-Up Charts - over all data - commercial success and critical acclaim - same as 2a2

import pandas as pd
import matplotlib.pyplot as plt

# Define file paths and corresponding columns
file_paths = [
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Year-End Charts Number Ones.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Best-Selling Albums.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Best-Selling Singles.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Artists.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Producers.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Songwriters.csv'
]

columns_to_extract = [
    'Artist Age',  # For the first 4 files
    'Artist Age',  # For the second file
    'Artist Age',  # For the third file
    'Artist Age',  # For the fourth file
    'Producer Age',  # For the fifth file
    'Songwriter Age'  # For the sixth file
]

# Combine the relevant data from all CSV files into one dataframe
all_data = pd.DataFrame()

for file_path, column in zip(file_paths, columns_to_extract):
    try:
        # Read the file
        data = pd.read_csv(file_path)
        
        # Check if the column exists and extract it
        if column in data.columns:
            temp_df = data[[column]].rename(columns={column: 'Age'})  # Standardize column name to 'Age'
            all_data = pd.concat([all_data, temp_df], ignore_index=True)
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

# Convert the 'Age' column to numeric, dropping any invalid entries
all_data['Age'] = pd.to_numeric(all_data['Age'], errors='coerce').dropna()

# Calculate statistics
mean_age = all_data['Age'].mean()
median_age = all_data['Age'].median()
mode_age = all_data['Age'].mode()[0] if not all_data['Age'].mode().empty else 'N/A'
stdev_age = all_data['Age'].std()
variance_age = all_data['Age'].var()
range_age = all_data['Age'].max() - all_data['Age'].min()

# Create two buckets: ages < 30 and >= 30
plt.figure(figsize=(8, 5))
age_bins = [0, 30, all_data['Age'].max() + 1]  # Adding 1 to include the max value in the >=30 bucket
bucket_labels = ['< 30', '>= 30']
bucket_counts = pd.cut(all_data['Age'], bins=age_bins, right=False, labels=bucket_labels).value_counts()

# Reorder the buckets to ensure '< 30' appears first
bucket_counts = bucket_counts.reindex(['< 30', '>= 30'])

# Plot the histogram with two buckets
plt.bar(bucket_counts.index, bucket_counts.values, color='#1f77b4', edgecolor='black', alpha=0.7)

# Display counts and percentages on the bars
total = len(all_data['Age'])
for index, value in enumerate(bucket_counts.values):
    percentage = (value / total) * 100
    plt.text(index, value, f'{value} ({percentage:.1f}%)', ha='center', va='bottom', fontsize=10)

# Add a vertical line for the 30-year mark
plt.axvline(x=0.5, color='purple', linestyle='-.', linewidth=1.5, label='Age 30')

# Add a text box with variance, standard deviation, and range
stats_text = (f"Variance: {variance_age:.2f}\nStandard Deviation: {stdev_age:.2f}\n"
              f"Range: {range_age}")
plt.text(0.98, 0.95, stats_text, ha='right', va='top', transform=plt.gca().transAxes,
         bbox=dict(facecolor='white', alpha=0.5))

# Adding labels, title, legend, and grid
plt.title('Distribution of Ages in Two Ranges (< 30 and >= 30) - All Data')
plt.xlabel('Age Range')
plt.ylabel('Frequency')
plt.legend(loc='lower left')
plt.grid(axis='y', alpha=0.75)

# Display the histogram with the vertical marker
plt.show()


# 3b - < 30 and >= 30 All-Up Charts - over artists only (excl. producers and songwriters) - commercial success and critical acclaim - same as 2b2

import pandas as pd
import matplotlib.pyplot as plt

# Define file paths and corresponding columns
file_paths = [
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Year-End Charts Number Ones.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Best-Selling Albums.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Best-Selling Singles.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Artists.csv'
]

columns_to_extract = [
    'Artist Age',  # For the first 4 files
    'Artist Age',  # For the second file
    'Artist Age',  # For the third file
    'Artist Age'  # For the fourth file    
]

# Combine the relevant data from all CSV files into one dataframe
all_data = pd.DataFrame()

for file_path, column in zip(file_paths, columns_to_extract):
    try:
        # Read the file
        data = pd.read_csv(file_path)
        
        # Check if the column exists and extract it
        if column in data.columns:
            temp_df = data[[column]].rename(columns={column: 'Age'})  # Standardize column name to 'Age'
            all_data = pd.concat([all_data, temp_df], ignore_index=True)
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

# Convert the 'Age' column to numeric, dropping any invalid entries
all_data['Age'] = pd.to_numeric(all_data['Age'], errors='coerce').dropna()

# Calculate statistics
mean_age = all_data['Age'].mean()
median_age = all_data['Age'].median()
mode_age = all_data['Age'].mode()[0] if not all_data['Age'].mode().empty else 'N/A'
stdev_age = all_data['Age'].std()
variance_age = all_data['Age'].var()
range_age = all_data['Age'].max() - all_data['Age'].min()

# Create two buckets: ages < 30 and >= 30
plt.figure(figsize=(8, 5))
age_bins = [0, 30, all_data['Age'].max() + 1]  # Adding 1 to include the max value in the >=30 bucket
bucket_labels = ['< 30', '>= 30']
bucket_counts = pd.cut(all_data['Age'], bins=age_bins, right=False, labels=bucket_labels).value_counts()

# Reorder the buckets to ensure '< 30' appears first
bucket_counts = bucket_counts.reindex(['< 30', '>= 30'])

# Plot the histogram with two buckets
plt.bar(bucket_counts.index, bucket_counts.values, color='#1f77b4', edgecolor='black', alpha=0.7)

# Display counts and percentages on the bars
total = len(all_data['Age'])
for index, value in enumerate(bucket_counts.values):
    percentage = (value / total) * 100
    plt.text(index, value, f'{value} ({percentage:.1f}%)', ha='center', va='bottom', fontsize=10)

# Add a vertical line for the 30-year mark
plt.axvline(x=0.5, color='purple', linestyle='-.', linewidth=1.5, label='Age 30')

# Add a text box with variance, standard deviation, and range
stats_text = (f"Variance: {variance_age:.2f}\nStandard Deviation: {stdev_age:.2f}\n"
              f"Range: {range_age}")
plt.text(0.98, 0.95, stats_text, ha='right', va='top', transform=plt.gca().transAxes,
         bbox=dict(facecolor='white', alpha=0.5))

# Adding labels, title, legend, and grid
plt.title('Distribution of Ages in Two Ranges (< 30 and >= 30) - Artists Only')
plt.xlabel('Age Range')
plt.ylabel('Frequency')
plt.legend(loc='lower left')
plt.grid(axis='y', alpha=0.75)

# Display the histogram with the vertical marker
plt.show()


# 3c - < 30 and >= 30 All-Up Charts - commercial success only - same as 2c2

import pandas as pd
import matplotlib.pyplot as plt

# Define file paths and corresponding columns
file_paths = [
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Year-End Charts Number Ones.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Best-Selling Albums.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Best-Selling Singles.csv'    
]

columns_to_extract = [
    'Artist Age',  # For the first 4 files
    'Artist Age',  # For the second file
    'Artist Age'  # For the third file    
]

# Combine the relevant data from all CSV files into one dataframe
all_data = pd.DataFrame()

for file_path, column in zip(file_paths, columns_to_extract):
    try:
        # Read the file
        data = pd.read_csv(file_path)
        
        # Check if the column exists and extract it
        if column in data.columns:
            temp_df = data[[column]].rename(columns={column: 'Age'})  # Standardize column name to 'Age'
            all_data = pd.concat([all_data, temp_df], ignore_index=True)
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

# Convert the 'Age' column to numeric, dropping any invalid entries
all_data['Age'] = pd.to_numeric(all_data['Age'], errors='coerce').dropna()

# Calculate statistics
mean_age = all_data['Age'].mean()
median_age = all_data['Age'].median()
mode_age = all_data['Age'].mode()[0] if not all_data['Age'].mode().empty else 'N/A'
stdev_age = all_data['Age'].std()
variance_age = all_data['Age'].var()
range_age = all_data['Age'].max() - all_data['Age'].min()

# Create two buckets: ages < 30 and >= 30
plt.figure(figsize=(8, 5))
age_bins = [0, 30, all_data['Age'].max() + 1]  # Adding 1 to include the max value in the >=30 bucket
bucket_labels = ['< 30', '>= 30']
bucket_counts = pd.cut(all_data['Age'], bins=age_bins, right=False, labels=bucket_labels).value_counts()

# Reorder the buckets to ensure '< 30' appears first
bucket_counts = bucket_counts.reindex(['< 30', '>= 30'])

# Plot the histogram with two buckets
plt.bar(bucket_counts.index, bucket_counts.values, color='#1f77b4', edgecolor='black', alpha=0.7)

# Display counts and percentages on the bars
total = len(all_data['Age'])
for index, value in enumerate(bucket_counts.values):
    percentage = (value / total) * 100
    plt.text(index, value, f'{value} ({percentage:.1f}%)', ha='center', va='bottom', fontsize=10)

# Add a vertical line for the 30-year mark
plt.axvline(x=0.5, color='purple', linestyle='-.', linewidth=1.5, label='Age 30')

# Add a text box with variance, standard deviation, and range
stats_text = (f"Variance: {variance_age:.2f}\nStandard Deviation: {stdev_age:.2f}\n"
              f"Range: {range_age}")
plt.text(0.98, 0.95, stats_text, ha='right', va='top', transform=plt.gca().transAxes,
         bbox=dict(facecolor='white', alpha=0.5))

# Adding labels, title, legend, and grid
plt.title('Distribution of Ages in Two Ranges (< 30 and >= 30) - Commercial Success Only')
plt.xlabel('Age Range')
plt.ylabel('Frequency')
plt.legend(loc='lower left')
plt.grid(axis='y', alpha=0.75)

# Display the histogram with the vertical marker
plt.show()


# 3d - < 30 and >= 30 All-Up Charts - critical acclaim only - same as 2d2

import pandas as pd
import matplotlib.pyplot as plt

# Define file paths and corresponding columns
file_paths = [
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Artists.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Producers.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Songwriters.csv'
]

columns_to_extract = [
    'Artist Age',  # For the fourth file
    'Producer Age',  # For the fifth file
    'Songwriter Age'  # For the sixth file
]

# Combine the relevant data from all CSV files into one dataframe
all_data = pd.DataFrame()

for file_path, column in zip(file_paths, columns_to_extract):
    try:
        # Read the file
        data = pd.read_csv(file_path)
        
        # Check if the column exists and extract it
        if column in data.columns:
            temp_df = data[[column]].rename(columns={column: 'Age'})  # Standardize column name to 'Age'
            all_data = pd.concat([all_data, temp_df], ignore_index=True)
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

# Convert the 'Age' column to numeric, dropping any invalid entries
all_data['Age'] = pd.to_numeric(all_data['Age'], errors='coerce').dropna()

# Calculate statistics
mean_age = all_data['Age'].mean()
median_age = all_data['Age'].median()
mode_age = all_data['Age'].mode()[0] if not all_data['Age'].mode().empty else 'N/A'
stdev_age = all_data['Age'].std()
variance_age = all_data['Age'].var()
range_age = all_data['Age'].max() - all_data['Age'].min()

# Create two buckets: ages < 30 and >= 30
plt.figure(figsize=(8, 5))
age_bins = [0, 30, all_data['Age'].max() + 1]  # Adding 1 to include the max value in the >=30 bucket
bucket_labels = ['< 30', '>= 30']
bucket_counts = pd.cut(all_data['Age'], bins=age_bins, right=False, labels=bucket_labels).value_counts()

# Reorder the buckets to ensure '< 30' appears first
bucket_counts = bucket_counts.reindex(['< 30', '>= 30'])

# Plot the histogram with two buckets
plt.bar(bucket_counts.index, bucket_counts.values, color='#1f77b4', edgecolor='black', alpha=0.7)

# Display counts and percentages on the bars
total = len(all_data['Age'])
for index, value in enumerate(bucket_counts.values):
    percentage = (value / total) * 100
    plt.text(index, value, f'{value} ({percentage:.1f}%)', ha='center', va='bottom', fontsize=10)

# Add a vertical line for the 30-year mark
plt.axvline(x=0.5, color='purple', linestyle='-.', linewidth=1.5, label='Age 30')

# Add a text box with variance, standard deviation, and range
stats_text = (f"Variance: {variance_age:.2f}\nStandard Deviation: {stdev_age:.2f}\n"
              f"Range: {range_age}")
plt.text(0.98, 0.95, stats_text, ha='right', va='top', transform=plt.gca().transAxes,
         bbox=dict(facecolor='white', alpha=0.5))

# Adding labels, title, legend, and grid
plt.title('Distribution of Ages in Two Ranges (< 30 and >= 30) - Critical Acclaim Only')
plt.xlabel('Age Range')
plt.ylabel('Frequency')
plt.legend(loc='lower left')
plt.grid(axis='y', alpha=0.75)

# Display the histogram with the vertical marker
plt.show()


# 3e - < 30 and >= 30 All-Up Charts - critical acclaim only - grammy artists only - same as 2e2

import pandas as pd
import matplotlib.pyplot as plt

# Define file paths and corresponding columns
file_paths = [
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Artists.csv'
]

columns_to_extract = [
    'Artist Age'  # For the fourth file    
]

# Combine the relevant data from all CSV files into one dataframe
all_data = pd.DataFrame()

for file_path, column in zip(file_paths, columns_to_extract):
    try:
        # Read the file
        data = pd.read_csv(file_path)
        
        # Check if the column exists and extract it
        if column in data.columns:
            temp_df = data[[column]].rename(columns={column: 'Age'})  # Standardize column name to 'Age'
            all_data = pd.concat([all_data, temp_df], ignore_index=True)
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

# Convert the 'Age' column to numeric, dropping any invalid entries
all_data['Age'] = pd.to_numeric(all_data['Age'], errors='coerce').dropna()

# Calculate statistics
mean_age = all_data['Age'].mean()
median_age = all_data['Age'].median()
mode_age = all_data['Age'].mode()[0] if not all_data['Age'].mode().empty else 'N/A'
stdev_age = all_data['Age'].std()
variance_age = all_data['Age'].var()
range_age = all_data['Age'].max() - all_data['Age'].min()

# Create two buckets: ages < 30 and >= 30
plt.figure(figsize=(8, 5))
age_bins = [0, 30, all_data['Age'].max() + 1]  # Adding 1 to include the max value in the >=30 bucket
bucket_labels = ['< 30', '>= 30']
bucket_counts = pd.cut(all_data['Age'], bins=age_bins, right=False, labels=bucket_labels).value_counts()

# Reorder the buckets to ensure '< 30' appears first
bucket_counts = bucket_counts.reindex(['< 30', '>= 30'])

# Plot the histogram with two buckets
plt.bar(bucket_counts.index, bucket_counts.values, color='#1f77b4', edgecolor='black', alpha=0.7)

# Display counts and percentages on the bars
total = len(all_data['Age'])
for index, value in enumerate(bucket_counts.values):
    percentage = (value / total) * 100
    plt.text(index, value, f'{value} ({percentage:.1f}%)', ha='center', va='bottom', fontsize=10)

# Add a vertical line for the 30-year mark
plt.axvline(x=0.5, color='purple', linestyle='-.', linewidth=1.5, label='Age 30')

# Add a text box with variance, standard deviation, and range
stats_text = (f"Variance: {variance_age:.2f}\nStandard Deviation: {stdev_age:.2f}\n"
              f"Range: {range_age}")
plt.text(0.98, 0.95, stats_text, ha='right', va='top', transform=plt.gca().transAxes,
         bbox=dict(facecolor='white', alpha=0.5))

# Adding labels, title, legend, and grid
plt.title('Distribution of Ages in Two Ranges (< 30 and >= 30) - Critical Acclaim Artists Only')
plt.xlabel('Age Range')
plt.ylabel('Frequency')
plt.legend(loc='lower left')
plt.grid(axis='y', alpha=0.75)

# Display the histogram with the vertical marker
plt.show()


# 3f - < 30 and >= 30 All-Up Charts - critical acclaim only - grammy producers and songwriters only - same as 2f1

import pandas as pd
import matplotlib.pyplot as plt

# Define file paths and corresponding columns
file_paths = [
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Producers.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Songwriters.csv'
]

columns_to_extract = [    
    'Producer Age',  # For the fifth file
    'Songwriter Age'  # For the sixth file
]

# Combine the relevant data from all CSV files into one dataframe
all_data = pd.DataFrame()

for file_path, column in zip(file_paths, columns_to_extract):
    try:
        # Read the file
        data = pd.read_csv(file_path)
        
        # Check if the column exists and extract it
        if column in data.columns:
            temp_df = data[[column]].rename(columns={column: 'Age'})  # Standardize column name to 'Age'
            all_data = pd.concat([all_data, temp_df], ignore_index=True)
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

# Convert the 'Age' column to numeric, dropping any invalid entries
all_data['Age'] = pd.to_numeric(all_data['Age'], errors='coerce').dropna()

# Calculate statistics
mean_age = all_data['Age'].mean()
median_age = all_data['Age'].median()
mode_age = all_data['Age'].mode()[0] if not all_data['Age'].mode().empty else 'N/A'
stdev_age = all_data['Age'].std()
variance_age = all_data['Age'].var()
range_age = all_data['Age'].max() - all_data['Age'].min()

# Create two buckets: ages < 30 and >= 30
plt.figure(figsize=(8, 5))
age_bins = [0, 30, all_data['Age'].max() + 1]  # Adding 1 to include the max value in the >=30 bucket
bucket_labels = ['< 30', '>= 30']
bucket_counts = pd.cut(all_data['Age'], bins=age_bins, right=False, labels=bucket_labels).value_counts()

# Reorder the buckets to ensure '< 30' appears first
bucket_counts = bucket_counts.reindex(['< 30', '>= 30'])

# Plot the histogram with two buckets
plt.bar(bucket_counts.index, bucket_counts.values, color='#1f77b4', edgecolor='black', alpha=0.7)

# Display counts and percentages on the bars
total = len(all_data['Age'])
for index, value in enumerate(bucket_counts.values):
    percentage = (value / total) * 100
    plt.text(index, value, f'{value} ({percentage:.1f}%)', ha='center', va='bottom', fontsize=10)

# Add a vertical line for the 30-year mark
plt.axvline(x=0.5, color='purple', linestyle='-.', linewidth=1.5, label='Age 30')

# Add a text box with variance, standard deviation, and range
stats_text = (f"Variance: {variance_age:.2f}\nStandard Deviation: {stdev_age:.2f}\n"
              f"Range: {range_age}")
plt.text(0.98, 0.95, stats_text, ha='right', va='top', transform=plt.gca().transAxes,
         bbox=dict(facecolor='white', alpha=0.5))

# Adding labels, title, legend, and grid
plt.title('Distr. of Ages in 2 Ranges (< 30 & >= 30) - Critical Accl. Producers & Songwriters')
plt.xlabel('Age Range')
plt.ylabel('Frequency')
plt.legend(loc='lower left')
plt.grid(axis='y', alpha=0.75)

# Display the histogram with the vertical marker
plt.show()


# 4 - Bar charts detail

# 4a - < 30 and >= 30 Detail Charts - over all data - commercial success and critical acclaim - same as 2a2

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Define file paths and corresponding columns
file_paths = [
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Year-End Charts Number Ones.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Best-Selling Albums.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Best-Selling Singles.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Artists.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Producers.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Songwriters.csv'
]

columns_to_extract = [
    'Artist Age',  # For the first file
    'Artist Age',  # For the second file
    'Artist Age',  # For the third file
    'Artist Age',  # For the fourth file
    'Producer Age',  # For the fifth file
    'Songwriter Age'  # For the sixth file
]

labels = [
    'WW Year-End Charts Number Ones',
    'WW Best-Selling Albums',
    'WW Best-Selling Singles',
    'US Grammy Winners - Artists',
    'US Grammy Winners - Producers',
    'US Grammy Winners - Songwriters'
]

# Data storage for plotting
bucket_counts_all = []

for file_path, column, label in zip(file_paths, columns_to_extract, labels):
    try:
        # Read the file
        data = pd.read_csv(file_path)
        
        # Check if the column exists and extract it
        if column in data.columns:
            ages = pd.to_numeric(data[column], errors='coerce').dropna()
            # Create two buckets: ages < 30 and >= 30
            age_bins = [0, 30, ages.max() + 1]  # Adding 1 to include the max value in the >=30 bucket
            bucket_labels = ['< 30', '>= 30']
            bucket_counts = pd.cut(ages, bins=age_bins, right=False, labels=bucket_labels).value_counts()
            bucket_counts_all.append(bucket_counts)
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

# Prepare data for grouped bar chart
x = np.arange(len(labels))  # x positions for each dataset
bar_width = 0.4

# Extract counts for each bucket
counts_below_30 = [bucket_counts['< 30'] if '< 30' in bucket_counts.index else 0 for bucket_counts in bucket_counts_all]
counts_above_30 = [bucket_counts['>= 30'] if '>= 30' in bucket_counts.index else 0 for bucket_counts in bucket_counts_all]

# Plot the bars
plt.figure(figsize=(14, 8))
bars1 = plt.bar(x - bar_width / 2, counts_below_30, bar_width, label='< 30', color='#1f77b4', alpha=0.7)
bars2 = plt.bar(x + bar_width / 2, counts_above_30, bar_width, label='>= 30', color='#7fb9f8', alpha=0.7)

# Annotate counts and percentages on top of bars
for i, (below, above) in enumerate(zip(counts_below_30, counts_above_30)):
    total = below + above
    if total > 0:  # Avoid division by zero
        percentage_below = (below / total) * 100
        percentage_above = (above / total) * 100
        # Annotate below 30
        plt.text(x[i] - bar_width / 2, below + 2, f'{below}\n({percentage_below:.1f}%)',
                 ha='center', va='bottom', fontsize=12, color='black')
        # Annotate above 30
        plt.text(x[i] + bar_width / 2, above + 2, f'{above}\n({percentage_above:.1f}%)',
                 ha='center', va='bottom', fontsize=12, color='black')

# Add labels, title, legend, and grid
plt.title('Age Distribution by Dataset (< 30 and >= 30) - All Data', fontsize=16)
plt.xlabel('Datasets', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.xticks(x, labels, rotation=45, ha='right', fontsize=12)
plt.legend(loc='upper right', fontsize=12)
plt.grid(axis='y', alpha=0.75)

# Adjust layout for better display
plt.tight_layout()
plt.show()


# 4b - < 30 and >= 30 Detail Charts - over artists only (excl. producers and songwriters) - commercial success and critical acclaim - same as 2b2

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Define file paths and corresponding columns
file_paths = [
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Year-End Charts Number Ones.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Best-Selling Albums.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Best-Selling Singles.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Artists.csv'    
]

columns_to_extract = [
    'Artist Age',  # For the first file
    'Artist Age',  # For the second file
    'Artist Age',  # For the third file
    'Artist Age'  # For the fourth file    
]

labels = [
    'WW Year-End Charts Number Ones',
    'WW Best-Selling Albums',
    'WW Best-Selling Singles',
    'US Grammy Winners - Artists'    
]

# Data storage for plotting
bucket_counts_all = []

for file_path, column, label in zip(file_paths, columns_to_extract, labels):
    try:
        # Read the file
        data = pd.read_csv(file_path)
        
        # Check if the column exists and extract it
        if column in data.columns:
            ages = pd.to_numeric(data[column], errors='coerce').dropna()
            # Create two buckets: ages < 30 and >= 30
            age_bins = [0, 30, ages.max() + 1]  # Adding 1 to include the max value in the >=30 bucket
            bucket_labels = ['< 30', '>= 30']
            bucket_counts = pd.cut(ages, bins=age_bins, right=False, labels=bucket_labels).value_counts()
            bucket_counts_all.append(bucket_counts)
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

# Prepare data for grouped bar chart
x = np.arange(len(labels))  # x positions for each dataset
bar_width = 0.4

# Extract counts for each bucket
counts_below_30 = [bucket_counts['< 30'] if '< 30' in bucket_counts.index else 0 for bucket_counts in bucket_counts_all]
counts_above_30 = [bucket_counts['>= 30'] if '>= 30' in bucket_counts.index else 0 for bucket_counts in bucket_counts_all]

# Plot the bars
plt.figure(figsize=(14, 8))
bars1 = plt.bar(x - bar_width / 2, counts_below_30, bar_width, label='< 30', color='#1f77b4', alpha=0.7)
bars2 = plt.bar(x + bar_width / 2, counts_above_30, bar_width, label='>= 30', color='#7fb9f8', alpha=0.7)

# Annotate counts and percentages on top of bars
for i, (below, above) in enumerate(zip(counts_below_30, counts_above_30)):
    total = below + above
    if total > 0:  # Avoid division by zero
        percentage_below = (below / total) * 100
        percentage_above = (above / total) * 100
        # Annotate below 30
        plt.text(x[i] - bar_width / 2, below + 2, f'{below}\n({percentage_below:.1f}%)',
                 ha='center', va='bottom', fontsize=12, color='black')
        # Annotate above 30
        plt.text(x[i] + bar_width / 2, above + 2, f'{above}\n({percentage_above:.1f}%)',
                 ha='center', va='bottom', fontsize=12, color='black')

# Add labels, title, legend, and grid
plt.title('Age Distribution by Dataset (< 30 and >= 30) - Artists Only', fontsize=16)
plt.xlabel('Datasets', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.xticks(x, labels, rotation=45, ha='right', fontsize=12)
plt.legend(loc='upper right', fontsize=12)
plt.grid(axis='y', alpha=0.75)

# Adjust layout for better display
plt.tight_layout()
plt.show()


# 4c - < 30 and >= 30 Detail Charts - commercial success only - same as 2c2

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Define file paths and corresponding columns
file_paths = [
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Year-End Charts Number Ones.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Best-Selling Albums.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Best-Selling Singles.csv'    
]

columns_to_extract = [
    'Artist Age',  # For the first file
    'Artist Age',  # For the second file
    'Artist Age'  # For the third file    
]

labels = [
    'WW Year-End Charts Number Ones',
    'WW Best-Selling Albums',
    'WW Best-Selling Singles',
]

# Data storage for plotting
bucket_counts_all = []

for file_path, column, label in zip(file_paths, columns_to_extract, labels):
    try:
        # Read the file
        data = pd.read_csv(file_path)
        
        # Check if the column exists and extract it
        if column in data.columns:
            ages = pd.to_numeric(data[column], errors='coerce').dropna()
            # Create two buckets: ages < 30 and >= 30
            age_bins = [0, 30, ages.max() + 1]  # Adding 1 to include the max value in the >=30 bucket
            bucket_labels = ['< 30', '>= 30']
            bucket_counts = pd.cut(ages, bins=age_bins, right=False, labels=bucket_labels).value_counts()
            bucket_counts_all.append(bucket_counts)
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

# Prepare data for grouped bar chart
x = np.arange(len(labels))  # x positions for each dataset
bar_width = 0.4

# Extract counts for each bucket
counts_below_30 = [bucket_counts['< 30'] if '< 30' in bucket_counts.index else 0 for bucket_counts in bucket_counts_all]
counts_above_30 = [bucket_counts['>= 30'] if '>= 30' in bucket_counts.index else 0 for bucket_counts in bucket_counts_all]

# Plot the bars
plt.figure(figsize=(14, 8))
bars1 = plt.bar(x - bar_width / 2, counts_below_30, bar_width, label='< 30', color='#1f77b4', alpha=0.7)
bars2 = plt.bar(x + bar_width / 2, counts_above_30, bar_width, label='>= 30', color='#7fb9f8', alpha=0.7)

# Annotate counts and percentages on top of bars
for i, (below, above) in enumerate(zip(counts_below_30, counts_above_30)):
    total = below + above
    if total > 0:  # Avoid division by zero
        percentage_below = (below / total) * 100
        percentage_above = (above / total) * 100
        # Annotate below 30
        plt.text(x[i] - bar_width / 2, below + 2, f'{below}\n({percentage_below:.1f}%)',
                 ha='center', va='bottom', fontsize=12, color='black')
        # Annotate above 30
        plt.text(x[i] + bar_width / 2, above + 2, f'{above}\n({percentage_above:.1f}%)',
                 ha='center', va='bottom', fontsize=12, color='black')

# Add labels, title, legend, and grid
plt.title('Age Distribution by Dataset (< 30 and >= 30) - Commercial Success Only', fontsize=16)
plt.xlabel('Datasets', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.xticks(x, labels, rotation=45, ha='right', fontsize=12)
plt.legend(loc='upper right', fontsize=12)
plt.grid(axis='y', alpha=0.75)

# Adjust layout for better display
plt.tight_layout()
plt.show()


# 4d - < 30 and >= 30 Detail Charts - critical acclaim only - same as 2d2

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Define file paths and corresponding columns
file_paths = [    
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Artists.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Producers.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Songwriters.csv'
]

columns_to_extract = [
    'Artist Age',  # For the fourth file
    'Producer Age',  # For the fifth file
    'Songwriter Age'  # For the sixth file
]

labels = [
    'US Grammy Winners - Artists',
    'US Grammy Winners - Producers',
    'US Grammy Winners - Songwriters'
]

# Data storage for plotting
bucket_counts_all = []

for file_path, column, label in zip(file_paths, columns_to_extract, labels):
    try:
        # Read the file
        data = pd.read_csv(file_path)
        
        # Check if the column exists and extract it
        if column in data.columns:
            ages = pd.to_numeric(data[column], errors='coerce').dropna()
            # Create two buckets: ages < 30 and >= 30
            age_bins = [0, 30, ages.max() + 1]  # Adding 1 to include the max value in the >=30 bucket
            bucket_labels = ['< 30', '>= 30']
            bucket_counts = pd.cut(ages, bins=age_bins, right=False, labels=bucket_labels).value_counts()
            bucket_counts_all.append(bucket_counts)
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

# Prepare data for grouped bar chart
x = np.arange(len(labels))  # x positions for each dataset
bar_width = 0.4

# Extract counts for each bucket
counts_below_30 = [bucket_counts['< 30'] if '< 30' in bucket_counts.index else 0 for bucket_counts in bucket_counts_all]
counts_above_30 = [bucket_counts['>= 30'] if '>= 30' in bucket_counts.index else 0 for bucket_counts in bucket_counts_all]

# Plot the bars
plt.figure(figsize=(14, 8))
bars1 = plt.bar(x - bar_width / 2, counts_below_30, bar_width, label='< 30', color='#1f77b4', alpha=0.7)
bars2 = plt.bar(x + bar_width / 2, counts_above_30, bar_width, label='>= 30', color='#7fb9f8', alpha=0.7)

# Annotate counts and percentages on top of bars
for i, (below, above) in enumerate(zip(counts_below_30, counts_above_30)):
    total = below + above
    if total > 0:  # Avoid division by zero
        percentage_below = (below / total) * 100
        percentage_above = (above / total) * 100
        # Annotate below 30
        plt.text(x[i] - bar_width / 2, below + 2, f'{below}\n({percentage_below:.1f}%)',
                 ha='center', va='bottom', fontsize=12, color='black')
        # Annotate above 30
        plt.text(x[i] + bar_width / 2, above + 2, f'{above}\n({percentage_above:.1f}%)',
                 ha='center', va='bottom', fontsize=12, color='black')

# Add labels, title, legend, and grid
plt.title('Age Distribution by Dataset (< 30 and >= 30) - Critical Acclaim Only', fontsize=16)
plt.xlabel('Datasets', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.xticks(x, labels, rotation=45, ha='right', fontsize=12)
plt.legend(loc='upper right', fontsize=12)
plt.grid(axis='y', alpha=0.75)

# Adjust layout for better display
plt.tight_layout()
plt.show()


# 4e - < 30 and >= 30 Detail Charts - critical acclaim only - grammy artists only - same as 2e2

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Define file paths and corresponding columns
file_paths = [
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Artists.csv'    
]

columns_to_extract = [    
    'Artist Age',  # For the fourth file    
]

labels = [    
    'US Grammy Winners - Artists'    
]

# Data storage for plotting
bucket_counts_all = []

for file_path, column, label in zip(file_paths, columns_to_extract, labels):
    try:
        # Read the file
        data = pd.read_csv(file_path)
        
        # Check if the column exists and extract it
        if column in data.columns:
            ages = pd.to_numeric(data[column], errors='coerce').dropna()
            # Create two buckets: ages < 30 and >= 30
            age_bins = [0, 30, ages.max() + 1]  # Adding 1 to include the max value in the >=30 bucket
            bucket_labels = ['< 30', '>= 30']
            bucket_counts = pd.cut(ages, bins=age_bins, right=False, labels=bucket_labels).value_counts()
            bucket_counts_all.append(bucket_counts)
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

# Prepare data for grouped bar chart
x = np.arange(len(labels))  # x positions for each dataset
bar_width = 0.4

# Extract counts for each bucket
counts_below_30 = [bucket_counts['< 30'] if '< 30' in bucket_counts.index else 0 for bucket_counts in bucket_counts_all]
counts_above_30 = [bucket_counts['>= 30'] if '>= 30' in bucket_counts.index else 0 for bucket_counts in bucket_counts_all]

# Plot the bars
plt.figure(figsize=(14, 8))
bars1 = plt.bar(x - bar_width / 2, counts_below_30, bar_width, label='< 30', color='#1f77b4', alpha=0.7)
bars2 = plt.bar(x + bar_width / 2, counts_above_30, bar_width, label='>= 30', color='#7fb9f8', alpha=0.7)

# Annotate counts and percentages on top of bars
for i, (below, above) in enumerate(zip(counts_below_30, counts_above_30)):
    total = below + above
    if total > 0:  # Avoid division by zero
        percentage_below = (below / total) * 100
        percentage_above = (above / total) * 100
        # Annotate below 30
        plt.text(x[i] - bar_width / 2, below + 2, f'{below}\n({percentage_below:.1f}%)',
                 ha='center', va='bottom', fontsize=12, color='black')
        # Annotate above 30
        plt.text(x[i] + bar_width / 2, above + 2, f'{above}\n({percentage_above:.1f}%)',
                 ha='center', va='bottom', fontsize=12, color='black')

# Add labels, title, legend, and grid
plt.title('Age Distribution by Dataset (< 30 and >= 30) - Critical Acclaim Artists Only', fontsize=16)
plt.xlabel('Datasets', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.xticks(x, labels, rotation=45, ha='right', fontsize=12)
plt.legend(loc='upper right', fontsize=12)
plt.grid(axis='y', alpha=0.75)

# Adjust layout for better display
plt.tight_layout()
plt.show()


# 4f - < 30 and >= 30 Detail Charts - critical acclaim only - grammy producers and songwriters only - same as 2f1

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Define file paths and corresponding columns
file_paths = [    
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Producers.csv',
    r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Songwriters.csv'
]

columns_to_extract = [    
    'Producer Age',  # For the fifth file
    'Songwriter Age'  # For the sixth file
]

labels = [    
    'US Grammy Winners - Producers',
    'US Grammy Winners - Songwriters'
]

# Data storage for plotting
bucket_counts_all = []

for file_path, column, label in zip(file_paths, columns_to_extract, labels):
    try:
        # Read the file
        data = pd.read_csv(file_path)
        
        # Check if the column exists and extract it
        if column in data.columns:
            ages = pd.to_numeric(data[column], errors='coerce').dropna()
            # Create two buckets: ages < 30 and >= 30
            age_bins = [0, 30, ages.max() + 1]  # Adding 1 to include the max value in the >=30 bucket
            bucket_labels = ['< 30', '>= 30']
            bucket_counts = pd.cut(ages, bins=age_bins, right=False, labels=bucket_labels).value_counts()
            bucket_counts_all.append(bucket_counts)
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

# Prepare data for grouped bar chart
x = np.arange(len(labels))  # x positions for each dataset
bar_width = 0.4

# Extract counts for each bucket
counts_below_30 = [bucket_counts['< 30'] if '< 30' in bucket_counts.index else 0 for bucket_counts in bucket_counts_all]
counts_above_30 = [bucket_counts['>= 30'] if '>= 30' in bucket_counts.index else 0 for bucket_counts in bucket_counts_all]

# Plot the bars
plt.figure(figsize=(14, 8))
bars1 = plt.bar(x - bar_width / 2, counts_below_30, bar_width, label='< 30', color='#1f77b4', alpha=0.7)
bars2 = plt.bar(x + bar_width / 2, counts_above_30, bar_width, label='>= 30', color='#7fb9f8', alpha=0.7)

# Annotate counts and percentages on top of bars
for i, (below, above) in enumerate(zip(counts_below_30, counts_above_30)):
    total = below + above
    if total > 0:  # Avoid division by zero
        percentage_below = (below / total) * 100
        percentage_above = (above / total) * 100
        # Annotate below 30
        plt.text(x[i] - bar_width / 2, below + 2, f'{below}\n({percentage_below:.1f}%)',
                 ha='center', va='bottom', fontsize=12, color='black')
        # Annotate above 30
        plt.text(x[i] + bar_width / 2, above + 2, f'{above}\n({percentage_above:.1f}%)',
                 ha='center', va='bottom', fontsize=12, color='black')

# Add labels, title, legend, and grid
plt.title('Age Distribution by Dataset (< 30 and >= 30) - Critical Acclaim Producers & Songwriters only', fontsize=16)
plt.xlabel('Datasets', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.xticks(x, labels, rotation=45, ha='right', fontsize=12)
plt.legend(loc='upper right', fontsize=12)
plt.grid(axis='y', alpha=0.75)

# Adjust layout for better display
plt.tight_layout()
plt.show()


# 5 - Intelligence charts

# 5a - < 30 and >= 30 Detail Charts - over all data - commercial success and critical acclaim - same as 2a2

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statistics import mode 

# Load data from all files
files = {
    'WW Year-End Charts': r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Year-End Charts Number Ones.csv',
    'WW Best-Selling Albums': r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Best-Selling Albums.csv',
    'WW Best-Selling Singles': r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Best-Selling Singles.csv',
    'US Grammy Winners - Artists': r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Artists.csv',
    'US Grammy Winners - Producers': r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Producers.csv',
    'US Grammy Winners - Songwriters': r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Songwriters.csv'
}

columns = {
    'WW Year-End Charts': 'Artist Age',
    'WW Best-Selling Albums': 'Artist Age',
    'WW Best-Selling Singles': 'Artist Age',
    'US Grammy Winners - Artists': 'Artist Age',
    'US Grammy Winners - Producers': 'Producer Age',
    'US Grammy Winners - Songwriters': 'Songwriter Age'
}

# Combine ages from all files into one list
all_ages = []

for key, file in files.items():
    df = pd.read_csv(file)
    column_name = columns[key]
    if column_name in df.columns:
        ages = df[column_name].dropna()
        all_ages.extend(ages)

# Convert all ages to a pandas Series
all_ages_series = pd.Series(all_ages)

# Calculate statistics for the combined artist age distribution
mean_age = all_ages_series.mean()
median_age = all_ages_series.median()
try:
    mode_age = mode(all_ages_series)
except:
    mode_age = 'N/A'
stdev_age = all_ages_series.std()
variance_age = all_ages_series.var()
min_age = all_ages_series.min()
max_age = all_ages_series.max()
range_age = max_age - min_age

# Define the extended age range for cognitive abilities (0 to 100)
ages = np.arange(0, 101, 5)

# Simulate realistic cognitive performance data using consistent piecewise functions
fluid_intelligence = np.piecewise(
    ages, 
    [ages < 5, (ages >= 5) & (ages < 20), ages >= 20],
    [lambda x: 20 * x, lambda x: 5 * x, lambda x: np.maximum(100 - 0.7 * (x - 20), 20)]
)
crystallized_intelligence = np.piecewise(
    ages,
    [ages < 5, (ages >= 5) & (ages < 20), ages >= 20],
    [lambda x: 10 * x, lambda x: 2.5 * x, lambda x: np.maximum(50 + 0.3 * (x - 20), 30)]
)
short_term_memory = np.piecewise(
    ages,
    [ages < 5, (ages >= 5) & (ages < 20), ages >= 20],
    [lambda x: 15 * x, lambda x: 4.5 * x, lambda x: np.maximum(90 - 0.5 * (x - 20), 20)]
)
processing_speed = np.piecewise(
    ages,
    [ages < 5, (ages >= 5) & (ages < 20), ages >= 20],
    [lambda x: 20 * x, lambda x: 5 * x, lambda x: np.maximum(100 - 0.9 * (x - 20), 15)]
)
executive_function = np.piecewise(
    ages,
    [ages < 5, (ages >= 5) & (ages < 20), ages >= 20],
    [lambda x: 18 * x, lambda x: 4 * x, lambda x: np.maximum(100 - 0.6 * (x - 20), 20)]
)

# Combined age and cognitive performance chart
fig, ax1 = plt.subplots(figsize=(12, 8))

# Plot the histogram for combined ages (primary y-axis)
counts, bins, patches = ax1.hist(all_ages_series, bins=20, color='#1f77b4', edgecolor='black', alpha=0.7)
ax1.set_xlabel('Age')
ax1.set_ylabel('Frequency of Ages', color='black')
ax1.tick_params(axis='y', labelcolor='black')
ax1.grid(axis='y', alpha=0.75)

# Add vertical lines for mean, median, mode, and 30-year mark
ax1.axvline(mean_age, color='red', linestyle='--', linewidth=1.5, label='Mean')
ax1.axvline(median_age, color='green', linestyle='-', linewidth=1.5, label='Median')
ax1.axvline(30, color='cyan', linestyle='--', linewidth=1.5, label='30-Year Mark')  # 30-year-old line
if mode_age != 'N/A':
    ax1.axvline(mode_age, color='blue', linestyle='-', linewidth=1.5, label='Mode')

# Create a secondary y-axis for cognitive abilities
ax2 = ax1.twinx()
ax2.set_ylabel('Cognitive Performance (%)', color='black')
ax2.plot(ages, fluid_intelligence, label="Fluid Intelligence", linestyle='-', marker='o', color='purple')
ax2.plot(ages, crystallized_intelligence, label="Crystallized Intelligence", linestyle='-', marker='o', color='orange')
ax2.plot(ages, short_term_memory, label="Short-term Memory", linestyle='-', marker='o', color='green')
ax2.plot(ages, processing_speed, label="Processing Speed", linestyle='-', marker='o', color='red')
ax2.plot(ages, executive_function, label="Executive Function", linestyle='-', marker='o', color='brown')
ax2.tick_params(axis='y', labelcolor='black')

# Move the text box with statistical values to the top left
stats_text = (f"Mean: {mean_age:.2f}\nMedian: {median_age:.2f}\nMode: {mode_age}\n"
              f"Variance: {variance_age:.2f}\nStd Dev: {stdev_age:.2f}\n"
              f"Range: {range_age}\nMin Age: {min_age}\nMax Age: {max_age}")
ax1.text(0.02, 0.98, stats_text, ha='left', va='top', transform=ax1.transAxes,
         bbox=dict(facecolor='white', alpha=0.7))

# Combine all legends into one box on the top right
handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
handles = handles1 + handles2
labels = labels1 + labels2
ax1.legend(handles=handles, labels=labels, loc='upper right', fontsize=10)

# Add title and adjust layout
plt.title('Combined Age Distribution and Cognitive Abilities Across the Lifespan (0-100 Years) - All Data', fontsize=16)
fig.tight_layout()

# Display the chart
plt.show()


# 5b - < 30 and >= 30 Detail Charts - over artists only (excl. producers and songwriters) - commercial success and critical acclaim - same as 2b2

 # Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statistics import mode 

# Load data from all files
files = {
    'WW Year-End Charts': r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Year-End Charts Number Ones.csv',
    'WW Best-Selling Albums': r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Best-Selling Albums.csv',
    'WW Best-Selling Singles': r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Best-Selling Singles.csv',
    'US Grammy Winners - Artists': r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Artists.csv'    
}

columns = {
    'WW Year-End Charts': 'Artist Age',
    'WW Best-Selling Albums': 'Artist Age',
    'WW Best-Selling Singles': 'Artist Age',
    'US Grammy Winners - Artists': 'Artist Age'    
}

# Combine ages from all files into one list
all_ages = []

for key, file in files.items():
    df = pd.read_csv(file)
    column_name = columns[key]
    if column_name in df.columns:
        ages = df[column_name].dropna()
        all_ages.extend(ages)

# Convert all ages to a pandas Series
all_ages_series = pd.Series(all_ages)

# Calculate statistics for the combined artist age distribution
mean_age = all_ages_series.mean()
median_age = all_ages_series.median()
try:
    mode_age = mode(all_ages_series)
except:
    mode_age = 'N/A'
stdev_age = all_ages_series.std()
variance_age = all_ages_series.var()
min_age = all_ages_series.min()
max_age = all_ages_series.max()
range_age = max_age - min_age

# Define the extended age range for cognitive abilities (0 to 100)
ages = np.arange(0, 101, 5)

# Simulate realistic cognitive performance data using consistent piecewise functions
fluid_intelligence = np.piecewise(
    ages, 
    [ages < 5, (ages >= 5) & (ages < 20), ages >= 20],
    [lambda x: 20 * x, lambda x: 5 * x, lambda x: np.maximum(100 - 0.7 * (x - 20), 20)]
)
crystallized_intelligence = np.piecewise(
    ages,
    [ages < 5, (ages >= 5) & (ages < 20), ages >= 20],
    [lambda x: 10 * x, lambda x: 2.5 * x, lambda x: np.maximum(50 + 0.3 * (x - 20), 30)]
)
short_term_memory = np.piecewise(
    ages,
    [ages < 5, (ages >= 5) & (ages < 20), ages >= 20],
    [lambda x: 15 * x, lambda x: 4.5 * x, lambda x: np.maximum(90 - 0.5 * (x - 20), 20)]
)
processing_speed = np.piecewise(
    ages,
    [ages < 5, (ages >= 5) & (ages < 20), ages >= 20],
    [lambda x: 20 * x, lambda x: 5 * x, lambda x: np.maximum(100 - 0.9 * (x - 20), 15)]
)
executive_function = np.piecewise(
    ages,
    [ages < 5, (ages >= 5) & (ages < 20), ages >= 20],
    [lambda x: 18 * x, lambda x: 4 * x, lambda x: np.maximum(100 - 0.6 * (x - 20), 20)]
)

# Combined age and cognitive performance chart
fig, ax1 = plt.subplots(figsize=(12, 8))

# Plot the histogram for combined ages (primary y-axis)
counts, bins, patches = ax1.hist(all_ages_series, bins=20, color='#1f77b4', edgecolor='black', alpha=0.7)
ax1.set_xlabel('Age')
ax1.set_ylabel('Frequency of Ages', color='black')
ax1.tick_params(axis='y', labelcolor='black')
ax1.grid(axis='y', alpha=0.75)

# Add vertical lines for mean, median, mode, and 30-year mark
ax1.axvline(mean_age, color='red', linestyle='--', linewidth=1.5, label='Mean')
ax1.axvline(median_age, color='green', linestyle='-', linewidth=1.5, label='Median')
ax1.axvline(30, color='cyan', linestyle='--', linewidth=1.5, label='30-Year Mark')  # 30-year-old line
if mode_age != 'N/A':
    ax1.axvline(mode_age, color='blue', linestyle='-', linewidth=1.5, label='Mode')

# Create a secondary y-axis for cognitive abilities
ax2 = ax1.twinx()
ax2.set_ylabel('Cognitive Performance (%)', color='black')
ax2.plot(ages, fluid_intelligence, label="Fluid Intelligence", linestyle='-', marker='o', color='purple')
ax2.plot(ages, crystallized_intelligence, label="Crystallized Intelligence", linestyle='-', marker='o', color='orange')
ax2.plot(ages, short_term_memory, label="Short-term Memory", linestyle='-', marker='o', color='green')
ax2.plot(ages, processing_speed, label="Processing Speed", linestyle='-', marker='o', color='red')
ax2.plot(ages, executive_function, label="Executive Function", linestyle='-', marker='o', color='brown')
ax2.tick_params(axis='y', labelcolor='black')

# Move the text box with statistical values to the top left
stats_text = (f"Mean: {mean_age:.2f}\nMedian: {median_age:.2f}\nMode: {mode_age}\n"
              f"Variance: {variance_age:.2f}\nStd Dev: {stdev_age:.2f}\n"
              f"Range: {range_age}\nMin Age: {min_age}\nMax Age: {max_age}")
ax1.text(0.02, 0.98, stats_text, ha='left', va='top', transform=ax1.transAxes,
         bbox=dict(facecolor='white', alpha=0.7))

# Combine all legends into one box on the top right
handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
handles = handles1 + handles2
labels = labels1 + labels2
ax1.legend(handles=handles, labels=labels, loc='upper right', fontsize=10)

# Add title and adjust layout
plt.title('Combined Age Distribution and Cognitive Abilities Across the Lifespan (0-100 Years) - Artists Only', fontsize=16)
fig.tight_layout()

# Display the chart
plt.show()


 # 5c - < 30 and >= 30 Detail Charts - commercial success only - same as 2c2

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statistics import mode 

# Load data from all files
files = {
    'WW Year-End Charts': r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Year-End Charts Number Ones.csv',
    'WW Best-Selling Albums': r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Best-Selling Albums.csv',
    'WW Best-Selling Singles': r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Best-Selling Singles.csv'    
}

columns = {
    'WW Year-End Charts': 'Artist Age',
    'WW Best-Selling Albums': 'Artist Age',
    'WW Best-Selling Singles': 'Artist Age'    
}

# Combine ages from all files into one list
all_ages = []

for key, file in files.items():
    df = pd.read_csv(file)
    column_name = columns[key]
    if column_name in df.columns:
        ages = df[column_name].dropna()
        all_ages.extend(ages)

# Convert all ages to a pandas Series
all_ages_series = pd.Series(all_ages)

# Calculate statistics for the combined artist age distribution
mean_age = all_ages_series.mean()
median_age = all_ages_series.median()
try:
    mode_age = mode(all_ages_series)
except:
    mode_age = 'N/A'
stdev_age = all_ages_series.std()
variance_age = all_ages_series.var()
min_age = all_ages_series.min()
max_age = all_ages_series.max()
range_age = max_age - min_age

# Define the extended age range for cognitive abilities (0 to 100)
ages = np.arange(0, 101, 5)

# Simulate realistic cognitive performance data using consistent piecewise functions
fluid_intelligence = np.piecewise(
    ages, 
    [ages < 5, (ages >= 5) & (ages < 20), ages >= 20],
    [lambda x: 20 * x, lambda x: 5 * x, lambda x: np.maximum(100 - 0.7 * (x - 20), 20)]
)
crystallized_intelligence = np.piecewise(
    ages,
    [ages < 5, (ages >= 5) & (ages < 20), ages >= 20],
    [lambda x: 10 * x, lambda x: 2.5 * x, lambda x: np.maximum(50 + 0.3 * (x - 20), 30)]
)
short_term_memory = np.piecewise(
    ages,
    [ages < 5, (ages >= 5) & (ages < 20), ages >= 20],
    [lambda x: 15 * x, lambda x: 4.5 * x, lambda x: np.maximum(90 - 0.5 * (x - 20), 20)]
)
processing_speed = np.piecewise(
    ages,
    [ages < 5, (ages >= 5) & (ages < 20), ages >= 20],
    [lambda x: 20 * x, lambda x: 5 * x, lambda x: np.maximum(100 - 0.9 * (x - 20), 15)]
)
executive_function = np.piecewise(
    ages,
    [ages < 5, (ages >= 5) & (ages < 20), ages >= 20],
    [lambda x: 18 * x, lambda x: 4 * x, lambda x: np.maximum(100 - 0.6 * (x - 20), 20)]
)

# Combined age and cognitive performance chart
fig, ax1 = plt.subplots(figsize=(12, 8))

# Plot the histogram for combined ages (primary y-axis)
counts, bins, patches = ax1.hist(all_ages_series, bins=20, color='#1f77b4', edgecolor='black', alpha=0.7)
ax1.set_xlabel('Age')
ax1.set_ylabel('Frequency of Ages', color='black')
ax1.tick_params(axis='y', labelcolor='black')
ax1.grid(axis='y', alpha=0.75)

# Add vertical lines for mean, median, mode, and 30-year mark
ax1.axvline(mean_age, color='red', linestyle='--', linewidth=1.5, label='Mean')
ax1.axvline(median_age, color='green', linestyle='-', linewidth=1.5, label='Median')
ax1.axvline(30, color='cyan', linestyle='--', linewidth=1.5, label='30-Year Mark')  # 30-year-old line
if mode_age != 'N/A':
    ax1.axvline(mode_age, color='blue', linestyle='-', linewidth=1.5, label='Mode')

# Create a secondary y-axis for cognitive abilities
ax2 = ax1.twinx()
ax2.set_ylabel('Cognitive Performance (%)', color='black')
ax2.plot(ages, fluid_intelligence, label="Fluid Intelligence", linestyle='-', marker='o', color='purple')
ax2.plot(ages, crystallized_intelligence, label="Crystallized Intelligence", linestyle='-', marker='o', color='orange')
ax2.plot(ages, short_term_memory, label="Short-term Memory", linestyle='-', marker='o', color='green')
ax2.plot(ages, processing_speed, label="Processing Speed", linestyle='-', marker='o', color='red')
ax2.plot(ages, executive_function, label="Executive Function", linestyle='-', marker='o', color='brown')
ax2.tick_params(axis='y', labelcolor='black')

# Move the text box with statistical values to the top left
stats_text = (f"Mean: {mean_age:.2f}\nMedian: {median_age:.2f}\nMode: {mode_age}\n"
              f"Variance: {variance_age:.2f}\nStd Dev: {stdev_age:.2f}\n"
              f"Range: {range_age}\nMin Age: {min_age}\nMax Age: {max_age}")
ax1.text(0.02, 0.98, stats_text, ha='left', va='top', transform=ax1.transAxes,
         bbox=dict(facecolor='white', alpha=0.7))

# Combine all legends into one box on the top right
handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
handles = handles1 + handles2
labels = labels1 + labels2
ax1.legend(handles=handles, labels=labels, loc='upper right', fontsize=10)

# Add title and adjust layout
plt.title('Combined Age Distr. & Cognitive Abilities Across the Lifespan (0-100 Yrs) - Commercial Success', fontsize=16)
fig.tight_layout()

# Display the chart
plt.show()


# 5d - < 30 and >= 30 Detail Charts - critical acclaim only - same as 2d2

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statistics import mode 

# Load data from all files
files = {    
    'US Grammy Winners - Artists': r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Artists.csv',
    'US Grammy Winners - Producers': r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Producers.csv',
    'US Grammy Winners - Songwriters': r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Songwriters.csv'
}

columns = {    
    'US Grammy Winners - Artists': 'Artist Age',
    'US Grammy Winners - Producers': 'Producer Age',
    'US Grammy Winners - Songwriters': 'Songwriter Age'
}

# Combine ages from all files into one list
all_ages = []

for key, file in files.items():
    df = pd.read_csv(file)
    column_name = columns[key]
    if column_name in df.columns:
        ages = df[column_name].dropna()
        all_ages.extend(ages)

# Convert all ages to a pandas Series
all_ages_series = pd.Series(all_ages)

# Calculate statistics for the combined artist age distribution
mean_age = all_ages_series.mean()
median_age = all_ages_series.median()
try:
    mode_age = mode(all_ages_series)
except:
    mode_age = 'N/A'
stdev_age = all_ages_series.std()
variance_age = all_ages_series.var()
min_age = all_ages_series.min()
max_age = all_ages_series.max()
range_age = max_age - min_age

# Define the extended age range for cognitive abilities (0 to 100)
ages = np.arange(0, 101, 5)

# Simulate realistic cognitive performance data using consistent piecewise functions
fluid_intelligence = np.piecewise(
    ages, 
    [ages < 5, (ages >= 5) & (ages < 20), ages >= 20],
    [lambda x: 20 * x, lambda x: 5 * x, lambda x: np.maximum(100 - 0.7 * (x - 20), 20)]
)
crystallized_intelligence = np.piecewise(
    ages,
    [ages < 5, (ages >= 5) & (ages < 20), ages >= 20],
    [lambda x: 10 * x, lambda x: 2.5 * x, lambda x: np.maximum(50 + 0.3 * (x - 20), 30)]
)
short_term_memory = np.piecewise(
    ages,
    [ages < 5, (ages >= 5) & (ages < 20), ages >= 20],
    [lambda x: 15 * x, lambda x: 4.5 * x, lambda x: np.maximum(90 - 0.5 * (x - 20), 20)]
)
processing_speed = np.piecewise(
    ages,
    [ages < 5, (ages >= 5) & (ages < 20), ages >= 20],
    [lambda x: 20 * x, lambda x: 5 * x, lambda x: np.maximum(100 - 0.9 * (x - 20), 15)]
)
executive_function = np.piecewise(
    ages,
    [ages < 5, (ages >= 5) & (ages < 20), ages >= 20],
    [lambda x: 18 * x, lambda x: 4 * x, lambda x: np.maximum(100 - 0.6 * (x - 20), 20)]
)

# Combined age and cognitive performance chart
fig, ax1 = plt.subplots(figsize=(12, 8))

# Plot the histogram for combined ages (primary y-axis)
counts, bins, patches = ax1.hist(all_ages_series, bins=20, color='#1f77b4', edgecolor='black', alpha=0.7)
ax1.set_xlabel('Age')
ax1.set_ylabel('Frequency of Ages', color='black')
ax1.tick_params(axis='y', labelcolor='black')
ax1.grid(axis='y', alpha=0.75)

# Add vertical lines for mean, median, mode, and 30-year mark
ax1.axvline(mean_age, color='red', linestyle='--', linewidth=1.5, label='Mean')
ax1.axvline(median_age, color='green', linestyle='-', linewidth=1.5, label='Median')
ax1.axvline(30, color='cyan', linestyle='--', linewidth=1.5, label='30-Year Mark')  # 30-year-old line
if mode_age != 'N/A':
    ax1.axvline(mode_age, color='blue', linestyle='-', linewidth=1.5, label='Mode')

# Create a secondary y-axis for cognitive abilities
ax2 = ax1.twinx()
ax2.set_ylabel('Cognitive Performance (%)', color='black')
ax2.plot(ages, fluid_intelligence, label="Fluid Intelligence", linestyle='-', marker='o', color='purple')
ax2.plot(ages, crystallized_intelligence, label="Crystallized Intelligence", linestyle='-', marker='o', color='orange')
ax2.plot(ages, short_term_memory, label="Short-term Memory", linestyle='-', marker='o', color='green')
ax2.plot(ages, processing_speed, label="Processing Speed", linestyle='-', marker='o', color='red')
ax2.plot(ages, executive_function, label="Executive Function", linestyle='-', marker='o', color='brown')
ax2.tick_params(axis='y', labelcolor='black')

# Move the text box with statistical values to the top left
stats_text = (f"Mean: {mean_age:.2f}\nMedian: {median_age:.2f}\nMode: {mode_age}\n"
              f"Variance: {variance_age:.2f}\nStd Dev: {stdev_age:.2f}\n"
              f"Range: {range_age}\nMin Age: {min_age}\nMax Age: {max_age}")
ax1.text(0.02, 0.98, stats_text, ha='left', va='top', transform=ax1.transAxes,
         bbox=dict(facecolor='white', alpha=0.7))

# Combine all legends into one box on the top right
handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
handles = handles1 + handles2
labels = labels1 + labels2
ax1.legend(handles=handles, labels=labels, loc='upper right', fontsize=10)

# Add title and adjust layout
plt.title('Combined Age Distribution and Cognitive Abilities Across the Lifespan (0-100 Years) - Critical Acclaim Only', fontsize=16)
fig.tight_layout()

# Display the chart
plt.show()


 # 5e - < 30 and >= 30 Detail Charts - critical acclaim only - grammy artists only - same as 2e2

 # Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statistics import mode 

# Load data from all files
files = {    
    'US Grammy Winners - Artists': r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Artists.csv'    
}

columns = {    
    'US Grammy Winners - Artists': 'Artist Age'    
}

# Combine ages from all files into one list
all_ages = []

for key, file in files.items():
    df = pd.read_csv(file)
    column_name = columns[key]
    if column_name in df.columns:
        ages = df[column_name].dropna()
        all_ages.extend(ages)

# Convert all ages to a pandas Series
all_ages_series = pd.Series(all_ages)

# Calculate statistics for the combined artist age distribution
mean_age = all_ages_series.mean()
median_age = all_ages_series.median()
try:
    mode_age = mode(all_ages_series)
except:
    mode_age = 'N/A'
stdev_age = all_ages_series.std()
variance_age = all_ages_series.var()
min_age = all_ages_series.min()
max_age = all_ages_series.max()
range_age = max_age - min_age

# Define the extended age range for cognitive abilities (0 to 100)
ages = np.arange(0, 101, 5)

# Simulate realistic cognitive performance data using consistent piecewise functions
fluid_intelligence = np.piecewise(
    ages, 
    [ages < 5, (ages >= 5) & (ages < 20), ages >= 20],
    [lambda x: 20 * x, lambda x: 5 * x, lambda x: np.maximum(100 - 0.7 * (x - 20), 20)]
)
crystallized_intelligence = np.piecewise(
    ages,
    [ages < 5, (ages >= 5) & (ages < 20), ages >= 20],
    [lambda x: 10 * x, lambda x: 2.5 * x, lambda x: np.maximum(50 + 0.3 * (x - 20), 30)]
)
short_term_memory = np.piecewise(
    ages,
    [ages < 5, (ages >= 5) & (ages < 20), ages >= 20],
    [lambda x: 15 * x, lambda x: 4.5 * x, lambda x: np.maximum(90 - 0.5 * (x - 20), 20)]
)
processing_speed = np.piecewise(
    ages,
    [ages < 5, (ages >= 5) & (ages < 20), ages >= 20],
    [lambda x: 20 * x, lambda x: 5 * x, lambda x: np.maximum(100 - 0.9 * (x - 20), 15)]
)
executive_function = np.piecewise(
    ages,
    [ages < 5, (ages >= 5) & (ages < 20), ages >= 20],
    [lambda x: 18 * x, lambda x: 4 * x, lambda x: np.maximum(100 - 0.6 * (x - 20), 20)]
)

# Combined age and cognitive performance chart
fig, ax1 = plt.subplots(figsize=(12, 8))

# Plot the histogram for combined ages (primary y-axis)
counts, bins, patches = ax1.hist(all_ages_series, bins=20, color='#1f77b4', edgecolor='black', alpha=0.7)
ax1.set_xlabel('Age')
ax1.set_ylabel('Frequency of Ages', color='black')
ax1.tick_params(axis='y', labelcolor='black')
ax1.grid(axis='y', alpha=0.75)

# Add vertical lines for mean, median, mode, and 30-year mark
ax1.axvline(mean_age, color='red', linestyle='--', linewidth=1.5, label='Mean')
ax1.axvline(median_age, color='green', linestyle='-', linewidth=1.5, label='Median')
ax1.axvline(30, color='cyan', linestyle='--', linewidth=1.5, label='30-Year Mark')  # 30-year-old line
if mode_age != 'N/A':
    ax1.axvline(mode_age, color='blue', linestyle='-', linewidth=1.5, label='Mode')

# Create a secondary y-axis for cognitive abilities
ax2 = ax1.twinx()
ax2.set_ylabel('Cognitive Performance (%)', color='black')
ax2.plot(ages, fluid_intelligence, label="Fluid Intelligence", linestyle='-', marker='o', color='purple')
ax2.plot(ages, crystallized_intelligence, label="Crystallized Intelligence", linestyle='-', marker='o', color='orange')
ax2.plot(ages, short_term_memory, label="Short-term Memory", linestyle='-', marker='o', color='green')
ax2.plot(ages, processing_speed, label="Processing Speed", linestyle='-', marker='o', color='red')
ax2.plot(ages, executive_function, label="Executive Function", linestyle='-', marker='o', color='brown')
ax2.tick_params(axis='y', labelcolor='black')

# Move the text box with statistical values to the top left
stats_text = (f"Mean: {mean_age:.2f}\nMedian: {median_age:.2f}\nMode: {mode_age}\n"
              f"Variance: {variance_age:.2f}\nStd Dev: {stdev_age:.2f}\n"
              f"Range: {range_age}\nMin Age: {min_age}\nMax Age: {max_age}")
ax1.text(0.02, 0.98, stats_text, ha='left', va='top', transform=ax1.transAxes,
         bbox=dict(facecolor='white', alpha=0.7))

# Combine all legends into one box on the top right
handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
handles = handles1 + handles2
labels = labels1 + labels2
ax1.legend(handles=handles, labels=labels, loc='upper right', fontsize=10)

# Add title and adjust layout
plt.title('Combined Age Distribution and Cognitive Abilities Across the Lifespan (0-100 Years) - Critical Acclaim Artists Only', fontsize=16)
fig.tight_layout()

# Display the chart
plt.show()


 # 5f - < 30 and >= 30 Detail Charts - critical acclaim only - grammy producers and songwriters only - same as 2f1
 
 # Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statistics import mode 

# Load data from all files
files = {    
    'US Grammy Winners - Producers': r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Producers.csv',
    'US Grammy Winners - Songwriters': r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Songwriters.csv'
}

columns = {
    'US Grammy Winners - Producers': 'Producer Age',
    'US Grammy Winners - Songwriters': 'Songwriter Age'
}

# Combine ages from all files into one list
all_ages = []

for key, file in files.items():
    df = pd.read_csv(file)
    column_name = columns[key]
    if column_name in df.columns:
        ages = df[column_name].dropna()
        all_ages.extend(ages)

# Convert all ages to a pandas Series
all_ages_series = pd.Series(all_ages)

# Calculate statistics for the combined artist age distribution
mean_age = all_ages_series.mean()
median_age = all_ages_series.median()
try:
    mode_age = mode(all_ages_series)
except:
    mode_age = 'N/A'
stdev_age = all_ages_series.std()
variance_age = all_ages_series.var()
min_age = all_ages_series.min()
max_age = all_ages_series.max()
range_age = max_age - min_age

# Define the extended age range for cognitive abilities (0 to 100)
ages = np.arange(0, 101, 5)

# Simulate realistic cognitive performance data using consistent piecewise functions
fluid_intelligence = np.piecewise(
    ages, 
    [ages < 5, (ages >= 5) & (ages < 20), ages >= 20],
    [lambda x: 20 * x, lambda x: 5 * x, lambda x: np.maximum(100 - 0.7 * (x - 20), 20)]
)
crystallized_intelligence = np.piecewise(
    ages,
    [ages < 5, (ages >= 5) & (ages < 20), ages >= 20],
    [lambda x: 10 * x, lambda x: 2.5 * x, lambda x: np.maximum(50 + 0.3 * (x - 20), 30)]
)
short_term_memory = np.piecewise(
    ages,
    [ages < 5, (ages >= 5) & (ages < 20), ages >= 20],
    [lambda x: 15 * x, lambda x: 4.5 * x, lambda x: np.maximum(90 - 0.5 * (x - 20), 20)]
)
processing_speed = np.piecewise(
    ages,
    [ages < 5, (ages >= 5) & (ages < 20), ages >= 20],
    [lambda x: 20 * x, lambda x: 5 * x, lambda x: np.maximum(100 - 0.9 * (x - 20), 15)]
)
executive_function = np.piecewise(
    ages,
    [ages < 5, (ages >= 5) & (ages < 20), ages >= 20],
    [lambda x: 18 * x, lambda x: 4 * x, lambda x: np.maximum(100 - 0.6 * (x - 20), 20)]
)

# Combined age and cognitive performance chart
fig, ax1 = plt.subplots(figsize=(12, 8))

# Plot the histogram for combined ages (primary y-axis)
counts, bins, patches = ax1.hist(all_ages_series, bins=20, color='#1f77b4', edgecolor='black', alpha=0.7)
ax1.set_xlabel('Age')
ax1.set_ylabel('Frequency of Ages', color='black')
ax1.tick_params(axis='y', labelcolor='black')
ax1.grid(axis='y', alpha=0.75)

# Add vertical lines for mean, median, mode, and 30-year mark
ax1.axvline(mean_age, color='red', linestyle='--', linewidth=1.5, label='Mean')
ax1.axvline(median_age, color='green', linestyle='-', linewidth=1.5, label='Median')
ax1.axvline(30, color='cyan', linestyle='--', linewidth=1.5, label='30-Year Mark')  # 30-year-old line
if mode_age != 'N/A':
    ax1.axvline(mode_age, color='blue', linestyle='-', linewidth=1.5, label='Mode')

# Create a secondary y-axis for cognitive abilities
ax2 = ax1.twinx()
ax2.set_ylabel('Cognitive Performance (%)', color='black')
ax2.plot(ages, fluid_intelligence, label="Fluid Intelligence", linestyle='-', marker='o', color='purple')
ax2.plot(ages, crystallized_intelligence, label="Crystallized Intelligence", linestyle='-', marker='o', color='orange')
ax2.plot(ages, short_term_memory, label="Short-term Memory", linestyle='-', marker='o', color='green')
ax2.plot(ages, processing_speed, label="Processing Speed", linestyle='-', marker='o', color='red')
ax2.plot(ages, executive_function, label="Executive Function", linestyle='-', marker='o', color='brown')
ax2.tick_params(axis='y', labelcolor='black')

# Move the text box with statistical values to the top left
stats_text = (f"Mean: {mean_age:.2f}\nMedian: {median_age:.2f}\nMode: {mode_age}\n"
              f"Variance: {variance_age:.2f}\nStd Dev: {stdev_age:.2f}\n"
              f"Range: {range_age}\nMin Age: {min_age}\nMax Age: {max_age}")
ax1.text(0.02, 0.98, stats_text, ha='left', va='top', transform=ax1.transAxes,
         bbox=dict(facecolor='white', alpha=0.7))

# Combine all legends into one box on the top right
handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
handles = handles1 + handles2
labels = labels1 + labels2
ax1.legend(handles=handles, labels=labels, loc='upper right', fontsize=10)

# Add title and adjust layout
plt.title('Age Distr. & Cognitive Abilities Across Lifespan (0-100 Yrs) - Critical Accl. Producers & Songwriters', fontsize=16)
fig.tight_layout()

# Display the chart
plt.show()


# 6 - Development and psychology charts

# 6a - < 30 and >= 30 Detail Charts - over all data - commercial success and critical acclaim - same as 2a2

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statistics import mode

# Load data from all provided files
files = {
    'WW Year-End Charts': r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Year-End Charts Number Ones.csv',
    'WW Best-Selling Albums': r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Best-Selling Albums.csv',
    'WW Best-Selling Singles': r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Best-Selling Singles.csv',
    'US Grammy Winners - Artists': r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Artists.csv',
    'US Grammy Winners - Producers': r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Producers.csv',
    'US Grammy Winners - Songwriters': r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Songwriters.csv'
}

columns = {
    'WW Year-End Charts': 'Artist Age',
    'WW Best-Selling Albums': 'Artist Age',
    'WW Best-Selling Singles': 'Artist Age',
    'US Grammy Winners - Artists': 'Artist Age',
    'US Grammy Winners - Producers': 'Producer Age',
    'US Grammy Winners - Songwriters': 'Songwriter Age'
}

# Combine all ages into a single list
all_ages = []
for key, file in files.items():
    df = pd.read_csv(file)
    column_name = columns[key]
    if column_name in df.columns:
        all_ages.extend(df[column_name].dropna())

# Convert all ages into a pandas Series for statistics
all_ages_series = pd.Series(all_ages)

# Calculate statistics
mean_age = all_ages_series.mean()
median_age = all_ages_series.median()
try:
    mode_age = mode(all_ages_series)
except:
    mode_age = 'N/A'
stdev_age = all_ages_series.std()
variance_age = all_ages_series.var()
min_age = all_ages_series.min()
max_age = all_ages_series.max()
range_age = max_age - min_age

# Define the age range for developmental trajectories
ages = np.arange(0, 101, 1)

# Simulate developmental trajectories
openness = np.clip(100 - (ages / 1.8) ** 1.2, 20, 100)
divergent_thinking = np.clip(100 - (ages / 1.5) ** 1.5, 10, 100)
convergent_thinking = np.clip((ages / 1.2) ** 1.2, 0, 100)
intrinsic_motivation = np.piecewise(
    ages, [ages < 20, (ages >= 20) & (ages <= 50), ages > 50],
    [lambda x: 80 + (x / 25), 90, lambda x: 90 - (x - 50) / 6]
)
crystallized_intelligence = np.clip((ages / 1.1) ** 0.9, 0, 100)
fluid_intelligence = np.clip(100 - (ages / 1.6) ** 1.3, 30, 100)
neuroplasticity = np.clip(100 - (ages / 1.5) ** 1.3, 10, 100)
risk_taking = np.clip(100 - (ages - 25) ** 2 / 400, 0, 100)
emotional_regulation = np.clip((ages / 1.8) ** 1.4, 30, 100)
dopamine_levels = np.clip(100 - (ages / 2.0) ** 1.2, 20, 100)

# Plot the combined chart
fig, ax1 = plt.subplots(figsize=(12, 8))

# Histogram for combined ages
counts, bins, patches = ax1.hist(all_ages_series, bins=15, color='#1f77b4', edgecolor='black', alpha=0.7)
ax1.set_xlabel('Age')
ax1.set_ylabel('Frequency of Ages', color='black')
ax1.tick_params(axis='y', labelcolor='black')

# Add vertical lines for mean, median, mode, and 30-year mark
ax1.axvline(mean_age, color='red', linestyle='--', linewidth=1.5, label='Mean')
ax1.axvline(median_age, color='green', linestyle='-', linewidth=1.5, label='Median')
if mode_age != 'N/A':
    ax1.axvline(mode_age, color='blue', linestyle='-', linewidth=1.5, label='Mode')
ax1.axvline(30, color='cyan', linestyle='--', linewidth=1.5, label='30-Year Mark')  # 30-year-old mark

# Secondary y-axis for developmental trajectories
ax2 = ax1.twinx()
ax2.set_ylabel('Developmental Factors (%)', color='black')
ax2.plot(ages, openness, label="Openness to Experience", linestyle='-', color='red')
ax2.plot(ages, divergent_thinking, label="Divergent Thinking", linestyle='--', color='green')
ax2.plot(ages, convergent_thinking, label="Convergent Thinking", linestyle='-.', color='orange')
ax2.plot(ages, intrinsic_motivation, label="Intrinsic Motivation", linestyle=':', color='purple')
ax2.plot(ages, crystallized_intelligence, label="Crystallized Intelligence", linestyle='-', color='brown')
ax2.plot(ages, fluid_intelligence, label="Fluid Intelligence", linestyle='--', color='blue')
ax2.plot(ages, neuroplasticity, label="Neuroplasticity", linestyle='-.', color='cyan')
ax2.plot(ages, risk_taking, label="Risk-Taking Behavior", linestyle=':', color='magenta')
ax2.plot(ages, emotional_regulation, label="Emotional Regulation", linestyle='-', color='darkgreen')
ax2.plot(ages, dopamine_levels, label="Dopamine Levels", linestyle='--', color='navy')
ax2.tick_params(axis='y', labelcolor='black')

# Add combined legend with larger font size
lines = ax1.get_legend_handles_labels()[0] + ax2.get_legend_handles_labels()[0]
labels = ax1.get_legend_handles_labels()[1] + ax2.get_legend_handles_labels()[1]
ax2.legend(lines, labels, loc='upper right', fontsize=10)  # Adjusted font size

# Add statistics text box
stats_text = (f"Mean: {mean_age:.2f}\nMedian: {median_age:.2f}\nMode: {mode_age}\n"
              f"Variance: {variance_age:.2f}\nStd Dev: {stdev_age:.2f}\n"
              f"Range: {range_age}\nMin Age: {min_age}\nMax Age: {max_age}")
ax1.text(0.98, 0.02, stats_text, ha='right', va='bottom', transform=ax1.transAxes,
         bbox=dict(facecolor='white', alpha=0.7))

# Finalize plot
plt.title('Combined Age Distribution and Developmental Factors Over Age (0-100 Years) - All Data', fontsize=14)
fig.tight_layout()
plt.show()


# 6b - < 30 and >= 30 Detail Charts - over artists only (excl. producers and songwriters) - commercial success and critical acclaim - same as 2b2
 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statistics import mode

# Load data from all provided files
files = {
    'WW Year-End Charts': r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Year-End Charts Number Ones.csv',
    'WW Best-Selling Albums': r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Best-Selling Albums.csv',
    'WW Best-Selling Singles': r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Best-Selling Singles.csv',
    'US Grammy Winners - Artists': r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Artists.csv'    
}

columns = {
    'WW Year-End Charts': 'Artist Age',
    'WW Best-Selling Albums': 'Artist Age',
    'WW Best-Selling Singles': 'Artist Age',
    'US Grammy Winners - Artists': 'Artist Age'
}

# Combine all ages into a single list
all_ages = []
for key, file in files.items():
    df = pd.read_csv(file)
    column_name = columns[key]
    if column_name in df.columns:
        all_ages.extend(df[column_name].dropna())

# Convert all ages into a pandas Series for statistics
all_ages_series = pd.Series(all_ages)

# Calculate statistics
mean_age = all_ages_series.mean()
median_age = all_ages_series.median()
try:
    mode_age = mode(all_ages_series)
except:
    mode_age = 'N/A'
stdev_age = all_ages_series.std()
variance_age = all_ages_series.var()
min_age = all_ages_series.min()
max_age = all_ages_series.max()
range_age = max_age - min_age

# Define the age range for developmental trajectories
ages = np.arange(0, 101, 1)

# Simulate developmental trajectories
openness = np.clip(100 - (ages / 1.8) ** 1.2, 20, 100)
divergent_thinking = np.clip(100 - (ages / 1.5) ** 1.5, 10, 100)
convergent_thinking = np.clip((ages / 1.2) ** 1.2, 0, 100)
intrinsic_motivation = np.piecewise(
    ages, [ages < 20, (ages >= 20) & (ages <= 50), ages > 50],
    [lambda x: 80 + (x / 25), 90, lambda x: 90 - (x - 50) / 6]
)
crystallized_intelligence = np.clip((ages / 1.1) ** 0.9, 0, 100)
fluid_intelligence = np.clip(100 - (ages / 1.6) ** 1.3, 30, 100)
neuroplasticity = np.clip(100 - (ages / 1.5) ** 1.3, 10, 100)
risk_taking = np.clip(100 - (ages - 25) ** 2 / 400, 0, 100)
emotional_regulation = np.clip((ages / 1.8) ** 1.4, 30, 100)
dopamine_levels = np.clip(100 - (ages / 2.0) ** 1.2, 20, 100)

# Plot the combined chart
fig, ax1 = plt.subplots(figsize=(12, 8))

# Histogram for combined ages
counts, bins, patches = ax1.hist(all_ages_series, bins=15, color='#1f77b4', edgecolor='black', alpha=0.7)
ax1.set_xlabel('Age')
ax1.set_ylabel('Frequency of Ages', color='black')
ax1.tick_params(axis='y', labelcolor='black')

# Add vertical lines for mean, median, mode, and 30-year mark
ax1.axvline(mean_age, color='red', linestyle='--', linewidth=1.5, label='Mean')
ax1.axvline(median_age, color='green', linestyle='-', linewidth=1.5, label='Median')
if mode_age != 'N/A':
    ax1.axvline(mode_age, color='blue', linestyle='-', linewidth=1.5, label='Mode')
ax1.axvline(30, color='cyan', linestyle='--', linewidth=1.5, label='30-Year Mark')  # 30-year-old mark

# Secondary y-axis for developmental trajectories
ax2 = ax1.twinx()
ax2.set_ylabel('Developmental Factors (%)', color='black')
ax2.plot(ages, openness, label="Openness to Experience", linestyle='-', color='red')
ax2.plot(ages, divergent_thinking, label="Divergent Thinking", linestyle='--', color='green')
ax2.plot(ages, convergent_thinking, label="Convergent Thinking", linestyle='-.', color='orange')
ax2.plot(ages, intrinsic_motivation, label="Intrinsic Motivation", linestyle=':', color='purple')
ax2.plot(ages, crystallized_intelligence, label="Crystallized Intelligence", linestyle='-', color='brown')
ax2.plot(ages, fluid_intelligence, label="Fluid Intelligence", linestyle='--', color='blue')
ax2.plot(ages, neuroplasticity, label="Neuroplasticity", linestyle='-.', color='cyan')
ax2.plot(ages, risk_taking, label="Risk-Taking Behavior", linestyle=':', color='magenta')
ax2.plot(ages, emotional_regulation, label="Emotional Regulation", linestyle='-', color='darkgreen')
ax2.plot(ages, dopamine_levels, label="Dopamine Levels", linestyle='--', color='navy')
ax2.tick_params(axis='y', labelcolor='black')

# Add combined legend with larger font size
lines = ax1.get_legend_handles_labels()[0] + ax2.get_legend_handles_labels()[0]
labels = ax1.get_legend_handles_labels()[1] + ax2.get_legend_handles_labels()[1]
ax2.legend(lines, labels, loc='upper right', fontsize=10)  # Adjusted font size

# Add statistics text box
stats_text = (f"Mean: {mean_age:.2f}\nMedian: {median_age:.2f}\nMode: {mode_age}\n"
              f"Variance: {variance_age:.2f}\nStd Dev: {stdev_age:.2f}\n"
              f"Range: {range_age}\nMin Age: {min_age}\nMax Age: {max_age}")
ax1.text(0.98, 0.02, stats_text, ha='right', va='bottom', transform=ax1.transAxes,
         bbox=dict(facecolor='white', alpha=0.7))

# Finalize plot
plt.title('Combined Age Distribution and Developmental Factors Over Age (0-100 Years) - Artists Only', fontsize=14)
fig.tight_layout()
plt.show()


 # 6c - < 30 and >= 30 Detail Charts - commercial success only - same as 2c2

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statistics import mode

# Load data from all provided files
files = {
    'WW Year-End Charts': r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Year-End Charts Number Ones.csv',
    'WW Best-Selling Albums': r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Best-Selling Albums.csv',
    'WW Best-Selling Singles': r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\WW Best-Selling Singles.csv'    
}

columns = {
    'WW Year-End Charts': 'Artist Age',
    'WW Best-Selling Albums': 'Artist Age',
    'WW Best-Selling Singles': 'Artist Age'
}

# Combine all ages into a single list
all_ages = []
for key, file in files.items():
    df = pd.read_csv(file)
    column_name = columns[key]
    if column_name in df.columns:
        all_ages.extend(df[column_name].dropna())

# Convert all ages into a pandas Series for statistics
all_ages_series = pd.Series(all_ages)

# Calculate statistics
mean_age = all_ages_series.mean()
median_age = all_ages_series.median()
try:
    mode_age = mode(all_ages_series)
except:
    mode_age = 'N/A'
stdev_age = all_ages_series.std()
variance_age = all_ages_series.var()
min_age = all_ages_series.min()
max_age = all_ages_series.max()
range_age = max_age - min_age

# Define the age range for developmental trajectories
ages = np.arange(0, 101, 1)

# Simulate developmental trajectories
openness = np.clip(100 - (ages / 1.8) ** 1.2, 20, 100)
divergent_thinking = np.clip(100 - (ages / 1.5) ** 1.5, 10, 100)
convergent_thinking = np.clip((ages / 1.2) ** 1.2, 0, 100)
intrinsic_motivation = np.piecewise(
    ages, [ages < 20, (ages >= 20) & (ages <= 50), ages > 50],
    [lambda x: 80 + (x / 25), 90, lambda x: 90 - (x - 50) / 6]
)
crystallized_intelligence = np.clip((ages / 1.1) ** 0.9, 0, 100)
fluid_intelligence = np.clip(100 - (ages / 1.6) ** 1.3, 30, 100)
neuroplasticity = np.clip(100 - (ages / 1.5) ** 1.3, 10, 100)
risk_taking = np.clip(100 - (ages - 25) ** 2 / 400, 0, 100)
emotional_regulation = np.clip((ages / 1.8) ** 1.4, 30, 100)
dopamine_levels = np.clip(100 - (ages / 2.0) ** 1.2, 20, 100)

# Plot the combined chart
fig, ax1 = plt.subplots(figsize=(12, 8))

# Histogram for combined ages
counts, bins, patches = ax1.hist(all_ages_series, bins=15, color='#1f77b4', edgecolor='black', alpha=0.7)
ax1.set_xlabel('Age')
ax1.set_ylabel('Frequency of Ages', color='black')
ax1.tick_params(axis='y', labelcolor='black')

# Add vertical lines for mean, median, mode, and 30-year mark
ax1.axvline(mean_age, color='red', linestyle='--', linewidth=1.5, label='Mean')
ax1.axvline(median_age, color='green', linestyle='-', linewidth=1.5, label='Median')
if mode_age != 'N/A':
    ax1.axvline(mode_age, color='blue', linestyle='-', linewidth=1.5, label='Mode')
ax1.axvline(30, color='cyan', linestyle='--', linewidth=1.5, label='30-Year Mark')  # 30-year-old mark

# Secondary y-axis for developmental trajectories
ax2 = ax1.twinx()
ax2.set_ylabel('Developmental Factors (%)', color='black')
ax2.plot(ages, openness, label="Openness to Experience", linestyle='-', color='red')
ax2.plot(ages, divergent_thinking, label="Divergent Thinking", linestyle='--', color='green')
ax2.plot(ages, convergent_thinking, label="Convergent Thinking", linestyle='-.', color='orange')
ax2.plot(ages, intrinsic_motivation, label="Intrinsic Motivation", linestyle=':', color='purple')
ax2.plot(ages, crystallized_intelligence, label="Crystallized Intelligence", linestyle='-', color='brown')
ax2.plot(ages, fluid_intelligence, label="Fluid Intelligence", linestyle='--', color='blue')
ax2.plot(ages, neuroplasticity, label="Neuroplasticity", linestyle='-.', color='cyan')
ax2.plot(ages, risk_taking, label="Risk-Taking Behavior", linestyle=':', color='magenta')
ax2.plot(ages, emotional_regulation, label="Emotional Regulation", linestyle='-', color='darkgreen')
ax2.plot(ages, dopamine_levels, label="Dopamine Levels", linestyle='--', color='navy')
ax2.tick_params(axis='y', labelcolor='black')

# Add combined legend with larger font size
lines = ax1.get_legend_handles_labels()[0] + ax2.get_legend_handles_labels()[0]
labels = ax1.get_legend_handles_labels()[1] + ax2.get_legend_handles_labels()[1]
ax2.legend(lines, labels, loc='upper right', fontsize=10)  # Adjusted font size

# Add statistics text box
stats_text = (f"Mean: {mean_age:.2f}\nMedian: {median_age:.2f}\nMode: {mode_age}\n"
              f"Variance: {variance_age:.2f}\nStd Dev: {stdev_age:.2f}\n"
              f"Range: {range_age}\nMin Age: {min_age}\nMax Age: {max_age}")
ax1.text(0.98, 0.02, stats_text, ha='right', va='bottom', transform=ax1.transAxes,
         bbox=dict(facecolor='white', alpha=0.7))

# Finalize plot
plt.title('Combined Age Distribution and Developmental Factors Over Age (0-100 Years) - Commercial Success Only', fontsize=14)
fig.tight_layout()
plt.show()


# 6d - < 30 and >= 30 Detail Charts - critical acclaim only - same as 2d2

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statistics import mode

# Load data from all provided files
files = {
    'US Grammy Winners - Artists': r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Artists.csv',
    'US Grammy Winners - Producers': r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Producers.csv',
    'US Grammy Winners - Songwriters': r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Songwriters.csv'
}

columns = {
    'US Grammy Winners - Artists': 'Artist Age',
    'US Grammy Winners - Producers': 'Producer Age',
    'US Grammy Winners - Songwriters': 'Songwriter Age'
}

# Combine all ages into a single list
all_ages = []
for key, file in files.items():
    df = pd.read_csv(file)
    column_name = columns[key]
    if column_name in df.columns:
        all_ages.extend(df[column_name].dropna())

# Convert all ages into a pandas Series for statistics
all_ages_series = pd.Series(all_ages)

# Calculate statistics
mean_age = all_ages_series.mean()
median_age = all_ages_series.median()
try:
    mode_age = mode(all_ages_series)
except:
    mode_age = 'N/A'
stdev_age = all_ages_series.std()
variance_age = all_ages_series.var()
min_age = all_ages_series.min()
max_age = all_ages_series.max()
range_age = max_age - min_age

# Define the age range for developmental trajectories
ages = np.arange(0, 101, 1)

# Simulate developmental trajectories
openness = np.clip(100 - (ages / 1.8) ** 1.2, 20, 100)
divergent_thinking = np.clip(100 - (ages / 1.5) ** 1.5, 10, 100)
convergent_thinking = np.clip((ages / 1.2) ** 1.2, 0, 100)
intrinsic_motivation = np.piecewise(
    ages, [ages < 20, (ages >= 20) & (ages <= 50), ages > 50],
    [lambda x: 80 + (x / 25), 90, lambda x: 90 - (x - 50) / 6]
)
crystallized_intelligence = np.clip((ages / 1.1) ** 0.9, 0, 100)
fluid_intelligence = np.clip(100 - (ages / 1.6) ** 1.3, 30, 100)
neuroplasticity = np.clip(100 - (ages / 1.5) ** 1.3, 10, 100)
risk_taking = np.clip(100 - (ages - 25) ** 2 / 400, 0, 100)
emotional_regulation = np.clip((ages / 1.8) ** 1.4, 30, 100)
dopamine_levels = np.clip(100 - (ages / 2.0) ** 1.2, 20, 100)

# Plot the combined chart
fig, ax1 = plt.subplots(figsize=(12, 8))

# Histogram for combined ages
counts, bins, patches = ax1.hist(all_ages_series, bins=15, color='#1f77b4', edgecolor='black', alpha=0.7)
ax1.set_xlabel('Age')
ax1.set_ylabel('Frequency of Ages', color='black')
ax1.tick_params(axis='y', labelcolor='black')

# Add vertical lines for mean, median, mode, and 30-year mark
ax1.axvline(mean_age, color='red', linestyle='--', linewidth=1.5, label='Mean')
ax1.axvline(median_age, color='green', linestyle='-', linewidth=1.5, label='Median')
if mode_age != 'N/A':
    ax1.axvline(mode_age, color='blue', linestyle='-', linewidth=1.5, label='Mode')
ax1.axvline(30, color='cyan', linestyle='--', linewidth=1.5, label='30-Year Mark')  # 30-year-old mark

# Secondary y-axis for developmental trajectories
ax2 = ax1.twinx()
ax2.set_ylabel('Developmental Factors (%)', color='black')
ax2.plot(ages, openness, label="Openness to Experience", linestyle='-', color='red')
ax2.plot(ages, divergent_thinking, label="Divergent Thinking", linestyle='--', color='green')
ax2.plot(ages, convergent_thinking, label="Convergent Thinking", linestyle='-.', color='orange')
ax2.plot(ages, intrinsic_motivation, label="Intrinsic Motivation", linestyle=':', color='purple')
ax2.plot(ages, crystallized_intelligence, label="Crystallized Intelligence", linestyle='-', color='brown')
ax2.plot(ages, fluid_intelligence, label="Fluid Intelligence", linestyle='--', color='blue')
ax2.plot(ages, neuroplasticity, label="Neuroplasticity", linestyle='-.', color='cyan')
ax2.plot(ages, risk_taking, label="Risk-Taking Behavior", linestyle=':', color='magenta')
ax2.plot(ages, emotional_regulation, label="Emotional Regulation", linestyle='-', color='darkgreen')
ax2.plot(ages, dopamine_levels, label="Dopamine Levels", linestyle='--', color='navy')
ax2.tick_params(axis='y', labelcolor='black')

# Add combined legend with larger font size
lines = ax1.get_legend_handles_labels()[0] + ax2.get_legend_handles_labels()[0]
labels = ax1.get_legend_handles_labels()[1] + ax2.get_legend_handles_labels()[1]
ax2.legend(lines, labels, loc='upper right', fontsize=10)  # Adjusted font size

# Add statistics text box
stats_text = (f"Mean: {mean_age:.2f}\nMedian: {median_age:.2f}\nMode: {mode_age}\n"
              f"Variance: {variance_age:.2f}\nStd Dev: {stdev_age:.2f}\n"
              f"Range: {range_age}\nMin Age: {min_age}\nMax Age: {max_age}")
ax1.text(0.98, 0.02, stats_text, ha='right', va='bottom', transform=ax1.transAxes,
         bbox=dict(facecolor='white', alpha=0.7))

# Finalize plot
plt.title('Combined Age Distribution and Developmental Factors Over Age (0-100 Years) - Critical Acclaim Only', fontsize=14)
fig.tight_layout()
plt.show()


 # 6e - < 30 and >= 30 Detail Charts - critical acclaim only - grammy artists only - same as 2e2
 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statistics import mode

# Load data from all provided files
files = {
    'US Grammy Winners - Artists': r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Artists.csv'
}

columns = {
    'US Grammy Winners - Artists': 'Artist Age'    
}

# Combine all ages into a single list
all_ages = []
for key, file in files.items():
    df = pd.read_csv(file)
    column_name = columns[key]
    if column_name in df.columns:
        all_ages.extend(df[column_name].dropna())

# Convert all ages into a pandas Series for statistics
all_ages_series = pd.Series(all_ages)

# Calculate statistics
mean_age = all_ages_series.mean()
median_age = all_ages_series.median()
try:
    mode_age = mode(all_ages_series)
except:
    mode_age = 'N/A'
stdev_age = all_ages_series.std()
variance_age = all_ages_series.var()
min_age = all_ages_series.min()
max_age = all_ages_series.max()
range_age = max_age - min_age

# Define the age range for developmental trajectories
ages = np.arange(0, 101, 1)

# Simulate developmental trajectories
openness = np.clip(100 - (ages / 1.8) ** 1.2, 20, 100)
divergent_thinking = np.clip(100 - (ages / 1.5) ** 1.5, 10, 100)
convergent_thinking = np.clip((ages / 1.2) ** 1.2, 0, 100)
intrinsic_motivation = np.piecewise(
    ages, [ages < 20, (ages >= 20) & (ages <= 50), ages > 50],
    [lambda x: 80 + (x / 25), 90, lambda x: 90 - (x - 50) / 6]
)
crystallized_intelligence = np.clip((ages / 1.1) ** 0.9, 0, 100)
fluid_intelligence = np.clip(100 - (ages / 1.6) ** 1.3, 30, 100)
neuroplasticity = np.clip(100 - (ages / 1.5) ** 1.3, 10, 100)
risk_taking = np.clip(100 - (ages - 25) ** 2 / 400, 0, 100)
emotional_regulation = np.clip((ages / 1.8) ** 1.4, 30, 100)
dopamine_levels = np.clip(100 - (ages / 2.0) ** 1.2, 20, 100)

# Plot the combined chart
fig, ax1 = plt.subplots(figsize=(12, 8))

# Histogram for combined ages
counts, bins, patches = ax1.hist(all_ages_series, bins=15, color='#1f77b4', edgecolor='black', alpha=0.7)
ax1.set_xlabel('Age')
ax1.set_ylabel('Frequency of Ages', color='black')
ax1.tick_params(axis='y', labelcolor='black')

# Add vertical lines for mean, median, mode, and 30-year mark
ax1.axvline(mean_age, color='red', linestyle='--', linewidth=1.5, label='Mean')
ax1.axvline(median_age, color='green', linestyle='-', linewidth=1.5, label='Median')
if mode_age != 'N/A':
    ax1.axvline(mode_age, color='blue', linestyle='-', linewidth=1.5, label='Mode')
ax1.axvline(30, color='cyan', linestyle='--', linewidth=1.5, label='30-Year Mark')  # 30-year-old mark

# Secondary y-axis for developmental trajectories
ax2 = ax1.twinx()
ax2.set_ylabel('Developmental Factors (%)', color='black')
ax2.plot(ages, openness, label="Openness to Experience", linestyle='-', color='red')
ax2.plot(ages, divergent_thinking, label="Divergent Thinking", linestyle='--', color='green')
ax2.plot(ages, convergent_thinking, label="Convergent Thinking", linestyle='-.', color='orange')
ax2.plot(ages, intrinsic_motivation, label="Intrinsic Motivation", linestyle=':', color='purple')
ax2.plot(ages, crystallized_intelligence, label="Crystallized Intelligence", linestyle='-', color='brown')
ax2.plot(ages, fluid_intelligence, label="Fluid Intelligence", linestyle='--', color='blue')
ax2.plot(ages, neuroplasticity, label="Neuroplasticity", linestyle='-.', color='cyan')
ax2.plot(ages, risk_taking, label="Risk-Taking Behavior", linestyle=':', color='magenta')
ax2.plot(ages, emotional_regulation, label="Emotional Regulation", linestyle='-', color='darkgreen')
ax2.plot(ages, dopamine_levels, label="Dopamine Levels", linestyle='--', color='navy')
ax2.tick_params(axis='y', labelcolor='black')

# Add combined legend with larger font size
lines = ax1.get_legend_handles_labels()[0] + ax2.get_legend_handles_labels()[0]
labels = ax1.get_legend_handles_labels()[1] + ax2.get_legend_handles_labels()[1]
ax2.legend(lines, labels, loc='upper right', fontsize=10)  # Adjusted font size

# Add statistics text box
stats_text = (f"Mean: {mean_age:.2f}\nMedian: {median_age:.2f}\nMode: {mode_age}\n"
              f"Variance: {variance_age:.2f}\nStd Dev: {stdev_age:.2f}\n"
              f"Range: {range_age}\nMin Age: {min_age}\nMax Age: {max_age}")
ax1.text(0.98, 0.02, stats_text, ha='right', va='bottom', transform=ax1.transAxes,
         bbox=dict(facecolor='white', alpha=0.7))

# Finalize plot
plt.title('Combined Age Distribution and Developmental Factors Over Age (0-100 Years) - Critical Acclaim Artists Only', fontsize=14)
fig.tight_layout()
plt.show()


 # 6f - < 30 and >= 30 Detail Charts - critical acclaim only - grammy producers and songwriters only - same as 2f1
 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statistics import mode

# Load data from all provided files
files = {
    'US Grammy Winners - Producers': r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Producers.csv',
    'US Grammy Winners - Songwriters': r'C:\Users\winte\OneDrive\Documents\Family\3 - Michael\Work\Data Science and AI\Music Analysis\Data\Actively used - yes\US Grammy Winners - Songwriters.csv'
}

columns = {
    'US Grammy Winners - Producers': 'Producer Age',
    'US Grammy Winners - Songwriters': 'Songwriter Age'
}

# Combine all ages into a single list
all_ages = []
for key, file in files.items():
    df = pd.read_csv(file)
    column_name = columns[key]
    if column_name in df.columns:
        all_ages.extend(df[column_name].dropna())

# Convert all ages into a pandas Series for statistics
all_ages_series = pd.Series(all_ages)

# Calculate statistics
mean_age = all_ages_series.mean()
median_age = all_ages_series.median()
try:
    mode_age = mode(all_ages_series)
except:
    mode_age = 'N/A'
stdev_age = all_ages_series.std()
variance_age = all_ages_series.var()
min_age = all_ages_series.min()
max_age = all_ages_series.max()
range_age = max_age - min_age

# Define the age range for developmental trajectories
ages = np.arange(0, 101, 1)

# Simulate developmental trajectories
openness = np.clip(100 - (ages / 1.8) ** 1.2, 20, 100)
divergent_thinking = np.clip(100 - (ages / 1.5) ** 1.5, 10, 100)
convergent_thinking = np.clip((ages / 1.2) ** 1.2, 0, 100)
intrinsic_motivation = np.piecewise(
    ages, [ages < 20, (ages >= 20) & (ages <= 50), ages > 50],
    [lambda x: 80 + (x / 25), 90, lambda x: 90 - (x - 50) / 6]
)
crystallized_intelligence = np.clip((ages / 1.1) ** 0.9, 0, 100)
fluid_intelligence = np.clip(100 - (ages / 1.6) ** 1.3, 30, 100)
neuroplasticity = np.clip(100 - (ages / 1.5) ** 1.3, 10, 100)
risk_taking = np.clip(100 - (ages - 25) ** 2 / 400, 0, 100)
emotional_regulation = np.clip((ages / 1.8) ** 1.4, 30, 100)
dopamine_levels = np.clip(100 - (ages / 2.0) ** 1.2, 20, 100)

# Plot the combined chart
fig, ax1 = plt.subplots(figsize=(12, 8))

# Histogram for combined ages
counts, bins, patches = ax1.hist(all_ages_series, bins=15, color='#1f77b4', edgecolor='black', alpha=0.7)
ax1.set_xlabel('Age')
ax1.set_ylabel('Frequency of Ages', color='black')
ax1.tick_params(axis='y', labelcolor='black')

# Add vertical lines for mean, median, mode, and 30-year mark
ax1.axvline(mean_age, color='red', linestyle='--', linewidth=1.5, label='Mean')
ax1.axvline(median_age, color='green', linestyle='-', linewidth=1.5, label='Median')
if mode_age != 'N/A':
    ax1.axvline(mode_age, color='blue', linestyle='-', linewidth=1.5, label='Mode')
ax1.axvline(30, color='cyan', linestyle='--', linewidth=1.5, label='30-Year Mark')  # 30-year-old mark

# Secondary y-axis for developmental trajectories
ax2 = ax1.twinx()
ax2.set_ylabel('Developmental Factors (%)', color='black')
ax2.plot(ages, openness, label="Openness to Experience", linestyle='-', color='red')
ax2.plot(ages, divergent_thinking, label="Divergent Thinking", linestyle='--', color='green')
ax2.plot(ages, convergent_thinking, label="Convergent Thinking", linestyle='-.', color='orange')
ax2.plot(ages, intrinsic_motivation, label="Intrinsic Motivation", linestyle=':', color='purple')
ax2.plot(ages, crystallized_intelligence, label="Crystallized Intelligence", linestyle='-', color='brown')
ax2.plot(ages, fluid_intelligence, label="Fluid Intelligence", linestyle='--', color='blue')
ax2.plot(ages, neuroplasticity, label="Neuroplasticity", linestyle='-.', color='cyan')
ax2.plot(ages, risk_taking, label="Risk-Taking Behavior", linestyle=':', color='magenta')
ax2.plot(ages, emotional_regulation, label="Emotional Regulation", linestyle='-', color='darkgreen')
ax2.plot(ages, dopamine_levels, label="Dopamine Levels", linestyle='--', color='navy')
ax2.tick_params(axis='y', labelcolor='black')

# Add combined legend with larger font size
lines = ax1.get_legend_handles_labels()[0] + ax2.get_legend_handles_labels()[0]
labels = ax1.get_legend_handles_labels()[1] + ax2.get_legend_handles_labels()[1]
ax2.legend(lines, labels, loc='upper right', fontsize=10)  # Adjusted font size

# Add statistics text box
stats_text = (f"Mean: {mean_age:.2f}\nMedian: {median_age:.2f}\nMode: {mode_age}\n"
              f"Variance: {variance_age:.2f}\nStd Dev: {stdev_age:.2f}\n"
              f"Range: {range_age}\nMin Age: {min_age}\nMax Age: {max_age}")
ax1.text(0.98, 0.02, stats_text, ha='right', va='bottom', transform=ax1.transAxes,
         bbox=dict(facecolor='white', alpha=0.7))

# Finalize plot
plt.title('Combined Age Distr. & Developmental Factors Over Age (0-100 Yrs) - Critical Acclaim Producers & Songwriters', fontsize=14)
fig.tight_layout()
plt.show()
