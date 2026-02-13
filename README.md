# Video Game Sales - Exploratory Data Analysis

This repository contains exploratory data analysis (EDA) on video game sales data.

## About the Data

The dataset includes information about video games with the following columns:

### Sales Metrics
- **Name**: Title of the game
- **Platform**: Gaming platform (e.g., PS4, Xbox, PC)
- **Year_of_Release**: Year the game was released
- **Genre**: Game genre (e.g., Action, Sports, RPG)
- **Publisher**: Company that published the game
- **NA_Sales**: Sales in North America (in millions)
- **EU_Sales**: Sales in Europe (in millions)
- **JP_Sales**: Sales in Japan (in millions)
- **Other_Sales**: Sales in other regions (in millions)
- **Global_Sales**: Total worldwide sales (in millions)

### Review Metrics
- **Critic_Score**: Aggregate score compiled by Metacritic staff
- **Critic_Count**: The number of critics used in coming up with the Critic_score
- **User_Score**: Score by Metacritic's subscribers
- **User_Count**: Number of users who gave the user_score

### Additional Information
- **Developer**: Party responsible for creating the game
- **Rating**: The ESRB ratings (e.g., E, T, M)

## Project Structure

```
video-game-eda/
├── data/
│   ├── raw/          # Raw data files
│   └── processed/    # Processed/cleaned data
├── notebooks/        # Jupyter notebooks for analysis
├── src/             # Source code for data processing
├── requirements.txt # Python dependencies
└── README.md        # Project documentation
```

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/nay-gupta/video-game-eda.git
   cd video-game-eda
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Open the Jupyter notebooks to explore the analysis:
   ```bash
   jupyter notebook
   ```

## Analysis Topics

The EDA includes:
- Sales trends over time
- Popular platforms and genres
- Regional sales comparisons
- Correlation between critic/user scores and sales
- Publisher and developer analysis
- Rating distribution analysis