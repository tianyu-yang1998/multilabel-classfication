from typing import * 
from pathlib import Path
import moviepy
import decord
import numpy as np 
from numpy import ndarray
import os 
from PIL import Image

def get_video_feature(video_path: Union[str, Path]=""):
    if os.path.isdir(video_path):
        frame_path_list: List[str] = sorted((os.path.join(video_path, x) for x in os.listdir(video_path)))
        frames: List[ndarray] = [np.asarray(Image.open(x)) for x in frame_path_list]
    else:
        video: decord.VideoLoader = decord.VideoLoader(video_path)
        frames: List[ndarray] = [x.asnumpy() for x in video]
        print(frames[0])
    return 
        

def main() -> None:
    get_video_feature("/home/tianyu/multilabel-classfication/AVQA/data/video_frames/00000002") 

if __name__ == "__main__":
    main() 