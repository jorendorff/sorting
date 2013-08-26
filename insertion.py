def insertion_sort(data):
    for j in range(1, len(data)):
        i = j - 1
        value = data[j]

        while i >= 0 and data[i] > value:
            data[i + 1] = data[i]
            i -= 1

        data[i + 1] = value

if __name__ == '__main__':
    import animation
    animation.play_sorting_movie(insertion_sort)
