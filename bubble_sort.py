def bubble_sort(data):
    done = False
    while not done:
        done = True  # maybe we are all done
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                done = False  # nope

if __name__ == '__main__':
    import animation
    animation.play_sorting_movie(bubble_sort)
