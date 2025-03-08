import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the dataset
def load_data(filepath):
    df = pd.read_csv(filepath, parse_dates=['date'], index_col='date')
    return df

# Clean the data
def clean_data(df):
    # Calculate the 2.5% and 97.5% quantiles
    lower_bound = df['value'].quantile(0.025)
    upper_bound = df['value'].quantile(0.975)

    # Filter the DataFrame
    df_cleaned = df[(df['value'] >= lower_bound) & (df['value'] <= upper_bound)]
    return df_cleaned


# Function to draw line plot
def draw_line_plot(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['value'], color='blue', linewidth=1)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('line_plot.png')
    plt.show()

# Function to draw bar plot
def draw_bar_plot(df):
    # Prepare data for bar plot
    df['year'] = df.index.year
    df['month'] = df.index.month_name()
    df_grouped = df.groupby(['year', 'month'])['value'].mean().unstack()

    plt.figure(figsize=(12, 6))
    df_grouped.plot(kind='bar', ax=plt.gca())
    plt.title('Average Daily Page Views per Month')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')
    plt.tight_layout()
    plt.savefig('bar_plot.png')
    plt.show()

# Function to draw box plot
def draw_box_plot(df):
    # Prepare data for box plot
    df['year'] = df.index.year
    df['month'] = df.index.month

    plt.figure(figsize=(12, 6))
    sns.boxplot(x='year', y='value', data=df)
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    plt.tight_layout()
    plt.savefig('box_plot_year.png')
    plt.show()

    plt.figure(figsize=(12, 6))
    sns.boxplot(x='month', y='value', data=df, order=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    plt.tight_layout()
    plt.savefig('box_plot_month.png')
    plt.show()
