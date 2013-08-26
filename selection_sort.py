def selection_sort(data):
    for j in range(0, len(data) - 1):
        lowest = j
        for i in range(j + 1, len(data)):
            if data[i] < data[lowest]:
                lowest = i
        if j != lowest:
            data[j], data[lowest] = data[lowest], data[j]

if __name__ == '__main__':
    import animation
    animation.play_sorting_movie(selection_sort)

