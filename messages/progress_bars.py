import time
from tqdm import tqdm


def progressBar1():
    for x in tqdm(range(100)):
        time.sleep(0.0005)