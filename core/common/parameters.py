from pathlib import Path # use this to implement getting path to image?

# TODO restructure, enumlike?

class ImagePath:
    HEALTHY_IMG_PATH = 'input/healthy/'
    STROKE_IMG_PATH = 'input/stroke/'
    CONV = 'conv'

    def _get_parent_img_path(self, patient_num):
        if Subjects().is_healthy(patient_num):
            return self.HEALTHY_IMG_PATH
        return self.STROKE_IMG_PATH

    def _get_path(self, patient_num):
        path_to_image_dir = self._get_parent_img_path(patient_num)
        path_to_img = Path(__file__).joinpath('..','..', '..', path_to_image_dir, patient_num).resolve()
        return path_to_img

    def get_conv_path(self, patient_num):
        path = self._get_path(patient_num)
        return str(path.joinpath('conv').resolve())

    def get_vme_path(self, patient_num, img_title):
        path_to_image_dir = self._get_parent_img_path(patient_num)
        path_to_img = Path(__file__).joinpath('..','..', '..', path_to_image_dir, patient_num, str(img_title)).resolve()
        return str(path_to_img)

class Subjects:
    HEALTHY_SUBJECTS = ['8234', '8988']
    UNHEALTHY_SUBJECTS = ['0006', '1841', '1538a', '1538b', '1538c'] # TODO account for 3 sets of images here

    SUBJECT1 = '8234'
    SUBJECT2 = '8988'
    SUBJECT3 = '0006'
    SUBJECT4 = '1842'
    SUBJECT5 = '1538a'
    SUBJECT6 = '1538b'
    SUBJECT7 = '1538c'

    def is_healthy(self, patient_num):
        return patient_num in self.HEALTHY_SUBJECTS

    @classmethod
    def get_all_subjects(cls):
        return cls.HEALTHY_SUBJECTS + cls.UNHEALTHY_SUBJECTS