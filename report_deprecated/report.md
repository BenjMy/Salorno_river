---
title: 3D ERT Time-Lapse on a River Bank (Salerno2)
description: ""
date: 2021-08-11T23:37:33.990Z
authors:
  - name: Benjamin M.
    userId: 4hjVRcSwHgd3ONBMyRs9VxBrHAB2
    orcid: 0000-0001-7199-2885
    corresponding: null
    email: null
    roles: null
    affiliations: null
name: report
oxa: oxa:wjcU0xFUCQKRwMTRhf0q/Hgd8tnoHxT8YAlQ7clog
---

# 3D ERT Time-Lapse on a River Bank (Salerno2)

+++ {"oxa":"oxa:wjcU0xFUCQKRwMTRhf0q/KRJeu2LlBvzPnzxN8N8j.3"}

ERT cross-boreholes tomography on a River bank

Report for the background dataset, collected in Salerno.

📅 December 6th, 2021

🗺️ Salerno field site 2

+++ {"oxa":"oxa:wjcU0xFUCQKRwMTRhf0q/FirTZMUZz6ZNUJWrXfI6.3"}

# Data acquisition

````{important}
* number of boreholes: 5
* electrode spacing: 1m
* nb of electrodes/boreholes: 24
* ! Topography, 1st electrode depth different according to borehole position

````

+++ {"oxa":"oxa:wjcU0xFUCQKRwMTRhf0q/TufHnhraubhTNpiMII9Y.2"}

```{figure} images/wjcU0xFUCQKRwMTRhf0q-TufHnhraubhTNpiMII9Y-v2.png
:name: 1638834957204
```

+++ {"oxa":"oxa:wjcU0xFUCQKRwMTRhf0q/8cuT44f8aXgN2HgXpty1.2"}



+++ {"oxa":"oxa:wjcU0xFUCQKRwMTRhf0q/9ZCzy67iQHmxOrniPtUE.5"}

# Data processing

* 1167 duplicates removed


* reciprocal filter 10%

````{note}
```
Survey.filterDefault: 1167 duplicates removed.
Survey.filterDefault: 2 measurements with A or B == M or N
filterData: 2 / 19221 quadrupoles removed.
18558/19219 reciprocal measurements found.
6512 measurements error > 20 %
18558/19219 reciprocal measurements found.
6512 measurements error > 20 %
9542 measurements with greater than 10.0% reciprocal error removed!
```

````

## Mesh

Correction of topography

## Inversion

+++ {"oxa":"oxa:wjcU0xFUCQKRwMTRhf0q/tcI0eYEPtsTGofecEZYN.1"}



+++ {"oxa":"oxa:wjcU0xFUCQKRwMTRhf0q/NK5JKBTIDMvr7BGZKPdy.3"}

# Preliminary Results (November 22, 2021) - coarse mesh

For interactive vtk visualization see output folder.

+++ {"oxa":"oxa:wjcU0xFUCQKRwMTRhf0q/WE3xCmoyMjOZmbh3mmHB.1"}

```{figure} images/wjcU0xFUCQKRwMTRhf0q-WE3xCmoyMjOZmbh3mmHB-v1.png
:name: 1638845895548
```

+++ {"oxa":"oxa:wjcU0xFUCQKRwMTRhf0q/M1Ar4iwtFqDlabdtY92u.1"}

```{figure} images/wjcU0xFUCQKRwMTRhf0q-M1Ar4iwtFqDlabdtY92u-v1.png
:name: 1638845959591
```

+++ {"oxa":"oxa:wjcU0xFUCQKRwMTRhf0q/36Pg5o2swFKA0siGupj3.1"}

Notebook to reproduce the data: [Salanto_2](oxa:wjcU0xFUCQKRwMTRhf0q/Fue00wSSGvzP47PFOSsM "Salanto_2")

