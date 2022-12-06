import matplotlib.dates as mdates

import matplotlib.pyplot as plt

def ten_charts(df, fn, title):
    fig = plt.figure(figsize=(30,20))
    fig.autofmt_xdate()

    arts = df['title'].unique()

    # Create the subplots
    ax = [plt.subplot(5, 2, i+1) for i in range(10)]

    # Create different colors for each subplot
    palette = plt.get_cmap('terrain')
    num = 30

    # Create each chart
    for a, art in zip(ax, arts):
        num += 5

        # Create the plot
        temp = df.loc[df['title'] == art].sort_values(by='day_time').reset_index(drop=True)

        x = temp['day_time']
        y = temp['rolling_pv']

        a.plot(x, y, color=palette(num))
        a.xaxis.set_major_locator(mdates.MinuteLocator(interval=60))
        a.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

        # Add a title
        a.title.set_text(art[:70] + '...')
        a.title.set_size(18)

        a.tick_params(
            axis='both',
            which='major',
            labelsize=12
        )

        for tick in a.get_xticklabels():
            tick.set_rotation(45)

    fig.suptitle(
        title,
        fontsize=22,
        y=.93
    )

    plt.subplots_adjust(
        wspace=0.08,
        hspace=0.6
    )

    plt.savefig(fn)

