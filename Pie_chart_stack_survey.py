from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

# elements in Pie chart is needed in form of list or array-like

# Language Popularity0

# slices contain numbers of people know lan relative to labels lan
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
# explode list contain elem want to offset from chart (emphasis)
# explode contains float num describe distance from chart radius
explode = [0,0,0,0.1,0]

# plot Pie chart just look good when compare 5 things (using bar-chart to compare more things)
plt.pie(slices, labels=labels,explode=explode,shadow=True
        ,startangle=90, autopct='%1.1f%%'
        ,wedgeprops={'edgecolor':'black'}) # wedgeprops to adjust regions seperate

plt.title('My Awesome Pie Chart')
plt.tight_layout()
plt.show()
