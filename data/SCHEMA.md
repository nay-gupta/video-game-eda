# Video Game Sales Data Schema

## Column Definitions

### Game Information
| Column Name | Data Type | Description | Example |
|------------|-----------|-------------|---------|
| Name | String | Title of the video game | "Wii Sports", "Grand Theft Auto V" |
| Platform | String | Gaming platform/console | "PS4", "Xbox360", "PC", "Wii" |
| Year_of_Release | Integer/Float | Year the game was released | 2006, 2013, 2020 |
| Genre | String | Game genre/category | "Action", "Sports", "RPG", "Shooter" |
| Publisher | String | Company that published the game | "Nintendo", "Electronic Arts", "Activision" |
| Developer | String | Party responsible for creating the game | "Nintendo EAD", "Rockstar North" |
| Rating | String | ESRB (Entertainment Software Rating Board) rating | "E" (Everyone), "T" (Teen), "M" (Mature) |

### Sales Data (in millions of units)
| Column Name | Data Type | Description | Example |
|------------|-----------|-------------|---------|
| NA_Sales | Float | Sales in North America (millions) | 41.49, 15.85 |
| EU_Sales | Float | Sales in Europe (millions) | 29.02, 12.88 |
| JP_Sales | Float | Sales in Japan (millions) | 3.77, 1.15 |
| Other_Sales | Float | Sales in other regions (millions) | 8.46, 3.01 |
| Global_Sales | Float | Total worldwide sales (millions) | 82.74, 32.89 |

### Review/Rating Metrics
| Column Name | Data Type | Description | Example |
|------------|-----------|-------------|---------|
| Critic_Score | Float | Aggregate score compiled by Metacritic staff (0-100 scale) | 76, 97, 82 |
| Critic_Count | Integer | Number of critics used in coming up with the Critic_score | 51, 45, 38 |
| User_Score | Float | Score by Metacritic's subscribers (0-10 scale) | 8.0, 9.1, 7.5 |
| User_Count | Integer | Number of users who gave the user_score | 322, 2965, 1621 |

## Data Notes

### Sales Figures
- All sales figures are in millions of units
- Global_Sales = NA_Sales + EU_Sales + JP_Sales + Other_Sales
- Sales represent physical and digital copies sold

### Regional Breakdown
- **NA_Sales**: Covers North America (USA, Canada, Mexico)
- **EU_Sales**: Covers European countries
- **JP_Sales**: Covers Japan only
- **Other_Sales**: Rest of the world excluding NA, EU, and JP

### Score Scales
- **Critic_Score**: Ranges from 0-100 (higher is better)
- **User_Score**: Ranges from 0-10 (higher is better)
- May contain missing values for some games

### ESRB Ratings
Common ratings include:
- **E**: Everyone (suitable for all ages)
- **E10+**: Everyone 10 and older
- **T**: Teen (13+)
- **M**: Mature (17+)
- **AO**: Adults Only (18+)
- **RP**: Rating Pending

### Platforms
Examples include:
- PlayStation family: PS, PS2, PS3, PS4, PS5, PSP, PSV
- Xbox family: Xbox, Xbox360, XOne, XS
- Nintendo: Wii, WiiU, Switch, DS, 3DS, GBA, GameCube
- PC
- Others: Dreamcast, Saturn, etc.

### Genres
Common genres include:
- Action
- Adventure
- Fighting
- Misc
- Platform
- Puzzle
- Racing
- Role-Playing (RPG)
- Shooter
- Simulation
- Sports
- Strategy

## Missing Values
- Some games may not have all data fields populated
- Older games may lack review scores
- Some games may have incomplete sales data for certain regions

## Data Quality Considerations
1. **Year_of_Release**: May contain missing or incorrect values for some games
2. **User_Score**: Sometimes stored as string "tbd" (to be determined) instead of numeric value
3. **Publisher/Developer**: May have variations in naming (e.g., "EA" vs "Electronic Arts")
4. Handle missing values appropriately during analysis
