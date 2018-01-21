# https://github.com/scentellegher/code_snippets/blob/master/bar_chart_formatted_dates/Bar_chart_with_formatted_dates.ipynb
# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# set ggplot style
plt.style.use('ggplot')

# read data from csv
data = pd.read_csv('/home/pbolle/Dokumente/weather/converted/model1.csv', usecols=['date', 'hum_in'], parse_dates=['date'])
# set date as index
data.set_index('date', inplace=True)

# plot data
fig, ax = plt.subplots(figsize=(15, 7))
ax.bar(data.index, data['hum_in'])

# set ticks every week
ax.xaxis.set_major_locator(mdates.WeekdayLocator())
# format date
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))

ax.set_title('Game of Thrones Wikipedia Page Views')
ax.set_xlabel('hum_out')
ax.set_ylabel('Date')

plt.show()
