# Sorting

There are tons of different sorting methods available.  Reading about
them is one thing; watching them run is something entirely different.
This project allows you to easily watch as various sorting algorithms
perform their magic, helping you to gain a better understanding of how
they work.

# Setup

Getting started with this project is as easy as

    git clone https://github.com/jasonamyers/sorting.git
    cd sorting
    pip install -r requirements.txt
    python <filename_of_algorithm>

# Contribute

If you would like to add an additional sorting mechanism,
just look at one of the existing files, like `bubble_sort.py`,
to see how it's done.

In short, you write a function that implements a sorting algorithm,
then call `animation.show_sorting_movie(my_sort_function)`
to see it at work.
