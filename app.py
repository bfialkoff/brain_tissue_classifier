import numpy as np

from core.dal.image_reader import ImageReader
from core.bll.img_processor import ImgProcessor
from core.utils.image_viewer import display_image
from core.common.parameters import Subjects

all_patients = Subjects.get_all_subjects()
p = all_patients[0]
im_reader = ImageReader(p)
img_data = im_reader.get_images()
im_processor = ImgProcessor(img_data)
isolated_vmes = im_processor.apply_mask_to_vmes()
mask = im_processor._get_brain_mask()

i, j = np.non_zero(mask)
hu_array = isolated_vmes[:, mask]

pass