import "andax/bump_extras.rhai" as bump;
import "andax/spec.rhai" as spec;

rpm.version(find(`<small>ffmpeg-([\d.]+?)\.tar\.xz</small>`, get("https://ffmpeg.org/download.html"), 1));

open_file("anda/multimedia/ffmpeg/VERSION_x265.txt", "w").write(bump::madoguchi("x265", labels.branch));
open_file("anda/multimedia/ffmpeg/VERSION_tesseract.txt", "w").write(bump::bodhi("tesseract", bump::as_bodhi_ver(labels.branch)));
open_file("anda/multimedia/ffmpeg/VERSION_vvenc.txt", "w").write(bump::madoguchi("vvenc-libs", labels.branch));

import "andax/ci/bump_release.rhai";
