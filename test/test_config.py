#
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
import os

from sionna_rt_gui import CONFIGS_DIR
from sionna_rt_gui.config import load_config, save_config


def test_example_config():
    cfg = load_config(os.path.join(CONFIGS_DIR, "example.yaml"))
    assert cfg.radio_map.display_radius_min == 1.0
    assert cfg.paths.display_radius_min == 0.3


def test_default_radius_config_values():
    cfg = load_config(os.path.join(CONFIGS_DIR, "base.yaml"))
    assert cfg.radio_map.display_radius_min == 1.0
    assert cfg.paths.display_radius_min == 0.3


def test_config_round_trip(tmp_path):
    source_path = os.path.join(CONFIGS_DIR, "example.yaml")
    output_path = tmp_path / "round_trip.yaml"

    cfg = load_config(source_path, scene_filename="custom_scene.xml")
    save_config(cfg, output_path)
    loaded = load_config(output_path)

    assert loaded.scene_filename == "custom_scene.xml"
    assert loaded.gui_mode == cfg.gui_mode
    assert loaded.background_color == cfg.background_color
    assert loaded.tx_array.vertical_spacing == cfg.tx_array.vertical_spacing
    assert loaded.rendering.max_accumulated_spp == cfg.rendering.max_accumulated_spp
    assert loaded.radio_map.display_radius_min == cfg.radio_map.display_radius_min
    assert loaded.paths.display_radius_min == cfg.paths.display_radius_min
