import Augmentor
import os
def makedir(path):
    '''
    if path does not exist in the file system, create it
    '''
    if not os.path.exists(path):
        os.makedirs(path)

try:
    # datasets_root_dir = '/home/csantiago/CBIS/images/'
    datasets_root_dir = './../data/inbreast/'
    dir = datasets_root_dir + 'train_images/'
    mask_dir = datasets_root_dir + 'train_masks/'
    target_dir = datasets_root_dir + 'train_augmented/'

    makedir(target_dir)
    folders = [os.path.join(dir, folder) for folder in next(os.walk(dir))[1]]
    target_folders = [os.path.join(target_dir, folder) for folder in next(os.walk(dir))[1]]
    mask_folders = [os.path.join(mask_dir, folder) for folder in next(os.walk(mask_dir))[1]]


    for i in range(len(folders)):
        fd = folders[i]
        tfd = target_folders[i]
        mask_fd = mask_folders[i]
        # rotation
        p = Augmentor.Pipeline(source_directory=fd, output_directory=tfd)
        p.ground_truth(mask_fd)
        p.rotate_without_crop(probability=1, max_left_rotation=15, max_right_rotation=15)
        p.flip_left_right(probability=0.5)
        for i in range(10):
            p.process()
        del p
        # skew
        # p = Augmentor.Pipeline(source_directory=fd, output_directory=tfd)
        # p.ground_truth(mask_dir)
        # p.skew(probability=1, magnitude=0.2)  # max 45 degrees
        # p.flip_left_right(probability=0.5)
        # for i in range(10):
        #     p.process()
        # del p
        # # shear
        # p = Augmentor.Pipeline(source_directory=fd, output_directory=tfd)
        # p.ground_truth(mask_dir)
        # p.shear(probability=1, max_shear_left=10, max_shear_right=10)
        # p.flip_left_right(probability=0.5)
        # for i in range(10):
        #     p.process()
        # del p
        # random_distortion
        #p = Augmentor.Pipeline(source_directory=fd, output_directory=tfd)
        #p.random_distortion(probability=1.0, grid_width=10, grid_height=10, magnitude=5)
        #p.flip_left_right(probability=0.5)
        #for i in range(10):
        #    p.process()
        #del p
except Exception as e:
    print(e)
    print('Augmentation failed')
    pass
