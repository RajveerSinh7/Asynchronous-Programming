import time

start = time.time()

def get_movie_tickets():
    time.sleep(3)
    print("got the movie tickets")

def use_instagram():
    time.sleep(1)
    print("opened instagram")

def main():
    get_movie_tickets()
    use_instagram()

main()

end = time.time()
print('time of execution: ', (end-start))