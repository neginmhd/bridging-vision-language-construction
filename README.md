# bridging-vision-language-construction
Repository for a systematic search and review of visual-to-text generation in construction, with shared raw search results, code, and supplementary materials.
## Workflow Overview

```mermaid
flowchart TD

A[Construction Problems<br/>• Safety management<br/>• Progress & schedule control<br/>• Scene documentation<br/>• Damage & condition assessment]

A --> B[Input<br/>• Acquisition platforms<br/>• Source type<br/>• Datasets employed]

B --> C[Data Preparation<br/>• Image preprocessing<br/>• Text preprocessing<br/>• Video preprocessing<br/>• Annotation strategy<br/>• Feature mapping]

C --> D[Model Development<br/>• Model architecture<br/>• Temporal modeling<br/>• Language decoding<br/>• Training paradigm<br/>• Adaptation strategy]

D --> E[Output Characteristics<br/>• Function<br/>• Expression<br/>• Control]

E --> F[Evaluation & Assessment<br/>• Automatic<br/>• Text-reference alignment<br/>• Vision-language alignment<br/>• Visual understanding<br/>• Human-centered<br/>• Efficiency]

F --> G[Real-world Deployment<br/>• Data pipeline<br/>• System integration<br/>• Organizational & operational factors]

G --> H[End]
