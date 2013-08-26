def bubble_sort(data):
    for curstep in range(len(data) - 1, 0, -1):
        for i in range(curstep):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]

if __name__ == '__main__':
    import animation
    animation.play_sorting_movie(bubble_sort)
