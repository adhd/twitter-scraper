# reads a list of Twitter handles from a file named handles.txt, cleans them up by removing any 
# leading/trailing whitespaces or punctuation marks, and submits each handle to a Celery task 
# named do_work using .delay()

# Import the 'do_work' function from the 'task_receiver' module
from .task_receiver import do_work

# Define a function to submit a list of Twitter handles to the 'do_work' task
def submit_handles(handles):
    # For each handle in the list, clean it up and submit it to the 'do_work' task
    for handle in handles:
        # Remove any leading/trailing whitespaces or punctuation marks from the handle
        handle = handle.strip()
        handle = handle.strip(".!,")
        # Submit the cleaned up handle to the 'do_work' task using Celery's '.delay()' method
        do_work.delay(handle)
        # Print a message for the handle submitted for debugging purposes
        print("submitted " + handle)

# If this module is run as the main program, read the list of handles from 'handles.txt' and submit them to the 'submit_handles' function
if __name__ == '__main__':
    handles = list()
    with open("handles.txt", "r") as f:
        handles = f.readlines()

    submit_handles(handles)
