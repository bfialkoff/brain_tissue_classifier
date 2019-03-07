from skimage import morphology

class ImgProcessor:
    def __init__(self, img_data):
        self.conv = img_data['conv']
        self.vme_box = img_data['vmes']

    def _get_brain_mask(self):
        first_step = self._segmenter(self.conv, 15, 45, should_fill_holes=True)
        isolated_conv = self._segmenter(first_step, 17, 48)
        mask = isolated_conv > 0
        return mask

    def _segmenter(self, conv, bottom_val, top_val, should_fill_holes=False):
        bottom_bound = (conv > bottom_val + 1024).reshape(conv.shape)
        top_bound = (conv < top_val + 1024).reshape(conv.shape)
        mask = bottom_bound * top_bound
        mask = morphology.remove_small_objects(mask, 1000)
        if should_fill_holes:
            morphology.remove_small_holes(mask, in_place=True)
        return mask * conv

    def apply_mask_to_conv(self):
        mask = self._get_brain_mask()
        return mask * self.conv


    def apply_mask_to_vmes(self):
        mask = self._get_brain_mask()
        masked_vmes = mask * self.vme_box #problem, actually i think this is fine
        return masked_vmes
