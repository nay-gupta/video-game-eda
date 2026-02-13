"""
Source code package for video game sales EDA utilities.
"""

from .data_utils import (
    load_video_game_data,
    get_data_info,
    clean_video_game_data,
    filter_by_year,
    get_top_games_by_sales,
    get_sales_by_platform,
    get_sales_by_genre
)

from .visualization import (
    plot_sales_trend_by_year,
    plot_top_platforms,
    plot_top_genres,
    plot_regional_sales_comparison,
    plot_sales_distribution,
    plot_score_vs_sales,
    plot_correlation_heatmap,
    plot_top_publishers
)

__all__ = [
    # Data utilities
    'load_video_game_data',
    'get_data_info',
    'clean_video_game_data',
    'filter_by_year',
    'get_top_games_by_sales',
    'get_sales_by_platform',
    'get_sales_by_genre',
    # Visualization utilities
    'plot_sales_trend_by_year',
    'plot_top_platforms',
    'plot_top_genres',
    'plot_regional_sales_comparison',
    'plot_sales_distribution',
    'plot_score_vs_sales',
    'plot_correlation_heatmap',
    'plot_top_publishers',
]
