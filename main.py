from time_series_visualizer import load_data, clean_data, draw_line_plot, draw_bar_plot, draw_box_plot

def main():
    # Load the data
    df = load_data('fcc-forum-pageviews.csv')

    # Clean the data
    df_cleaned = clean_data(df)

    # Generate the plots
    draw_line_plot(df_cleaned)
    draw_bar_plot(df_cleaned)
    draw_box_plot(df_cleaned)

if __name__ == '__main__':
    main()
