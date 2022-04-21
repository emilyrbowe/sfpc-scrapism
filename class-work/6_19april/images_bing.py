from bing_image_downloader import downloader

# downloader.download(
#     "Rosa Luxemburg",
#     limit=100,
#     output_dir="rosa",
#     adult_filter_off=False,
#     force_replace=False,
#     timeout=60,
# )

downloader.download(
    "smart city",
    limit=30,
    output_dir="smart_city",
    adult_filter_off=False,
    force_replace=False,
    timeout=60,
)