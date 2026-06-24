#
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
import os

from sionna_rt_gui import CONFIGS_DIR
from sionna_rt_gui.config import load_config


def test_example_config():
    cfg = load_config(os.path.join(CONFIGS_DIR, "example.yaml"))
    assert cfg.radio_map.display_radius_min == 1.0
    assert cfg.paths.display_radius_min == 0.3


def test_default_radius_config_values():
    cfg = load_config(os.path.join(CONFIGS_DIR, "base.yaml"))
    assert cfg.radio_map.display_radius_min == 1.0
    assert cfg.paths.display_radius_min == 0.3
