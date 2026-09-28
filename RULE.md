# Use Case Guideline

- Use cases cover Copilot, Agent Builder, Copilot Studio, Foundry, Fabric
- Copilot use cases cover Chat, Word, PowerPoint, Excel, Outlook, Teams
- Minimum number of use cases: Copilot - 2, Agent Builder - 2, Copilot Studio - 1, Foundry - 1, Fabric - 1
- Describe use case scenario, pain points, benefits, demo steps in README.md
- For agent, foundry, and fabric, describe env and setup in setup.md
- Standardized industry use cases, minimize country specifics
- If you already have use cases tailored for specific country, add them in a sub-folder with country/region name
- Reference publicly available data, but use a fictitious customer name


# Folder structure:

├── industry                             # Industry readiness stream
│   ├── README.md
│   ├── FSI
│   │   ├── README.md
│   │   ├── Copilot
│   │   │   ├── use-case-name-1
│   │   │   │   ├── README.md           # Scenario, painpoints, benefits, demo steps
│   │   │   │   └── data-files          # All supporting data files in the same folder
│   │   │   └── use-case-name-2
│   │   ├── Agent-Builder
│   │   │   └── use-case-name-1
│   │   │       ├── README.md           # Scenario, painpoints, benefits, agent config, demo steps
│   │   │       └── data-files          # All supporting data files in the same folder
│   │   ├── Copilot-Studio
│   │   │   └── use-case-name-1
│   │   │       ├── README.md           # Scenario, painpoints, benefits, demo steps
│   │   │       ├── setup.md            # Agent setup guide
│   │   │       └── data-files          # All supporting data files in the same folder
│   │   ├── Foundry
│   │   │   └── use-case-name-1
│   │   │       ├── README.md           # Scenario, painpoints, benefits, demo steps
│   │   │       ├── setup.md            # Foundry setup guide
│   │   │       └── source              # Folder for all Python code
│   │   │           ├── source-file1
│   │   │           └── ...
│   │   └── Fabric
│   │       └── use-case-name-1
│   │           ├── README.md           # Scenario, painpoints, benefits, demo steps
│   │           ├── setup.md            # Fabric setup guide
│   │           ├── notebook            # Demo notebooks
│   │           │   ├── notebook1
│   │           │   └── ...
│   │           └── data
│   │               ├── data-file1
│   │               └── ...
