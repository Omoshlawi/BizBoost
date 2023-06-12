import os

CATEGORY_IMAGES_PATH = os.path.join("uploads", "products", "category")
PRODUCTS_IMAGES_PATH = os.path.join("uploads", "products", "products")


def category_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.slug, ext)
    return os.path.join(CATEGORY_IMAGES_PATH, filename)


def product_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (instance.slug, instance.category.slug, ext)
    return os.path.join(PRODUCTS_IMAGES_PATH, filename)


def product_secondary_image_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.product.slug, ext)
    return os.path.join(PRODUCTS_IMAGES_PATH, filename)
