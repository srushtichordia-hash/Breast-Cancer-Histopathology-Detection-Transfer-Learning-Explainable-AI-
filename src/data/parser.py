from pathlib import Path

import pandas as pd


class BreakHisParser:

    IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff"}

    def __init__(self, dataset_path: Path):
        self.dataset_path = dataset_path

    def _is_image(self, file: Path) -> bool:
        return file.suffix.lower() in self.IMAGE_EXTENSIONS

    def build_metadata(self) -> pd.DataFrame:
        rows = []

        for class_folder in self.dataset_path.iterdir():

            if not class_folder.is_dir():
                continue

            class_name = class_folder.name

            sob_folder = class_folder / "SOB"

            if not sob_folder.exists():
                continue

            for subtype_folder in sob_folder.iterdir():

                if not subtype_folder.is_dir():
                    continue

                subtype = subtype_folder.name

                for patient_folder in subtype_folder.iterdir():

                    if not patient_folder.is_dir():
                        continue

                    patient_id = patient_folder.name

                    for magnification_folder in patient_folder.iterdir():

                        if not magnification_folder.is_dir():
                            continue

                        magnification = magnification_folder.name

                        for image_file in magnification_folder.iterdir():

                            if not image_file.is_file():
                                continue

                            if not self._is_image(image_file):
                                continue

                            rows.append(
                                {
                                    "image_path": str(image_file.resolve()),
                                    "class": class_name,
                                    "subtype": subtype,
                                    "patient_id": patient_id,
                                    "magnification": magnification,
                                }
                            )

        return pd.DataFrame(rows)