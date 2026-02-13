"""
Data loading and processing utilities for video game sales EDA.
"""

import pandas as pd
from typing import Optional, List


def load_video_game_data(filepath: str) -> pd.DataFrame:
    """
    Load video game sales data from a CSV file.
    
    Parameters:
    -----------
    filepath : str
        Path to the CSV file containing video game data
        
    Returns:
    --------
    pd.DataFrame
        DataFrame containing the video game sales data
    """
    df = pd.read_csv(filepath)
    return df


def get_data_info(df: pd.DataFrame) -> None:
    """
    Display basic information about the video game dataset.
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame containing video game data
    """
    print("Dataset Shape:", df.shape)
    print("\nColumn Names:")
    print(df.columns.tolist())
    print("\nData Types:")
    print(df.dtypes)
    print("\nMissing Values:")
    print(df.isnull().sum())
    print("\nBasic Statistics:")
    print(df.describe())


def clean_video_game_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the video game sales dataset.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Raw DataFrame containing video game data
        
    Returns:
    --------
    pd.DataFrame
        Cleaned DataFrame
    """
    # Create a copy to avoid modifying the original
    cleaned_df = df.copy()
    
    # Convert Year_of_Release to numeric if present
    if 'Year_of_Release' in cleaned_df.columns:
        cleaned_df['Year_of_Release'] = pd.to_numeric(
            cleaned_df['Year_of_Release'], 
            errors='coerce'
        )
    
    # Convert User_Score to numeric if present (might be stored as string)
    if 'User_Score' in cleaned_df.columns:
        cleaned_df['User_Score'] = pd.to_numeric(
            cleaned_df['User_Score'], 
            errors='coerce'
        )
    
    return cleaned_df


def filter_by_year(df: pd.DataFrame, 
                   start_year: Optional[int] = None, 
                   end_year: Optional[int] = None) -> pd.DataFrame:
    """
    Filter video game data by year range.
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame containing video game data
    start_year : int, optional
        Starting year (inclusive)
    end_year : int, optional
        Ending year (inclusive)
        
    Returns:
    --------
    pd.DataFrame
        Filtered DataFrame
    """
    filtered_df = df.copy()
    
    if start_year is not None:
        filtered_df = filtered_df[filtered_df['Year_of_Release'] >= start_year]
    
    if end_year is not None:
        filtered_df = filtered_df[filtered_df['Year_of_Release'] <= end_year]
    
    return filtered_df


def get_top_games_by_sales(df: pd.DataFrame, 
                           n: int = 10, 
                           region: str = 'Global_Sales') -> pd.DataFrame:
    """
    Get the top N games by sales in a specific region.
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame containing video game data
    n : int, default=10
        Number of top games to return
    region : str, default='Global_Sales'
        Sales column to sort by (e.g., 'NA_Sales', 'EU_Sales', 'Global_Sales')
        
    Returns:
    --------
    pd.DataFrame
        Top N games sorted by sales
    """
    return df.nlargest(n, region)


def get_sales_by_platform(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate total sales by platform.
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame containing video game data
        
    Returns:
    --------
    pd.DataFrame
        Sales aggregated by platform
    """
    sales_columns = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
    
    # Filter to only include columns that exist in the dataframe
    available_sales_cols = [col for col in sales_columns if col in df.columns]
    
    platform_sales = df.groupby('Platform')[available_sales_cols].sum().sort_values(
        'Global_Sales' if 'Global_Sales' in available_sales_cols else available_sales_cols[0],
        ascending=False
    )
    
    return platform_sales


def get_sales_by_genre(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate total sales by genre.
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame containing video game data
        
    Returns:
    --------
    pd.DataFrame
        Sales aggregated by genre
    """
    sales_columns = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
    
    # Filter to only include columns that exist in the dataframe
    available_sales_cols = [col for col in sales_columns if col in df.columns]
    
    genre_sales = df.groupby('Genre')[available_sales_cols].sum().sort_values(
        'Global_Sales' if 'Global_Sales' in available_sales_cols else available_sales_cols[0],
        ascending=False
    )
    
    return genre_sales
