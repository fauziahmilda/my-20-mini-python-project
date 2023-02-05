import matplotlib.pyplot as plt

# line graph
# remember graph has x and y axis
# this coordinate


def graph():
    x1 = [1, 4, 5, 8, 11, 12]
    y1 = [1, 3, 6, 12, 10, 13]

    x2 = [2, 3, 7, 10, 11, 13]
    y2 = [2, 4, 5, 8, 9, 10]

    plt.plot(x1, y1, label='Line 1', color="black", linestyle='dashed',
             linewidth='2.0', marker='o', mec="pink", ms=10, mfc='pink')
    # marker size = ms
    # marker color = mec
    # marker fill color = mfc
    plt.plot(x2, y2, label='Line 2', color="purple")

    plt.xlim(1, 14)
    plt.ylim(1, 14)

    # axis's label
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')

    # graph's title
    plt.title('Demo Graph - Two Lines')

    # show color indicator
    plt.legend()

    plt.show()


# -----------
# bar chart
def bar_chart():
    left = [1, 2, 3, 4, 5]
    height = [10, 11, 23, 36, 4]

    tick_label = ['one', 'two', 'three', 'four', 'five']
    plt.bar(left, height, tick_label=tick_label,
            width=0.8, color=['pink', 'grey'])

    # axis's label
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')

    plt.title("Bar Chart")

    # show color indicator
    plt.legend()
    plt.show()


# first one will show
graph()
# when you close the graph, bar chart will show
bar_chart()
