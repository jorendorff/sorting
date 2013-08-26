def quicksort(data):
    def f(start, stop):
        if stop - start < 2:
            return  # nothing to do
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

        # Swap the pivot to the middle.
        data[stop - 1] = data[i]
        data[i] = pivot

        # Sort the halves and we're done.
        f(start, i)
        f(i + 1, stop)
    f(0, len(data))

if __name__ == '__main__':
    import animation
    animation.play_sorting_movie(quicksort)
