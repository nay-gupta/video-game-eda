"""
Visualization utilities for video game sales EDA.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from typing import Optional, List


# Set default style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)


def plot_sales_trend_by_year(df: pd.DataFrame, 
                              sales_column: str = 'Global_Sales',
                              title: Optional[str] = None) -> None:
    """
    Plot sales trend over years.
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame containing video game data
    sales_column : str, default='Global_Sales'
        Sales column to plot
    title : str, optional
        Custom plot title
    """
    yearly_sales = df.groupby('Year_of_Release')[sales_column].sum().sort_index()
    
    plt.figure(figsize=(14, 6))
    plt.plot(yearly_sales.index, yearly_sales.values, marker='o', linewidth=2)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel(f'{sales_column} (millions)', fontsize=12)
    plt.title(title or f'{sales_column} Trend Over Years', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_top_platforms(df: pd.DataFrame, 
                       n: int = 10,
                       sales_column: str = 'Global_Sales') -> None:
    """
    Plot top N platforms by sales.
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame containing video game data
    n : int, default=10
        Number of top platforms to show
    sales_column : str, default='Global_Sales'
        Sales column to use for ranking
    """
    platform_sales = df.groupby('Platform')[sales_column].sum().sort_values(ascending=False).head(n)
    
    plt.figure(figsize=(12, 6))
    platform_sales.plot(kind='bar', color='steelblue')
    plt.xlabel('Platform', fontsize=12)
    plt.ylabel(f'{sales_column} (millions)', fontsize=12)
    plt.title(f'Top {n} Platforms by {sales_column}', fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


def plot_top_genres(df: pd.DataFrame, 
                    n: int = 10,
                    sales_column: str = 'Global_Sales') -> None:
    """
    Plot top N genres by sales.
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame containing video game data
    n : int, default=10
        Number of top genres to show
    sales_column : str, default='Global_Sales'
        Sales column to use for ranking
    """
    genre_sales = df.groupby('Genre')[sales_column].sum().sort_values(ascending=False).head(n)
    
    plt.figure(figsize=(12, 6))
    genre_sales.plot(kind='barh', color='coral')
    plt.xlabel(f'{sales_column} (millions)', fontsize=12)
    plt.ylabel('Genre', fontsize=12)
    plt.title(f'Top {n} Genres by {sales_column}', fontsize=14)
    plt.tight_layout()
    plt.show()


def plot_regional_sales_comparison(df: pd.DataFrame) -> None:
    """
    Plot comparison of sales across different regions.
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame containing video game data
    """
    regional_sales = {
        'North America': df['NA_Sales'].sum(),
        'Europe': df['EU_Sales'].sum(),
        'Japan': df['JP_Sales'].sum(),
        'Other': df['Other_Sales'].sum()
    }
    
    plt.figure(figsize=(10, 6))
    plt.bar(regional_sales.keys(), regional_sales.values(), color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
    plt.xlabel('Region', fontsize=12)
    plt.ylabel('Total Sales (millions)', fontsize=12)
    plt.title('Total Sales by Region', fontsize=14)
    plt.tight_layout()
    plt.show()


def plot_sales_distribution(df: pd.DataFrame, 
                           sales_column: str = 'Global_Sales') -> None:
    """
    Plot distribution of sales.
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame containing video game data
    sales_column : str, default='Global_Sales'
        Sales column to plot
    """
    plt.figure(figsize=(12, 6))
    plt.hist(df[sales_column].dropna(), bins=50, color='skyblue', edgecolor='black', alpha=0.7)
    plt.xlabel(f'{sales_column} (millions)', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.title(f'Distribution of {sales_column}', fontsize=14)
    plt.tight_layout()
    plt.show()


def plot_score_vs_sales(df: pd.DataFrame, 
                       score_column: str = 'Critic_Score',
                       sales_column: str = 'Global_Sales') -> None:
    """
    Plot relationship between scores and sales.
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame containing video game data
    score_column : str, default='Critic_Score'
        Score column to plot (e.g., 'Critic_Score' or 'User_Score')
    sales_column : str, default='Global_Sales'
        Sales column to plot
    """
    # Remove missing values
    plot_df = df[[score_column, sales_column]].dropna()
    
    plt.figure(figsize=(10, 6))
    plt.scatter(plot_df[score_column], plot_df[sales_column], alpha=0.5, s=20)
    plt.xlabel(score_column, fontsize=12)
    plt.ylabel(f'{sales_column} (millions)', fontsize=12)
    plt.title(f'{score_column} vs {sales_column}', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_correlation_heatmap(df: pd.DataFrame) -> None:
    """
    Plot correlation heatmap for numeric columns.
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame containing video game data
    """
    # Select numeric columns
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    correlation = df[numeric_cols].corr()
    
    plt.figure(figsize=(12, 10))
    sns.heatmap(correlation, annot=True, fmt='.2f', cmap='coolwarm', 
                center=0, square=True, linewidths=1)
    plt.title('Correlation Heatmap', fontsize=14)
    plt.tight_layout()
    plt.show()


def plot_top_publishers(df: pd.DataFrame, 
                       n: int = 10,
                       sales_column: str = 'Global_Sales') -> None:
    """
    Plot top N publishers by sales.
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame containing video game data
    n : int, default=10
        Number of top publishers to show
    sales_column : str, default='Global_Sales'
        Sales column to use for ranking
    """
    publisher_sales = df.groupby('Publisher')[sales_column].sum().sort_values(ascending=False).head(n)
    
    plt.figure(figsize=(12, 6))
    publisher_sales.plot(kind='barh', color='mediumseagreen')
    plt.xlabel(f'{sales_column} (millions)', fontsize=12)
    plt.ylabel('Publisher', fontsize=12)
    plt.title(f'Top {n} Publishers by {sales_column}', fontsize=14)
    plt.tight_layout()
    plt.show()
