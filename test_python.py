# -*- coding:utf-8 -*-
import os, shutil
import pandas as pd
import matplotlib.pyplot as plt



class DrawPlots:
    """Class for drawing plots"""
    #def __init__(self):
    #    pass

    def draw_plots(self, path_df):

        paths_plots = []

        try:
            curr_df = pd.read_json(path_df)

            main_path_plots = 'plots//'
            if os.path.exists(main_path_plots) is True:
                shutil.rmtree('plots')
            os.mkdir('plots')

            #plot 1 (check - model found all corners or not?)
            plt.title('Difference in number of corners (real and predicted)', fontsize=15)
            plt.xlabel('Index of room', fontsize=12, color='black')
            plt.ylabel('Difference', fontsize=12, color='black')
            plt.plot(curr_df.index, curr_df['gt_corners'] - curr_df['rb_corners'])
            plt.savefig(main_path_plots + 'Difference in number of corners (real and predicted).png')
            paths_plots.append(main_path_plots + 'Difference in number of corners (real and predicted).png')
            #plt.show()
            plt.close()

            #plot 2 (how many types of rooms based on number of corners)
            plt.title('Groups of rooms based on number of corners', fontsize=15)
            plt.xlabel('Corners quantity', fontsize=12, color='black')
            plt.ylabel('Number of rooms', fontsize=12, color='black')
            plt.grid()
            plt.hist(curr_df['gt_corners'], color='blue', edgecolor='black')
            plt.semilogy()
            plt.savefig(main_path_plots + 'Groups of rooms.png')
            paths_plots.append(main_path_plots + 'Groups of rooms.png')
            #plt.show()
            plt.close()

            #plot 3
            plt.title('Deviations of max floor angles for all kind of rooms', fontsize=15)
            plt.xlabel('Corners quantity', fontsize=12, color='black')
            plt.ylabel('Deviations of max floor angles', fontsize=12, color='black')
            plt.scatter(curr_df['gt_corners'], curr_df['floor_max'], c='green')
            plt.savefig(main_path_plots + 'Deviations of max floor angles for all kind of rooms.png')
            paths_plots.append(main_path_plots + 'Deviations of max floor angles for all kind of rooms.png')
            #plt.show()
            plt.close()

            #plot 4
            plt.figure(figsize= (7,5))
            plt.title('Ratio of mean deviations of floors and ceilings by rooms', fontsize=15)
            plt.xlabel('Deviations of mean ceiling angles', fontsize=12, color='black')
            plt.ylabel('Deviations of mean floor angles', fontsize=12, color='black')
            plt.scatter(curr_df[curr_df['gt_corners'] == 4]['ceiling_mean'],
                        curr_df[curr_df['gt_corners'] == 4]['floor_mean'], c='green')

            plt.scatter(curr_df[curr_df['gt_corners'] == 6]['ceiling_mean'],
                        curr_df[curr_df['gt_corners'] == 6]['floor_mean'], c='red')

            plt.scatter(curr_df[curr_df['gt_corners'] == 8]['ceiling_mean'],
                        curr_df[curr_df['gt_corners'] == 8]['floor_mean'], c='blue')

            plt.scatter(curr_df[curr_df['gt_corners'] == 10]['ceiling_mean'],
                        curr_df[curr_df['gt_corners'] == 10]['floor_mean'], c='yellow')

            plt.legend(["4 corns", "6 corns", "8 corns", "10 corns"])
            plt.savefig(main_path_plots + 'Ratio of mean deviations of floors and ceilings.png')
            paths_plots.append(main_path_plots +
                               'Ratio of mean deviations of floors and ceilings.png')
            #plt.show()
            plt.close()

            #plot 5
            plt.figure(figsize= (12,8))
            plt.title('Ratio between mean deviations and mean floor deviations', fontsize=15)
            plt.xlabel('Mean deviations', fontsize=12, color='black')
            plt.ylabel('Floor mean deviations', fontsize=12, color='black')
            plt.scatter(curr_df['mean'], curr_df['floor_mean'], c='g')
            plt.grid()
            plt.savefig(main_path_plots + 'Ratio between mean deviations and mean floor deviations.png')
            paths_plots.append(main_path_plots + 'Ratio between mean deviations and mean floor deviations.png')
            #plt.show()
            plt.close()

            #plot 6
            plt.figure(figsize= (12,8))
            plt.title('Ratio between mean deviations and mean ceiling deviations', fontsize=15)
            plt.xlabel('Mean deviations', fontsize=12, color='black')
            plt.ylabel('Ceiling mean deviations', fontsize=12, color='black')
            plt.scatter(curr_df['mean'], curr_df['ceiling_mean'], c='g')
            plt.grid()
            plt.savefig(main_path_plots + 'Ratio between mean deviations and mean ceiling deviations.png')
            paths_plots.append(main_path_plots + 'Ratio between mean deviations and mean ceiling deviations.png')
            #plt.show()
            plt.close()

        except:
            print("Can't open json file")

        #paths
        #for i in os.listdir(main_path_plots):
        #    paths_plots.append(os.path.abspath(i))
        return paths_plots


def main():
    path_df = 'data/deviation.json'

    list_of_plots = DrawPlots().draw_plots(path_df)
    print(list_of_plots)

if __name__ == "__main__":
    main()
