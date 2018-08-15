import multiprocessing


class CountCores:
    def execute(self):
        print("Numbr of CPUs: " + str(multiprocessing.cpu_count()) + "\n")
        print("Current Processes; " + str(multiprocessing.current_process()) +"\n")

if __name__ == "__main__":
    count_cores = CountCores()
    count_cores.execute()
