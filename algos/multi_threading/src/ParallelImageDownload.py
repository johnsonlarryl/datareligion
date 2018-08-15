import urllib.request
import time
import threading

PYTHON_URL = "https://cdn-images-1.medium.com/max/2000/1*PXHkfdYyliqb1qCrznu5TQ.jpeg"

HTTP_REQUEST_HEADERS = [('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),
                        ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
                        ('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'),
                        ('Accept-Encoding', 'none'),
                        ('Accept-Language', 'en-US,en;q=0.8'),
                        ('Connection', 'keep-alive')]


def download_image(image_path, file_name):
    opener = urllib.request.build_opener()
    opener.addheaders = HTTP_REQUEST_HEADERS
    urllib.request.install_opener(opener)
    # request = urllib.request.Request(image_path, headers=HTTP_REQUEST_HEADER)
    print("Downloading Image from ", image_path)
    urllib.request.urlretrieve(image_path, file_name)

def executeThread(i):
    image_name = "/Users/facts/Downloads/pythons/"
    download_image(PYTHON_URL, image_name + "python" + str(i) + ".jpeg")


def main():
    t0 = time.time()
    threads = []

    for i in range(100):
        thread = threading.Thread(target=executeThread, args=(i,))
        threads.append(thread)
        thread.start()

    # Ensure all threads have completed their execution before we log total completion time
    for thread in threads:
        thread.join()

    t1 = time.time()
    total_time = t1 - t0
    print("TOtal Execution Time {}".format(total_time))

if __name__ == "__main__":
    main()