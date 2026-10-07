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

## Use Case Guideline
- Use cases cover Copilot, Agent Builder, Copilot Studio, Foundry, Fabric
- Copilot use cases cover Chat, Word, PowerPoint, Excel, Outlook, Teams
- Minimum number of use cases: Copilot - 2, Agent Builder - 2, Copilot Studio - 1, Foundry - 1, Fabric - 1
- Describe use case scenario, pain points, benefits, demo steps in README.md
- For agent, foundry, and fabric, describe env and setup in setup.md
- Standardized industry use cases, minimize country specifics
- If you already have use cases tailored for specific country, add them in a sub-folder with country/region name
- Reference publicly available data, but use a fictitious customer name
- For all deliverables, another person in the team should be paired with the author to verify the setup and instruction.


## Copilot Studio Agent Guideline
To make it easy for MTTs to create the demo agent in their environment, we will provide the solution export. Create one solution per demo agent.
To facilitate the import of Power Platform solution containing Copilot Studio agents, use the following naming standards.

- Publisher
    | Industry  | Publisher Display Name  | Publisher Name  | Publisher Prefix  |
    | --- |  --- |  --- |  --- |
    | Digital Native  | Digital Native  | DigitalNative  | dn  |
    | Financial Services  | Financial Services  | FinancialServices  | fsi  |
    | Healthcare  | Healthcare  | Healthcare  | hc  |
    | IT & ITeS  | IT & ITeS  | IT&ITeS  | it  |
    | Manufacturing & Mobility  | Manufacturing & Mobility  | Manufacturing&Mobility  | mfg  |
    | Public Sector  | Public Sector  | PublicSector  | ps  |
    | Retail & Consumer Goods  | Retail & Consumer Goods  | Retail&ConsumerGoods  | rt  |
    | Telco  | Telco  | Telco  | telco  |

- Solution 
  - Choose the publisher name according to industry. 
  - Create solution name based on the use case name. Shorten the use case name if necessary. 
- Schema - Let Copilot Studio auto generated based on the agent name