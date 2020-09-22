import matplotlib.pyplot as plt
from LoRaSim.SimIntervals import Interval


class Plotter:
    def __init__(self, intervals):
        assert isinstance(intervals, list)
        assert isinstance(intervals[0], tuple)
        assert isinstance(intervals[0][0], Interval)
        self.intervals = intervals

    def show_plot(self):
        p_succ_y = []
        p_succ_x = []
        succ, tot = 0, 0

        for interval in self.intervals:
            metadata = interval[0]
            data = interval[1]
            model = metadata.model

            plt.vlines(metadata.start_time, 0, 1, linestyle=':', color='gray', linewidth=2)
            plt.text(metadata.start_time + 10, 0.9, model.title, color='gray')

            for sample in data:
                if sample[1]:
                    succ += 1
                tot += 1
                p_succ_y.append(succ/tot)

            colors = ['lime' if i[1] else 'r' for i in data]
            x = [i[0] for i in data]
            plt.scatter(x, [0]*len(x), c=colors, marker='|')
            p_succ_x.extend(x)

        plt.plot(p_succ_x, p_succ_y)
        plt.xlabel("Time (ms)")
        plt.ylabel("Success probability")
        plt.show()
