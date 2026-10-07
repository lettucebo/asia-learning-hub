# Contributing to Asia Learning Hub

This guide is the single source of truth for industry use cases in this
repository. Human reviewers, the structure check, and the Copilot use-case
review all evaluate pull requests against the rules below.

## How to contribute

1. Create a branch and open a pull request against `main`. Do not push or
   upload files directly to `main`.
2. Follow the [use case guideline](#use-case-guideline) and
   [folder structure](#folder-structure).
3. Optionally run the [self-check](#self-check-with-your-own-copilot-cli)
   with your own Copilot CLI before you open the pull request.
4. Ask another team member to pair with you: they verify the setup and
   instructions and approve the pull request.
5. Address the **Structure check** result. The **Use case review** comment
   from Copilot is advisory, not an approval.

## Use case guideline

- Use cases cover Copilot, Agent Builder, Copilot Studio, Foundry, and Fabric.
- Copilot use cases cover Chat, Word, PowerPoint, Excel, Outlook, and Teams.
- Minimum number of use cases: Copilot - 2, Agent Builder - 2,
  Copilot Studio - 1, Foundry - 1, Fabric - 1. This is overall coverage, not
  a requirement for an individual pull request.
- Describe the use case scenario, pain points, benefits, and demo steps in
  `README.md`. Agent Builder use cases also describe the agent configuration.
- For Copilot Studio, Foundry, and Fabric, describe the environment and setup
  in `setup.md`. For Agent Builder, `setup.md` is optional; the agent
  configuration in `README.md` is sufficient.
- Standardize industry use cases and minimize country specifics.
- If you already have use cases tailored for a specific country, add them in a
  sub-folder with the country/region name.
- Reference publicly available data, but use a fictitious customer name.
- For all deliverables, another person in the team should be paired with the
  author to verify the setup and instructions.

## Folder structure

Use kebab-case for use-case folder names (for example,
`relationship-manager-assistant`). A country/region variant goes in an
optional sub-folder between the industry and the product:
`industry/<Industry>/[<Country-or-region>/]<Product>/<use-case>/`.

```text
industry                                 # Industry readiness stream
├── README.md
├── FSI
│   ├── README.md
│   ├── Copilot
│   │   ├── use-case-name-1
│   │   │   ├── README.md               # Scenario, pain points, benefits, demo steps
│   │   │   └── data-files              # All supporting data files in the same folder
│   │   └── use-case-name-2
│   ├── Agent-Builder
│   │   └── use-case-name-1
│   │       ├── README.md               # Scenario, pain points, benefits, agent config, demo steps
│   │       ├── setup.md                # Optional agent setup guide
│   │       └── data-files              # All supporting data files in the same folder
│   ├── Copilot-Studio
│   │   └── use-case-name-1
│   │       ├── README.md               # Scenario, pain points, benefits, demo steps
│   │       ├── setup.md                # Agent setup guide
│   │       └── data-files              # All supporting data files in the same folder
│   ├── Foundry
│   │   └── use-case-name-1
│   │       ├── README.md               # Scenario, pain points, benefits, demo steps
│   │       ├── setup.md                # Foundry setup guide
│   │       └── source                  # Folder for all Python code
│   │           ├── source-file1
│   │           └── ...
│   └── Fabric
│       └── use-case-name-1
│           ├── README.md               # Scenario, pain points, benefits, demo steps
│           ├── setup.md                # Fabric setup guide
│           ├── notebook                # Demo notebooks
│           │   ├── notebook1
│           │   └── ...
│           └── data
│               ├── data-file1
│               └── ...
```

The industry names in the [publisher table](#copilot-studio-agent-guideline)
are canonical. The current `industry/` folder names are provisional and are
not checked.

## Copilot Studio agent guideline

To make it easy for MTTs to create the demo agent in their environment, we
provide the solution export. Create one solution per demo agent. To
facilitate the import of Power Platform solutions containing Copilot Studio
agents, use the following naming standards.

- Publisher

  | Industry | Publisher Display Name | Publisher Name | Publisher Prefix |
  | --- | --- | --- | --- |
  | Digital Native | Digital Native | DigitalNative | dn |
  | Financial Services | Financial Services | FinancialServices | fsi |
  | Healthcare | Healthcare | Healthcare | hc |
  | IT & ITeS | IT & ITeS | IT&ITeS | it |
  | Manufacturing & Mobility | Manufacturing & Mobility | Manufacturing&Mobility | mfg |
  | Public Sector | Public Sector | PublicSector | ps |
  | Retail & Consumer Goods | Retail & Consumer Goods | Retail&ConsumerGoods | rt |
  | Telco | Telco | Telco | telco |

- Solution
  - Choose the publisher according to the industry.
  - Create the solution name based on the use case name. Shorten the use case
    name if necessary.
- Schema: let Copilot Studio generate it automatically based on the agent name.

## Review checks

Each check below has a stable ID. Automated reviews of a pull request report
every ID, for the use cases changed in that pull request only.

| ID | Check |
| --- | --- |
| STRUCT-01 | The use case is at `industry/<Industry>/[<Country-or-region>/]<Product>/<use-case>/`, where Product is `Copilot`, `Agent-Builder`, `Copilot-Studio`, `Foundry`, or `Fabric`. |
| STRUCT-02 | The use-case folder name is kebab-case. |
| STRUCT-03 | The use case has `README.md`; Copilot-Studio, Foundry, and Fabric use cases also have `setup.md`. |
| STRUCT-04 | Supporting files are in `data-files/` for Copilot, Agent-Builder, and Copilot-Studio; `source/` for Foundry; `notebook/` or `data/` for Fabric. |
| CONTENT-01 | `README.md` describes the scenario, pain points, benefits, and demo steps; Agent-Builder use cases also describe the agent configuration. |

## Self-check with your own Copilot CLI

You can run the same review locally with your own
[GitHub Copilot CLI](https://docs.github.com/copilot/how-tos/copilot-cli)
before you open a pull request. It uses your Copilot plan, reads the rules
from the base branch, and does not change any files except `.review/`, which
Git ignores.

Use the remote that points to this repository as the base: `origin/main` if
you cloned this repository, or `upstream/main` if you work from a fork.

Bash:

```bash
base_remote=origin
if git remote get-url upstream >/dev/null 2>&1; then base_remote=upstream; fi
git fetch "$base_remote" main
if ! python3 .github/scripts/prepare_review.py "$base_remote/main" HEAD; then exit 1; fi
if grep -q '"skipped": true' .review/metadata.json; then exit 0; fi
copilot --agent use-case-review -s --available-tools=view --allow-tool=read \
  -p "$(cat .review/prompt.md)"
```

PowerShell 7:

```powershell
$baseRemote = if (git remote get-url upstream 2>$null) { "upstream" } else { "origin" }
git fetch $baseRemote main
python .github/scripts/prepare_review.py "$baseRemote/main" HEAD
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
if ((Get-Content .review/metadata.json -Raw | ConvertFrom-Json).skipped) { exit 0 }
copilot --agent use-case-review -s --available-tools=view --allow-tool=read `
  -p (Get-Content .review/prompt.md -Raw)
```

If `prepare_review.py` reports that the review was skipped, there are no
changed use cases to review.