# MultiWOZ 2.4
This is the dataset described in the paper: **MultiWOZ 2.4: A Multi-Domain Task-Oriented Dialogue Dataset with Essential Annotation Corrections to Improve State Tracking Evaluation. Fanghua Ye, Jarana Manotumruksa, Emine Yilmaz. SIGDIAL 2022.** [[paper](https://arxiv.org/abs/2104.00773)]

MultiWOZ 2.4 is a refined version of MultiWOZ 2.1. Specifically, we carefully rectified (almost) all the annotation errors in the validation set and test set. We keep the training set intact.

MultiWOZ 2.4 shares exactly the same format as MultiWOZ 2.1, thus it is pretty easy for us to run existing models that are built upon MultiWOZ 2.1 on MultiWOZ 2.4.

## Data Preprocessing
MultiWOZ 2.4 can be preprocessed by the script create_data.py
```console
❱❱❱ python3 create_data.py
```
or simply by the script split.py
```console
❱❱❱ python3 split.py
```

## Benchmark Results
We test the performance of nine SOTA dialogue state tracking models on MultiWOZ 2.4. All the chosen models demonstrate much higher performance (joint goal accuracy), benefiting from the improved test set.

| Model | MultiWOZ 2.1 | MultiWOZ 2.4 |
|-------|--------------|--------------|
| SUMBT |    49.01%    |    61.86%  |
| CHAN  |53.38%|68.25%|
|[STAR](https://arxiv.org/pdf/2101.09374.pdf)|56.36%|73.62%|
|TRADE|45.60%|55.05%|
|PIN|48.40%|58.92%|
|SOM-DST|51.24%|66.78%|
|SimpleTOD|51.75%|57.18%|
|SAVN|54.86%|60.55%|
|TripPy|55.18%|64.75%|
|[IC-DST (GPT3)](https://arxiv.org/abs/2203.08568)|50.65%|62.43%|
|[Seq2Seq](https://arxiv.org/pdf/2108.13990.pdf)|54.4%|67.10%|
|[TripPy-R](https://arxiv.org/pdf/2202.03354.pdf)|55.99%|69.87%|
|[D3ST (XXL)](https://arxiv.org/pdf/2201.08904.pdf)|57.8%|75.90%|
|[ASSIST (STAR)](https://arxiv.org/pdf/2202.13024.pdf)|-|79.41%|
|[MetaASSIST (STAR)](https://arxiv.org/pdf/2210.12397.pdf)|-|80.10%|
