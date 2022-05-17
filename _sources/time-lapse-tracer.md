---
title: Time Lapse tracer inversion
description: ""
date: 2022-05-16T08:36:17.295Z
authors:
  - name: Benjamin M.
    userId: 4hjVRcSwHgd3ONBMyRs9VxBrHAB2
    orcid: 0000-0001-7199-2885
    corresponding: null
    email: null
    roles: null
    affiliations: null
name: time-lapse-tracer
oxa: oxa:wjcU0xFUCQKRwMTRhf0q/tpJGfhsFrbKLKPkfPbSG
---

# Time Lapse tracer inversion

+++ {"oxa":"oxa:wjcU0xFUCQKRwMTRhf0q/ry560j0tdnlpVSnuHpOo.1"}

````{danger}
Here I’m not sure to understand why the differences between background inversion and differences injection for the 1st times (T2/T3) are such different. The max differences for the background is about 450% (!!) while 10% for the difference inversion.

````

+++ {"oxa":"oxa:wjcU0xFUCQKRwMTRhf0q/WG6yJvfs0KxzY5QvXugC.1"}

# Difference inversion

a(T2/T3) | b (T3/T4)

c (T4/T5)| d (T5/T6)

+++ {"oxa":"oxa:wjcU0xFUCQKRwMTRhf0q/icGg93yCPEwIyreEPd45.5"}

```{figure} images/wjcU0xFUCQKRwMTRhf0q-icGg93yCPEwIyreEPd45-v5.png
:name: wcoZ7m1RNp

Time lapse inversion differences (in %) between two consecutive times from T2 (file120data2.dat April 4, 2022) to T6. Differences range from 0 to 10%.
```

+++ {"oxa":"oxa:wjcU0xFUCQKRwMTRhf0q/HWb8jCebtB3oFik6Y8HJ.3"}

# Background inversion

a(T2/T3) | b (T2/T4)

c (T2/T5)| d (T2/T6)

+++ {"oxa":"oxa:wjcU0xFUCQKRwMTRhf0q/icGg93yCPEwIyreEPd45.4"}

```{figure} images/wjcU0xFUCQKRwMTRhf0q-icGg93yCPEwIyreEPd45-v4.png
:name: T2a3Qhc91I

Time lapse inversion differences (in %) between two consecutive times from T2 (file120data2.dat April 4, 2022) to T6. Differences range from 0 to 10%.
```

+++ {"oxa":"oxa:wjcU0xFUCQKRwMTRhf0q/ZJZo0yNlaLDDB59r9Y3O.4"}

```{figure} images/wjcU0xFUCQKRwMTRhf0q-ZJZo0yNlaLDDB59r9Y3O-v4.png
:name: AR4O6Y9UnP

Isovolumes of differences (%) computed from time lapse inversion between T2 (file120data2.dat April 4, 2022) and T3, T4, T5, T6.
```

+++ {"oxa":"oxa:wjcU0xFUCQKRwMTRhf0q/d16U88szrqQfgV6y6WJd.1"}

# Notebooks to reproduce

[Salorno_2_TL2b3456_reg1](oxa:wjcU0xFUCQKRwMTRhf0q/7AomtdrhcqACjYkF2873 "Salorno_2_TL2b3456_reg1") [Salorno_2_TL2b3456_reg2](oxa:wjcU0xFUCQKRwMTRhf0q/P7qkLSkSikI2jMDAx45k "Salorno_2_TL2b3456_reg2")

