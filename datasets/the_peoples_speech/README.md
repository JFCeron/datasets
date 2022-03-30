---
annotations_creators:
- crowdsourced
- machine-generated
language_creators:
- crowdsourced
- machine-generated
languages:
- en
licenses:
- cc-by-2.0
- cc-by-2.5
- cc-by-3.0
- cc-by-4.0
- cc-by-sa-2.5
- cc-by-sa-3.0
- cc-by-sa-4.0
multilinguality:
- monolingual
pretty_name: People's Speech
size_categories:
- 1T<n
source_datasets:
- original
task_categories:
- automatic-speech-recognition
task_ids:
- speech-recognition
- robust-speech-recognition
- noisy-speech-recognition
---

# Dataset Card for People's Speech

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
  - [Data Splits](#data-instances)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)

## Dataset Description

- **Homepage:** https://mlcommons.org/en/peoples-speech/
- **Repository:** https://github.com/mlcommons/peoples-speech
- **Paper:** https://arxiv.org/abs/2111.09344
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** datasets@mlcommons.org

### Dataset Summary

The People's Speech Dataset is among the world's largest English speech recognition corpus today that is licensed for academic and commercial usage under CC-BY-SA and CC-BY 4.0. It includes 30,000+ hours of transcribed speech in English languages with a diverse set of speakers. This open dataset is large enough to train speech-to-text systems and crucially is available with a permissive license.

### Supported Tasks and Leaderboards

[Needs More Information]

### Languages

English

## Dataset Structure

### Data Instances

{
    "id": "gov_DOT_uscourts_DOT_scotus_DOT_19-161/gov_DOT_uscourts_DOT_scotus_DOT_19-161_DOT_2020-03-02_DOT_mp3_00002.flac",
    "audio": {
        "path": "gov_DOT_uscourts_DOT_scotus_DOT_19-161/gov_DOT_uscourts_DOT_scotus_DOT_19-161_DOT_2020-03-02_DOT_mp3_00002.flac"
        "array": array([-6.10351562e-05, ...]),
        "sampling_rate": 16000
    }
    "duration_ms": 14490,
    "text": "contends that the suspension clause requires a [...]"
}

### Data Fields

{
    "id": datasets.Value("string"),
    "audio": datasets.Audio(sampling_rate=16_000),
    "duration_ms": datasets.Value("int32"),
    "text": datasets.Value("string"),
}

### Data Splits

We provide the following configurations for the dataset: `cc-by-clean`, `cc-by-dirty`, `cc-by-sa-clean`, `cc-by-sa-dirty`, and `microset`. We don't provide splits for any of the configurations.

## Dataset Creation

### Curation Rationale

See our [paper](https://arxiv.org/abs/2111.09344).

### Source Data

#### Initial Data Collection and Normalization

See our [paper](https://arxiv.org/abs/2111.09344).

#### Who are the source language producers?

See our [paper](https://arxiv.org/abs/2111.09344).

### Annotations

#### Annotation process

See our [paper](https://arxiv.org/abs/2111.09344).

#### Who are the annotators?

See our [paper](https://arxiv.org/abs/2111.09344).

### Personal and Sensitive Information

See our [paper](https://arxiv.org/abs/2111.09344).

## Considerations for Using the Data

### Social Impact of Dataset

See our [paper](https://arxiv.org/abs/2111.09344).

### Discussion of Biases

See our [paper](https://arxiv.org/abs/2111.09344).

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

[Needs More Information]

### Licensing Information

We provide CC-BY and CC-BY-SA subsets of the dataset.

### Citation Information

[Needs More Information]