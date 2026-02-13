# Data Directory

This directory contains the video game sales datasets.

## Structure

- `raw/`: Contains the original, unmodified data files
- `processed/`: Contains cleaned and processed data files ready for analysis

## Data Sources

Place your video game sales data CSV files in the `raw/` directory. The expected file should contain the following columns:

- Name
- Platform
- Year_of_Release
- Genre
- Publisher
- NA_Sales
- EU_Sales
- JP_Sales
- Other_Sales
- Global_Sales
- Critic_Score
- Critic_Count
- User_Score
- User_Count
- Developer
- Rating

## Note

Large data files may be excluded from version control. Check the `.gitignore` file for details.
