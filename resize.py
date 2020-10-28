from PIL import Image
import glob

for i, im in enumerate(glob.glob('*.png')):
    img = Image.open(im)

    img_resize = img.resize((256, 256))
    # img_resize.save('{}_resize.jpg'.format(i+3))

    img_resize_lanczos = img.resize((256, 256), Image.LANCZOS)
    img_resize_lanczos.save('{}_lanczos_resize.png'.format(i))
