import argparse
from pathlib import Path
import cv2
import numpy as np


def command():
	parser = argparse.ArgumentParser(description=help)
	parser.add_argument('img', nargs='1', help="input images")
	
	args = parser.parse_args()
	return args



def main(args):
	# 画像の出力先の設定
	save_dir = Path("out")
	if not save_dir.exists():
		save_dir.mkdir(parents=True)

	img = cv2.imread(img)

	cv2.imwrite(Path(save_dir+"img01.png"), img)

if __name__ == '__main__':
	main(command())