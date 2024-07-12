import os
import glob

import tyro
from src.config.argument_config import ArgumentConfig
from src.config.inference_config import InferenceConfig
from src.config.crop_config import CropConfig
from src.live_portrait_pipeline import LivePortraitPipeline


def partial_fields(target_class, kwargs):
    return target_class(**{k: v for k, v in kwargs.items() if hasattr(target_class, k)})


def process_single_image(args):
    live_portrait_pipeline.execute(args)


def process_multi_image(args, root):
    paths = glob.glob(os.path.join(root, "*"))
    for path in paths:
        args.source_image = path
        live_portrait_pipeline.execute(args)


if __name__ == '__main__':
    # set tyro theme
    tyro.extras.set_accent_color("bright_cyan")
    args = tyro.cli(ArgumentConfig)

    # specify configs for inference
    inference_cfg = partial_fields(InferenceConfig, args.__dict__)  # use attribute of args to initial InferenceConfig
    crop_cfg = partial_fields(CropConfig, args.__dict__)  # use attribute of args to initial CropConfig

    live_portrait_pipeline = LivePortraitPipeline(
        inference_cfg=inference_cfg,
        crop_cfg=crop_cfg
    )

    # process single image
    process_single_image(args)

    # process single image
    # process_multi_image(args, "assets/examples/source")
