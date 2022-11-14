import cv2
import numpy
import torch

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
P4th = "/home/josh/Pictures/kermit.png"


def open_cv_rotate(path, dire, key):
    image = cv2.imread(path)
    cv2.imshow("kermit", image)
    image = cv2.rotate(image, dire)
    cv2.imshow("kermit2", image)
    cv2.waitKey(key)


def numpy_rotate(path, key):
    image = cv2.imread(path)
    image = numpy.array(image)
    cv2.imshow("kermit3", image)
    image = numpy.rot90(image)
    cv2.imshow("kermit4", image)
    cv2.waitKey(key)


def man_rotate(path, key):
    image = cv2.imread(path)
    imarr = numpy.array(image)
    for i in range(imarr.size):
        for j in range(imarr[0].size):
            nimarr = imarr[j][i]
    cv2.imshow("Kermit5", nimarr)


def check_cuda(device):
    print('Using device:', device)
    if device.type == 'cuda':
        print(torch.cuda.get_device_name(0))
        print('Memory Usage:')
        print('Allocated:', round(torch.cuda.memory_allocated(0) / 1024 ** 3, 1), 'GB')
        print('Cached:   ', round(torch.cuda.memory_reserved(0) / 1024 ** 3, 1), 'GB')


open_cv_rotate(P4th, cv2.ROTATE_90_COUNTERCLOCKWISE, 0)
numpy_rotate(P4th, 0)
# man_rotate(P4th, 0)
check_cuda(device)
