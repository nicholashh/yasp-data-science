
from codecs import open as codecs_open
from gzip import open as g_zip_open
from json import loads as json_load_str
from random import random

# split a matches dump up into learning, testing, and validation datasets
def make_data_files (
    path_to_matches_dump,
    path_to_output,
    num_matches_to_write,
    testing_rate,
    validation_rate):

    # open the file as a stream and up-gzip it
    f = g_zip_open(path_to_matches_dump, 'r')

    # create the desired output files
    f_learning   = codecs_open(path_to_output + "learning",   "w", "utf-8-sig")
    f_testing    = codecs_open(path_to_output + "testing",    "w", "utf-8-sig")
    f_validation = codecs_open(path_to_output + "validation", "w", "utf-8-sig")

    # keep track of the number of matches written
    num_written_learning = 0
    num_written_testing = 0
    num_written_validation = 0
    num_attempts = 0

    # calculate the percentage cutoffs for the various datasets
    testing_cutoff = testing_rate
    validation_cutoff = testing_rate + validation_rate

    # print the algorithm's progress
    def print_status (prefix):
        print(prefix + " L %d T %d V %d" % (num_written_learning, 
            num_written_testing, num_written_validation))

    for line in f:

        # periodically print the algorithm's progress
        if num_attempts % 25 == 0: print_status("progress:")

        # attempt to parse the match as a JSON object
        num_attempts += 1
        line_as_string = line.decode("utf-8")
        try: match = json_load_str(line_as_string)

        # not all lines of the dump are JSON objects, so just ignore the ones 
        # that aren't (beginning the list, only containing a comma, etc)
        except: continue

        # randomly pick which dataset this match should join
        which_file = None
        rand_value = random()
        if rand_value < testing_cutoff:
            which_file = f_testing
            num_written_testing += 1
        elif rand_value < validation_cutoff:
            which_file = f_validation
            num_written_validation += 1
        else:
            which_file = f_learning
            num_written_learning += 1
        
        # add this match to that dataset
        which_file.write(str(match) + "\n")

        # stop writing when we've written the desired number of matches
        if num_written_learning >= num_matches_to_write: break

    # done! print the final status of the algorithm
    print_status("done! final:")

# actually run the code on your matches dump
make_data_files('./yasp-dump-2015-12-18.json.gz', './data/', 50, 0.1, 0.1)
