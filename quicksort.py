def quicksort(data):
    def sort_slice(start, stop):
        if stop - start < 2:
            return  # nothing to do

        # Choose a pivot. We do the simplest possible thing here, but
        # see <https://en.wikipedia.org/wiki/Quicksort#Choice_of_pivot>.
        pivot = data[stop - 1]

        # Split data[start:stop] into two piles,
        # those above the pivot and those below.
        i = start
        j = stop - 1
        while i < j:
            item = data[i]
            if item >= pivot:
                j -= 1
                data[i] = data[j]
                data[j] = item
            else:
                i += 1

        # Swap the pivot to the middle, between the two piles.
        data[stop - 1] = data[i]
        data[i] = pivot

        # Sort both piles and we're done.
        sort_slice(start, i)
        sort_slice(i + 1, stop)
    sort_slice(0, len(data))

if __name__ == '__main__':
    import animation
    animation.play_sorting_movie(quicksort)
