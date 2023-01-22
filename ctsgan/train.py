import os.path as osp
from basicsr.train import train_pipeline

import ctsgan.archs
import ctsgan.data
import ctsgan.models

if __name__=="__main__":
    root_path = osp.abspath(osp.join(__file__, osp.paradir, osp.paradir))
    train_pipeline(root_path)