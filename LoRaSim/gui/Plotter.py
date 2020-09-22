import math
import matplotlib.pyplot as plt
from LoRaSim.SimIntervals import Interval


class Plotter:
    def __init__(self, intervals):
        assert isinstance(intervals, list)
        assert isinstance(intervals[0], tuple)
        assert isinstance(intervals[0][0], Interval)
        assert isinstance(intervals[0][1], list)
        self.intervals = intervals

    def show_plot(self):
        x_vals = []
        p_succ_y = []
        ci_min, ci_max = [], []
        succ, tot = 0, 0

        for interval in self.intervals:
            metadata = interval[0]
            data = interval[1]
            model = metadata.model

            if len(self.intervals) > 1:
                plt.vlines(metadata.start_time, 0, 1, linestyle=':', color='gray', linewidth=2)
                plt.text(metadata.start_time, 1.1, model.title, fontsize=12, color='gray')

            for sample in data:
                if sample[1]:
                    succ += 1
                tot += 1

                p = succ/tot
                p_succ_y.append(p)
                ci = 1.96*math.sqrt(succ*(tot-succ))/(tot*math.sqrt(tot))
                ci_max.append(p+ci)
                ci_min.append(p-ci)

            x_vals.extend(i[0] for i in data)
            self._plot_recv_rate(data)

        plt.fill_between(x_vals, ci_min, ci_max, color='orange', alpha=0.4, label='95% CI')
        plt.plot(x_vals, p_succ_y, label='Success probability')
        plt.xlabel("Time (ms)")
        plt.ylabel("Success probability")
        plt.legend()
        plt.tight_layout()
        # plt.ylim([0, 1])
        plt.show()

    def _plot_recv_rate(self, data):
        colors = ['lime' if i[1] else 'r' for i in data]
        plt.scatter(list(i[0] for i in data), [0]*len(data), c=colors, marker='|')
