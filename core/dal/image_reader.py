import numpy as np
import pydicom

from core.common.parameters import ImagePath

class ImageReader:

    def __init__(self, patient_num, healthy=True):
        self.patient_num = patient_num
        self.conv_dicom = self._get_conv(patient_num, healthy)
        self.rows = self.conv_dicom.Rows
        self.columns = self.conv_dicom.Columns

    def _anonymize_dicom(self, img, file_name):
        img.PatientID = ''
        img.PatientName = ''
        img.InstitutionName = ''
        img.Manufacturer = ''
        img.InstitutionAddress = ''
        img.save_as(file_name)
        return img

    def _get_conv(self, patient_num, healthy):
        path = ImagePath().get_conv_path(patient_num)
        conv_dicom = pydicom.dcmread(path)
        conv_dicom = self._anonymize_dicom(conv_dicom, path)
        return conv_dicom

    def get_images(self):
        vme_array = np.zeros((7, self.rows, self.columns))
        vme_titles = np.arange(40, 110, 10)
        vme_indices = np.arange(0, 7, 1)

        # for path in path.glob() something...
        for img_title, index in zip(vme_titles, vme_indices):
            path = ImagePath().get_vme_path(self.patient_num, img_title)
            vme = pydicom.dcmread(path)
            vme = self._anonymize_dicom(vme, path)
            vme_array[index] = vme.pixel_array

        # this makes no sense, re-write to get image data, call conv, vme internally
        # remove  everything patient_num from init
        return {'conv': self.conv_dicom.pixel_array, 'vmes': vme_array}

