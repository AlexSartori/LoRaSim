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

    def show_plots(self):
        plt.show()

    def plot_rcv_prob(self):
        plt.figure()
        x_vals = []
        p_succ_y = []
        ci_min, ci_max = [], []
        succ, tot = 0, 0

        for metadata, data in self.intervals:
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

        self._plot_interval_lines(max(max(ci_max), max(p_succ_y)))
        plt.fill_between(x_vals, ci_min, ci_max, color='orange', alpha=0.4, label='95% CI')
        plt.plot(x_vals, p_succ_y, label='Success probability')

        plt.title("Reception Probability")
        plt.xlabel("Time (ms)")
        plt.ylabel("Success probability")
        plt.legend()
        plt.tight_layout()
        # plt.ylim([0, 1])
        plt.show()

    def _plot_recv_rate(self, data):
        colors = ['lime' if i[1] else 'r' for i in data]
        plt.scatter(list(i[0] for i in data), [0]*len(data), c=colors, marker='|')

    def _plot_interval_lines(self, height):
        for metadata, data in self.intervals:
            plt.vlines(metadata.start_time, 0, height, linestyle=':', color='gray', linewidth=2)
            plt.text(metadata.start_time, height, metadata.model.title, fontsize=12, color='gray')

    def plot_throughput(self):
        plt.figure()
        x_vals = []
        y_vals = []
        ci_min, ci_max = [], []

        for metadata, data in self.intervals:
            model = metadata.model

            for sample in data:
                if sample[1]:
                    y_vals.append(16/model.tx_time*1000) # !!! TODO !!! use actual packet size
                else:
                    y_vals.append(0)

            x_vals.extend(i[0] for i in data)
            self._plot_recv_rate(data)

        means = []
        square_diffs_from_mean = []
        for i, y in enumerate(y_vals):
            if i == 0:
                means.append(y)
                square_diffs_from_mean.append(0)
            else:
                new_m = (means[-1]*i + y)/(i+1)
                means.append(new_m)
                square_diffs_from_mean.append((y-new_m)**2)

            std = math.sqrt(sum(square_diffs_from_mean)/(i+1))
            ci = 1.96*std/math.sqrt(i+1)
            ci_min.append(means[-1] - ci)
            ci_max.append(means[-1] + ci)

        self._plot_interval_lines(max(y_vals))
        plt.fill_between(x_vals, ci_min, ci_max, color='orange', alpha=0.4, label='95% CI')
        plt.scatter(x_vals, y_vals, marker='+', alpha=0.4, label="Instantaneous throughput", c='blue')
        plt.plot(x_vals, means, label="Average Throughput", c='red')

        plt.title("Throughput")
        plt.xlabel("Time (ms)")
        plt.ylabel("Throughput (byte/s)")
        plt.legend()
        plt.tight_layout()
        plt.show()
