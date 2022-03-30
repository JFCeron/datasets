# Copyright 2020 The HuggingFace Datasets Authors and the current dataset script contributor.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import tarfile

import datasets
from datasets.tasks import AutomaticSpeechRecognition

# Find for instance the citation on arxiv or on the dataset repo/website
_CITATION = """\
@article{DBLP:journals/corr/abs-2111-09344,
  author    = {Daniel Galvez and
               Greg Diamos and
               Juan Ciro and
               Juan Felipe Ceron and
               Keith Achorn and
               Anjali Gopi and
               David Kanter and
               Maximilian Lam and
               Mark Mazumder and
               Vijay Janapa Reddi},
  title     = {The People's Speech: A Large-Scale Diverse English Speech Recognition
               Dataset for Commercial Usage},
  journal   = {CoRR},
  volume    = {abs/2111.09344},
  year      = {2021},
  url       = {https://arxiv.org/abs/2111.09344},
  eprinttype = {arXiv},
  eprint    = {2111.09344},
  timestamp = {Mon, 22 Nov 2021 16:44:07 +0100},
  biburl    = {https://dblp.org/rec/journals/corr/abs-2111-09344.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
"""

# You can copy an official description
_DESCRIPTION = """\
The People's Speech is a free-to-download 30,000-hour and growing supervised 
conversational English speech recognition dataset licensed for academic and 
commercial usage under CC-BY-SA (with a CC-BY subset).
"""

_HOMEPAGE = "https://mlcommons.org/en/peoples-speech/"

_LICENSE = [
    "cc-by-2.0", "cc-by-2.5", "cc-by-3.0", "cc-by-4.0", "cc-by-sa-2.5", 
    "cc-by-sa-3.0", "cc-by-sa-4.0"
]

# TODO: Add link to the official dataset URLs here
# The HuggingFace Datasets library doesn't host the datasets but only points to the original files.
# This can be an arbitrary nested dict/list of URLs (see below in `_split_generators` method)
_URLS = {
    "clean-cc-by": {
        "audio_tar": "",
        "manifest": "",
    },
    "dirty-cc-by": {
        "audio_tar": "",
        "manifest": "",
    },
    "clean-cc-by-sa": {
        "audio_tar": "",
        "manifest": "",
    },
    "dirty-cc-by-sa": {
        "audio_tar": "",
        "manifest": "",
    },
    "microset":  {
        "audio_tar": "",
        "manifest": "",
    },
}


class PeoplesSpeech(datasets.GeneratorBasedBuilder):
    """The People's Speech dataset."""
    
    VERSION = datasets.Version("1.1.0")
    BUILDER_CONFIGS = [
        datasets.BuilderConfig(name="clean-cc-by", version=VERSION, description="Clean, CC-BY licensed subset."),
        datasets.BuilderConfig(name="dirty-cc-by", version=VERSION, description="Dirty, CC-BY licensed subset."),
        datasets.BuilderConfig(name="clean-cc-by-sa", version=VERSION, description="Clean, CC-BY-SA licensed subset."),
        datasets.BuilderConfig(name="dirty-cc-by-sa", version=VERSION, description="Dirty, CC-BY-SA licensed subset."),
    ]
    DEFAULT_CONFIG_NAME = "clean-cc-by"
    DEFAULT_WRITER_BATCH_SIZE = 1

    def _info(self):
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=datasets.Features(
                {
                    "id": datasets.Value("string"),
                    "audio": datasets.Audio(sampling_rate=16_000),
                    "duration_ms": datasets.Value("int32"),
                    "text": datasets.Value("string"),
                }
            ),
            task_templates=[AutomaticSpeechRecognition()],
            supervised_keys=("file", "text"),
            homepage=_HOMEPAGE,
            license=_LICENSE,
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        url = _URLS[self.config.name]
        dl_paths = dl_manager.download(url)
        #dl_paths = {
        #    "audio_tar": "~/data/the_peoples_speech/cc-by-clean/1.1.0/audios.tar",
        #    "manifest": "~/data/the_peoples_speech/cc-by-clean/1.1.0/manifest.json",
        #}
        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN,
                gen_kwargs={
                    "audio_tarfile_path": dl_paths["audio_tar"],
                    "manifest_path": dl_paths["manifest"]
                },
            ),
        ]

    def _generate_examples(self, audio_tarfile_path, manifest_path):
        key = 0
        sample_metadata = {}

        with tarfile.open(audio_tarfile_path, mode="r|") as audio_tarfile, \
             open(manifest_path, "r") as manifest:

            for audio_tarinfo in audio_tarfile:
                audio_name = audio_tarinfo.name
                audio_file_obj = audio_tarfile.extractfile(audio_tarinfo)
                
                # Read from manifest until metadata for audio shows up
                metadata_found = audio_name in sample_metadata
                while not metadata_found:
                    try:
                        manifest_line = next(manifest)
                    except StopIteration:
                        break
                    manifest_line_struct = json.loads(manifest_line)
                    manifest_line_samples = manifest_line_struct["training_data"]
                    for duration_ms, label, other_audio_name in zip(
                        manifest_line_samples["duration_ms"],
                        manifest_line_samples["label"],
                        manifest_line_samples["name"]
                        ):
                        sample_metadata[other_audio_name] = {
                            "id": other_audio_name,
                            "duration_ms": duration_ms,
                            "text": label,
                        }
                    metadata_found = audio_name in sample_metadata
                
                # Yield if audio metadata was found
                if metadata_found:
                    audio = {
                        "path": audio_name,
                        "bytes": audio_file_obj.read()
                    }
                    sample = sample_metadata.pop(audio_name)
                    sample["audio"] = audio
                    yield key, sample
                    key += 1