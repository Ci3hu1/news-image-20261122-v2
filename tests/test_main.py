#!/usr/bin/env python3
"""Tests for the news-image-20261122 v2 entrypoint (main.py, pure stdlib).

Run: python3 -m unittest discover -s tests -v
"""
import hashlib
import importlib.util
import os
import shutil
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def _load_main():
    spec = importlib.util.spec_from_file_location(
        "v2_entrypoint", os.path.join(ROOT, "main.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class TestEntrypoint(unittest.TestCase):
    def setUp(self):
        self.mod = _load_main()
        self.tmp = tempfile.mkdtemp(prefix="ni22v2-")
        self.addCleanup(shutil.rmtree, self.tmp, True)

    def test_bundled_image_exists_and_matches_recorded_hash(self):
        src = self.mod._bundle_path()
        self.assertTrue(os.path.isfile(src), "entry.png must ship in repo")
        self.assertEqual(self.mod._digest(src), self.mod.BUNDLED_SHA256)
        self.assertLessEqual(os.path.getsize(src), 1024 * 1024,
                             "entry.png must be at most 1 MiB")
        from PIL import Image
        with Image.open(src) as im:
            self.assertEqual(im.size, (1024, 1024))
            self.assertEqual(im.mode, "RGB")

    def test_place_copies_byte_identical(self):
        src = self.mod._bundle_path()
        dst = os.path.join(self.tmp, "sub", "entry.png")
        placed = self.mod._place(src, dst)
        self.assertEqual(placed, dst)
        self.assertEqual(self.mod._digest(dst), self.mod.BUNDLED_SHA256)
        self.assertEqual(os.path.getsize(dst), os.path.getsize(src))

    def test_run_writes_to_makefun_output_dir(self):
        out_dir = os.path.join(self.tmp, "out")
        os.makedirs(out_dir)
        env = dict(os.environ)
        env["MAKEFUN_OUTPUT_DIR"] = out_dir
        old = os.environ.get("MAKEFUN_OUTPUT_DIR")
        os.environ["MAKEFUN_OUTPUT_DIR"] = out_dir
        try:
            rc = self.mod.run()
        finally:
            if old is None:
                del os.environ["MAKEFUN_OUTPUT_DIR"]
            else:
                os.environ["MAKEFUN_OUTPUT_DIR"] = old
        self.assertEqual(rc, 0)
        target = os.path.join(out_dir, "entry.png")
        self.assertTrue(os.path.isfile(target))
        self.assertEqual(self.mod._digest(target), self.mod.BUNDLED_SHA256)

    def test_run_falls_back_when_env_dir_unwritable(self):
        # Point the env dir at a path that cannot be created (a file).
        blocker = os.path.join(self.tmp, "blocker")
        with open(blocker, "w") as fh:
            fh.write("x")
        env_dir = os.path.join(blocker, "sub")
        os.environ["MAKEFUN_OUTPUT_DIR"] = env_dir
        cwd = os.getcwd()
        work = os.path.join(self.tmp, "work")
        os.makedirs(work)
        os.chdir(work)
        try:
            rc = self.mod.run()
        finally:
            os.chdir(cwd)
            del os.environ["MAKEFUN_OUTPUT_DIR"]
        # /output may exist in this sandbox; either it wrote there or to
        # ./output.png — both are acceptable fallbacks, exit must be 0.
        self.assertEqual(rc, 0)
        self.assertTrue(
            os.path.isfile(os.path.join(work, "output.png"))
            or os.path.isfile("/output/entry.png"))

    def test_destinations_order(self):
        os.environ["MAKEFUN_OUTPUT_DIR"] = "/tmp/ni22v2-out"
        try:
            dests = self.mod._destinations()
        finally:
            del os.environ["MAKEFUN_OUTPUT_DIR"]
        self.assertEqual(dests[0], "/tmp/ni22v2-out/entry.png")
        self.assertEqual(dests[1], "/output/entry.png")
        self.assertTrue(dests[2].endswith("output.png"))

    def test_story_count_and_regions(self):
        # The poster data must total 36 stories across 7 regions.
        import render_poster as rp
        total = len(rp.LEADS) + len(rp.FEATURED) + len(rp.ALSO_ON)
        self.assertEqual(total, 36)
        self.assertEqual(len(rp.REGIONS), 7)
        self.assertEqual(sum(int(r[0].rsplit(" ", 1)[1]) for r in rp.REGIONS),
                         36)
        # Every ALSO_ON number is unique and 14..36 in order.
        nums = [n for n, _ in rp.ALSO_ON]
        self.assertEqual(nums, list(range(14, 37)))
        # No off-day story may sit in the main list.
        main_text = " ".join(
            [h["headline"] for h in rp.LEADS]
            + [s["headline"] for s in rp.FEATURED]
            + [t for _, t in rp.ALSO_ON])
        self.assertNotIn("Peru quake", main_text)
        self.assertNotIn("Bulgari", main_text)
        self.assertNotIn("missile city", main_text.lower())
        # DATE CHECK must hold the excluded items.
        dc = " | ".join(rp.DATE_CHECK)
        self.assertIn("Peru M6.7 quake", dc)
        self.assertIn("Paolo Bulgari dies", dc)
        self.assertIn("400-drone barrage", dc)
        # One drone number in the main list: 186 launched, 161 shot down.
        self.assertIn("186", main_text)
        self.assertNotIn("400-drone", main_text)


if __name__ == "__main__":
    unittest.main()
