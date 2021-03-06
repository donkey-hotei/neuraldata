#
#  NAME
#    problem_set2_solutions.py
#
#  DESCRIPTION
#    Open, view, and analyze action potentials recorded during a behavioral
#    task.  In Problem Set 2, you will write create and test your own code to
#    create tuning curves.
#
#
#
#  In this problem set we will:
#  1. Write a function that sorts neural responses based on behavoral events..
#  2. Write a function to plot neural responses related to various behaviors.
#  3. Write a function to plot tuning curves.
#

#   

#Helper code to import some functions we will use
import numpy as np
import matplotlib.pylab as plt
import matplotlib.mlab as mlab
from scipy import optimize
from scipy import stats


def load_experiment(filename):
    """
    load_experiment takes the file name and reads in the data.  It returns a
    two-dimensional array, with the first column containing the direction of
    motion for the trial, and the second column giving you the time the
    animal began movement during tha    t trial.
    """
    data = np.load(filename)[()];
    return np.array(data)

def load_neuraldata(filename):
    """
    load_neuraldata takes the file name and reads in the data for that neuron.
    It returns an arary of spike times.
    """
    data = np.load(filename)[()];
    return np.array(data)


# example of spike alignment 
def bin_spikes(trials, spk_times, time_bin = 0.08):
    """
    bin_spikes takes the trials array (with directions and times) and the spk_times
    array with spike times and returns the average firing rate for each of the
    eight directions of motion, as calculated within a time_bin before and after
    the trial time (time_bin should be given in seconds).  For example,
    time_bin = .1 will count the spikes from 100ms before to 100ms after the 
    trial began.
    
    dir_rates should be an 8x2 array with the first column containing the directions
    (in degrees from 0-360) and the second column containing the average firing rate
    for each direction
    """
    directions = np.unique(trials[:,0])
    dir_rates = np.zeros( (8, 2) ) # intialize an 8x2 array of zeros 
    for direction in directions:
        nmbr_trials = float(len(plt.find(trials[:,0]==direction)))
        trial_times = [ t[1] for t in trials if t[0] == direction ]
        nmbr_spks = 0.0
        for time in trial_times:
            nmbr_spks += len(np.where(np.logical_and(spk_times>time-time_bin,spk_times<time+time_bin))[0])
        firing_rate = nmbr_spks/nmbr_trials/(2*time_bin)
        dir_rates[plt.find(directions==direction)] = [direction, firing_rate] 
    return dir_rates
    

# Tuning curves conveys information about the range of sensory input
# for which a neuron responds. Allowing us to see what stimuli 
# correspond to neural firing. 
def plot_tuning_curves(direction_rates, title):
    """
    This function takes the x-values and the y-values  in units of spikes/s 
    (found in the two columns of direction_rates) and plots a histogram and 
    polar representation of the tuning curve. It adds the given title.
    """
        # yank columns and keep in correspondance 
    directions = direction_rates[0:][:,0]
    rates = direction_rates[0:][:,1]
    # histogram plot 
    plt.subplot(2, 2, 1)
    plt.title('Histogram ' + title)
    plt.axis([0, 360, 0, 70])
    plt.xlim(-22.5,337.5)
    plt.xlabel('Directions (in degrees)')
    plt.ylabel('Average Firing Rate (in spikes/s)')
    plt.bar(directions, rates, width=45, align='center')
    plt.xticks(directions)
    # polar plot 
    plt.subplot(2,2,2,polar=True)
    plt.title('Polar plot ' + title)
    #plt.legend('Diring Rate (spikes/s)')
    rates = np.append(rates, rates[0]) 
    theta = np.arange(0,361,45)*np.pi/180
    plt.polar(theta, rates)

    plt.show()
    # end plot_tuning_curves
    return 0
    
def roll_axes(direction_rates):
    """
    roll_axes takes the x-values (directions) and y-values (direction_rates)
    and return new x and y values that have been "rolled" to put the maximum
    direction_rate in the center of the curve. The first and last y-value in the
    returned list should be set to be the same. (See problem set directions)
    Hint: Use np.roll()
    """
   directions = direction_rates[0:][:,0]
   rates = direction_rates[0:][:,0]
   rates = np.append(rates, rates[0])
   max_dir = directions[ plt.find(rates>=max(rates)) ]
   
    
    return new_xs, new_ys, roll_degrees    
    

def normal_fit(x,mu, sigma, A):
    """
    This creates a normal curve over the values in x with mean mu and
    variance sigma.  It is scaled up to height A.
    """
    n = A*mlab.normpdf(x,mu,sigma)
    return n

def fit_tuning_curve(centered_x,centered_y):
    """
    This takes our rolled curve, generates the guesses for the fit function,
    and runs the fit.  It returns the parameters to generate the curve.
    """

    return NotImplementedError
    
def plot_fits(direction_rates,fit_curve,title):
    """
    This function takes the x-values and the y-values  in units of spikes/s 
    (found in the two columns of direction_rates and fit_curve) and plots the 
    actual values with circles, and the curves as lines in both linear and 
    polar plots.
    """
    return NotImplementedError 

def von_mises_fitfunc(x, A, kappa, l, s):
    """
    This creates a scaled Von Mises distrubition.
    """
    return A*stats.vonmises.pdf(x, kappa, loc=l, scale=s)


    
def preferred_direction(fit_curve):
    """
    The function takes a 2-dimensional array with the x-values of the fit curve
    in the first column and the y-values of the fit curve in the second.  
    It returns the preferred direction of the neuron (in degrees).
    """

    return NotImplementedError
    
        
##########################
#You can put the code that calls the above functions down here    
if __name__ == '__main__':
    trials = load_experiment('trials.npy')
    spikes = load_neuraldata('example_spikes.npy')
    # now we want to bin the data and determine the rate of firing for each direction
    dir_spikes = bin_spikes(trials, spk_times)
