from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

# elements in Pie chart is needed in form of list or array-like
slices = [120,80,30,20]
labels = ['Sixty','Forty','Extra_1','Extra_2']
# adding colors relatetively with labels
colors = ['#008fd5','#fc4f30','#e5ae37','#6d904f']

# plot Pie chart
plt.pie(slices, labels=labels,colors=colors,wedgeprops={'edgecolor':'black'}) # wedgeprops to adjust regions seperate

plt.title('My Awesome Pie Chart')
plt.tight_layout()
plt.show()

# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f
