import os

BS_CATEGORY_IMAGES_PATH = os.path.join("uploads", "shop", "category", 'business')
MARKER_IMAGES_PATH = os.path.join("uploads", "shop", "category", "marker")
BUSINESS_IMAGES_PATH = os.path.join("uploads", "shop", "business")


def bs_category_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (instance.slug, instance.id, ext)
    return os.path.join(BS_CATEGORY_IMAGES_PATH, filename)


def markers_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (instance.slug, instance.id, ext)
    return os.path.join(MARKER_IMAGES_PATH, filename)


def business_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (instance.slug, instance.id, ext)
    return os.path.join(BUSINESS_IMAGES_PATH, instance.name, 'main', filename)


def business_branch_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (instance.slug, instance.id, ext)
    return os.path.join(BUSINESS_IMAGES_PATH, instance.business.name, 'branch', filename)

