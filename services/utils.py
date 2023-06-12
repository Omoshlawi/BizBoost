import os

SERVICES_CATEGORY_IMAGES_PATH = os.path.join("uploads", "services", "category")
SERVICES_IMAGES_PATH = os.path.join("uploads", "services", "products")


def service_category_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (instance.slug, instance.id, ext)
    return os.path.join(SERVICES_CATEGORY_IMAGES_PATH, filename)


def service_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (instance.slug, instance.category.slug, ext)
    return os.path.join(SERVICES_IMAGES_PATH, filename)
